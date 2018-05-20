# this imports the random module
import random


# this defines the roll function for a two dice
def roll(sides=12):
    num_rolled = random.randint(2, sides + 1)
    return num_rolled


# this function defines the main Dice rolling game
def dice_rolling_game():
    sides = 12
    rolling = True
    while rolling is True:
        roll_again = input("Ready to roll?, Press r to roll and q to quit:  ")
# tests the user input
        if roll_again == "r":
            num_rolled = roll(sides)
            print("You rolled", num_rolled)
        elif roll_again == "q":
            print("Thanks for Playing.")
            break
        elif "r" is not roll_again or "q" is not roll_again:
            print("Kindly Press r to play or q to quit ")
        else:
            break

dice_rolling_game()