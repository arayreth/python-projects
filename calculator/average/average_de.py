def Average(list):
    return sum(list) / len(list)

print("Hallo \nDieses Programm ermöglicht es Ihnen, Ihren Durchschnitt zu berechnen !")
number_grades_input = int(input("Wie viele Noten hast du ?"))
list = [  ]
for x in range(number_grades_input):
  grades = int(input("Was ist deine Note ?"))
  list.append(grades)
average = Average(list)
print("Ihr Durchschnitt ist :", round(average, 2))