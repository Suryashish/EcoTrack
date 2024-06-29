import streamlit as st
from fileupload import file_upload_page
from openaiupload import upload_file_OPENAI
from DataAnalysis.csvtographfinal import plot_data
from DataAnalysis.carboncalc import calculate_and_save_carbon_emissions
from datetime import date

def navbar():
    # Use columns to create a horizontal layout
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Home"):
            st.session_state.page = "home"
    with col2:
        if st.button("Upload"):
            st.session_state.page = "upload"
    with col3:
        if st.button("Analyze"):
            st.session_state.page = "analyze"
    with col4:
        if st.button("About"):
            st.session_state.page = "about"

def main():
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    if 'file_uploaded' not in st.session_state:
        st.session_state.file_uploaded = False

    # Set page config
    st.set_page_config(page_title="EcoTrack", layout="wide", page_icon="🌿", initial_sidebar_state="expanded")

    # Custom CSS for white background and navbar styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: black;
        }
        .stButton>button {
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the navbar
    navbar()

    # Display content based on the selected page

    if st.session_state.page == "home":
        st.title("Welcome to EcoTrack")
        st.write("This is your one-stop solution for carbon emission compliance")

    elif st.session_state.page == "upload":
        st.title("Upload Files")

        upload_result = file_upload_page()

        if upload_result:
            st.session_state.file_uploaded = True
            st.success("File uploaded successfully!")

        if st.session_state.file_uploaded:
            calc_button = st.button("Calculate Carbon Emission")

            if calc_button:
                with st.spinner("Calculating carbon emission..."):
                    try:
                        result = calculate_and_save_carbon_emissions()
                        st.success("Calculation completed successfully!")
                        st.write(result)  # Assuming calculate_carbon_emission returns a result
                    except FileNotFoundError:
                        st.error("Error: The uploaded file could not be found. Please try uploading again.")
                    except Exception as e:
                        st.error(f"An error occurred during calculation: {str(e)}")
                        st.exception(e)  # This will display the full traceback

        if not st.session_state.file_uploaded:
            st.info("Please upload a file to proceed with calculation.")
            
            if st.button("Upload to OpenAI"):
                try:
                    upload_file_OPENAI("Files/Untitled.py")
                except FileNotFoundError:
                    st.error("Error: The file to upload to OpenAI could not be found.")
                except Exception as e:
                    st.error(f"An error occurred during OpenAI upload: {str(e)}")

    elif st.session_state.page == "analyze":

        year_month = st.date_input(
            "Select Year and Month",
            value=date.today().replace(day=1),
            format="YYYY-MM"
)

        st.title("Analyze Data")
        if st.session_state.file_uploaded:
            if st.button("Display Analysis"):
                try:
                    plot_data()
                except FileNotFoundError:
                    st.error("Error: The data file could not be found. Please upload a file first.")
                except Exception as e:
                    st.error(f"An error occurred during analysis: {str(e)}")
        else:
            st.warning("Please upload a file in the Upload section before analyzing.")

    elif st.session_state.page == "about":
        st.title("About EcoTrack")
        st.write("EcoTrack is a powerful tool for managing and analyzing carbon emissions data.")

if __name__ == "__main__":
    main()