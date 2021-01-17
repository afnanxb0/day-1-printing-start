#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 21:28:43 2021

@author: afnan
"""


year = int(input("Which year do you want to check? "))

if year % 4 != 0:
  print(f"{year} is not a leap year")
elif year % 100 != 0:
  print(f"{year} is a leap year")
elif year % 400 != 0:
  print(f"{year} is not a leap year") 
else:
  print(f"{year} is a leap year")   

