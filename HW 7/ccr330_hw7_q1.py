line = input("Please enter a line of text: ")
char = input("Please enter the character you want to remove: ")
new_line = " ";
for i in line:
    if i != char:
        new_line += i;
    
print(new_line);
        
        







