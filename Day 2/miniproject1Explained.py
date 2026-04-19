# Combination of Numpy + Pandas + Matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic sales data
# Created the data from 1st Jan 2024 to 31st Dec 2024
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
n_days = len(dates)

# Create dataset - Dataframe
data = {
    'Date': dates,
    # Product A - Random Numbers b/w 20 to 100 for 365 days (One Year)
    'Product_A': np.random.randint(20, 100, n_days),
    # Product B - Random Numbers b/w 15 to 80 for 365 days (One Year)
    'Product_B': np.random.randint(15, 80, n_days),
    # Product C - Random Numbers b/w 5 to 50 for 365 days (One Year)
    'Product_C': np.random.randint(5, 50, n_days),
    # Assigned 4 regions: North, South, East & West
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n_days),
    # Discount: 0, 5, 10, 15 & 20 - Randomly assigned
    'Discount': np.random.choice([0, 5, 10, 15, 20], n_days, p=[0.6, 0.2, 0.1, 0.05, 0.05])
}

df = pd.DataFrame(data)

print(f"Dataset contains:\n {df}")

# Calculate total sales and revenue
# Calculate the total units sold for the individual day
df['Total_Units'] = df['Product_A'] + df['Product_B'] + df['Product_C']
# Product A costs 50, Product B costs 75, Product C costs 100

# Revenue: Multiply the number of products with actual cost - discount
df['Revenue'] = (df['Product_A'] * 50 + df['Product_B'] * 75 + df['Product_C'] * 100) * (1 - df['Discount']/100)

print("Total Units Sold on each day along with Revenue: \n", df['Total_Units'], df['Revenue'])

# Extract time features
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Quarter'] = df['Date'].dt.quarter

print("="*60)
print("SALES DATA ANALYSIS DASHBOARD")
print("="*60)
print(f"Dataset Shape: {df.shape}")
print(f"Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Total Revenue: ${df['Revenue'].sum():,.2f}")
print(f"Total Units Sold: {df['Total_Units'].sum():,}")
print("="*60)