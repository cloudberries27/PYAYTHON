def return_first(phrase):
    ls = phrase.split();
    return ls[0];
    
def remove_first(phrase):
    ls1 = phrase.split();
    ls1.pop(0);
    str1 = ' '.join(ls1);
    return str1;
    
def reverse_string(phrase):
    rev = ""
    ls1 = phrase.split();
    for i in range(0 ,len(ls1)):
        rev += ls1[(len(ls1) -1) - i]
        rev += " "
    return rev
    
    
def main():
    phrase = input("Please insert a phrase: ");
    print(return_first(phrase));
    print(remove_first(phrase));
    print(reverse_string(phrase));
main()


