import math
a = int(input("Please enter value of a: "))
b = int(input("Please enter value of b: "))
c = int(input("Please enter value of c: "))
x = (math.pow(b,2)) - (4*a*c)
if(a==0 and b==0 and c==0):
    print("This equation has infinite solutions")
elif(a==0 and b==0):
    print("This eqution has no solution")
elif(x<0):
    print("This equation had no real solution")
elif(x==0):
    sol= ((-b)+(math.pow(x,.5)))/(2*a)
    sol2= ((-b)-(math.pow(x,.5)))/(2*a) 
    y = a*(math.pow(sol,2))+(b*sol)+c
    if(y==0):
        print("This equation has a single solution x=", sol)
    else:
        print("This equation has a single solution x=",sol2)
elif(x>0):
    sol= ((-b)+(math.pow(x,.5)))/(2*a)
    sol2= ((-b)-(math.pow(x,.5)))/(2*a) 
    y = a*(math.pow(sol,2))+(b*sol)+c
    print("This equation has two solutions x=", sol,"and x=", sol2)
	