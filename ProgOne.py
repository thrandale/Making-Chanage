'''
Theo Crandall
Program Make Change

Gets the user's wallet amount, the cost of their purchase, and prints the amount of change they will receive.
'''

from pickle import FALSE


DOLLAR = 1
QUARTER = .25
DIME = .10
NICKEL = .05
PENNY = .01


def validateInput(input, max):
    '''
    Validates the user's input.
    '''

    # Checks if the input is a number
    try:
        input = float(input)
    except ValueError:
        print("Input must be a number\n")
        return False

    # Checks if the input is a positive number and less than the max
    if input <= 0:
        print("Input must be greater than 0\n")
        return False
    elif input > max:
        print("Input must be less than or equal to $\n", max)
        return False
    else:
        return True


def getInput(prompt, inputMax):
    '''
    Gets the user's input and validates it.
    '''
    attempts = 3
    while attempts > 0:
        userInput = input(prompt)
        if validateInput(userInput, inputMax):
            return round(float(userInput), 2)
        attempts -= 1

    print("Maximum attempts reached. Exiting program.\n")
    exit()


# get the amount of money in the wallet
walletAmount = getInput("How much money do you have in your wallet? ", 1000000)

# get the amount of money to spend
costOfItem = getInput("How much does the item cost? ", walletAmount)

# calculate the change
change = walletAmount - costOfItem

print("\nYour change is: $" + str(round(change, 2)))
print("Dollars:", str(int(change / DOLLAR)))

change %= DOLLAR
print("Quarters: " + str(int(change / QUARTER)))

change %= QUARTER
print("Dimes: " + str(int(change / DIME)))

change %= DIME
print("Nickels: " + str(int(change / NICKEL)))

change %= NICKEL
print("Pennies: " + str(int(change / PENNY)))
