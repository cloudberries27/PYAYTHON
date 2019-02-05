  
    
def print_shifted_triangle(n,m,symbol):
    for j in range (0,n):
        line = symbol * ((j*2) + 1)
        print (((m -j + (m-1) ) * " ")  + line)
        n-=1  
        
def print_pine_tree(n, symbol):
    
    for i in range (2, n+2):
        space = n+2        
        print_shifted_triangle(i,space,symbol)
        space-=1
        
def main():
    n = int(input("Please enter a positve integer: "));  
    #m = int(input("Please enter the number of spaces: "));
    symbol = input("Please enter the type of symbol: ");
    
    #print_shifted_triangle(n,m,symbol);
    print_pine_tree(n,symbol);
    
main();