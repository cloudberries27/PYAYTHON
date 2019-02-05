
shift = int(input("Enter a right shift: "));
string = input("Enter a string with at least one capital letter: ");
new_string = " "

for i in string:
    
    if 65 <= ord(i) and ord(i)<= 90:
        new = ord(i)+shift;
        if new>90:
            newnew = ord(i) - (26-shift)
            new_string += chr(newnew);
        else:
            new_string+=chr(new);            
        
    elif 97<=ord(i) and ord(i)<=122:
        new = ord(i)+shift;
        if new>122:
            remain = new%26
            newnew = ord(i) - (26-shift)
            new_string += chr(newnew);
        else:
            new_string+=chr(new);
    else:
        new_string+=i;
        
print (new_string);