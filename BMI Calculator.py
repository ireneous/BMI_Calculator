import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")

st.title("Simple BMI Calculator")

name = st.text_input("Enter your name")
weight = st.number_input("Weight (in pounds)", min_value=1)
height = st.number_input("Height (in inches)", min_value=1)

if name and weight and height:
    bmi = (weight * 703) / (height ** 2)
    st.subheader(f"{name}, your BMI is {round(bmi, 2)}")

    if bmi < 18.5:
        st.write("You are underweight. You need to start eating more.")
    elif bmi < 25:
        st.write("You have a normal weight. Keep it up!")
    elif bmi < 30:
        st.write("You are overweight. Time to start running!")
    elif bmi < 35:
        st.write("You are obese. Please take action.")
    elif bmi < 40:
        st.write("You are severely obese. Health at risk.")
    else:
        st.write("You are morbidly obese. Take your life seriously!")
