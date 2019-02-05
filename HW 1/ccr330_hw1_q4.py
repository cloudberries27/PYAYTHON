years = int(input("How many years: "))
pop = 307357870
seconds = 31536000*years
birth = seconds / 7
death = seconds / 13
immigrant = seconds /35
newpop = int(pop+birth-death+immigrant)
print (newpop) 
 
 