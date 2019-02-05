# CLAUDIA RODRIGUEZ HW3

#A
def print_triangle(n):
    if n > 0:
        print_triangle(n-1)
        print('*'*n)
        
#B        
def print_opposite_triangles (n):
    if n != 0:
        print (n*'*');
        print_opposite_triangles(n-1);

        
def main():
    print_opposite_triangles(4)
    print_triangle(4)
    
     
main();