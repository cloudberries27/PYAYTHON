def string_method(character):
    if (character.isupper()):
        print(character,"is an upper case letter.");
    elif(character.islower()):
        print(character,"is a lower case letter.");
    elif(character.isdigit()):
        print(character,"is a digit.");
    else:
        print(character,"is a non-alphanumeric character.");
        
def non_string_method(character):
    new = ord(character);
    if (new>=48 and new <=57):
        print(character,"is a digit.");
    elif(new>=97 and new <=122):
        print(character,"is a lower case letter.");
    elif(new>=65 and new <= 90):
        print(character,"is an upper case letter.");
    else:
        print(character,"is a non-alphanumeric character.");
    
    
    
def main():
    character=input("Enter a character: ");
    string_method(character);
    non_string_method(character);
    
main();







