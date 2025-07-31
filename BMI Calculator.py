import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1)
height = st.number_input("Enter your height (cm)", min_value=1)

if st.button("Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)
    st.success(f"Your BMI is {bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Normal weight")
    elif 25 <= bmi < 30:
        st.info("Overweight")
    else:
        st.error("Obesity")
