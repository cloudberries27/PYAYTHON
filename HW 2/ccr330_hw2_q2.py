print("Please	 enter number of coins: ")	
quarters = int(input("# of quarters: "))	
dimes = int(input("# of dimes: "))	
nickels = int(input("# of nickels: "))
pennies = int(input("# of pennies: "))
q = .25 * quarters
d = .10 * dimes
n = .05 * nickels
p = .01 * pennies
dollars = q + d + n + p
cents = (dollars%1)*100
print("The total is",int(dollars),"dollars and", int(cents),"cents")