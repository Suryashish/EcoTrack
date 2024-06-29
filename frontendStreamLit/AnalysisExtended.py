import openai
import time

# Set your API key
openai.api_key = 'sk-proj-3ThQs6nvx2E9f3SMxPIQT3BlbkFJzjTuW70JKduEO0szEf2T'

# List all files
file_list = openai.File.list()

# Check if there are any files
if file_list.data:
    # Get the ID of the first (most recent) file
    most_recent_file_id = file_list.data[0].id

# Create an Assistant
assistant = openai.beta.assistants.create(
    name="My Assistant",
    instructions="You are a helpful assistant.",
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
    file_ids=["existing-file-id"]  # Use the ID of your pre-uploaded file
)

# Create a Thread
thread = openai.beta.threads.create()

# Add a Message to the Thread
message = openai.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What information can you provide based on the context in the file?"
)

# Run the Assistant
run = openai.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please provide information based on the context in the file."
)

# Wait for the Run to complete
while run.status != 'completed':
    time.sleep(1)
    run = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

# Retrieve the response
messages = openai.beta.threads.messages.list(thread_id=thread.id)
for message in messages.data:
    if message.role == 'assistant':
        print(message.content[0].text.value)