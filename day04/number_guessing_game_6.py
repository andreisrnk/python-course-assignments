import random
import sys

debug = False
move_mode = False
number = random.randint(1, 20)

print("Number Guessing 1–20 (x=exit, s=show, d=debug, m=move, n=new game).")
while True:
    if debug:
        print(f"Number is {number}")
    guess = input("Your guess: ").strip().lower()
    if guess == 'x':
        print("Bye!")
        sys.exit()
    if guess == 's':
        print(f"(Cheat) It's {number}")
        continue
    if guess == 'd':
        debug = not debug
        print(f"Debug {'ON' if debug else 'OFF'}")
        continue
    if guess == 'm':
        move_mode = not move_mode
        print(f"Move {'ON' if move_mode else 'OFF'}")
        continue
    if guess == 'n':
        number = random.randint(1, 20)
        print("New game started!")
        continue
    if not guess.isdigit():
        print("Enter a number or one of x, s, d, m, n.")
        continue

    guess = int(guess)
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Right! Starting a new game.")
        number = random.randint(1, 20)
        continue

    if move_mode:
        delta = random.choice([-2, -1, 0, 1, 2])
        number = max(1, min(20, number + delta))
