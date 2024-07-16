import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64
import matplotlib.pyplot as plt

st.sidebar.title('Python')     #to create sidebar

a=st.sidebar.button("Go")
if a:
    st.sidebar.code('www.github.com') 

d=st.sidebar.checkbox('lectures')
if d:
    st.sidebar.selectbox('Select Python Lecture',{1:'1 lecture',2:'2 lecture'})

def stream():
    st.title("Python-T")
    st.header('Python Study-Materials')         #header has larger size
    st.subheader('Notes,codes,etc')            #subheader has mid size
    st.write('g')            #write has normal/small size-understands datatype
    st.write(3)
    st.markdown('abc')           #understands format
    st.markdown('_italic_')    #_abc_-------two underscore for italic
    st.markdown(2)
    st.markdown("""              
    |col1|col2|
    |----|----|
    |  1 | 3  |
    |  4 | 6  |
    """)                       #""" are used to make table
    st.write(pd.DataFrame({'A':[1,2,3],'B':[4,5,6]}))  #dataFrame are used for having data in tabular form using dict
# st.code('www.github.com')      #we can copy link by adding a website path-------we cannot go to that link directly



def visualize():
    if 'show_image' not in st.session_state:
        st.session_state.show_image = False

    up_loaded_file = st.file_uploader("Choose a file", type={"py", "txt", "pdf", "docx", "jpg"})

# Button to show/hide image
    if st.button("Show/Hide Image"):
        st.session_state.show_image = not st.session_state.show_image

# Display the uploaded image if button is clicked
    if st.session_state.show_image:
        if up_loaded_file is not None:
            image = Image.open(up_loaded_file)
            st.image(image, caption="Uploaded Image.", use_column_width=True)
            st.write("Successful")
        else:
            st.write("No image uploaded.")
    else:
        st.write("Image hidden.")

    data={
        'A':[4,5,6,7,8,2,3,4,5,5],
        'B':[10,20,34,45,34,56,78,23,45,23]
    }
    df=pd.DataFrame(data)

    st.write('Sample DataFrame')
    st.dataframe(df)

    plt.figure(figsize=(10,5)) #set the figure size
    plt.hist(df['A'],bins=5,alpha=0.75)
    plt.title("Histogram of column A") #Set the title of chart
    plt.xlabel("Value") #Set the x-axis label
    plt.ylabel('Frequency') #Set the y-axis label
    #display histogram
    st.pyplot(plt)


choice=st.sidebar.selectbox("Select",{1:"one",2:"two"})
st.sidebar.title("Sidebar")
if choice==1:
    stream()
elif choice==2:
    visualize()


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: 1500px 730px;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('C:\\Users\\Mahesh\\Desktop\\Python\\bg.jpg')
 #''' -----means css style





