# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 20:30:26 2016

@author: Claudia Rodriguez
"""
day = str(input("Enter the day the call started at: "))
time = int(input("Enter the time the call started at(hhmm): "))
min = int(input("Enter the duration of the call (in minutes): "))
cost = 0
if (day == "Mon" or "Tue" or "Wed" or "Thr" or "Fri" ):
    if(800<=min<=1800):
        cost = min*0.4
    else:
        cost = min*0.25
else:
    cost = min*0.15

print("This call will cost $",cost)
