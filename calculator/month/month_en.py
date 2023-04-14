print("Hello ! \nThis program lets you know the number of days in a month according to its year !")
input_years = input("What is the year ?")
## if the input of years is a string, give an error message else continue
if input_years.isdigit(): 
    ## force the input_years variable in int
    int_years = int(input_years)
    ## list of month in letter and number
    month_list = ["January","01","1","February","02","2","March","03","3","April","04","4","May","05","5","June","06","6","July","07","7","August","08","8","September","09","9","October","10","November","11","December","12"]
    ## if the years is divisible by 4, this a leap Year
    if int_years%4 == 0:
        month_bis = input("What is the month ?")
        ## if the month is not in the list give an error message
        if month_bis in month_list:
            list_31_day = ["January","March","May","July","August","October","December","01","1","03","3","04","4","07","7","08","8","12"]
            if month_bis=="February" or month_bis=="2" or month_bis=="02":
                print("This month has 29 days !")
            elif month_bis in list_31_day:
                print("this month has 31 days !")   
            else:
                print("This month has 30 days !)    
        else:
            print("You need to enter a real month !")
            quit()
    else:
        month = input("What is the month ?")
        if month in month_list:
            list_31_day = ["January","March","May","July","August","October","December","01","1","03","3","04","4","07","7","08","8","12"]
            if month=="February" or month=="2" or month=="02":
                print("This month has 28 days !")
            elif month in list_31_day:
                print("This month has 31 days !")   
            else:
                print("This month has 30 days !")
        else:
            print("You need to enter a real month !")
            quit()                
else:
    print("You need to enter a number !")
    quit()
