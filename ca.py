import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


df=pd.read_csv('Dataset.csv') #read csv file using pandas
print(df)
print(df.isna().sum())#------return null in true or false so sum is used 
print(df.duplicated().sum())#checks duplicates

st.sidebar.write("Sidebar")
st.sidebar.write(df.columns.values)
st.title("EDA Drugs Hospital ")
st.subheader("Original Dataset")
st.write(df) # writes df of csv file
df.shape   #gives total col and row

st.subheader("Null Value are:")
st.write(df.isna().sum())

st.subheader("Duplicated Value are:")
st.write(df.duplicated().sum())

a=st.selectbox("Select:",df.columns,index=9) #in selectbox using .columns all the names of columns will appear in selectbox
#st.write(df['avg'].value_counts()) #
# st.write(df['avg'].value_counts().values)
# st.write(df['avg'].value_counts().index)
st.subheader("Bar Graph")
st.bar_chart(df[a].head(25),color='#90EE90')

st.subheader("Line Graph")
st.line_chart(df[a].head(25),color='#90EE90')

st.subheader("Scatter Graph")
st.scatter_chart(df[a].head(25),color='#90EE90')

st.subheader("Pie Graph")
plt.figure(figsize=[10,10])
plt.pie(df[a].value_counts().head(30).values,labels = df[a].value_counts().head(30).index, colors=['darkblue','green','yellow','blue'],autopct='%1.2f%%')
st.pyplot(plt)

#white box jispe graph plot hota hai use bolte hai figure

st.subheader("Barh Chart")
plt.figure()
plt.barh(df[a].head(30).value_counts().index,df[a].head(30).value_counts().values,color='#90EE90')
st.pyplot(plt)















