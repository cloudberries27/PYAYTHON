import os
#I couldn't figure out how to get the sums to be equal
#I think I was pretty close but I ran out of time
def share(lst):
    sum_of_list = sum(lst)
    if sum_of_list%3==0:
        result = [[] for i in range(3)]
        sums = {i:0 for i in range(3)}
        num = 0
        for elem in lst:
            for total in sums:
                if num == sums[total]:
                    result[total].append(elem)
                    break
            sums[total] += elem
            num = min(sums.values())    
        print (result)
        print(sums)
        print(num)
        return True    
    else: 
        return False
#os.fork did not work for me. I tried google to
#see if maybe someone could help but they said
#Windows does not use fork so I didn't know what else to do
def subsetSum(lst,target): 
    sum_of_list = sum(lst)
    sub_set = []
    for i in lst: 
        if os.fork()==0: 
            sub_set.append(i)
        if sum(sub_set)==(sum_of_list//3): 
            print(sub_set," sums to ",sum_of_list)
        

#My FairShare function does not work...Sorry
      
def main():
    subsetSum([1,5,2,7,18,22],15)
    print(share([434,722,50,334,50,178,333,303,30,566]))
    print(share([434,722,50,333,50,178,333,303,30,566]))
main()
























