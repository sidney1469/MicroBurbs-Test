import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("forecast_history.csv")

data.replace({'\$': '', ',': '', 'I': '1', 'O': '0'}, regex=True, inplace=True)
data = data.apply(pd.to_numeric, errors='coerce')

data['Median Growth (%)'] = data['Median house price'].pct_change() * 100
correlations = data.corr()['Median Growth (%)']

most_correlated_forecast = correlations.dropna().idxmax()

X = data[['year', most_correlated_forecast]].dropna().values
y = data['Median Growth (%)'].dropna().values[:len(X)]

model = LinearRegression()
model.fit(X, y)

future_years = np.array([[2025, np.nan], [2026, np.nan], [2027, np.nan]])
future_predictions = model.predict(future_years)

plt.figure(figsize=(10, 6))
plt.scatter(data['year'], data['Median Growth (%)'], label='Actual Growth', color='blue')
plt.plot(data['year'], model.predict(X), label='Fitted Line', color='red')
plt.scatter(future_years[:, 0], future_predictions, label='Future Predictions', color='green')
plt.xlabel('Year')
plt.ylabel('Median Growth (%)')
plt.title('Median House Price Growth Prediction')
plt.legend()
plt.show()