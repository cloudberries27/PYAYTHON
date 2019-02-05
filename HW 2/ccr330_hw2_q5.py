daysJ = int(input("Please enter the number of days John has worked: "))
hoursJ = int(input("Please enter the number of hours John has worked: "))
minJ = int(input("Please enter the number of minutes John has worked: "))
daysB = int(input("Please enter the number of days Bill has worked: "))
hoursB = int(input("Please enter the number of hours Bill has worked: "))
minB = int(input("Please enter the number of minutes Bill has worked: "))
days = daysJ + daysB
hours = hoursJ + hoursB
Totalhours = hours%24
hours= hours/24
days += int(hours)
min = minJ+minB
Totalmin = min%60
min = min/60
Totalhours += int(min)
print("The total time both of them worked together is:",days,"days,",Totalhours,
"hours, and",Totalmin,"minutes")
