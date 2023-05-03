print("Bonjour \nCe programme permet de calculer la loi d'ohms !")
choices_input = str(input("Quel lettre veut tu calculer (U,I ou R) ? "))
if choices_input == "U":
    r = int(input("Quel est la valeur de R ?"))
    i = int(input("Quel est la valeur de I ? "))
    final_values = r*i
    print("La valeur de U est",final_values)
elif choices_input == "I":
    u = int(input("Quel est la valeur de U ? ")) 
    r = int(input("Quel est la valeur de R ? "))
    final_values = u/r
    print("La valeur de I est",final_values)
elif choices_input == "R":
    u = int(input("Quel est la valeur de U ? "))
    i = int(input("Quel est la valeur de I ? "))
    final_values = u/i
    print("La valeur de R est",final_values)
else:
    print(choices_input,"n'est pas un choix valide !")    