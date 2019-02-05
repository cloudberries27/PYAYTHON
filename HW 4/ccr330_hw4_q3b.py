
val = int(input("Please enter a value less than 1000: "))
valn = val%1000
valne = val%500
valnew = valne%100
val_new = valnew%50
val_new2 = val_new%10
val_new3 = val_new2%5
val_new4 = val_new3%1
s=" "
if (valn < 1000):
    
    if (1 <= (valn/500) < 2 ):
        s+="D"
    if (2 <= (valn/500) < 3 ):
        s+="DD"
    if (3 <= (valn/500) < 4 ):
        s+="DDD"
    if (4 <= (valn/500) < 5 ):
        s+="DDDD"
    if (1 <= (valn/500) < 2 ):
        s+="M"
if (valne < 500):
    
    if (1 <= (valne/100) < 2 ):
        s+="C"
    if (2 <= (valne/100) < 3 ):
        s+="CC"
    if (3 <= (valne/100) < 4 ):
        s+="CCC"
    if (4 <= (valne/100) < 5 ):
        s+="CCCC"
    if (5 <= (valnew/100) ):
        s+="D"
        
if (valnew<100):
    
    if((valnew/50) >= 1):
            s +="L"
            
if (val_new<50):
       
       if(1 <= (val_new/10) < 2):
            s += "X"
       if(2 <= (val_new/10) < 3):
            s+="XX"
       if(3 <= (val_new/10) < 4):
            s+="XXX"
       if(4 <= (val_new/10) < 5):
            s+="XXXX"
            
if (val_new2<10):        
    
    if((val_new2/5)>=1):
            s+="V"
            
if(val_new3<5):    
    
    if((val_new3/4)==1):
            s+="IIII"
    if((val_new3/3)==1):
            s+="III"
    if((val_new3/2)==1):
            s+="II"
    if((val_new3/1)==1):
            s+="I"

print(val,"is",s)



