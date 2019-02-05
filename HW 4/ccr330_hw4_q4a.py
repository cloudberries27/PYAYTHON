length = int(input("Please enter the length of the sequence: "))
n= input("Please enter your sequence: ")

l = list(n)
print (l)
inside = 1
for i  in range (length):
    inside *= int(l[i])
    
total = inside ** (1/length)

print ("The geometric mean is: ",total)
