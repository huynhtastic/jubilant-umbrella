print("Hello World!")


"""
newName = input("Enter first name.")
lastName = input("Enter last name.")
age = input("Enter your age.")
iceCream = input ("What is your favorite flavor of ice cream.")
print("Welcome" + newName ,lastName + ", I can't believe your'e " + age + ". Good thing you "
                                                                          "love " + iceCream ,"ice cream because we "
                                                                                              "have tons of it!" )

"""
#use input from user to find the two roots for any polynomial with real roots
import math
a = int(input ("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
x = (b**2)
y = (4*a*c)
j = (x-y)
i = ((-b + math.sqrt(j))/2*a)
z = ((-b - math.sqrt(j))/2*a)
print (i , z)
#x = (-b + math.sqrt((b**2)-(4*a*c))/2*a)
#y = (-b - math.sqrt((b**2)-(4*a*c))/2*a)
