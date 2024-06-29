import openai

# List all files
file_list = openai.File.list()

# Check if there are any files
if file_list.data:
    # Get the ID of the first (most recent) file
    most_recent_file_id = file_list.data[0].id
    most_recent_file_name = file_list.data[0].filename
    
    print(f"Most recent file ID: {most_recent_file_id}")
    print(f"Most recent file name: {most_recent_file_name}")
else:
    print("No files found in your OpenAI account.")

# Now you can use most_recent_file_id in your API calls