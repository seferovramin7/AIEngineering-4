
### **Homework Assignment: Analyzing Jakarta's Air Quality**

**Background:**

Jakarta, the capital of Indonesia, frequently faces significant air quality challenges. High levels of pollutants, particularly PM2.5, pose serious health risks to its millions of residents. As a junior data analyst working for the Jakarta Environmental Agency, your task is to analyze recent air quality data to identify trends and highlight critical periods of pollution.

Your findings will help the agency understand the severity of the problem and provide data-driven evidence for potential public health advisories.

**The Dataset:**

You have been provided with a CSV file, `jakarta_aqi_data.csv`, which contains daily measurements for key air pollutants.

* **`Date`**: The date of the measurement.
* **`PM2.5`**: Particulate Matter 2.5 concentration ($µg/m^3$). These are fine, inhalable particles that are a primary health concern.
* **`O3`**: Ozone concentration ($µg/m^3$).
* **`CO`**: Carbon Monoxide concentration ($µg/m^3$).

**Your Tasks:**

You must create a single Python script named `jakarta_air_quality_analysis.py` that performs the following tasks. Your script should print the answers to each question with clear, explanatory labels.

**1. Data Loading and Cleaning:**
    a. Load the `jakarta_aqi_data.csv` file into a Pandas DataFrame.
    b. The `Date` column is currently text; convert it into a proper `datetime` object.
    c. Our sensors were occasionally offline, resulting in missing data (`NaN`). For each pollutant column, fill any missing values with the **average (mean)** value for that specific column.

**2. Descriptive Analysis:**
    a. Calculate and display the basic descriptive statistics (count, mean, std, min, max, etc.) for all pollutant columns to get a general overview of the data.
    b. Based on the statistics, print a statement answering: **Which pollutant has the highest average concentration?**

**3. Health Threshold Analysis:**
    a. According to health guidelines, a PM2.5 level **above 55.5 $µg/m^3$** is considered "Unhealthy". Identify all the days where the PM2.5 level was in the "Unhealthy" range. Print the total count of these days.
    b. Find the exact date with the **highest PM2.5 pollution** in the entire dataset and print the date and its value.

**4. Weekend Effect Analysis:**
    a. A common hypothesis is that pollution levels might be lower during the weekend due to reduced traffic and industrial activity. Investigate this "weekend effect."
    b. Create a new column in your DataFrame called `Day_of_Week`.
    c. Group your data by the `Day_of_Week` and calculate the **average PM2.5 level for each day** (i.e., the average for all Mondays, all Tuesdays, etc.).
    d. Print the results and a concluding sentence stating whether the data suggests a "weekend effect" (i.e., if Saturday and Sunday have noticeably lower average PM2.5 levels).

**Submission Requirements:**

* A single Python file named `jakarta_air_quality_analysis.py`.
* The output of your script should be well-commented and clearly print the answers to each task with descriptive text.


### **Data for `jakarta_aqi_data.csv`**