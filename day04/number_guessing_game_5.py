import random
import sys

number = random.randint(1, 20)
debug = False
move_mode = False
print("Guess 1-20 (x=exit, s=show, d=debug, m=move mode).")
while True:
    if debug:
        print(f"[DEBUG] Number is {number}")
    guess = input("Your guess: ")
    if guess == 'x':
        print("Bye!")
        sys.exit()
    if guess == 's':
        print(f"The number is {number}")
        continue
    if guess == 'd':
        debug = not debug
        print(f"Debug mode {'ON' if debug else 'OFF'}")
        continue
    if guess == 'm':
        move_mode = not move_mode
        print(f"Move mode {'ON' if move_mode else 'OFF'}")
        continue
    if not guess.isdigit():
        print("Enter a number or one of x, s, d, m.")
        continue

    guess = int(guess)
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print("You got it!")
        break

    if move_mode:
        delta = random.choice([-2,-1,0,1,2])
        number = max(1, min(20, number + delta))
