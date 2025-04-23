import random

# Computer chooses a random number between 1 and 20
secret_number = random.randint(1, 20)

# Prompt the user for a guess
guess = int(input("Guess a number between 1 and 20: "))

# Provide feedback
if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Correct! You guessed the number.")
