"""
    Author: Rachel Schreiber
    Date Created: 7/7/2016
    Assignment Code: 3-2
    Assignment Name: Shop 'til You Drop
    Description:
        Read in the groceries from a file, and calculate the total cost
        depending on the number of items, and possible discounts
        - Make sure the shopping.txt file has 1 item on each line, with a blank line at the end of file
        - ex:
            apple
            apple
            banana

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

amounts = {  # how much of each item the person is getting
    'apple': 0,
    'banana': 0,
    'orange': 0,
    'steak': 0,
    'chicken': 0,
    'beans': 0,
    'milk': 0,
    'dozen eggs': 0,
    'frozen pizza': 0,
    'UnderWatch Root Edition': 0
}

file = open('shopping.txt', 'r')
item = file.readline()
while item != "":
    item = item[:-1]   # get '\n' off end of word
    amounts[item] += 1
    item = file.readline()
file.close()
total_cost = 0
for item in amounts:
    item_cost = items[item]*amounts[item]   # how much of the item * cost of item
    if amounts[item] >= discounts[item]:    # if number of items >= number needed for discount, apply discount
        item_cost *= .75
    total_cost += item_cost     # add cost for item to total cost

print("cost: $%.2f" % total_cost)
