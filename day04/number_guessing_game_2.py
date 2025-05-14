import random
import sys

number = random.randint(1, 20)
print("Guess the number between 1 and 20 (or 'x' to exit).")
while True:
    guess = input("Your guess: ")
    if guess == 'x':
        print("Goodbye!")
        sys.exit()
    if not guess.isdigit():
        print("Enter a number or 'x' to quit.")
        continue
    guess = int(guess)
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print("That's it!")
        break
    
