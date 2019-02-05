
def add_list(lst1,lst2):
    new_list= []
    j = 0
    for i in lst1:
        new_list.append(int(i)+int(lst2[j]));
        j+=1                  
    return (new_list)
    
def main():
    list1 = (input("Input: "));
    lst = []
    lst.append(list1);
    while list1 != 'done':
        list1 = (input("Input: "));    
        if list1 != 'done':
            lst.append(list1);
            
    list2 = (input("Input: "));
    lst2 = []
    lst2.append(list2);
    while list2 != 'done':
        list2 = (input("Input: "));    
        if list2 != 'done':
            lst2.append(list2);
    if len(lst) == len(lst2):
        print(add_list(lst,lst2));
    else:
        print("Lists are different lengths");
main();
