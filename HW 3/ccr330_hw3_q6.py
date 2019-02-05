import turtle
import math
l1 = int(input("Please enter a value for 1st length: "))
l2 = int(input("Please enter a value for 2nd length: "))
a1 = int(input("Please enter a value for the angle: "))
l3 = math.pow((math.pow(l1,2) + (math.pow(l2,2)) - (2*l1*l2*math.cos(a1))),.5) 
a2 = math.acos((math.pow(l2,2) + math.pow(l3,2) - math.pow(l1,2))/(2*l2*l3))
a = a2 *(180/math.pi)
turtle.forward(l1)
turtle.left(180-a1)
turtle.forward(l2)
turtle.left(180-a)
turtle.home()




