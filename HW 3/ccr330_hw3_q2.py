
first = int(input("Enter	price of first item: "))
second = int(input("Enter price of second item: "))
subtotal0 = first + second 

if (first>second):
    second=second/2
else:
    first=first/2
    
subtotal = first + second   

club = input("Does customer have a club card? (Y/N): ")

if (club =='y' or 'Y'):
    subtotal -= (10*subtotal)/100
if (club =='n' or 'N'):
    subtotal = subtotal
    
tax = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

totaltax = (subtotal*tax)/100
total = (subtotal + totaltax)
total2 = round(total,2)

print("Base price = ",subtotal0)
print("Price after discounts = ",subtotal)
print("Total price = ",total2)
	
	