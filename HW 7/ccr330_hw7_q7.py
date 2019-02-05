
def encoder(string_one):
    ls = [];
    length = len(string_one);
    i = 0;
    while (length > 0):
        j = i + 1;
        while (j < len(string_one) and string_one[i] == string_one[j]):
            j += 1;
            length -= 1;
        ls.append([string_one[i], j - i]);
        i = j;
        length -= 1;
    return (ls);

def decoder(list_one):
    new_string = " ";
    i = 0;
    for j in range(len(list_one)):
        new_string += (list_one[i][0]) * int((list_one[i][1]));
        i+=1;
        
    return(new_string);
            
    
def main ():
    list_one = [['a', 2], ['d', 1], ['c', 4], ['a', 2]];
    print(decoder(list_one));
    string_one = input("Please give me a string: ");
    print (encoder(string_one));
    
main();








