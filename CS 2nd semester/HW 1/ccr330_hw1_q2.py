#Claudia Rodriguez HW1 Q2
def shift(lst, k, direction = "L"):
    if direction == "R":
        l = lst[k:] + lst[:-k]
    
        for i in range (len(lst)):
            lst[i] = l[i];
    if direction == "L":
        l = lst[-k:] + lst[:-k]
    
        for i in range (len(lst)):
            lst[i] = l[i];
        
        
def main():
    direction = input("Left or Right? (L/R): ");
    lst = [1, 2, 3, 4, 5, 6];
    k = 2;
    shift(lst, k, direction);
    print(lst);
main();
