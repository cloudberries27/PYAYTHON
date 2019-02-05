#Claudia Rodriguez HW1 Q5
import copy
def filterun(pred, lst):
    new_lst = copy.deepcopy(lst);
    if new_lst == lst:   
        return pred;
def remove_odd(lst):
    for num in lst:
        if (num % 2 == 0):
            lst.remove(num);
    return lst; 
def starts_with_a_vowel(strings_lst):
    vowels = ['A','a','E','e','I','i','O','o','U','u']
    vow_lst = []    
    for i in strings_lst:
        if i[0] in vowels:
            vow_lst.append(i);
    print(vow_lst)       
def main():
    lissy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print (filterun(True, lissy))
    print(remove_odd(lissy))    
    lissy2 = ["It", "is", "fun"];
    starts_with_a_vowel(lissy2);

main();