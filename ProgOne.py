'''
Theo Crandall
Program Make Change

Gets the user's wallet amount, the cost of their purchase, and prints the amount of change they will receive.
'''

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
        print("Input must be a number")
        exit()

    # Checks if the input is a positive number and less than the max
    if input <= 0:
        print("Input must be greater than 0")
        exit()
    elif input > max:
        print("Input must be less than or equal to $", max)
        exit()
    else:
        return round(input, 2)


# get the amount of money in the wallet
walletAmount = input("How much money is in your wallet? ")
walletAmount = validateInput(walletAmount, 1000000)

# get the amount of money to spend
costOfItem = input("How much money do you want to spend? ")
costOfItem = validateInput(costOfItem, walletAmount)

# calculate the change
change = walletAmount - costOfItem

print("Your change is: $" + str(round(change, 2)))
print("Dollars:", str(int(change / DOLLAR)))

change %= DOLLAR
print("Quarters: " + str(int(change / QUARTER)))

change %= QUARTER
print("Dimes: " + str(int(change / DIME)))

change %= DIME
print("Nickels: " + str(int(change / NICKEL)))

change %= NICKEL
print("Pennies: " + str(int(change / PENNY)))
