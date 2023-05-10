import random

print("Hallo \nDieses Programm generiert eine Zufallszahl und Sie müssen sie erraten !")
secret_number = random.randint(1,100)
guess_number = 0
while guess_number != secret_number:
    guess_number = int(input("Was ist die Nummer ? "))
    if guess_number == secret_number:
        print("Du gewinnst ! \nDie geheime Nummer war ", secret_number, " !")
    elif guess_number > secret_number:
        print("Zu hoch !")
    elif guess_number < secret_number:
        print("Zu niedrig !")