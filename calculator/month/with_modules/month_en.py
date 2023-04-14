## import of the calendar module
import calendar

print("Hello ! \nThis program allows you to know the number of days of a month depending on its year !")
## ask the year
input_years = int(input("What is the year ? "))
## ask the month
month = input("What is the month ? ")
## list of months
month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
## if the month is a number and that this number is between 1 and 12 (because there are only 12 months) transform the variable month in integer
if month.isdigit() and 0<int(month)<13:
    month = int(month)
## else if the month is in the list of months transform the month which is in letter (recover its position in the list) into a number to be able to use the function monthrange    
elif month in month_list:
    month = month_list.index(month)+1
## else indicate to the user that the month is not valid and quit the program    
else:
    print("You must enter a valid month !")
    quit()
## calculate the number of days in the month with the monthrange function of the calendar module     	
nb_day = calendar.monthrange(input_years,month)
## indicate to the user the result of the calculation (nb_day [1] because we need the second result of the monthrange function, the first being the first day of the month and the second being the number of days in the month)
print("This month has: ",nb_day[1]," days !")
