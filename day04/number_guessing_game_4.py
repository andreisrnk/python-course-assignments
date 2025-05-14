import random
import sys

number = random.randint(1, 20)
debug = False
print("Guess the number 1-20 (x=exit, s=show, d=toggle).")
while True:
    if debug:
        print(f"Number is {number}")
    guess = input("Your guess: ")
    if guess == 'x':
        print("Bye!")
        sys.exit()
    if guess == 's':
        print(f"The number is {number}")
        continue
    if guess == 'd':
        debug = not debug
        state = "ON" if debug else "OFF"
        print(f"Debug mode {state}")
        continue
    if not guess.isdigit():
        print("Enter a number or one of x, s, d.")
        continue
    guess = int(guess)
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print("Correct!")
        break
