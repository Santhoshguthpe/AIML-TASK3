# linear_regression.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset (downloaded from Kaggle)
df = pd.read_csv("Housing.csv")  # ensure Housing.csv is in same folder

# Preview data
print("Dataset Head:\n", df.head())
print("\nColumns:\n", df.columns)

# Select features and target (example: 'area', 'bedrooms' -> 'price')
X = df[['area', 'bedrooms']]  # independent variables
y = df['price']               # dependent variable

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R² Score:", r2)

# Coefficients
print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Plot actual vs predicted
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.show()
