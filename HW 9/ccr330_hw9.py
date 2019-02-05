'''
Claudia Rodriguez:ccr330
This is HW 9
''' 

def enter_trainline(trainline):
    dicto = {}
    file = open("hw9 - mta train stop data.csv", "r");
    file.readline();
    for line in file:
        line_list = line.split(',');
        letternumber = line_list[0][0];
        if letternumber not in dicto:
            dicto[letternumber] = []
            dicto[letternumber].append(line_list[2])
        else:
            if (line_list[2] not in dicto[letternumber]):
                dicto[letternumber].append(line_list[2])
    
    if trainline in dicto:
        return (', '.join(dicto[trainline]))        
    else:
        print("Train line does not exist.");
    
    
def main():
    trainline = input("Please enter train line or 'done' to stop: ");
    while trainline != 'done':
        if trainline != 'done':
            print(trainline,"line:",enter_trainline(trainline));
            trainline = input("Please enter train line or 'done' to stop: ");
            
main();