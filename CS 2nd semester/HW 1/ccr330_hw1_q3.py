#Claudia Rodriguez HW1 Q3

#PART A
def sum_of_squares(num):
    count = 0;    
    while num>0:
        count += (num*num);
        num-=1;
    return count;
    
#PART C
def sum_of_odd_squares(num):
    count = 0;    
    while num>0:
        if (num % 2 != 0):
            count += (num*num);
            num-=1;
        else:
            num-=1;
    return count;
   
def main():
    n = int(input("Give me a num: "))
    #PART B
    print(sum ([i*i for i in range (1,n+1)]))
    
    print(sum_of_squares(n));
    print(sum_of_odd_squares(n));
    
    #PART D
    print(sum([i*i for i in range(1,n+1) if i % 2 != 0]))
main();
