import streamlit as st
import pandas as pd
from datetime import time

def main():
    st.title("Detailed Streamlit Widgets Examples")

    # Checkbox
    show_data = st.checkbox("Show data table")
    if show_data:
        st.write(show_data)
        st.write(pd.DataFrame({
            'Column 1': [1, 2, 3, 4],
            'Column 2': [10, 20, 30, 40]
        }))

    # Button
    button_val = st.button('Click me!')
    if button_val:
        
        st.write(button_val)

    # Radio widget
    genre = st.radio(
        "What's your favorite movie genre",
        ('Comedy', 'Drama', 'Action', 'Sci-Fi')
    )
    st.write(f'You selected {genre}')

    # Select box
    option = st.selectbox(
        'Choose your favorite color',
        ('Red', 'Green', 'Blue', 'Yellow')
    )
    st.write(f'Your favorite color is {option}')
    print(type(option))
    # Multi Select
    options = st.multiselect(
        'What are your favorite fruits',
        ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
        ['Apple', 'Banana']
    )
    st.write(f'You selected: {", ".join(options)}')

    # Select slider
    start_color, end_color = st.select_slider(
        'Select a range of color wavelength',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
        value=('red', 'blue')
    )
    st.write(f'You selected wavelengths between {start_color} and {end_color}')

    # Slider
    age = st.slider('How old are you?', 0, 130, 25)
    st.write(f"I'm {age} years old")

    # Number input
    number = st.number_input('Enter a number', min_value=0, max_value=100, value=50, step=1)
    st.write(f'The number you entered is {number}')

    # Text Input
    name = st.text_input('Enter your name', 'John Doe')
    st.write(f'Hello, {name}!')


    # Date input
    date = st.date_input('Enter a date')
    st.write(f'The date you entered is {date}')
    # print((date))


    # Time input
    appointment_time = st.time_input('Set an appointment time', time(9, 30))
    st.write(f'Your appointment is set for {appointment_time}')

    # Text area
    txt = st.text_area('Enter some text', 'Type here...')
    st.write(f'You entered: {txt}')

    # File uploader
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.write(f"Filename: {uploaded_file.name}")
        # You can read the file contents here if needed
        file_contents = uploaded_file.read()
        print(type(file_contents))

    # Color picker
    color = st.color_picker('Pick a color', '#00f900')
    st.write(f'The color you picked is {color}')

if __name__ == "__main__":
    main()