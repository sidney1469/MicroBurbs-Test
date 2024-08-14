import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

data = pd.read_csv("forecast_history.csv")

data.replace({'\$': '', ',': '', 'I': '1', 'O': '0'}, regex=True, inplace=True)
data = data.apply(pd.to_numeric, errors='coerce')

data['Median Growth (%)'] = data['Median house price'].pct_change() * 100
correlations = data.corr()['Median Growth (%)']

most_correlated_forecast = correlations.dropna().idxmax()

X = data[['year', most_correlated_forecast]].dropna().values
y = data['Median Growth (%)'].dropna().values[:len(X)]

imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

model = LinearRegression()
model.fit(X_imputed, y)

future_years = np.array([[2025, np.nan], [2026, np.nan], [2027, np.nan]])

future_years[:, 1] = np.mean(data[most_correlated_forecast].dropna().values)

future_predictions = model.predict(future_years)

print(str(future_predictions))