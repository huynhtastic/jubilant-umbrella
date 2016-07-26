"""
Shop 'til You Drop
Bethany Salazar

If you buy a certain amount of a certain item, customers get a discount!

Create three functions:
•One that aggregates all of the items that were bought
•One that determines the subtotal of the transaction
•And one that determines the discounts applicable to the transaction

Whenever a certain item is bought enough times during the transaction, the buyer is given a 25% discount for
that particular item.
HIB team has given you the database converted to a Python Dictionary with the
prices and discounts.

"""

items = {
    'apple': 0.99,
    'banana': 0.50,
    'orange': 1.00,
    'steak': 5.00,
    'chicken': 3.25,
    'beans': 2.45,
    'milk': 2.99,
    'dozen eggs': 1.67,
    'frozen pizza': 4.54,
    'UnderWatch Root Edition': 49.99
}

discounts = {
    'apple': 4,
    'banana': 9,
    'orange': 5,
    'steak': 4,
    'chicken': 5,
    'beans': 5,
    'milk': 2,
    'dozen eggs': 3,
    'frozen pizza': 10,
    'UnderWatch Root Edition': 3
}
"""
This was my original idea. Forgot to use txt. file. This way uses user input. The actual scanner.

# This part takes everything a person buys from the txt. file
# Will put the items in a list of what the person buys with the total number

# creates a list with persons items
custList = [str(x) for x in amountOfItems.split()]
print(custList)  # testing purposes
"""

# first method detects whats been "scanned" (the txt. file) and see's what items from the
# dictionary were bought. It transfers the items from the txt. file to a list and then counts
# how many of each item were bought.
def aggregate():
    total = open("scannedItems.txt", "r+")

    # creates list called itemsbought
    itemsbought = {}

    # the list takes the same words and counts them
    for item in total:
        if item[:-1] not in itemsbought:
            itemsbought[item[:-1]] = 0
            itemsbought[item[:-1]] += 1
        else:
            itemsbought[item[:-1]] += 1

    # print(itemsbought)
    total.close()
    return itemsbought

# gives count of how many of each item there is
print("Items bought:", aggregate())

# uses the number of items in aggregate for the subtotal
def subtotal(aggregate):
    # sets aggregate to itemsbought to manipulate list
    itemsbought = aggregate()

    # sets variable balance for total balance
    global balance
    balance = 0

    # creates list of each item total
    itemtotals = {}

    # references items from dictionary to get the prices then multiplies them by the
    # number of items bought to give the total of each item
    for x, value in itemsbought.items():
        itemtotals[x] = itemsbought[x] * items[x]

    #takes the total of all items put together
    for item, total in itemtotals.items():
        balance += total
    # returns the the individual item totals
    return itemtotals

print("Total of each individual item (before discount):", subtotal(aggregate))
print("Total (no discount included):", round(balance, 2))

# uses the discount dictionary, depending on the discount on the item it uses gives
# discount accordingly.
def discount():
    # uses method aggregate to take the individual items
    itemsbought = aggregate()

    # takes subtotal and stores it in cost
    cost = subtotal(aggregate)
    savings = 0

    # initializes x and value, variable
    for x, value in itemsbought.items():
        # uses discounts dictionary. Checks dictionary to see if they bought a certain number of items
        # gives discount at a specific discount value from dictionary
        # if value is larger or equal to the discount number specified then it does the discount
        if value >= discounts[x]:
            savings += cost[x] * .25
    return savings

print("Discounted:", round(discount(),2), "off of original price.")
print("Official total (includes discount):", round((balance) - discount(), 2))
