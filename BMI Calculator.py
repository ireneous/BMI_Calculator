#!/usr/bin/env python
# coding: utf-8

# BMI Calculator in Python

name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print("Your BMI is:", round(BMI, 2))

if BMI > 0:
    if BMI < 18.5:
        print(name + ", you are underweight. You need to start eating more.")
    elif BMI <= 24.9:
        print(name + ", you are normal weight. Keep it up!")
    elif BMI <= 29.9:
        print(name + ", you are overweight. Time to start running!")
    elif BMI <= 34.9:
        print(name + ", you are obese. Please take action.")
    elif BMI <= 39.9:
        print(name + ", you are severely obese. Health at risk.")
    else:
        print(name + ", you are morbidly obese. Take your life seriously!")

# BMI Reference Chart:
# ---------------------
# Under 18.5        - Underweight         - Minimal Risk
# 18.5 - 24.9       - Normal Weight       - Minimal Risk
# 25 - 29.9         - Overweight          - Increased Risk
# 30 - 34.9         - Obese               - High Risk
# 35 - 39.9         - Severely Obese      - Very High Risk
# 40 and over       - Morbidly Obese      - Extremely High Risk
