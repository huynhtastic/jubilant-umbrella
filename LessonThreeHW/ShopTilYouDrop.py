"""
    Alexandra Triampol
    7/8/16
    This code contains 3 fucntions: aggregates(), subtotal(), and discountPrice().
    aggregates() prints out how many items you bought.
    subtotal() prints out the amount you pay before discounts.
    discountPrice() prints out the amount you pay after discounts.

"""

# item is a dictionary
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

# discounts is a dictionary
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

# starts an empty list for the items to be put in later
scannedList = []

# This takes in all the items that the person bought and scans them.
# It will put them in a list and prints the total number of items you bought.
# It also returns the list of items so that you can reuse it for the other functions.
def aggregates(scannedList):
    prompt = ("What'd you buy? You probably bought either apples, bananas, oranges, "
                 + "\n" + "steak, chicken, beans, milk, dozen eggs, frozen pizza, or "
                 + "\n" + "Underwatch Root Edition." +"\n")
    print(prompt)
    scan = input("Please use all lowercase when typing your items here and keep it singular." + "\n"
                 + "(Exceptions are beans, dozen eggs, and Underwatch Root Edition.)" + "\n")
    scannedList.append(scan)
    while True:
        scan = input("\n" + "Anything else?  If you're done, type(done). " + "\n")
        if (scan == ("done")):
            break
        scannedList.append(scan)
    print("\n" + "Looks like you bought " + str(len(scannedList)) + " item(s).")

    return scannedList

# This takes in all the items that the person bought and counts them.
# Then it creates the total price you pay based on the data from the items{} dictionary.
# It returns the subtotal value.
def subtotal(scannedList):
    appleCount = scannedList.count("apple")
    bananaCount = scannedList.count("banana")
    orangeCount = scannedList.count("orange")
    steakCount = scannedList.count("steak")
    chickenCount = scannedList.count("chicken")
    beansCount = scannedList.count("beans")
    milkCount = scannedList.count("milk")
    DEcount = scannedList.count("dozen eggs")
    FPcount = scannedList.count("frozen pizza")
    UREcount = scannedList.count("Underwatch Root Edition")

    addedSubTotal = (appleCount*items['apple'])+(bananaCount*items['banana'])+(orangeCount*items['orange'])+\
                    (steakCount*items['steak'])+(chickenCount*items['chicken'])+(beansCount*items['beans'])+\
                    (milkCount*items['milk'])+(DEcount*items['dozen eggs'])+(FPcount*items['frozen pizza'])+\
                    (UREcount*items['UnderWatch Root Edition'])

    return addedSubTotal

# This takes in all the items that the person bought and creates the discounted prices.
# It checks if you have the right amount of items to qualify for a discount.
# Then it does the calculations for the discounted price and adds them up.
# It returns the total discounted value.
def discountPrice(scannedList):
    percentOff = 0.25
    overallTotal = 0
    if (scannedList.count("apple")>= discounts['apple']): #figure out discount
        initialPrice = scannedList.count("apple")*items['apple']
        createDiscount = initialPrice*percentOff
        reducedPrice = initialPrice-createDiscount
        overallTotal+=reducedPrice

    if (scannedList.count("banana") >= discounts['banana']):  # figure out discount
        initialPrice = scannedList.count("banana")*items['banana']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    if (scannedList.count("orange") >= discounts['orange']):  # figure out discount
        initialPrice = scannedList.count("orange") * items['orange']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    if (scannedList.count("steak") >= discounts['steak']):  # figure out discount
        initialPrice = scannedList.count("steak") * items['steak']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    if (scannedList.count("chicken") >= discounts['chicken']):  # figure out discount
        initialPrice = scannedList.count("chicken") * items['chicken']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    if (scannedList.count("beans") >= discounts['beans']):  # figure out discount
        initialPrice = scannedList.count("beans") * items['beans']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    if (scannedList.count("milk") >= discounts['milk']):  # figure out discount
        initialPrice = scannedList.count("milk") * items['milk']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    if (scannedList.count("dozen eggs") >= discounts['dozen eggs']):  # figure out discount
        initialPrice = scannedList.count("dozen eggs") * items['dozen eggs']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    if (scannedList.count("frozen pizza") >= discounts['frozen pizza']):  # figure out discount
        initialPrice = scannedList.count("frozen pizza") * items['frozen pizza']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    if (scannedList.count("Underwatch Root Edition") >= discounts['UnderWatch Root Edition']):  # figure out discount
        initialPrice = scannedList.count("Underwatch Root Edition") * items['UnderWatch Root Edition']
        createDiscount = initialPrice * percentOff
        reducedPrice = initialPrice - createDiscount
        overallTotal += reducedPrice

    return overallTotal

#These lines of code initiate the three functions above.

aggregates(scannedList)
originalPrice = subtotal(scannedList)
print("Your subtotal is",originalPrice,"dollars, but you might have some discounts.")
finalPrice = discountPrice(scannedList)
print("With your discounts included, your total comes to",finalPrice,"dollars.  Thanks for shopping at HIB!")
