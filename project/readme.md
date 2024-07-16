# COVID-19 Pandemic Dataset

## Overview
This project is an interactive online application that uses Streamlit to generate a dashboard for data visualization related to lung cancer, based on Python. The dataset contains variables for age, gender, anxiety, chronic illness, smoking habits, and lung cancer symptoms. Data analysis, file management, exception handling, data cleaning, and visualization are all covered by modules on the dashboard. Lung cancer trends can be predicted and understood by users by loading data from a CSV file, displaying the dataset, and exploring important insights through a variety of plots and charts.

## Contents
The dataset contains the following columns:
- **GENDER**: Gender of the patient.
- **AGE**: Age of the patient.
- **SMOKING**: Smoking habits of the patient.
- **YELLOW_FINGERS**: Presence of yellow fingers (indicative of smoking).
- **ANXIETY**: Anxiety levels of the patient.
- **PEER_PRESSURE**: Influence of peer pressure on the patient.
- **CHRONIC DISEASE**: Presence of chronic diseases.
- **FATIGUE**: Levels of fatigue experienced by the patient.
- **ALLERGY**: Presence of allergies.
- **WHEEZING**: Presence of wheezing.
- **ALCOHOL CONSUMING**: Alcohol consumption habits.
- **COUGHING**: Frequency of coughing.
- **SHORTNESS OF BREATH**: Incidence of shortness of breath.
- **SWALLOWING DIFFICULTY**: Difficulty in swallowing.
- **CHEST PAIN**: Presence of chest pain.
- **LUNG_CANCER**: Indicates whether the patient has lung cancer (positive or negative).
- **cause**: Cause of lung cancer (if available).


## Steps to Create a Lung Cancer Analysis Dashboard using Streamlit (dashboard.py)

#### **Setup and Dependencies**
- Install necessary Python packages such as **Streamlit**, **NumPy**, **Pandas**, **Matplotlib**, and **Altair**.
- Import the required libraries in your Python script.

#### **Load and Prepare Data**
- Load the cleaned lung cancer dataset (e.g., **survey_lung_cancer_cleaned_data.csv**) using **Pandas**.
- Optionally, perform initial data analysis or preprocessing as needed.

#### **Define Dashboard Functions**
- Create a function to display dataset information and analysis results.
- Develop a function to generate various visualizations based on user input.

#### Build the Streamlit App
- Use Streamlit functions (e.g., **st.title()**, **st.write()**, **st.sidebar.selectbox()**) to create the layout and interactive elements of the dashboard.
- Designate sections for displaying dataset information, charts, and interactive components based on user selections.

#### Integrate Visualization
- Embed visualizations using **Matplotlib** and **Altair** within your Streamlit app for a dynamic and interactive visual representation of the data.

#### Run and Test
- Run the Streamlit app locally with the command **streamlit run dashboard.py** to test functionality and ensure the dashboard displays correctly.

#### Set Background Image (Optional)
- Implement a function to set a custom background image for the dashboard to enhance visual appeal.


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
