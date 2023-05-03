print("Hello \nThis program allows you to calculate the ohms law!")
choices_input = str(input("Which letter do you want to calculate (U, I or R) ? "))
if choices_input == "U":
    r = int(input("What is the value of R ? "))
    i = int(input("What is the value of I ? "))
    final_values = r*i
    print("The value of U is",final_values)
elif choices_input == "I":
    u = int(input("What is the value of U ? ")) 
    r = int(input("What is the value of R ? "))
    final_values = u/r
    print("The value of I is",final_values)
elif choices_input == "R":
    u = int(input("What is the value of U ? "))
    i = int(input("What is the value of I ? "))
    final_values = u/i
    print("The value of R is",final_values)
else:
    print(choices_input,"is not a valid choices")    