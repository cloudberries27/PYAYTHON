#Claudia Rodriguez HW2 Q6 DONE 

def two_sum(lst, target):
    x = 0;
    y = 1;
    gap = abs(target- lst[x]-lst[y])
    
    for i in range (0, len(lst)):
        curr = lst[i];
        fsum = curr + lst[x];
        if (fsum == target):
            return (x, i);
        ssum = curr + lst[y];
        if (ssum == target):
            return (y, i);
        if abs(target - fsum) < gap and abs(target-fsum) < abs(target - ssum):
            y = i
        if abs(target - ssum) < gap and abs(target-ssum) < abs(target - fsum):
            x = i
            
    
            
def main():
    lst = [-2, 7, 11, 15, 20, 21]
    tar = 28
    print(two_sum(lst, tar))
    
main();
