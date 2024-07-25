import streamlit as st
import time as t

st.image('Bleach.png',width=500)


# Title - It is used to give title to the app
st.title("Welcome")

# Header    
st.header("Machine Learning")

# Sub Header
st.subheader("Linear Regression")

# information
st.info("Information for the users")

# For warning Msg
st.warning("cautious!")

# error message
st.error("Wrong password")

# Success message
st.success("Congrats")

# write functin : It can handle different kinds of input, including text, Markdown, data frames, dictionaries, and even Matplotlib figures

st.write("Employee Name")

st.write(range(50)) # in coding format

# Markdown
st.markdown('# Markdown function')
st.markdown('## Markdown function') # smaller font size
st.markdown('### Markdown function')
st.markdown(':moon:') # emoji of moon

# Text
st.text("A normal text")

# To write a caption
st.caption("A Caption text")

# To display mathematical exp
st.latex(r''' a+bx^2+c ''')

# -------------------------------------------

# Widgets

# Checkbox
st.checkbox("Login")

# Button
st.button("Click me")

# Radio widget
st.radio("Pick your gender",['Male','Female'])

# Select box(drop down)
st.selectbox("Pick your course",['ML','GenAi','Web D','Cyber security'])

# Multi Select
st.multiselect("Choose the Department",['Content','Sales','Marketing'])

# Select slider
st.select_slider("Rating",['Bad','Good','Excellent','Outsanding'])

# Slider(to pick number)
st.slider("Enter a number",0,100)

# Number input
st.number_input("Pick a number",0,100)

# Text Input
st.text_input("Enter the text")

# Date input
st.date_input("Opening ceremony")

# Time input
st.time_input("Time")

# Text area (for more than one line input)
st.text_area("Welcome write your review")

# To upload file
st.file_uploader("upload your file/folder")

# To choose color
st.color_picker("Choose the color")

# Progess bar
st.progress(60) # %age of progress

# Spinner(Temporary waiting msg)
with st.spinner('Just wait'):
    t.sleep(2)

# Ballons
st.balloons()


# Side Bar
st.sidebar.title('Welcome to Company')
st.sidebar.text_input('Mail address')
st.sidebar.button('Send')


# Data visualization
import pandas as pd
import numpy as np

st.title("Bar chart")
data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)
