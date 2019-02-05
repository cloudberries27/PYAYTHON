def reverse_to_new_list(lst1):
    new_list = [];
    for i in range (len(lst1)):
        new_list.append(lst1[len(lst1) - 1 - i]);
    return new_list;
        
        
def reverse_in_place(lst1):
    h = 0
    j = len(lst1) - 1    
    if (len(lst1) % 2 == 0):
        for i in range (len(lst1)//2):
            temp = lst1[h]
            lst1[h] = lst1[j]
            lst1[j] = temp
            h+=1
            j-=1
            
    else:
        for i in range ((len(lst1)//2) - 1):
            temp = lst1[h]
            lst1[h] = lst1[j]
            lst1[j] = temp
            h+=1
            j-=1

def main():
     lst1 = [1, 2, 3, 4, 5, 6]
     rev_lst1 = reverse_to_new_list(lst1)
     print("After reverse_to_new_list, lst1 is", lst1,
    "and the returned list is", rev_lst1)
    
     lst2 = [1, 2, 3, 4, 5, 6]
     print("Before reverse_in_place, lst2 is", lst2)
     reverse_in_place (lst2)
     print("After reverse_in_place, lst2 is", lst2)
     
     
main();

