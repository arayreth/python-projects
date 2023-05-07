## importieren des Kalendermoduls
import calendar

print("Hallo ! \nDieses Programm ermöglicht es Ihnen, die Anzahl der Tage eines Monats je nach Jahr zu erfahren !")
## fragen Sie das Jahr
input_years = int(input("Was ist das Jahr ? "))
## fragen Sie den Monat
month = input("Was ist der Monat ? ")
## Liste der Monate
month_list = ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]
## Wenn der Monat eine Zahl ist und diese Zahl zwischen 1 und 12 liegt (weil es nur 12 Monate gibt), wandeln Sie die Variable Monat in eine Ganzzahl um
if month.isdigit() and 0<int(month)<13:
    month = int(month)
## sonst, wenn der Monat in der Liste der Monate enthalten ist, wandeln Sie den Monat, der in Buchstaben ist (wiederherstellen seiner Position in der Liste) in eine Zahl um, um die Funktion monthrange verwenden zu können
elif month in month_list:
    month = month_list.index(month)+1
## sonst weisen Sie den Benutzer darauf hin, dass der Monat nicht gültig ist, und beenden Sie das Programm
else:
    print("Sie müssen einen gültigen Monat eingeben !")
    quit()
## berechnen Sie die Anzahl der Tage im Monat mit der monthrange-Funktion des Kalendermoduls
nb_day = calendar.monthrange(input_years,month)
## geben Sie dem Benutzer das Ergebnis der Berechnung an (nb_day [1], weil wir das zweite Ergebnis der monthrange-Funktion benötigen, das erste ist der erste Tag des Monats und das zweite ist die Anzahl der Tage im Monat)
print("Dieser Monat hat: ",nb_day[1]," Tage !")