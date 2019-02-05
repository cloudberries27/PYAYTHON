#Claudia Rodriguez HW@ Q4 DONE
import math
def e_approx(n):
    return (1/math.factorial(n));
    
def main(): 
    sum = 0;
    for n in range(15):         
        sum += e_approx(n) 
        approx_str = "{:.15f}".format(sum)
        print("n =", n, "Approximation:", approx_str)
        
main();
