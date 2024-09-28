import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 7

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100. You have 7 attempts to guess it.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break
        attempts -= 1
        print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

number_guessing_game()
