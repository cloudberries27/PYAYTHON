# Claudia Rodriguez HW2 Q7 DONE 

def findChange(lst01):
    for elem in lst01:
        if elem == 1:
            return lst01.index(elem);
def main():
    lst01 = [0, 0, 0, 0, 0, 1, 1, 1]
    print(findChange(lst01))
main()
