# indonesia_rice_price_analysis.py
#
# GOAL: To analyze rice price data across Indonesian provinces with highly
# explanatory logging, creating a self-documenting report of the findings.

import pandas as pd
import numpy as np
from datetime import datetime

def analyze_rice_prices(file_path):
    """
    Loads, cleans, and analyzes rice price data, printing a detailed log of each step.
    """
    # --- Report Header ---
    print("=" * 70)
    print("INDONESIAN RICE PRICE STABILITY ANALYSIS REPORT")
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    try:
        # --- Step 1: Data Loading ---
        print("\n[PHASE 1: DATA LOADING AND PREPARATION]")
        print(f"--> Action: Loading dataset from the file '{file_path}'...")
        df = pd.read_csv(file_path)
        print(f"--> Success: Data loaded successfully. Found {df.shape[0]} rows and {df.shape[1]} columns.")
        print("-" * 70)

        # --- Step 2: Data Cleaning and Validation ---
        print("\n[PHASE 2: DATA CLEANING AND VALIDATION]")
        print("--> Goal: Ensure data is accurate and ready for time-series analysis.")

        # Convert 'Date' column
        print("--> Action: Converting 'Date' column from text to a proper datetime format.")
        df['Date'] = pd.to_datetime(df['Date'])
        print("--> Success: 'Date' column is now in datetime format.")

        # Check for missing values before cleaning
        missing_values = df['Price_per_Kg'].isnull().sum()
        print(f"--> Action: Checking for missing values in 'Price_per_Kg' column...")
        if missing_values > 0:
            print(f"--> Result: Found {missing_values} missing price entries. These must be handled.")
            # Handle missing values using a forward-fill strategy
            print("--> Action: Handling missing values using a forward-fill method grouped by province.")
            print("--> Why: This assumes a missing price is the same as the last known price for that specific province, preventing data from one region affecting another.")
            df['Price_per_Kg'] = df.groupby('Province')['Price_per_Kg'].transform(
                lambda x: x.ffill().bfill()
            )
            # Verify that no missing values remain
            if df['Price_per_Kg'].isnull().sum() == 0:
                print("--> Success: All missing price values have been handled.")
            else:
                print("--> Warning: Some missing values could not be filled.")
        else:
            print("--> Success: No missing values found in the price column.")
        print("-" * 70)


        # --- Step 3: National Level Analysis ---
        print("\n[PHASE 3: NATIONAL LEVEL ANALYSIS]")
        print("--> Goal: Understand the overall price trend across the entire country.")
        print("--> Action: Grouping data by 'Date' to calculate the daily national average price.")

        national_average_daily = df.groupby('Date')['Price_per_Kg'].mean().round(2)
        overall_national_avg = national_average_daily.mean()

        print("--> Success: National average trend calculated.")
        print(f"--> Insight: The overall national average price during this period was: Rp {overall_national_avg:,.2f} per Kg.")
        print("-" * 70)


        # --- Step 4: Provincial Level Analysis for Volatility ---
        print("\n[PHASE 4: PROVINCIAL LEVEL ANALYSIS]")
        print("--> Goal: Identify price volatility and average costs at the regional level.")
        print("--> Why: National averages can hide regional extremes. This analysis pinpoints specific provinces that require attention.")
        print("--> Action: Grouping data by 'Province' and calculating key statistics (mean, std, min, max).")
        print("--> Key Metric: Standard Deviation ('std') is used to measure volatility. A higher value means less stable prices.")

        provincial_stats = df.groupby('Province')['Price_per_Kg'].agg(['mean', 'std', 'min', 'max'])
        provincial_stats.rename(columns={'mean': 'Average_Price', 'std': 'Volatility (Std_Dev)', 'min': 'Min_Price', 'max': 'Max_Price'}, inplace=True)
        provincial_stats.fillna(0, inplace=True)

        print("--> Success: Provincial statistics calculated. Preparing final report...")
        print("-" * 70)


        # --- Step 5: Final Report Generation ---
        most_volatile = provincial_stats.sort_values(by='Volatility (Std_Dev)', ascending=False)
        most_expensive = provincial_stats.sort_values(by='Average_Price', ascending=False)

        print("\n" + "="*20 + " FINAL REPORT " + "="*20)
        print("\n[--- FINDING 1: MOST VOLATILE PROVINCES ---]")
        print("The following provinces exhibit the highest price instability. These regions may be")
        print("experiencing supply chain disruptions or other market pressures, making them a priority for review.")
        print(most_volatile.head().to_string(formatters={'Average_Price':'Rp {:,.2f}'.format, 'Volatility (Std_Dev)':'{:.2f}'.format, 'Min_Price':'Rp {:,.2f}'.format, 'Max_Price':'Rp {:,.2f}'.format}))

        print("\n[--- FINDING 2: MOST EXPENSIVE PROVINCES ---]")
        print("The following provinces have the highest average rice prices, indicating a greater")
        print("financial burden on consumers for this essential food item.")
        print(most_expensive.head().to_string(formatters={'Average_Price':'Rp {:,.2f}'.format, 'Volatility (Std_Dev)':'{:.2f}'.format, 'Min_Price':'Rp {:,.2f}'.format, 'Max_Price':'Rp {:,.2f}'.format}))

        print("\n" + "="*54)
        print("\n[--- SUMMARY ---]")
        print("This analysis has successfully identified key provinces based on rice price volatility and average cost.")
        print(f"The most volatile province was '{most_volatile.index[0]}', while the most expensive was '{most_expensive.index[0]}'.")
        print("These data-driven insights can be used to inform targeted economic policies and ensure food security.")

    except FileNotFoundError:
        print(f"\n[CRITICAL ERROR] File Not Found: The file '{file_path}' was not found.")
        print("Please ensure the data file is in the same directory as the script and is named correctly.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] An unexpected error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    # Define the path to the dataset
    data_file = 'indonesia_rice_prices.csv'
    analyze_rice_prices(data_file)