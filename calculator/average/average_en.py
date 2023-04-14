def Average(list):
    return sum(list) / len(list)

number_grades_input = int(input("How many notes do you have ? "))
list = [  ]
for x in range(number_grades_input):
  grades = int(input("What is your note ? "))
  list.append(grades)
average = Average(list)
print("You average is: ", round(average, 2))
