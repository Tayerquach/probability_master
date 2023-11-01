"""
Module for Dice Roll Probability
    @Author:  Boi Mai Quach
    @Version: 0.1
    @Date:   29/10/2023

"""

from random import randint
from collections import Counter
import itertools
from config import *

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

class Dice:
    def __init__(self, num_dice, num_sides):
        self.num_dice  = num_dice
        self.num_sides = num_sides
        
    def roll_random_dice(self):
        dice = []
        if self.num_sides != 6:
            print('We only visualise a 6-sided dice')
        else:
            for die in range(self.num_dice):
                dice.append(randint(1, 6))
                
        # PRINT HORIZONTALLY
        for line in range(5):
            for die in dice:
                print(dice_art.get(die)[line], end="")
            print()
        
    def get_dice_probability(self, num_trials = NUM_TRIALS):
        """
        Determine the probability of certain outcomes when rolling dice

        Parameter: variable number of arguments for sides of dice (e.g., 6)
        Return: table of probability for each possible outcome
        """
        dice = [self.num_sides] * self.num_dice
        counts = Counter()
        outcomes = []
        probabilities = []
        for roll in range(num_trials):
            counts[sum((randint(1, sides) for sides in dice))] += 1

        print('OUTCOME PROBABILITY')
        for outcome in range(len(dice), sum(dice) + 1):
            outcomes.append(outcome)
            probability = counts[outcome]*100/num_trials
            probabilities.append(probability)
            print('{}\t{:0.2f}%'.format(outcome, probability))

        return outcomes, probabilities
            
    def get_sum_probability(self, total):
        
        # Generate all possible outcomes when rolling n dice
        dice_outcomes = range(1, self.num_sides + 1)
        all_combinations = list(itertools.product(dice_outcomes, repeat=self.num_dice))
        event_outcomes = 0
        
        for outcome in all_combinations:
            if sum(outcome) == total:
                for line in range(5):
                    for die in outcome:
                        print(dice_art.get(die)[line], end="")
                    print()
                event_outcomes += 1
        
        probability = event_outcomes/self.num_sides**self.num_dice 
        # Convert the probability to a percentage
        probability_percentage = probability * 100

        print(f"The probability of getting a sum of 11 when rolling {self.num_dice} dice is: {probability_percentage:.2f}%")
        
    
def menu():
    print("---------------------------------------")
    print("  Welcome to Dice Probability Problems!")
    print("---------------------------------------")
    print("\n[1] Dice Roll Simulation")
    print("\n[2] Dice Roll Probability")
    print("\n[3] Sum Probability")
    print("\n[0] Exit the program")
    print("---------------------------------------")
    
if __name__ == '__main__':
    menu()

    while True:
        option =input("Enter your option: ")

        if option == '1':
            num_dice = int(input("How many dice?: "))
            num_sides = int(input("How many sides?: "))

            # Create Dice object
            roll = Dice(num_dice, num_sides)
            roll.roll_random_dice()
        elif option == '2':
            num_dice = int(input("How many dice?: "))
            num_sides = int(input("How many sides?: "))

            # Create Dice object
            roll = Dice(num_dice, num_sides)
            roll.get_dice_probability()
        elif option == '3':
            num_dice = int(input("How many dice?: "))
            num_sides = int(input("How many sides?: "))

            # Create Dice object
            roll = Dice(num_dice, num_sides)
            total = int(input("Sum of two dice is: "))
            roll.get_sum_probability(total)
        elif option == '0':
            break
        else:
            print("Invalid option")
            pass

        print("")
        menu()

    print("\nThanks for using this program.")

