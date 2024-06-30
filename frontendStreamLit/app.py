import streamlit as st
from fileupload import file_upload_page
from DataAnalysis.csvtographfinal import plot_data
from DataAnalysis.carboncalc import calculate_and_save_carbon_emissions

from DataAnalysis.prediction import predict_carbon_emissions
from DataAnalysis.prediction import report

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
                    result = calculate_and_save_carbon_emissions()
                    if result:
                        st.success("Calculation completed successfully!")
                        
            

    elif st.session_state.page == "analyze":

        st.title("User Input Example")
        # Create a text input box
        year = st.text_input("Enter the Year and month (YYYY-MM)")
        # Create a submit button

        # Create a submit button
        if st.button("Submit"):
            if year:
                predict_carbon_emissions(year)
            else:
                st.write("Please enter some text before submitting.")


        st.title("Analyze Data")
        if st.session_state.file_uploaded:
            if st.button("Display Analysis"):

                temp12 = plot_data()
                if temp12:
                    report()
        else:
            st.warning("Please upload a file in the Upload section before analyzing.")

    elif st.session_state.page == "about":
        st.title("About EcoTrack")
        st.write("EcoTrack is a powerful tool for managing and analyzing carbon emissions data.")

if __name__ == "__main__":
    main()