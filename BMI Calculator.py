#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BMI Calculator


# In[20]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name + ", You are under weight.You need to start eating much lol")
    elif (BMI <= 24.9):
        print(name + ", You are normal weight. Keep working out")
    elif (BMI < 29.9):
        print(name + ", You are overweight. You need to start running to burn some fats")
    elif (BMI < 34.9):
        print(name + ", You are obese. You will explore soon lmao")
    elif (BMI < 39.9):
        print(name + ", You are Severely obese. hmmmm, too bad!!")
    else:
        print(name + ", Morbidly Obese. Take your life serious!!!")


# In[ ]:





# In[ ]:


Under 18.5	Underweight	Minimal
18.5 - 24.9	Normal Weight	Minimal
25 - 29.9	Overweight	Increased
30 - 34.9	Obese	High
35 - 39.9	Severely Obese	Very High
40 and over	Morbidly Obese	Extremely High


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




