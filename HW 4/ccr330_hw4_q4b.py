print("Please enter a non-empty sequence of positive integers, each one in a seperate line. End your sequence by typing done");
n = 0;
sum = 1;
num = ' ';
while ( num != 'done'):
    x = input();
    if (x =='done'):
        if (n != 0):
            print ('The geometric mean is: ',sum ** (1/n));
        else: 
            print ('No sequence was enetered')
    else:
        sum= sum*float(x)
        n+=1
    



