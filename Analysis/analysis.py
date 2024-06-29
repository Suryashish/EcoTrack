# create a ai model from scratch to predict the trend based on a csv file which has date and total carbon emission amount an generate the output of prediction


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.optimizers import Adam

# Step 1: Read the CSV file
df = pd.read_csv('path_to_your_csv.csv')

# Step 2: Preprocess the data
# Convert dates to ordinal numbers
df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
# Normalize the total carbon emission amounts
scaler = MinMaxScaler(feature_range=(0, 1))
df['total_carbon_emission'] = scaler.fit_transform(df[['total_carbon_emission']])

# Step 3: Split the data
X = df['date'].values.reshape(-1, 1)
y = df['total_carbon_emission'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Step 5: Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Step 6: Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)

# Step 7: Evaluate the model
model.evaluate(X_test, y_test)

# Step 8: Make predictions
# Example: Predicting for a new date
new_date = pd.to_datetime(['2025-01-01']).map(pd.Timestamp.toordinal).values.reshape(-1, 1)
predicted_emission = model.predict(new_date)
# Inverse transform to get the actual emission value
predicted_emission = scaler.inverse_transform(predicted_emission)
print(f"Predicted carbon emission for 2025-01-01: {predicted_emission[0][0]}")

# Step 9: Generate output
# This step depends on how you want to display or save your predictions. This example simply prints a prediction.
