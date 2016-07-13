"""
    Author: Cynthia Zaragoza
    Assignment Code:
    Date Created: 7/13/2016
    Assignment Name: Shop 'til You Drop
    Description: Run through a txt file, identify
                which items were scanned, identify
                their costs, identify the discounts,
                figure out the total before and after
                discounts.
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

#aggragate itmes bought
userB = {
    'apple': int(input("How many apples did you buy?")),
    'banana': int(input("How many bananas did you buy?")),
    'orange': int(input("How many oranges did you buy?")),
    'steak': int(input("How many steaks did you buy?")),
    'chicken': int(input("How many chickens did you buy?")),
    'beans': int(input("How many beans did you buy?")),
    'milk': int(input("How many milk bottles did you buy?")),
    'dozen eggs': int(input("How many dozen eggs did you buy?")),
    'frozen pizza': int(input("How many frozen pizzas did you buy?")),
    'UnderWatch Root Edition': int(input("How many underwater root editions did you buy?"))
}

print()
# set var to 0
numItems = 0
for x in userB: #use for loop to go through user's input dictionary
    numItems += userB[x] #add the number of items that
                            # user provided to the empty variable
print("Number of items bought:", numItems)

# subtotal of transaction before discounts
# multiply the intVariable for spec. items bought
    #by it's price
totalb4 = items['apple']* userB['apple'] + items['banana']*userB['banana'] + items['orange'] * userB['orange']\
          + items['steak'] * userB['steak'] + items['chicken']* userB['chicken'] + items['beans']*userB['beans']\
          + items['milk'] *userB['milk'] + items['dozen eggs'] * userB['dozen eggs'] + items['frozen pizza']*userB['frozen pizza']\
          + items['UnderWatch Root Edition']*userB['UnderWatch Root Edition']

print()
print("Subtotal of transaction (without discounts): ", totalb4)

totalAft= 0
l = userB['apple']* items['apple']
if userB['apple'] >= discounts['apple']: #if they match then the discounts apply
    totalAft += l-((l*25)/100)#apply the 25%discount to item total

l = userB['banana']*items['banana']
if userB['banana'] >= items['banana']:
    totalAft += l - ((l * 25) / 100)

l = userB['orange'] * items['orange']
if userB['orange'] >= items['orange']:
    totalAft += l - ((l * 25) / 100)

l = userB['steak'] * items['steak']
if userB['steak'] >= items['steak']:
    totalAft += l - ((l * 25) / 100)

l = userB['chicken'] * items['chicken']
if userB['chicken'] >= items['chicken']:
    totalAft += l - ((l * 25) / 100)

l = userB['beans']*items['beans']
if userB['beans'] >= items['beans']:
    totalAft += l - ((l * 25) / 100)

l = userB['milk']*items['milk']
if userB['milk'] >= items['milk']:
    totalAft += l - ((l * 25) / 100)

l = userB['dozen eggs']*items['dozen eggs']
if userB['dozen eggs'] >= items['dozen eggs']:
    totalAft += l - ((l * 25) / 100)

l = userB['frozen pizza'] * items['frozen pizza']
if userB['frozen pizza'] >= items['frozen pizza']:
    totalAft += l - ((l * 25) / 100)

l = userB['UnderWatch Root Edition']*items['UnderWatch Root Edition']
if userB['UnderWatch Root Edition'] >= items['UnderWatch Root Edition']:
    totalAft += l - ((l * 25) / 100)

    #subtotal after discounts
print('Total after discounts:', totalb4 - totalAft)
