import pandas as pd
from data_cleaning import clean_covid_data
from file_handling import save_cleaned_data, load_cleaned_data
import matplotlib.pyplot as plt

file_path = 'E:\\nimu\\ass7\\country_wise_latest.csv'
cleaned_data = clean_covid_data(file_path)  

save_cleaned_data(cleaned_data, 'E:\\nimu\\ass7\\clean_covid_data.csv') 
cleaned_data = load_cleaned_data('E:\\nimu\\ass7\\clean_covid_data.csv')

print("\nAnalysis of the COVID-19 Dataset:")
total_confirmed = cleaned_data['Confirmed'].sum()
total_deaths = cleaned_data['Deaths'].sum()
total_recovered = cleaned_data['Recovered'].sum()
print(f"Total Confirmed Cases: {total_confirmed}")
print(f"Total Deaths: {total_deaths}")
print(f"Total Recovered: {total_recovered}")

country_cases = cleaned_data.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False)
highest_cases_country = country_cases.index[0]
highest_cases_count = country_cases.max()
lowest_cases_country = country_cases.index[-1]
lowest_cases_count = country_cases.min()
print(f"Country/State with highest cases: {highest_cases_country}, Cases: {highest_cases_count}")
print(f"Country/State with lowest cases: {lowest_cases_country}, Cases: {lowest_cases_count}")
