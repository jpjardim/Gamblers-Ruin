# Author: Paulo Jardim
# Student Number: l00161844
# Date: 17/01/2021
# Description: This program provides a Java implementation of the Gambler's Ruin application.
# The program starts by asking the player what their starting pot is and the target amount they
# want to reach. The game then starts by simulating rolls. If the player's score is < 6 they win 1.
# If the score is >= 6 they lose 1. The game will continue until they reach their target amount or
# lose all of their money.

import random


# simulates a dice rolling
# generate a random number in the chosen range
def rollDice(minimum, maximum):
    return random.randint(minimum, maximum)


if __name__ == "__main__":
    pot = 0
    goal = 0
    numGames = 1
    numBets = 1
    numWins = 0
    playAgain = True

    print("\n----Welcome to Gambler's Ruin-----\n")

    while playAgain:
        pot = int(input("Please enter you starting pot: "))
        goal = int(input("Please enter your  target goal: "))
        print("\n\nGame: " + str(numGames))

        while 0 < pot < goal:
            numBets += 1
            roll = rollDice(1, 12)
            print("\nThrowing the dice...")
            print("You threw a:  " + str(roll))

            # if the random number is less than 6, add one to pot
            if roll < 6:
                pot += 1
                numWins += 1
                print("Congratulations you won 1 and you now have: " + str(pot) + "\n")
            # if random number is 6 or higher, remove one from the pot
            else:
                pot -= 1
                print("Bad luck, you lost a 1 and now have: " + str(pot) + "\n")

        # if you you reached the goal
        if pot == goal:
            temp = input("Well played you reached your goal. Would you like to play again? Y/N: ")
        else:
            temp = input("Bad luck, you lost all of your pot. Would you like to play again? Y/N: ")

        # ask if user wants to play again
        if temp.upper() == 'N' or temp.upper() == 'NO':
            playAgain = False

        print("\n\nThe total number of bets: " + str(numBets))
        print("The total number of wins : " + str(numWins))
        print('{:.2%}'.format(float(numWins) / float(numBets)))
