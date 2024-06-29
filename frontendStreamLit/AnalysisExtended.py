import openai
import requests
import csv
import json
import os

# Set up the OpenAI client
client = openai.OpenAI(api_key=os.environ.get('API_KEY'))

# Retrieve the most recent file ID
files = client.files.list()
if files.data:
    most_recent_file = files.data[0]
    most_recent_file_id = most_recent_file.id
    
    # Download file content
    file_content = client.files.content(most_recent_file_id)

    # Define the custom context
    custom_context = "Based on the input fields and the file provided to you, retrieve data for each of the input fields from the file and give the data in csv with proper structure. For fields you cannot find, take an accurate average value. For non-numerical inputs, understand from the file."

    # Read input CSV file
    with open('csv/InputsOutput.csv', 'r') as input_file:
        csv_reader = csv.reader(input_file)
        headers = next(csv_reader)  # Read the header row

        # Open output CSV file in append mode
        with open('csv/AnalysisExtended.csv', 'a', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            
            # Write headers to output file if it's empty
            output_file.seek(0, 2)
            if output_file.tell() == 0:
                csv_writer.writerow(headers + ['API_Response'])

            # Process each row
            for row in csv_reader:
                user_input = ','.join(row)  # Convert row to string

                # Make API call
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": custom_context},
                        {"role": "user", "content": user_input}
                    ]
                )

                # Extract the response
                output = response.choices[0].message.content

                # Parse JSON response
                try:
                    output_json = json.loads(output)
                    # Append original row data and API response to output CSV
                    csv_writer.writerow(row + [json.dumps(output_json)])
                except json.JSONDecodeError:
                    # If response is not valid JSON, write it as is
                    csv_writer.writerow(row + [output])

print("Processing complete. Results appended ")