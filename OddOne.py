import math

def cone():
    diam = int(input("What do you want the cone diameter to be?    "))
    conicle = ""
    while diam > 1:
        conicle += "0"
        conicle += "1"
        diam -= 2
    if diam%2 != 0:
        conicle += "0"
    for x in range(0, ((len(conicle)+1)//2)):
        print(" "*x + conicle[0:len(conicle)-2*x])
cone()