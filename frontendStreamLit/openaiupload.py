from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key='sk-proj-3ThQs6nvx2E9f3SMxPIQT3BlbkFJzjTuW70JKduEO0szEf2T')

def upload_file_OPENAI(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return
    
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    if not files:
        print(f"No files found in {folder_path}")
        return
    
    uploaded_files = []
    
    for filename in files:
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a subdirectory)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'rb') as file:
                    # Upload the file
                    response = client.files.create(
                        file=file,
                        purpose='fine-tune'
                    )
                
                print(f"Uploaded {filename}:")
                print(response)
                uploaded_files.append(response)
            except Exception as e:
                print(f"Error uploading {filename}: {str(e)}")
    
    # Print summary of uploaded files
    print(f"\nUploaded {len(uploaded_files)} files.")
    
    # List all files to verify the upload
    all_files = client.files.list()
    print("\nAll files in OpenAI:")
    for file in all_files:
        print(f"ID: {file.id}, Filename: {file.filename}")
    
    return uploaded_files

# Usage
uploaded_files = upload_file_OPENAI('/path/to/your/folder')




































# import openai
# import os

# # Set your OpenAI API key
# openai.api_key = ''


# def upload_file_OPENAI(folder_path):


#     # Check if the folder exists
#     if not os.path.exists(folder_path):
#         print(f"The folder {folder_path} does not exist.")
#         return

#     # Get a list of all files in the folder
#     files = os.listdir(folder_path)

#     if not files:
#         print(f"No files found in {folder_path}")
#         return

#     uploaded_files = []

#     for filename in files:
#         file_path = os.path.join(folder_path, filename)
        
        
#         # Check if it's a file (not a subdirectory)
#         if os.path.isfile(file_path):
#             try:
#                 with open(file_path, 'rb') as file:
#                     # Upload the file
#                     response = openai.File.create(
#                         file=file,
#                         purpose='fine-tune'
#                     )
                
#                 print(f"Uploaded {filename}:")
#                 print(response)
#                 uploaded_files.append(response)
#             except Exception as e:
#                 print(f"Error uploading {filename}: {str(e)}")

#     # Print summary of uploaded files
#     print(f"\nUploaded {len(uploaded_files)} files.")

#     # List all files to verify the upload
#     all_files = openai.File.list()
#     print("\nAll files in OpenAI:")
#     for file in all_files.data:
#         print(f"ID: {file.id}, Filename: {file.filename}")

#     return uploaded_files
