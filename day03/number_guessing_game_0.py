import random

secret_number = random.randint(1, 20) # The program chooses a random number between 1 and 20
a = int(input("Guess a number between 1 and 20: ")) # Asking the user to guess a number

if a<1 or a>20:
    print("Out of range!")
else:
    if a<secret_number:
        print("Too low!")
    elif a>secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
