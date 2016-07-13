print("Here is the list of items we're selling and their prices:\n"
      "\napple (.99) banana(.50) orange(1.00)\nsteak(5.00) chicken(3.25) beans(2.45)"
      "\nmilk(2.99) dozen eggs(1.67) frozen pizza(4.54)\nUnderwatch Root Edition(49.99)\n")

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

amounts={
    'apple': 0,
    'banana': 0,
    'orange': 0,
    'steak':0,
    'chicken':0,
    'beans':0,
    'milk': 0,
    'dozen eggs':0,
    'frozen pizza':0,
    'UnderWatch Root Edition':0
}

def aggregate():

    f = open('shoppingList.txt', 'r')
    it=f.readline().strip("\n")
    while it != "":
        amounts[it]=amounts[it]+1
        it=f.readline().strip("\n")
    f.close()
aggregate()



sumy=0

for keys in amounts:
    keyscost=items[keys]*amounts[keys]
    if amounts[keys] >= discounts[keys]:
        keyscost *= .75
    sumy+= keyscost

print("Cost:", sumy)







