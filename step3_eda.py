import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_fmcg_data.csv", parse_dates=["date"])

# Set style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# 1. 📅 Monthly Sales Trend
df['month'] = df['date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('month')['sales_volume'].sum().reset_index()

plt.figure()
sns.lineplot(data=monthly_sales, x='month', y='sales_volume', marker='o')
plt.xticks(rotation=45)
plt.title("Monthly FMCG Sales Trend")
plt.ylabel("Total Sales Volume")
plt.tight_layout()
plt.savefig("fig_monthly_sales_trend.png")
plt.close()

# 2. 📦 Top Product Categories
category_sales = df.groupby('product_category')['sales_volume'].sum().sort_values(ascending=False).reset_index()

plt.figure()
sns.barplot(data=category_sales, x='sales_volume', y='product_category', palette='mako')
plt.title("Total Sales by Product Category")
plt.xlabel("Sales Volume")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig("fig_category_sales.png")
plt.close()

# 3. 🗺️ Sales by Region
location_sales = df.groupby('store_location')['sales_volume'].sum().reset_index()

plt.figure()
sns.barplot(data=location_sales, x='store_location', y='sales_volume', palette='flare')
plt.title("Sales Volume by Store Location")
plt.xlabel("Store Location")
plt.ylabel("Sales Volume")
plt.tight_layout()
plt.savefig("fig_sales_by_location.png")
plt.close()

# 4. 🎯 Promotion Impact
promo_sales = df.groupby('promotion')['sales_volume'].mean().reset_index()
promo_sales['promotion'] = promo_sales['promotion'].map({0: 'No Promotion', 1: 'Promotion Applied'})

plt.figure()
sns.barplot(data=promo_sales, x='promotion', y='sales_volume', palette='Set2')
plt.title("Average Sales Volume with and without Promotion")
plt.xlabel("Promotion")
plt.ylabel("Average Sales Volume")
plt.tight_layout()
plt.savefig("fig_promotion_impact.png")
plt.close()

print("✅ EDA complete. Visuals saved as PNG files.")
