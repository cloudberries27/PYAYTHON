
print ("Please enter the lengths of a triangle's sides: ")
x = int(input("Length of the first side: "))
y = int(input("Length of the second side: "))
z = int(input("Length of the third side: "))
if (x==y==z):
    print(x,',',y,',',z,"form an equilateral triangle.")
elif(x==y or y==z or x==z):
    if(x>y>z or x>z>y):
        if ((y*y) + (z*z) == (x*x)):
            print(x,',',y,',',z,"is an isosceles right triangle.")
        else:
            print(x,',',y,',',z,"is an isosceles triangle.")
    if(y>x>z or y>z>x):
        if ((x*x) + (z*z) == (y*y)):
            print(x,',',y,',',z,"is an isosceles right triangle.")
        else:
            print(x,',',y,',',z,"is an isosceles triangle.")        
    if(z>x>y or z>y>x):
        if ((x*x) + (y*y) == (z*z)):
            print(x,',',y,',',z,"is an isosceles right triangle.")
        else:
            print(x,',',y,',',z,"is an isosceles triangle.")
else:
    print(x,',',y,',',z,"is not an isosceles or equilateral triangle.")