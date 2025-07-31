import streamlit as st

# Streamlit App
st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and get health advice.")

# Input
name = st.text_input("Enter your name:")
weight = st.number_input("Enter your weight in pounds:", min_value=1)
height = st.number_input("Enter your height in inches:", min_value=1)

# Calculation and Output
if st.button("Calculate BMI"):
    if weight and height:
        bmi = (weight * 703) / (height * height)
        st.write(f"Your BMI is: **{round(bmi, 2)}**")

        # Advice
        if bmi < 18.5:
            st.warning(f"{name}, you are underweight. You need to start eating more.")
        elif bmi <= 24.9:
            st.success(f"{name}, you are normal weight. Keep it up!")
        elif bmi <= 29.9:
            st.warning(f"{name}, you are overweight. Time to start running!")
        elif bmi <= 34.9:
            st.error(f"{name}, you are obese. Please take action.")
        elif bmi <= 39.9:
            st.error(f"{name}, you are severely obese. Health at risk.")
        else:
            st.error(f"{name}, you are morbidly obese. Take your life seriously!")
    else:
        st.error("Please enter valid weight and height.")

# BMI Chart
st.markdown("""
### BMI Reference Chart:
- **Under 18.5** — Underweight (Minimal Risk)  
- **18.5 - 24.9** — Normal Weight (Minimal Risk)  
- **25 - 29.9** — Overweight (Increased Risk)  
- **30 - 34.9** — Obese (High Risk)  
- **35 - 39.9** — Severely Obese (Very High Risk)  
- **40 and over** — Morbidly Obese (Extremely High Risk)  
""")
