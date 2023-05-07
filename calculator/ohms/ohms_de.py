print("Hallo \nDieses Programm ermöglicht es Ihnen, das Ohm'sche Gesetz zu berechnen!")
choices_input = str(input("Welchen Buchstaben möchten Sie berechnen (U, I oder R) ? "))
if choices_input == "U":
    r = int(input("Was ist der Wert von R ? "))
    i = int(input("Was ist der Wert von I ? "))
    final_values = r*i
    print("Der Wert von U ist",final_values)
elif choices_input == "I":
    u = int(input("Was ist der Wert von U ? ")) 
    r = int(input("Was ist der Wert von R ? "))
    final_values = u/r
    print("Der Wert von I ist",final_values)
elif choices_input == "R":
    u = int(input("Was ist der Wert von U ? "))
    i = int(input("Was ist der Wert von I ? "))
    final_values = u/i
    print("Der Wert von R ist",final_values)
else:
    print(choices_input,"ist keine gültige Auswahl")                