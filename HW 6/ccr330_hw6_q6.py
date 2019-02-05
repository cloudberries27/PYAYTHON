password = input("Enter a password: ");
up = 0;
dig = 0;
low = 0;
special = 0;
specials = ["!", "@", "#", "$"]

for each in password:
        if each.isupper():
            up += 1
        if each.islower():
            low += 1
        if each.isdigit():
            dig += 1
        if each in specials:
            special += 1
           
if (len(password) >= 8 and up >= 2 and low >= 1 and special >= 1 and dig >= 2):
    print(password,"is a valid password.")
else:
    print(password,"is not a valid password.");



