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

def aggregate():
    total = open("scans.txt", "r+")

    bought = {
    }
    for item in total:
        if item[:-1] not in bought:
            bought[item[:-1]] = 0
            bought[item[:-1]] += 1
        else:
            bought[item[:-1]] += 1
    #print(bought)
    total.close()
    return bought
print(aggregate())

def subtotal(aggregate):
    bought = aggregate()
    global balance
    balance = 0
    item_totals = {
    }
    for key, value in bought.items():
        item_totals[key] = bought[key]*items[key]
    for item, total in item_totals.items():
        balance += total
    return item_totals
print(subtotal(aggregate))
print(round(balance, 2))

def discount():
    items_bought = aggregate()
    cost_bought = subtotal(aggregate)
    savings = 0
    for key, value in items_bought.items():
        if value >= discounts[key]:
            savings += cost_bought[key]*.25
    return savings
print(discount())