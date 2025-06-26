# 🛒 FMCG Demand Forecasting – India 🇮🇳

This project applies **time series forecasting**, **exploratory data analysis**, and **automated dashboard reporting** to analyze and forecast **FMCG product demand** across different regions in India.

---

## 📌 Objective

To enable data-driven decision-making in inventory planning and replenishment by:
- Forecasting **daily sales demand**
- Understanding demand by **product category**, **location**, and **promotions**
- Building a **dynamic dashboard** for real-time insights

---

## 📁 Project Structure

```
fmcg_demand_forecasting/
│
├── cleaned_fmcg_data.csv                    # Cleaned dataset for analysis
├── step1_data_load.py                       # Script to load and inspect raw data
├── step2_data_cleaning.py                   # Preprocessing and formatting
├── step3_eda.py                             # Exploratory Data Analysis & visuals
├── fmcg_dashboard.twb                       # Tableau workbook for dashboard
├── *.png                                    # All saved EDA visuals
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation
```

---

## 📊 Dataset Overview

**Source**: [Kaggle FMCG Dataset](https://www.kaggle.com/datasets/krishanukalita/fmcg-sales-demand-forecasting-and-optimization)

We used the `extended_fmcg_demand_forecasting.csv` file containing:
- 📆 Date (daily records)
- 🧴 Product Category
- 🧮 Sales Volume
- 💰 Price & Supplier Cost
- 📍 Store Location (Urban, Rural, Suburban)
- 📦 Stock Level
- 📢 Promotion Status
- ⏱️ Lead Time (replenishment)
- 🗓️ Weekday

---

## 🧼 Data Preprocessing

- Converted `Date` column to `datetime` format
- Standardized column names to snake_case
- Verified and cleaned all missing or inconsistent values
- Saved clean dataset as `cleaned_fmcg_data.csv`

✅ No missing data  
✅ Consistent data types  
✅ Ready for time series modeling and dashboarding

---

## 📈 Exploratory Data Analysis (EDA)

Python libraries: `Pandas`, `Seaborn`, `Matplotlib`

### 🔹 1. Sales by Product Category

![Category Sales](category_sales.png)

---

### 🔹 2. Sales by Store Location

![Location Sales](location_sales.png)

---

### 🔹 3. Impact of Promotions on Sales

![Promotion Impact](promotion_sales.png)

---

## ⏳ Time Series Forecasting (Next Steps)

We will apply:
- ARIMA or SARIMA models
- Exponential Smoothing
- Store-level demand forecasting

👉 Forecasting will help in **procurement**, **stock planning**, and **supplier management**.

---

## 📊 Tableau Dashboard

This project includes a Tableau dashboard showing:

- 🔹 Total Sales by Product Category
- 🔹 Daily Sales Trends
- 🔹 Promotion Impact Visualized
- 🔹 Inventory Stock vs Sales Insights

📁 Download dashboard: `fmcg_dashboard.twb`  
🔗 [View Tableau Dashboard Online](https://public.tableau.com/views/your-dashboard-link-here) *(if published)*

![Dashboard Preview](fmcg_dashboard_preview.png)

> Replace with a real preview image of your dashboard in PNG form

---

## ⚙️ Tech Stack

- **Python** (Pandas, Seaborn, Statsmodels)
- **Tableau Public**
- **Git & GitHub**
- **Jupyter / VS Code**

---

## 📌 Key Takeaways

- 🧠 Sales patterns are highly influenced by **product type** and **location**
- 🛍️ Promotions lead to short-term sales spikes
- 🧾 Tableau dashboards automate insights for FMCG managers

---

## 🧠 Future Work

- Incorporate **stock-level forecasting**
- Add **seasonality decomposition**
- Create **alerts for low stock levels**
- Extend dashboard to support **multi-region filtering**

---

## 👤 Author

**Arul Thakur**  
🔗 GitHub: [arulthakur123](https://github.com/arulthakur123)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
