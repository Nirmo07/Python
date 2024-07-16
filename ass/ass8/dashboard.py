import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64
import matplotlib.pyplot as plt 
from analysis import analysis
import altair as alt
from matplotlib import cm 

df = pd.read_csv("E:\\nimu\\ass7\\clean_covid_data.csv")
analysis_results = analysis(df)


def stream(df, analysis_results):
    st.title("Covid-19 Dataset Analysis")
    st.write("----------------------------")
    st.subheader("Original Cleaned Dataset:")
    st.write(df)
    st.write(f"Total Confirmed Cases: {analysis_results['total_confirmed']}")
    st.write(f"Total Deaths: {analysis_results['total_deaths']}")
    st.write(f"Total Recovered: {analysis_results['total_recovered']}")
    st.write(f"Country/State with highest cases: {analysis_results['highest_cases_country']} Cases: {analysis_results['highest_cases_count']}")
    st.write(f"Country/State with lowest cases: {analysis_results['lowest_cases_country']} Cases: {analysis_results['lowest_cases_count']}")

def ploting(df):
    st.header("Plotting based on Dataset:")
    a = st.selectbox("Select:", df.columns, index=9)
    st.subheader("Bar Graph")
    st.bar_chart(df[a].head(25), color='#90EE90')

    st.subheader("Line Graph")
    st.line_chart(df[a].head(25), color='#90EE90')

    st.subheader("Scatter Graph")
    st.scatter_chart(df[a].head(25), color='#90EE90')
    
    st.subheader("Pie Graph")
    cmap = cm.get_cmap("tab20")
    plt.figure(figsize=[10, 10])
    labels = df['Country/Region'].value_counts().head(30).index
    values = df[a].value_counts().head(30).values
    colors = [cmap(i / len(labels)) for i in range(len(labels))]
    plt.pie(values, labels=labels, colors=colors, autopct='%1.2f%%',wedgeprops = {'edgecolor': 'black', 'linewidth': 1})
    st.pyplot(plt)
    
def user_interaction(df):
    st.header("Plotting based on Country/Region:")
    g = st.selectbox("Select:", df['Country/Region'], index=1)
    if g:
        h=st.selectbox("Select Cases:",['Confirmed','Deaths','Recovered'], index=0)
        if g and h:
            country_data = df[df['Country/Region'] == g]
            
            st.subheader(f"{h} cases in {g}:")
            st.write(country_data[['Country/Region', h]])
            
        st.subheader(f"Plot of {h} cases in {g}:")
        bar_data = country_data.head(25)
        chart = alt.Chart(bar_data).mark_bar(size=30).encode(
            x=alt.X('Country/Region', title='Country/Region', axis=alt.Axis(labelAngle=0)),
            y=alt.Y(h, title=h),
            tooltip=['Country/Region', h]
        ).properties(
            width=600,
            height=400
        )
        
        # Adjust axis labels and title font sizes
        chart = chart.configure_axis(
            labelFontSize=12,
            titleFontSize=14
        )
        
        # Display Altair chart
        st.altair_chart(chart, use_container_width=True)
        
   
    st.subheader("Total Confirmed, Deaths, and Recovered Cases Over Time:")
    st.image('E:\\nimu\\ass8\\total_cases.png')
    
    st.subheader("Top 10 Countries with Highest Number of Cases:")
    st.image('E:\\nimu\\ass8\\top_countries.png')
            
st.sidebar.title("Sidebar")
choice = st.sidebar.selectbox('Select one:', {"Dataset": 'Dataset', "Plot": 'Plot',"Chart":'Chart'})
if choice == "Dataset":
    stream(df, analysis_results)
elif choice == "Plot":
    ploting(df)
elif choice=="Chart":
    user_interaction(df)
   
