
def print_month_calender(numofdays,startingday):
    date = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"];
    
    for i in range(len(date)):
        print (date[i], end = '\t');
    print()
    
    for j in range (startingday - 1):
        print ("", end = '\t');
    
    day = 1
    
    while day <= numofdays:
        print (day, end = '\t');
        if (startingday + day) % 7 == 1:
            print (" ")
        day+=1
        
    lastday = startingday + (numofdays%7);
    if lastday > 7:
        lastday -= 7
    print()
    return lastday;
    

def leap_year(year):
    if year % 400 == 0:
        return True;
    if year % 4 == 0 and year % 100 == 0:
        return False;
    if year % 4 == 0:
        return True;
    return False;
  
def print_year_calender(year, starting_day):
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    for i in range (12):
      print (month[i], year);
      if (month[i] == "September" or month[i] == "April" or month[i] == "June" or month[i]== "November"):
          starting_day = print_month_calender(30, starting_day);
      elif (month[i] == "February"):
          if leap_year(year) == True:
              starting_day = print_month_calender(29, starting_day);   
          else:
              starting_day = print_month_calender(28, starting_day);   
      else:
          starting_day = print_month_calender(31, starting_day);

    


def main():
    numofdays = int(input("Please enter the number of days in the month: "));
    startingday = int(input("Please enter the starting day (1-7): "));
    year = int(input("Please enter a year: "));
    
    print_month_calender(numofdays,startingday);
    print_year_calender(year, startingday);
    
main()

