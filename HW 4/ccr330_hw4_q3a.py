val = input("Please enter number in the simplified Roman numeral system: ")
l = list(val)
print (l)
v =len(l)
sum = 0
for i  in range (v):
    if (l[i] == 'M'):
        sum+=1000
for i  in range (v):
    if (l[i] == 'D'):
        sum+=500
for i  in range (v):
    if (l[i] == 'C'):
        sum+=100
for i  in range (v):
    if (l[i] == 'X'):
        sum+=10
for i  in range (v):
    if (l[i] == 'V'):
        sum+=5
for i  in range (v):
    if (l[i] == 'I'):
        sum+=1
print (sum)

