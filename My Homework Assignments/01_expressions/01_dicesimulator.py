"""
Program: dice_simulator
------------------------
Simulate rolling two dice, three times. Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Roll result: Die 1: {die1}, Die 2: {die2}, Total: {total}")

def main():
    print("Simulating rolling the dice three times:")
    roll_dice()
    roll_dice()
    roll_dice()

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
