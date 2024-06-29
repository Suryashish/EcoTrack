import csv
import requests
import json

# OpenAI API endpoint and your API key
api_url = "https://api.openai.com/v1/chat/completions"
api_key = "sk-proj-3ThQs6nvx2E9f3SMxPIQT3BlbkFJzjTuW70JKduEO0szEf2T"

# Your context
context = "When I provide the name of a manufacturing process, output the most important and required fields that are needed for calculating carbon emissions and related data, in a clear CSV format, directly start answering, no extra text before or after. Output inside a double inverted comma. For example, look for the amount of production, transportation, raw materials required, the various processes, etc., as per the process requirement. recheck before outputting"

# Function to make API call
def call_openai_api(message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": context},
            {"role": "user", "content": message}
        ]
    }
    
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    return response.json()

# Read input CSV file and make API calls
with open('csv/OnlyTitles.csv', 'r') as input_file, open('csv/InputsOutput.csv', 'a', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)
    
    next(csv_reader)  # Skip the first line
    
    for row in csv_reader:
        # Assuming the text you want to send is in the first column
        text = row[0]
        
        # Make API call
        result = call_openai_api(text)
        
        # Process the result and write to CSV
        if 'choices' in result and len(result['choices']) > 0:
            output = result['choices'][0]['message']['content']
            csv_writer.writerow([text, output])
            print(f"Processed: {text}")
        else:
            csv_writer.writerow([text, "Error: " + str(result)])
            print(f"Error processing: {text}")

print("Processing complete. Results have been appended to output_results.csv")