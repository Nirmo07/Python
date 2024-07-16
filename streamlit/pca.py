import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Pizza")
df=pd.read_csv("pizza.csv")
st.subheader("Original Dataset")
st.write(df)

st.write("Null values are:",df.isna().sum())
st.write("Duplicate values are:",df.duplicated().sum())
st.write("Non-null")
df.drop(columns=['remark'],inplace=True)
st.write(df)
st.write("No duplicates:")
df.dropna(inplace=True)
df.head()
st.write(df)
st.write("Null values are:",df.isna().sum())
st.write("Duplicate values are:",df.duplicated().sum())

a=st.selectbox("Select:",df.columns,index=8)

st.subheader("Bar Chart")
st.bar_chart(df[a].value_counts(30).values,color='#90EE90')

st.subheader("Line Chart")
st.line_chart(df[a].value_counts(30).values,color='#90EE90')

st.subheader("Scatter Graph")
st.scatter_chart(df[a].head(25),color='#90EE90')

st.subheader("Pie Chart")
plt.figure(figsize=[10,10])
plt.pie(df[a].head(30).value_counts().values,labels=df[a].head(30).value_counts().values, colors=['darkblue','green','yellow','blue'],autopct='%1.2f%%')
st.pyplot(plt)

st.subheader("Barh Chart")
plt.figure()
plt.barh(df[a].head(30).value_counts().index,df[a].head(30).value_counts().values,color='#90EE90')
st.pyplot(plt)
