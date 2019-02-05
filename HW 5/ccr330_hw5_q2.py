'''
Ask	user	to	input	a	positive	integer	n,	and	print	a	triangle	of	numbers	
aligned	to	the	right,	where	the	first	line	contains	the	number	1.	
The	second	line	contains	the	numbers	1,2.	The	third	line	contains	1,2,3.	
And	so	on.	For	example	if	n=5,	the	program	should	print:	        
        1        
       12       
      123      
     1234     
    12345
'''

num =int(input("Please enter a positve integer: "));
for row in range(1,num+1):    
    
    for column in range(1,num+1):
        
        if(column >= (num+1-row) ):
            print(column - (num - row), end = "")
        else:
            print(" ", end = "")
            
    print()





