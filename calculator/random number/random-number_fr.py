import random

print("Bonjour \nCe programme génère un nombre aléatoire et vous devez le deviner !")
secret_number = random.randint(1,100)
guess_number = 0
while guess_number != secret_number:
    guess_number = int(input("Quel est le nombre ? "))
    if guess_number == secret_number:
        print("Vous avez gagné ! \nLe nombre secret était ", secret_number, " !")
    elif guess_number > secret_number:
        print("Trop haut !")
    elif guess_number < secret_number:
        print("Trop bas !")