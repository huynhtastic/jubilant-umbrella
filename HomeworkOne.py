name = input("Please enter your full name: ")
age = input("Please enter your age: ")
flavor = input("Please enter your favorite ice cream flavor: ")

print("Welcome, " + name + "! Congratulations on being on this planet for the past "
      + age + " years! Have as much " + flavor + " ice cream as you want at the party!")

import math

a = int(input("Type in a: "))
b = int(input("Type in b: "))
c = int(input("Type in c: "))

root1 = int(-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
root2 = int(-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)

print("The first root is ", root1, ". The second root is ",root2)
