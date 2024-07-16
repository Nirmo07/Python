# COVID-19 Pandemic Dataset

## Overview
This dataset provides detailed information on the COVID-19 pandemic across various countries and regions worldwide. It includes metrics such as confirmed cases, deaths, recoveries, active cases, new cases, new deaths, new recoveries, and more.

## Contents
The dataset contains the following columns:
- **Country/Region**: The name of the country or region.
- **Confirmed**: Total confirmed cases of COVID-19.
- **Deaths**: Total deaths due to COVID-19.
- **Recovered**: Total recovered cases from COVID-19.
- **Active**: Active cases (Confirmed - Deaths - Recovered).
- **New cases**: New confirmed cases reported.
- **New deaths**: New deaths reported.
- **New recovered**: New recoveries reported.
- **Deaths / 100 Cases**: Percentage of deaths relative to the confirmed cases.
- **Recovered / 100 Cases**: Percentage of recoveries relative to the confirmed cases.
- **Deaths / 100 Recovered**: Percentage of deaths relative to the recoveries.
- **Confirmed last week**: Confirmed cases one week ago.
- **1 week change**: Change in confirmed cases compared to one week ago.
- **1 week % increase**: Percentage increase in confirmed cases compared to one week ago.
- **WHO Region**: World Health Organization (WHO) region to which the country/region belongs.

## Steps to Run Python Code in VS Code Terminal
1. **Install Python**: Download and install Python from [python.org](https://www.python.org).
2. **Install VS Code**: Download and install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com).
3. **Install Python Extension**: Open VS Code, go to Extensions view (Ctrl + Shift + X), search for "Python", and install the official extension by Microsoft.
4. **Open Your Project**: Open your Python project folder in VS Code (File -> Open Folder...).
5. **Open Terminal**: Press Ctrl + ` (backtick) to open the integrated terminal in VS Code.
6. **Navigate to Your Script**: Use `cd` to navigate to the directory containing your Python script (`cd path/to/your/python/script`).
7. **Run Your Script**: Type `python script_name.py` in the terminal and press Enter to run your Python script (`script_name.py` is your script's filename).
8. **View Output**: Any output or error messages will appear directly in the terminal.

## Data Cleaning Steps
1. **Data Loading**: Load COVID-19 data from a CSV file (`file_path`) into a Pandas DataFrame (`df`) using `pd.read_csv()`.
2. **Initial Data Inspection**:
   - **Display Dataframe**: Print the initial DataFrame (`print(df)`).
   - **Check for Null Values**: Count and print null values in each column with `df.isna().sum()`.
   - **Check for Duplicates**: Count and print duplicate rows with `df.duplicated().sum()`.
3. **Handling Null Values**: Fill null values in `df` with `0` using `df = df.fillna(value=0)`.
4. **Ensuring Data Types**: Convert columns to consistent data types:
   - Convert `int64` columns to `float64` using `astype()`.
5. **Final Cleaned DataFrame**: Print the cleaned DataFrame (`print(df)`).
6. **Exception Handling**:
   - Handle errors using `try-except`:
     - Raise `DataCleaningError` if a critical column is missing (`KeyError`).
     - Raise `DataCleaningError` for any unexpected errors (`Exception`).

## File Handling Steps
1. **Saving Cleaned Data**:
   - Save `df` to a CSV file (`file_path`) without the index using `df.to_csv(file_path, index=False)`.
2. **Loading Cleaned Data**:
   - Load cleaned data from a CSV file (`file_path`) into a DataFrame using `pd.read_csv(file_path)`.

## Exception Handling
1. **DataCleaningError**: Custom exception for data cleaning issues:
   - Handle `KeyError` for missing critical columns.
   - Handle all other unexpected errors with a generic message.

## Example Python Code for Exception Handling
```python
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}. Cannot divide by zero.")
        
print(divide_numbers(10, 2))   # Output: 5.0
print(divide_numbers(5, 0))    # Output: Error: division by zero.
