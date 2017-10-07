# Guess the Number
# A game by Luka Becerra
# Sep 23, 2017

# Import the random module
import random

# Game introduction
author = "Luka Becerra"
print("Welcome to Gues the Number!")
print("A game by {}. All Rights Reserved.".format(author))
print()
print("Please enter you name below:")
player = input()
print("Hi {}!".format(player))

# Play
correct_number = random.randint(1,20)
guess_number = 0
guesses = 0
max_guesses = 5
print("I'm thinking of a number between 1 and 20. Can you guess it?")
print("You have {} guesses to start with.".format(max_guesses))
print("If you use them all up you will loose!")
print("Enter you guesses below:")
while guesses < max_guesses and correct_number != guess_number:
    guess_number = int(input())
    if guess_number < correct_number:
          print("Your guess is too low. Try again!")
          guesses += 1
    elif guess_number > correct_number:
          print("Your guess is too high. Try again!")
          guesses += 1
    else:
          print("Congratulation! You guessed the right number and you did it in {} guesses!".format(guesses+1))
if guesses == max_guesses:
    print("Oh no! You're out of guesses!")
    print("The correct number was {}.".format(correct_number))
    print("Do you want to try again?")
    print("Print Yes or No.")
    again = "Yes" or "yes"
    not_again = "No" or "no"
    answer = input()
    if answer == again:
        print("Ok great!")
    elif answer == not_again:
        print("Aw that's too bad!")
    else:
        print("Your response is not a valid input. Please type either Yes or No.")
