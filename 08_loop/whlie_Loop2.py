#Number Gussing game

secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number:

    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Guess again: "))

print("Correct! 🎉")