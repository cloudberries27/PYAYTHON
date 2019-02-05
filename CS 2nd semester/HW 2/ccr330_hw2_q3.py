#Claudia Rodriguez HW2 Q3 DONE

def factors(num):
    fac_lst = [];
    for i in range(1,int(num**(1/2))+1):
        if (num % i == 0):
            fac_lst.append(i);
            if (num/i) not in fac_lst:
                fac_lst.append(num//i);
    fac_lst.sort();
    for elem in fac_lst:
        yield elem;
            
def main():
    for curr_factor in factors(1000):
        print(curr_factor);
main()
