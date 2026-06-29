# ============================================
# E-Commerce Sales Analysis - Python Analysis
# Tool: Python (pandas, matplotlib, seaborn)
# Dataset: Superstore Dataset (Kaggle)
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------------------
# Step 1: Load Dataset
# -----------------------------------------------
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')

# Fix column name issue
df.columns = df.columns.str.replace('ï»¿', '').str.strip()

print("✅ Dataset loaded successfully!")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")

# -----------------------------------------------
# Step 2: Data Cleaning
# -----------------------------------------------

# Remove duplicates
before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)
print(f"\n✅ Duplicates removed: {before - after}")

# Check missing values
print(f"\n✅ Missing values per column:")
print(df.isnull().sum())

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Month and Year
df['Month'] = df['Order Date'].dt.to_period('M')
df['Year'] = df['Order Date'].dt.year

print("\n✅ Data cleaning complete!")

# -----------------------------------------------
# Create output folder for charts
# -----------------------------------------------
os.makedirs('python/charts', exist_ok=True)

# -----------------------------------------------
# Chart 1: Revenue by Region (Bar Chart)
# -----------------------------------------------
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=region_sales, x='Region', y='Sales', palette='Blues_d')
plt.title('Total Revenue by Region', fontsize=16)
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('python/charts/chart1_revenue_by_region.png')
plt.close()
print("✅ Chart 1 saved!")

# -----------------------------------------------
# Chart 2: Profit Margin by Category (Bar Chart)
# -----------------------------------------------
category = df.groupby('Category').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum')
).reset_index()
category['Profit_Margin'] = (category['Total_Profit'] / category['Total_Sales']) * 100

plt.figure(figsize=(8, 5))
sns.barplot(data=category, x='Category', y='Profit_Margin', palette='Greens_d')
plt.title('Profit Margin by Category (%)', fontsize=16)
plt.xlabel('Category')
plt.ylabel('Profit Margin (%)')
plt.tight_layout()
plt.savefig('python/charts/chart2_profit_margin_by_category.png')
plt.close()
print("✅ Chart 2 saved!")

# -----------------------------------------------
# Chart 3: Monthly Sales Trend (Line Chart)
# -----------------------------------------------
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

plt.figure(figsize=(14, 5))
plt.plot(monthly_sales['Month'], monthly_sales['Sales'], marker='o', color='steelblue')
plt.title('Monthly Sales Trend (2014-2017)', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('python/charts/chart3_monthly_sales_trend.png')
plt.close()
print("✅ Chart 3 saved!")

# -----------------------------------------------
# Chart 4: Orders by Customer Segment (Pie Chart)
# -----------------------------------------------
segment = df.groupby('Segment')['Order ID'].nunique().reset_index()
segment.columns = ['Segment', 'Total_Orders']

plt.figure(figsize=(7, 7))
plt.pie(segment['Total_Orders'], labels=segment['Segment'],
        autopct='%1.1f%%', colors=['#4C72B0', '#55A868', '#C44E52'])
plt.title('Orders by Customer Segment', fontsize=16)
plt.tight_layout()
plt.savefig('python/charts/chart4_orders_by_segment.png')
plt.close()
print("✅ Chart 4 saved!")

# -----------------------------------------------
# Chart 5: Top 10 Products by Sales (Horizontal Bar)
# -----------------------------------------------
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=top_products, x='Sales', y='Product Name', palette='Oranges_d')
plt.title('Top 10 Products by Sales', fontsize=16)
plt.xlabel('Total Sales ($)')
plt.ylabel('Product Name')
plt.tight_layout()
plt.savefig('python/charts/chart5_top10_products.png')
plt.close()
print("✅ Chart 5 saved!")

print("\n🎉 All 5 charts saved in python/charts/ folder!")