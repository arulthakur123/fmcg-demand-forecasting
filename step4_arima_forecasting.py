import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

# Step 1: Load cleaned data
df = pd.read_csv("cleaned_fmcg_data.csv", parse_dates=['date'])
df = df.sort_values("date")

# Step 2: Resample to monthly sales volume
monthly_sales = df.resample('M', on='date').sum()['sales_volume']

# Step 3: Visualize sales trend
plt.figure(figsize=(10, 5))
monthly_sales.plot(title="Monthly FMCG Sales Volume")
plt.xlabel("Date")
plt.ylabel("Sales Volume")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# Step 4: Fit ARIMA model (order = (1,1,1) is a starting point)
model = ARIMA(monthly_sales, order=(1, 1, 1))
model_fit = model.fit()

# Step 5: Forecast next 6 months
forecast = model_fit.forecast(steps=6)

# Step 6: Plot forecast
plt.figure(figsize=(10, 5))
monthly_sales.plot(label='Historical', color='blue')
forecast.index = pd.date_range(start=monthly_sales.index[-1] + pd.offsets.MonthEnd(), periods=6, freq='M')
forecast.plot(label='Forecast', color='green')
plt.title("FMCG Sales Volume Forecast (Next 6 Months)")
plt.xlabel("Date")
plt.ylabel("Sales Volume")
plt.legend()
plt.tight_layout()
plt.savefig("fmcg_forecast_arima.png")
plt.close()

print("✅ Forecasting complete. Forecast plot saved as fmcg_forecast_arima.png")
