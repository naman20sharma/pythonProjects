# User will try to guess a random number
import random
import sys


def check_if_number(user_input):
    if not user_input.isdigit():
        sys.exit("Please enter a digit next time. ")
    user_input = int(user_input)
    if user_input < 0:
        sys.exit("Please enter a whole number next time. ")
    return int(user_input)


max_range = check_if_number(input("Type a number for the range: "))

random_number = random.randint(0, max_range)
guesses = 0

while True:
    user_guess = check_if_number(input("Make a guess: "))
    guesses += 1
    if user_guess > max_range:
        print(f'Please enter a number within the provided range. (Hint: 0 <= Your Guess <= {max_range})')
        continue
    if user_guess == random_number:
        print("You got it! Congratulations")
        break
    elif user_guess > random_number:
        print("You are above the number!")
    elif user_guess < random_number:
        print("You are below the number")
    else:
        print("Sorry :( You got it wrong, Please try again")

print(f'You took {guesses} guesses')