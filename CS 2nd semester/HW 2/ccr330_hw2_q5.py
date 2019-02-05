#Claudia Rodriguez HW2 Q5 DONE-

def split_parity(lst):
    for elem in range (len(lst)):
        if (lst[elem] % 2 == 0):
            lst.append(lst[elem]);
            x = elem;
            lst.remove(lst[x]);
    return lst
        
            
def main():
    lst = [1,2,3,4,5,6]
    print(split_parity(lst))
main()
