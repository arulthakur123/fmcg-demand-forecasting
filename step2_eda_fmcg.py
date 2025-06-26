import pandas as pd

# Load the raw dataset
df = pd.read_csv("extended_fmcg_demand_forecasting.csv")

# Preview the dataset
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Rename columns for clarity
df.rename(columns={
    "Date": "date",
    "Product_Category": "product_category",
    "Sales_Volume": "sales_volume",
    "Price": "price",
    "Promotion": "promotion",
    "Store_Location": "store_location",
    "Weekday": "weekday",
    "Supplier_Cost": "supplier_cost",
    "Replenishment_Lead_Time": "replenishment_lead_time",
    "Stock_Level": "stock_level"
}, inplace=True)

# Convert 'date' to datetime
df["date"] = pd.to_datetime(df["date"])

# Check data types
print("\n📦 Data Types:")
print(df.dtypes)

# Check for missing values
print("\n❗ Missing Values:")
print(df.isnull().sum())

# Save cleaned data
df.to_csv("cleaned_fmcg_data.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_fmcg_data.csv'")
