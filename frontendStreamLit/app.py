import streamlit as st
from fileupload import file_upload_page
from openaiupload import upload_file_OPENAI

# Title of the app
st.title('Hello Streamlit!')

# Display some text
st.write('Welcome to your first Streamlit app!')

# Call the file upload page function
file_upload_page()


# OPEN AI UPLOAD

# Create a radio button for page selection

# create a confirm button and clicking it will run the openai_upload_page function
if st.button("Upload to OpenAI"):
    upload_file_OPENAI("Files/")