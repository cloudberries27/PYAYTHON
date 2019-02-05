print("Please enter your amount in the format of dollars and cents in two seperate lines: ")
dollars = int(input())
cents = int(input())
quarters=dollars*4
quarters2=int(cents/25)
q = quarters + quarters2
d = ((cents%25)/10)
n = (((cents%25)%10)/5)
p = ((((cents%25)%10)%5)/1)
print (dollars,"dollars and",cents,"cents are:")
print(q,"quarters,",int(d),"dimes,",int(n),"nickels and ",int(p),"pennies")