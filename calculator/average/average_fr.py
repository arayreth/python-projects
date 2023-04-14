def Average(list):
    return sum(list) / len(list)

number_grades_input = int(input("Combien de notes as tu ? "))
list = [  ]
for x in range(number_grades_input):
  grades = int(input("Quelle est ta note ? "))
  list.append(grades)
average = Average(list)
print("Ta moyenne est de: ", round(average, 2))
