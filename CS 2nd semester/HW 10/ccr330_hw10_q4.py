
def k_largest_elements(lst,k):
    new_lst = []
    while len(new_lst) < k:
        x = max(lst)
        ind = lst.index(x)
        new_lst.append(lst.pop(ind))
        
    return new_lst
    
    
    
print(k_largest_elements([3,9,2,7,1,7,1,3],4))
