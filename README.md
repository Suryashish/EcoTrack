
# EcoTrack

The place to calculate the carbon footprint of the company (currently restricted to a few ones)


## Authors

- [@Biswadeep Mukhopadhyay](https://www.github.com/Biswadeep01)
- [@Debajit Dutta](https://www.github.com/debajit07)
- [@Suryashish Kundu](https://www.github.com/suryashish)


## Deployment

To deploy this project run

 ```bash
   https://github.com/Biswadeep01/EcoTrack.git
   cd EcoTrack
   cd frontendStreamLit
   ```

```bash
  pip install -r requirements.txt
```
then, 
```bash
  streamlit run app.py
```


## Features

- Efficient (in-house) Carbon Footprint estimation
- Automated system
- ML to predict future estimation
- Simple UI
- Grade Assignement based on future emission prediction and suggesting ways to solve this


## Documentation

# EcoTrack: Carbon Footprint Emission Prediction

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Usage](#usage)
   - [Input Data](#input-data)
   - [Emission Prediction](#emission-prediction)
   - [Future Prediction](#future-prediction)
   - [Grade Assignment and Recommendations](#grade-assignment-and-recommendations)

## Introduction
The Carbon Footprint Emission Prediction web application is designed to help companies assess and predict their carbon emissions. Built using Streamlit, the app allows users to input relevant data and receive an estimation of their current carbon footprint, as well as predictions for future emissions based on a specified date. The app also assigns a grade based on future emission predictions and provides recommendations for improvement.

## Features
-Efficient In-House Carbon Footprint Estimation: Accurate estimation using company-specific data.
-Automated System:Minimizes manual input and provides automated results.
-Machine Learning for Future Estimation:Uses ML models to predict future emissions.
-Simple UI:User-friendly interface for seamless data input and result visualization.
-Grade Assignment and Recommendations:Provides a grade based on future emissions and suggests ways to reduce the carbon footprint.


## Usage

### Input Data
Upon launching the app, you will be prompted to input the following data:
-Energy Consumption:Enter the total energy consumption (in kWh).
-Transportation:Provide details on the transportation methods and distance covered.
-Waste Production:Input the amount of waste produced (in tons).
-Other Factors:Any other relevant factors contributing to carbon emissions.

### Emission Prediction
After entering the data, click on the "Calculate Emissions" button. The app will process the data and display the current carbon footprint in metric tons of CO2 equivalent.

### Future Prediction
To predict future emissions:
1. Select a future date using the date picker.
2. Click on the "Predict Future Emissions" button.
3. The app will display the predicted carbon footprint for the selected date based on trends and provided data using machine learning models.

### Grade Assignment and Recommendations
Based on the future emission predictions:
1. The app assigns a grade (A+, A, B, etc.) to indicate the sustainability level of the company's carbon footprint.
2. Recommendations for reducing carbon emissions will be provided, such as energy-saving tips, transportation optimizations, and waste management strategies.



## FAQs
### Q1: What data is required to use the app?
A1: Users need to input data related to energy consumption, transportation, waste production, and any other relevant emission factors.

### Q2: How accurate are the future predictions?
A2: The accuracy of future predictions depends on the quality and comprehensiveness of the input data and the assumptions made by the predictive model.

### Q3: How is the grade determined?
A4: The grade is determined based on the predicted future emissions compared to industry standards and sustainability goals.

### Q4: What kind of recommendations are provided?
A5: Recommendations may include energy-saving tips,, investement in suistainable things, and other practices to reduce carbon emissions.
## Running Tests

To run tests, run the following command

```bash
   https://github.com/Biswadeep01/EcoTrack.git
   cd EcoTrack
   cd frontendStreamLit
   ```
```bash
    python -m venv myenv
```
```bash
    venv\Scripts\activate
```
```bash
  pip install -r requirements.txt
```
then, 
```bash
  streamlit run app.py
```

Select any type of company then submit.

Move to "Uploads" and upload the dataset.csv file there and select "Calculate Carbon Emission"

Move to Analyse section.

Enter desired year and month and click "Submit" once.

Wait for couple of seconds.

Then click Display Analysis, and you will get your analytics.



