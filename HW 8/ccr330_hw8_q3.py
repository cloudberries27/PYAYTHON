
# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.
    
    file = open(complete_weather_filename, "r");
    new_file = open(cleaned_weather_filename, "w");

    for line in file:
        split = line.strip().split(sep=",")
        if len(split) > 1:
            new_line = split[0:4]
            new_line1 = [split[8]]
            if 'T' in new_line1:
                x = new_line1.index('T');
                new_line1[x] = '0';
            great_line = new_line + new_line1
            for i in range(len(great_line) - 1):
                new_file.write(great_line[i] + ", ")
            new_file.write(great_line[len(great_line) - 1] + "\n");
            

# Part B
def f_to_c(f_temperature):
    c_temp = ((int(f_temperature) - 32) * (5/9));
    return c_temp

def in_to_cm(inches):
    cm = float(inches) * 2.54;
    return cm;

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    file = open(imperial_weather_filename, "r");
    new_file = open(metric_weather_filename, "w");
    file.readline();    
    for line in file:
        split = line.strip().split(sep=", ")
        if len(split) >= 1:
            high_temp = split[2]
            low_temp = split[3]
            preci = split[4]
            split[2] = f_to_c(high_temp);
            split[3] = f_to_c(low_temp);
            split[4] = in_to_cm(preci);
            metric_str = ""
            for i in split:
                metric_str += str(i) + ", "
            
            new_file.write(metric_str + "\n");


# Part C
def print_average_temps_per_month(city, weather_filename, unit_type):
        file = open(weather_filename, "r");
        high_temp = [0,0,0,0,0,0,0,0,0,0,0,0];
        low_temp = [0,0,0,0,0,0,0,0,0,0,0,0]
        months_days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December'];
        for line in file:
            line_becomes_list = line.strip().split(sep=", ")
            if line_becomes_list[0] == city:
                print("Average Temperature for",city,":");
                sep_date = line_becomes_list[1].split(sep="/");
                for date in range(1,13):
                    while date == sep_date[0]:
                        high_temp[date] += line_becomes_list[2]
                        low_temp[date] += line_becomes_list[3]
                    avg_high_temp = high_temp[date]/months_days[date];
                    avg_low_temp = low_temp[date]/months_days[date];
                    if unit_type == 'imperial':
                        print(months[date-1],avg_high_temp + 'F',avg_low_temp + 'F');
                    else:
                        print(months[date-1],avg_high_temp + 'C',avg_low_temp + 'C');
# Part D
#Highest Precipitation
def high_pre(weather_file):
    file = open(weather_file, "r");
    precipitation = []
    for line in file:
        split = line.strip().split(sep=", ")
        precipitation.append(split[4]);
    print(precipitation.max());

def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    high_pre("weather in imperial.csv")
main()
