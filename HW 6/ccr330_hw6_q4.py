math = input("Enter a mathematical expression: ");

space = chr(32);

new_math = math.split(space);

oprand1 = int(new_math[0]);
oprand2 = int(new_math[2]);
op = new_math[1];

if(op == "+"):
    print(oprand1, op, oprand2,"=",(oprand1+oprand2));
elif(op == "-"):
    print(oprand1, op, oprand2,"=",(oprand1-oprand2));
elif(op == "*"):
    print(oprand1, op, oprand2,"=",(oprand1*oprand2));
elif(op == "/"):
    print(oprand1, op, oprand2,"=",(oprand1/oprand2));






