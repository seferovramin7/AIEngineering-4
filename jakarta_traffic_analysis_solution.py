"""
Jakarta Traffic Congestion Analysis - Solution
=============================================

This script analyzes Jakarta traffic data to identify patterns and provide insights
for traffic management and urban planning decisions.

Author: Data Analysis Course
Date: 2024
"""

import pandas as pd
import numpy as np

def print_section_header(title):
    """Helper function to print formatted section headers"""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)

def print_subsection(title):
    """Helper function to print formatted subsection headers"""
    print(f"\n--- {title} ---")

# ============================================================================
# STEP 1: DATA LOADING AND INITIAL EXPLORATION
# ============================================================================

print_section_header("STEP 1: DATA LOADING AND INITIAL EXPLORATION")

try:
    # Load the CSV file
    df = pd.read_csv('jakarta_traffic_data.csv')
    print("✓ Successfully loaded jakarta_traffic_data.csv")
    
    # Display first 5 rows
    print_subsection("First 5 rows of the dataset")
    print(df.head())
    
    # Basic dataset information
    print_subsection("Dataset Information")
    print(f"Dataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    
    print("\nColumn data types:")
    print(df.dtypes)
    
    # Check for missing values
    print_subsection("Missing Values Check")
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    for column, missing_count in missing_values.items():
        if missing_count > 0:
            print(f"  {column}: {missing_count} missing values")
        else:
            print(f"  {column}: No missing values")
    
except FileNotFoundError:
    print("❌ Error: jakarta_traffic_data.csv file not found!")
    print("Please ensure the file is in the same directory as this script.")
    exit()

# ============================================================================
# STEP 2: DATA CLEANING AND PREPARATION
# ============================================================================

print_section_header("STEP 2: DATA CLEANING AND PREPARATION")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])
print("✓ Date column converted to datetime format")

# Handle missing values
print_subsection("Handling Missing Values")

# For numerical columns: fill with mean
numerical_cols = ['Vehicle_Count', 'Average_Speed_kmh']
for col in numerical_cols:
    if df[col].isnull().sum() > 0:
        mean_value = df[col].mean()
        df[col].fillna(mean_value, inplace=True)
        print(f"✓ Filled {col} missing values with mean: {mean_value:.1f}")

# For categorical columns: fill with most frequent value
categorical_cols = ['Weather_Condition', 'Is_Weekend']
for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        mode_value = df[col].mode()[0]
        df[col].fillna(mode_value, inplace=True)
        print(f"✓ Filled {col} missing values with mode: {mode_value}")

# Create Day_of_Week column
df['Day_of_Week'] = df['Date'].dt.day_name()
print("✓ Created Day_of_Week column")

# Create Time_Period column
def categorize_time_period(hour):
    """Categorize hours into time periods"""
    if 7 <= hour <= 9:
        return "Morning Rush"
    elif 10 <= hour <= 15:
        return "Midday"
    elif 16 <= hour <= 19:
        return "Evening Rush"
    else:
        return "Night"

df['Time_Period'] = df['Hour'].apply(categorize_time_period)
print("✓ Created Time_Period column")

print_subsection("Data Cleaning Summary")
print(f"✓ All missing values handled")
print(f"✓ New columns created: Day_of_Week, Time_Period")
print(f"✓ Final dataset shape: {df.shape[0]} rows × {df.shape[1]} columns")

# ============================================================================
# STEP 3: TRAFFIC PATTERN ANALYSIS
# ============================================================================

print_section_header("STEP 3: TRAFFIC PATTERN ANALYSIS")

# Peak Hours Analysis
print_subsection("Peak Hours Analysis")

# Hour with highest average vehicle count
hourly_vehicle_avg = df.groupby('Hour')['Vehicle_Count'].mean()
peak_vehicle_hour = hourly_vehicle_avg.idxmax()
peak_vehicle_count = hourly_vehicle_avg.max()

print(f"🚗 Peak traffic hour: {peak_vehicle_hour}:00 with {peak_vehicle_count:.0f} vehicles on average")

# Hour with lowest average speed
hourly_speed_avg = df.groupby('Hour')['Average_Speed_kmh'].mean()
slowest_hour = hourly_speed_avg.idxmin()
slowest_speed = hourly_speed_avg.min()

print(f"🐌 Slowest traffic hour: {slowest_hour}:00 with {slowest_speed:.1f} km/h average speed")

# Location Comparison
print_subsection("Location Comparison")

location_stats = df.groupby('Location').agg({
    'Vehicle_Count': 'mean',
    'Average_Speed_kmh': 'mean'
}).round(1)

print("Average traffic metrics by location:")
print(location_stats.sort_values('Vehicle_Count', ascending=False))

# Top 3 most congested locations
top_congested = location_stats.sort_values('Vehicle_Count', ascending=False).head(3)
print(f"\n🚦 Top 3 most congested locations:")
for i, (location, data) in enumerate(top_congested.iterrows(), 1):
    print(f"  {i}. {location}: {data['Vehicle_Count']:.0f} vehicles/hour")

# Location with slowest speed
slowest_location = location_stats.sort_values('Average_Speed_kmh').index[0]
slowest_location_speed = location_stats.loc[slowest_location, 'Average_Speed_kmh']
print(f"\n🐢 Slowest location: {slowest_location} ({slowest_location_speed:.1f} km/h)")

# Weekend vs Weekday Analysis
print_subsection("Weekend vs Weekday Analysis")

weekend_comparison = df.groupby('Is_Weekend').agg({
    'Vehicle_Count': 'mean',
    'Average_Speed_kmh': 'mean'
}).round(1)

weekday_vehicles = weekend_comparison.loc[False, 'Vehicle_Count']
weekend_vehicles = weekend_comparison.loc[True, 'Vehicle_Count']
weekday_speed = weekend_comparison.loc[False, 'Average_Speed_kmh']
weekend_speed = weekend_comparison.loc[True, 'Average_Speed_kmh']

print("Weekend vs Weekday comparison:")
print(f"  Weekdays: {weekday_vehicles:.0f} vehicles/hour, {weekday_speed:.1f} km/h")
print(f"  Weekends: {weekend_vehicles:.0f} vehicles/hour, {weekend_speed:.1f} km/h")

vehicle_diff_pct = ((weekend_vehicles - weekday_vehicles) / weekday_vehicles) * 100
speed_diff_pct = ((weekend_speed - weekday_speed) / weekday_speed) * 100

print(f"\n📊 Analysis:")
print(f"  Vehicle count difference: {vehicle_diff_pct:+.1f}% on weekends")
print(f"  Speed difference: {speed_diff_pct:+.1f}% on weekends")

if weekend_vehicles < weekday_vehicles and weekend_speed > weekday_speed:
    print("  ✓ Clear weekend effect: Less traffic and higher speeds on weekends")
else:
    print("  ⚠️ Weekend effect is not clearly evident in this dataset")

# ============================================================================
# STEP 4: WEATHER IMPACT ANALYSIS
# ============================================================================

print_section_header("STEP 4: WEATHER IMPACT ANALYSIS")

weather_stats = df.groupby('Weather_Condition').agg({
    'Vehicle_Count': 'mean',
    'Average_Speed_kmh': 'mean'
}).round(1)

print("Traffic patterns by weather condition:")
print(weather_stats.sort_values('Average_Speed_kmh'))

# Weather condition with most severe traffic (lowest speed)
worst_weather = weather_stats.sort_values('Average_Speed_kmh').index[0]
worst_weather_speed = weather_stats.loc[worst_weather, 'Average_Speed_kmh']

print(f"\n🌧️ Most severe traffic weather: {worst_weather} ({worst_weather_speed:.1f} km/h)")

# Compare sunny vs rainy conditions
if 'Sunny' in weather_stats.index and 'Rainy' in weather_stats.index:
    sunny_speed = weather_stats.loc['Sunny', 'Average_Speed_kmh']
    rainy_speed = weather_stats.loc['Rainy', 'Average_Speed_kmh']
    speed_reduction = ((sunny_speed - rainy_speed) / sunny_speed) * 100
    
    print(f"\n☀️ vs 🌧️ Speed comparison:")
    print(f"  Sunny weather: {sunny_speed:.1f} km/h")
    print(f"  Rainy weather: {rainy_speed:.1f} km/h")
    print(f"  Speed reduction in rain: {speed_reduction:.1f}%")

# ============================================================================
# STEP 5: ROAD TYPE PERFORMANCE
# ============================================================================

print_section_header("STEP 5: ROAD TYPE PERFORMANCE")

road_stats = df.groupby('Road_Type').agg({
    'Vehicle_Count': 'mean',
    'Average_Speed_kmh': 'mean'
}).round(1)

print("Traffic performance by road type:")
print(road_stats.sort_values('Vehicle_Count', ascending=False))

# Road type with most traffic volume
highest_volume_road = road_stats.sort_values('Vehicle_Count', ascending=False).index[0]
highest_volume_count = road_stats.loc[highest_volume_road, 'Vehicle_Count']

print(f"\n🛣️ Highest traffic volume: {highest_volume_road} ({highest_volume_count:.0f} vehicles/hour)")

# Road type with highest speed
fastest_road = road_stats.sort_values('Average_Speed_kmh', ascending=False).index[0]
fastest_road_speed = road_stats.loc[fastest_road, 'Average_Speed_kmh']

print(f"🏃 Fastest road type: {fastest_road} ({fastest_road_speed:.1f} km/h)")

# ============================================================================
# STEP 6: RUSH HOUR DEEP DIVE
# ============================================================================

print_section_header("STEP 6: RUSH HOUR DEEP DIVE")

# Filter for rush hours only
rush_hours = df[df['Time_Period'].isin(['Morning Rush', 'Evening Rush'])]

print_subsection("Rush Hour Analysis by Period")

for period in ['Morning Rush', 'Evening Rush']:
    period_data = rush_hours[rush_hours['Time_Period'] == period]
    
    # Most congested location during this period
    location_congestion = period_data.groupby('Location')['Vehicle_Count'].mean()
    most_congested = location_congestion.idxmax()
    congestion_level = location_congestion.max()
    
    # Average speed during this period
    avg_speed = period_data['Average_Speed_kmh'].mean()
    
    print(f"\n{period}:")
    print(f"  Most congested location: {most_congested} ({congestion_level:.0f} vehicles/hour)")
    print(f"  Average speed: {avg_speed:.1f} km/h")

# Compare morning vs evening rush severity
morning_rush = rush_hours[rush_hours['Time_Period'] == 'Morning Rush']
evening_rush = rush_hours[rush_hours['Time_Period'] == 'Evening Rush']

morning_avg_speed = morning_rush['Average_Speed_kmh'].mean()
evening_avg_speed = evening_rush['Average_Speed_kmh'].mean()
morning_avg_vehicles = morning_rush['Vehicle_Count'].mean()
evening_avg_vehicles = evening_rush['Vehicle_Count'].mean()

print_subsection("Morning vs Evening Rush Comparison")
print(f"Morning Rush: {morning_avg_vehicles:.0f} vehicles/hour, {morning_avg_speed:.1f} km/h")
print(f"Evening Rush: {evening_avg_vehicles:.0f} vehicles/hour, {evening_avg_speed:.1f} km/h")

if evening_avg_vehicles > morning_avg_vehicles:
    print("🌆 Evening rush hour is more congested than morning rush")
else:
    print("🌅 Morning rush hour is more congested than evening rush")

# Worst day for evening rush hour
evening_by_day = evening_rush.groupby('Day_of_Week').agg({
    'Vehicle_Count': 'mean',
    'Average_Speed_kmh': 'mean'
}).round(1)

worst_evening_day = evening_by_day.sort_values('Average_Speed_kmh').index[0]
worst_evening_speed = evening_by_day.loc[worst_evening_day, 'Average_Speed_kmh']

print(f"\n📅 Worst evening rush day: {worst_evening_day} ({worst_evening_speed:.1f} km/h)")

# ============================================================================
# STEP 7: INSIGHTS AND RECOMMENDATIONS
# ============================================================================

print_section_header("STEP 7: INSIGHTS AND RECOMMENDATIONS")

print_subsection("🔍 THREE KEY FINDINGS")

print("1. PEAK CONGESTION PATTERNS:")
print(f"   • Hour {peak_vehicle_hour}:00 has the highest traffic volume ({peak_vehicle_count:.0f} vehicles)")
print(f"   • Hour {slowest_hour}:00 has the slowest speeds ({slowest_speed:.1f} km/h)")
print(f"   • {slowest_location} is consistently the most problematic location")

print("\n2. WEATHER IMPACT:")
if 'Sunny' in weather_stats.index and 'Rainy' in weather_stats.index:
    print(f"   • Rainy weather reduces average speeds by {speed_reduction:.1f}%")
    print(f"   • Traffic moves {speed_reduction:.1f}% slower during rain")
else:
    print("   • Weather conditions significantly affect traffic flow patterns")

print("\n3. INFRASTRUCTURE PERFORMANCE:")
print(f"   • {highest_volume_road}s handle the most traffic ({highest_volume_count:.0f} vehicles/hour)")
print(f"   • {fastest_road}s maintain the highest speeds ({fastest_road_speed:.1f} km/h)")
print(f"   • Weekend traffic is {abs(vehicle_diff_pct):.1f}% {'lower' if vehicle_diff_pct < 0 else 'higher'} than weekdays")

print_subsection("💡 TWO DATA-DRIVEN RECOMMENDATIONS")

print("1. IMPLEMENT DYNAMIC TRAFFIC MANAGEMENT:")
print(f"   • Deploy additional traffic officers at {slowest_location} during hour {slowest_hour}:00")
print(f"   • Adjust traffic light timing during peak hours ({peak_vehicle_hour}:00)")
print("   • Consider congestion pricing during rush hours to distribute traffic")

print("\n2. WEATHER-RESPONSIVE TRAFFIC SYSTEMS:")
if 'Rainy' in weather_stats.index:
    print("   • Activate rain-specific traffic protocols when weather forecasts predict rain")
    print("   • Increase traffic light cycle times during rainy conditions")
    print("   • Deploy emergency response teams proactively during rainy weather")

print_subsection("🎯 ONE SURPRISING INSIGHT")

# Calculate the most surprising finding
time_periods_performance = df.groupby('Time_Period')['Average_Speed_kmh'].mean().sort_values(ascending=False)
best_time = time_periods_performance.index[0]
best_time_speed = time_periods_performance.iloc[0]

print(f"UNEXPECTED TRAFFIC FLOW PATTERN:")
print(f"• {best_time} period has the best traffic flow ({best_time_speed:.1f} km/h average)")

if best_time == "Night":
    print("• This suggests potential for promoting night-time business hours")
    print("• Consider incentivizing 24-hour operations for non-essential services")
elif best_time == "Midday":
    print("• This indicates good potential for flexible working hours")
    print("• Businesses could benefit from staggered lunch breaks")

print("\n" + "="*60)
print(" ANALYSIS COMPLETE - JAKARTA TRAFFIC INSIGHTS GENERATED")
print("="*60)
print("\n📊 This analysis provides actionable insights for:")
print("   • Traffic management optimization")
print("   • Infrastructure planning decisions") 
print("   • Public transportation scheduling")
print("   • Urban development policies") 