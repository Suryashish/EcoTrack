import pdfplumber
import pandas as pd
import os



current_directory = os.getcwd()

print("Current Directory:", current_directory)

# Create a variable for the file path
pdf_path = "Files/Untitled.pdf"  # Replace this with your actual file path

# Extract the table and get the second column
def extract_second_column(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        table = first_page.extract_table()
        
        # Convert the table to a pandas DataFrame
        df = pd.DataFrame(table[1:], columns=table[0])
        
        # Get the name of the second column
        second_column_name = df.columns[1]
        
        # Extract the second column
        second_column = df[second_column_name].tolist()
        
    return second_column

def extract_first_column(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        table = first_page.extract_table()
        
        # Convert the table to a pandas DataFrame
        df = pd.DataFrame(table[0:], columns=table[0])
        
        # Get the name of the second column
        first_column_name = df.columns[0]
        
        # Extract the second column
        first_column = df[first_column_name].tolist()
        
    return first_column

# Call the function and store the result in a variable
resultFirst = extract_first_column(pdf_path)
resultSecond = extract_second_column(pdf_path)

# Convert the result to a pandas DataFrame
df_resultFirst = pd.DataFrame(resultFirst, columns=["DATES"])
df_resultSecond = pd.DataFrame(resultSecond, columns=["Title"])

# Save the DataFrame to a CSV file
df_resultFirst.to_csv("csv/OnlyDates.csv", index=False)
df_resultSecond.to_csv("csv/OnlyTitles.csv", index=False)