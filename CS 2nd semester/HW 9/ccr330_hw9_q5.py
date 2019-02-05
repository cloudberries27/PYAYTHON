import hash_table

def intersection_list (lst1, lst2):
    new_list = []    
    for i in lst1:
        for j in lst2:
            if (i == j):
                new_list += [i]
    return new_list


def _intersection_list (lst1,lst2):
    ht = hash_table.ChainingHashTableMap()    
    new_list = []    
    for i in lst1:
        ht[i] = None
    for x in lst2:
        if x in ht:
            new_list.append(x)        
    return new_list


def main():
    print(_intersection_list([3,9,2,7,1],[4,1,8,2]))
main()            
            
    