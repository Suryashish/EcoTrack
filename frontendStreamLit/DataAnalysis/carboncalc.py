import pandas as pd

def calculate_and_save_carbon_emissions():
    def calculate_carbon_emission(row):
        # Constants for carbon emissions factors (hypothetical values for demonstration)
        carbon_factors = {
            'Raw Material Weight (tons)': 0.1,
            'Energy Consumption (kWh)': 0.5,
            'Water Usage (gallons)': 0.2,
            'Chemical Usage (liters)': 0.3,
            'Furnace Temperature (°C)': 0.4,
            'Production Time (hours)': 0.2,
            'Yield (%)': 0.1,
            'Scrap Metal (tons)': 0.1,
            'Maintenance Downtime (hours)': 0.3
        }

        # Calculate total carbon emission for the row
        total_emission = sum(row[field] * factor for field, factor in carbon_factors.items())

        return total_emission

    # Input and output file paths
    input_file = 'DataAnalysis/dataset.csv'  # Replace with your input CSV file path
    output_file = 'DataAnalysis/carbon_emission.csv'  # Replace with your desired output CSV file path

    # Read input CSV file into a pandas DataFrame
    data = pd.read_csv(input_file)

    # Calculate carbon emission for each row
    data['Estimated Carbon Emission'] = data.apply(calculate_carbon_emission, axis=1)

    # Select only Date and Estimated Carbon Emission columns
    output_data = data[['Date', 'Estimated Carbon Emission']]

    # Save results to output CSV file
    output_data.to_csv(output_file, index=False)

    print(f"Estimated carbon emissions calculated and saved to {output_file}.")
    return True