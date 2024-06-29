import streamlit as st
import os
from werkzeug.utils import secure_filename

def file_upload_page():
    st.title("File Upload Page")

    # Create a folder to store uploaded files if it doesn't exist
    UPLOAD_FOLDER = "DataAnalysis"
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "pdf"])

    if uploaded_file is not None:
        file_details = {
            "Filename": "Uploaded",
            "FileType": uploaded_file.type,
            "FileSize": uploaded_file.size
        }
        st.write(file_details)

        # Secure the filename before storing
        filename = secure_filename(uploaded_file.name)
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save the file
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File saved")

        # Display the content of the file based on its type
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file)
        elif uploaded_file.type == "text/plain":
            st.text(uploaded_file.read().decode("utf-8"))
        elif uploaded_file.type == "application/pdf":
            st.write("PDF file uploaded and saved. Processing of PDF content not implemented in this example.")
        else:
            st.write("File uploaded and saved successfully. Further processing depends on the file type.")
        
        return True

if __name__ == "__main__":
    file_upload_page()