import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_data():
    # Step 1: Read the CSV file into a pandas DataFrame
    df = pd.read_csv('DataAnalysis/predicted_emissions.csv')

    # Step 2: Extract x and y values from the DataFrame
    days = df['Date']
    values = df['Estimated Carbon Emission']

    # Step 3: Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(days, values, marker='o', linestyle='-')

    # Step 4: Customize the plot
    ax.set_title('Predicted Carbon Emission according to date')
    ax.set_xlabel('Days')
    ax.set_ylabel('Value')
    ax.grid(True)

    # Step 5: Display the plot in Streamlit
    st.pyplot(fig)

    # Optionally, display the DataFrame
    st.dataframe(df)

