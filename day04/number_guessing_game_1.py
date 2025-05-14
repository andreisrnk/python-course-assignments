import random

number = random.randint(1, 20)

while True:
    guess = input("Guess a number between 1 and 20: ")
    if not guess.isdigit():
        print("Please enter a valid whole number.")
        continue
    guess = int(guess)
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You got it.")
        break
