import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from exceptions import VisualizationError
from file_handling import load_csv

cleaned_data = load_csv('E:\\nimu\\ass7\\clean_covid_data.csv')

def plot_total_cases(cleaned_data):
   try:
        total_cases = cleaned_data.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
        total_cases = total_cases.sort_values(by='Confirmed', ascending=True)
        plt.figure(figsize=(10,10))
        plt.barh(total_cases['Country/Region'].head(50), total_cases['Confirmed'].head(50), color='skyblue', label='Confirmed')
        plt.barh(total_cases['Country/Region'].head(50), total_cases['Deaths'].head(50), color='salmon', label='Deaths')
        plt.barh(total_cases['Country/Region'].head(50), total_cases['Recovered'].head(50), color='lightgreen', label='Recovered')

        plt.xlabel('Total Cases')
        plt.ylabel('Country/Region')
        plt.title('Total COVID-19 Cases by Country/Region')
        plt.tight_layout()
        plt.show()
   except KeyError as e:
        raise VisualizationError("Required columns are missing in the dataframe") from e

    
def plot_top_countries(cleaned_data):
    try:
        top_countries = cleaned_data.groupby('Country/Region')['Confirmed'].sum().reset_index()
        top_countries = top_countries.sort_values(by='Confirmed', ascending=False).head(10)
        plt.figure(figsize=(10,10))
        bars = plt.bar(top_countries['Country/Region'], top_countries['Confirmed'], color='skyblue')

        plt.yticks(top_countries['Confirmed'])

        plt.xlabel('Country/Region')
        plt.ylabel('Total Confirmed Cases')
        plt.title('Top 10 Countries/Regions with Highest COVID-19 Cases')
        plt.tight_layout()
        plt.show()
    except KeyError as e:
        raise VisualizationError("Required columns are missing in the dataframe") from e
    