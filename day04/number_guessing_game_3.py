import random
import sys

number = random.randint(1, 20)
print("Guess the number between 1 and 20 (x=exit, s=show answer).")
while True:
    guess = input("Your guess: ")
    if guess == 'x':
        print("Bye!")
        sys.exit()
    if guess == 's':
        print(f"(Cheat) The number is {number}")
        continue
    if not guess.isdigit():
        print("Enter a number, 's' to cheat, or 'x' to quit.")
        continue
    guess = int(guess)
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print("You won!")
        break
