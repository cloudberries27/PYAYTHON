'''
Ask	the	user	to	input	a	positive	integer	n,	
and	print	a	textual	image	of	an	hourglass	
made	of	2n	lines	with	asterisks.		
For	example	if	n=4,	the	program	should	print:	
    *******  
     *****   
      ***    
       *    
       *   
      ***  
     ***** 
    *******
 '''   
n = int(input("Please enter a positive integer: "));
num = n
for i in range (0,n):
    line = '*'*((2*n)-1)
    print ((i* ' '+line))
    n -= 1
for j in range (0,num):
    line = '*' * ((j*2) + 1)
    print (((num) * ' ') + line)
    num-=1       