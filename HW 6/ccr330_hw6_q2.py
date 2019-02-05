string = input("Enter an odd length string: ");

x = len(string);
middle = int(x/2);
print ("Middle character: ", string[middle]);
new_string2 = string[0:middle];
new_string3 = string [middle+1:x];
print("First half: ",new_string2);
print("Second half: ",new_string3);











