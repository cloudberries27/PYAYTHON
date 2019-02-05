'''
Question	3:	Ask	user	to	input	a	positive	integer	n,	and	print	
all	of	the	numbers	from	1	to	n	that	have	more	even	digits	than	odd	digits.	
For	example,	if	n=30,	the	program	should	print:	
2	4	6	8	20	22	24	26	28	

'''
num = int(input("Please enter a positve integer: "));
for i in range(1, num + 1):
    even_count = 0
    odd_count = 0
    temp = i
    while (temp > 0):
        if (temp % 2 == 0):
            even_count += 1
        else:
            odd_count += 1
        temp //= 10
    if (even_count > odd_count):
        print(i)
        
        