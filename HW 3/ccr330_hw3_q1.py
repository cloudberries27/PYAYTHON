import math
weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))
bmi = (weight/(math.pow(height,2)))
print ("BMI is:",bmi)
if(bmi>=30):
    print("Obese")
elif(bmi>=25):
    print("Overqeight")
elif(bmi>=18.5):
    print("Normal")
elif(bmi<18.5):
    print("Underweight")