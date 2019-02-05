
def max_abs_val(lst):
    new_lst = []
    for i in lst:
        if i >= 0:
            mar = 0+(i);
            new_lst.append(mar);
        else:
            mar = 0-(i);
            new_lst.append(mar);
    return max(new_lst);
    
def main():
    lst = [-19,-3,20,-1,0,-25];
    print(max_abs_val(lst));
main();
    
    