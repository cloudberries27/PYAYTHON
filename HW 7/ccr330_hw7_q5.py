
def find_all(lst,val):
    ne_lst = []
    for i in range (len(lst)):
       if lst[i] == val:
           ne_lst.append(i);
           
    return (ne_lst)
    
def main():
    lst = ['a','b','10','bab','a'];
    val = 'a'
    print(find_all(lst,val));
    
main()