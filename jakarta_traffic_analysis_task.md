# Jakarta Traffic Congestion Analysis - Classroom Task

## Background

Jakarta, Indonesia's capital city, is notorious for having some of the world's worst traffic congestion. The city's 10+ million residents face daily challenges with commuting, leading to significant economic losses, increased pollution, and reduced quality of life. As a data analyst for the Jakarta Transportation Department, you've been tasked with analyzing traffic flow data to identify patterns and propose data-driven solutions.

Your analysis will help the department understand:
- Peak congestion hours across different areas
- Which routes are most problematic
- How weather conditions affect traffic flow
- Recommendations for traffic management improvements

## Dataset Description

You'll work with `jakarta_traffic_data.csv`, which contains daily traffic measurements from major roads and intersections across Jakarta over a 3-month period.

**Columns:**
- `Date`: Date of measurement (YYYY-MM-DD format)
- `Location`: Area/intersection name where data was collected
- `Hour`: Hour of the day (0-23, 24-hour format)
- `Vehicle_Count`: Number of vehicles passing through per hour
- `Average_Speed_kmh`: Average vehicle speed in km/h
- `Weather_Condition`: Weather during measurement (Sunny, Rainy, Cloudy)
- `Is_Weekend`: Boolean indicating if the date falls on weekend (True/False)
- `Road_Type`: Type of road (Highway, Main_Road, Secondary_Road)

## Task Requirements

Create a Python script named `jakarta_traffic_analysis.py` that performs the following analysis steps. Your script should print clear, well-formatted results for each step.

### Step 1: Data Loading and Initial Exploration (Easy)
1. Load the CSV file into a pandas DataFrame
2. Display the first 5 rows to understand the data structure
3. Show basic information about the dataset (number of rows, columns, data types)
4. Check for any missing values in each column

### Step 2: Data Cleaning and Preparation (Easy-Moderate)
1. Convert the `Date` column to datetime format
2. Handle any missing values appropriately:
   - For numerical columns (Vehicle_Count, Average_Speed_kmh): fill with the column mean
   - For categorical columns: fill with the most frequent value
3. Create a new column called `Day_of_Week` that shows the day name (Monday, Tuesday, etc.)
4. Create a new column called `Time_Period` that categorizes hours into:
   - "Morning Rush" (7-9)
   - "Midday" (10-15)
   - "Evening Rush" (16-19)
   - "Night" (20-6)

### Step 3: Traffic Pattern Analysis (Moderate)
1. **Peak Hours Analysis:**
   - Find the hour with the highest average vehicle count across all locations
   - Find the hour with the lowest average speed across all locations
   - Print both findings with explanatory text

2. **Location Comparison:**
   - Calculate the average vehicle count for each location
   - Identify the top 3 most congested locations (highest vehicle count)
   - Identify the location with the slowest average speed

3. **Weekend vs Weekday Analysis:**
   - Compare average vehicle counts between weekends and weekdays
   - Compare average speeds between weekends and weekdays
   - Determine if there's a significant difference and state your conclusion

### Step 4: Weather Impact Analysis (Moderate)
1. Group the data by weather condition and calculate:
   - Average vehicle count for each weather condition
   - Average speed for each weather condition
2. Determine which weather condition causes the most severe traffic (lowest speed)
3. Calculate the percentage difference in average speed between sunny and rainy conditions

### Step 5: Road Type Performance (Moderate)
1. Analyze traffic patterns by road type:
   - Average vehicle count per road type
   - Average speed per road type
2. Identify which road type handles the most traffic volume
3. Determine which road type maintains the highest average speed

### Step 6: Rush Hour Deep Dive (Moderate-Advanced)
1. Filter data for only "Morning Rush" and "Evening Rush" periods
2. For each rush period:
   - Find the most congested location (highest vehicle count)
   - Calculate the average speed during rush hours
3. Compare morning vs evening rush hour severity
4. Identify the day of the week with the worst evening rush hour traffic

### Step 7: Insights and Recommendations (Advanced)
Based on your analysis, provide:
1. **Three key findings** about Jakarta's traffic patterns
2. **Two data-driven recommendations** for improving traffic flow
3. **One surprising insight** from your analysis

## Output Format

Your script should produce well-formatted output with clear headers for each section. Example format:

```
=== JAKARTA TRAFFIC ANALYSIS REPORT ===

STEP 1: DATA OVERVIEW
- Dataset contains X rows and Y columns
- Data covers period from [start_date] to [end_date]
- Missing values found in: [list columns with missing values]

STEP 2: DATA CLEANING COMPLETED
- Date column converted to datetime format
- Missing values handled: [explain approach]
- New columns created: Day_of_Week, Time_Period

[Continue with similar formatting for each step...]
```

## Submission Requirements

- Single Python file: `jakarta_traffic_analysis.py`
- Code should be well-commented explaining each major step
- Output should be clear and professional, suitable for presentation to city officials
- Include error handling for file loading and data processing

## Learning Objectives

By completing this task, you will:
- Practice real-world data loading and cleaning techniques
- Learn to handle different data types (dates, booleans, categories)
- Apply groupby operations for meaningful analysis
- Create derived columns for better insights
- Present data analysis results in a professional format
- Understand how data analysis can inform urban planning decisions

## Extension Challenges (Optional)

For advanced students:
1. Create visualizations using matplotlib to show traffic patterns
2. Calculate correlation between weather and traffic speed
3. Identify the optimal time windows for road maintenance (lowest traffic)
4. Propose a traffic light timing optimization based on hourly patterns

---

*This task simulates real-world data analysis work that transportation departments use to make infrastructure and policy decisions. The skills you develop here are directly applicable to urban planning, logistics, and smart city initiatives.* 