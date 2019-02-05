"""
For	example,	if	lst=[1, 2, 3],	the	call	permutations(lst)	could	return	
[[1, 2, 3], [2, 1, 3], [1, 3, 2], [3, 2, 1], [3, 1, 2], [2, 3, 1]]	
	
"""        
def permutations(lst):
    length = len(lst)
    big_list = [0] * length
    new_list = []
    temp = lst.copy()
    new_list.append(temp)
    num = 1
    while num < length:
        if big_list[num] < num:
            numtwo = big_list[num] if num % 2 else 0
            lst[numtwo], lst[num] = lst[num], lst[numtwo]
            temp = lst.copy()
            new_list.append(temp)
            big_list[num] += 1
            num = 1
        else:
            big_list[num] = 0
            num += 1
    return(new_list)
def main():
    print(permutations([2,5,3,2]))
main()
    
            