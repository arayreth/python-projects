print("Hallo ! \nDieses Programm ermöglicht es Ihnen, die Anzahl der Tage eines Monats je nach Jahr zu erfahren !")
## fragen Sie das Jahr
input_years = input("Was ist das Jahr ? ")
## ob die Eingabe von Jahren eine Zeichenfolge ist, geben Sie eine Fehlermeldung aus, andernfalls fortfahren
if input_years.isdigit():
 ## erzwingen Sie die Variable input_years in int
    int_years = int(input_years)
    ## Liste der Monate in Buchstaben und Zahlen
    month_list = ["Januar","01","1","Februar","02","2","März","03","3","April","04","4","Mai","05","5","Juni","06","6","Juli","07","7","August","08","8","September","09","9","Oktober","10","November","11","Dezember","12"]
    ## Wenn die Jahre durch 4 teilbar sind, handelt es sich um ein Schaltjahr
    if int_years%4 == 0:
        month_bis = input("Was ist der Monat ? ")
        ## Wenn der Monat nicht in der Liste enthalten ist, geben Sie eine Fehlermeldung aus
        if month_bis in month_list:
            list_31_day = ["Januar","März","Mai","Juli","August","Oktober","Dezember","01","1","03","3","04","4","07","7","08","8","12"]
            if month_bis=="Februar" or month_bis=="2" or month_bis=="02":
                print("Dieser Monat hat 29 Tage !")
            elif month_bis in list_31_day:
                print("Dieser Monat hat 31 Tage !")   
            else:
                print("Dieser Monat hat 30 Tage !")    
        else:
            print("Sie müssen einen gültigen Monat eingeben !")
            quit()
    else:
        month = input("Was ist der Monat ? ")
        if month in month_list:
            list_31_day = ["Januar","März","Mai","Juli","August","Oktober","Dezember","01","1","03","3","04","4","07","7","08","8","12"]
            if month=="Februar" or month=="2" or month=="02":
                print("Dieser Monat hat 28 Tage !")
            elif month in list_31_day:
                print("Dieser Monat hat 31 Tage !")   
            else:
                print("Dieser Monat hat 30 Tage !")
        else:
            print("Sie müssen einen gültigen Monat eingeben !")
            quit()
else:
    print("Sie müssen eine Zahl eingeben !")
    quit()