
def create_prefix_lists(lst):
    new_list = [];
    
    for i in range (len(lst) + 1):
        new_list.append(lst[0:i]);  
    return new_list;
        
def main():
    lst = [2,4,6,8,10];
    print(create_prefix_lists(lst));
    
    
main();