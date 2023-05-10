import random

print("Hello \nThis programm generate a random number and you need to guess it !")
secret_number = random.randint(1,100)
guess_number = 0
while guess_number != secret_number:
    guess_number = int(input("What is the number ? "))
    if guess_number == secret_number:
        print("You win ! \nThe secret number was ", secret_number, " !")
    elif guess_number > secret_number:
        print("Too high !")
    elif guess_number < secret_number:
        print("Too low !")