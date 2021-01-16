#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:46:56 2021

@author: afnan
"""


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / height ** 2)
if BMI < 18.5:
  print(f"Your BMI is {BMI}, You're underweight")
elif BMI < 25:
  print(f"Your BMI is {BMI},You have a normal weight")
elif BMI < 30:
  print(f"Your BMI is {BMI}, You're slightly overweight")
elif BMI < 35:
  print(f"Your BMI is {BMI}, You're obese")
else:
  print(f"Your BMI is {BMI}, You're clinically obese") 





