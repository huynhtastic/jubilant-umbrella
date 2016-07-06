"""
    Object Oriented Programming (OOP)

    Making objects from a piece of code
    Objects - something that you make
    Class - bunch of similar characteristics

    Why do we use OOP?
    - easier to organize
    - logical
    - easy to understand
    ---
    - Modularize code: break up code
        into reusable snippets
        - Plug-in & plug-out code
    - Easier to maintain and modify code
    - Encourages abstraction to hide complicated code
    - Give users a clearly defined interface

    Why would we not use OOP?
    - Because it's fit for the job
    - There may be other programming paradigms right
        for the job
        - Data-driven
        - Functional Programming

    Programming Paradigm
    - A way of programming
    - Similar to TAXONOMY (i think)

    Objects and Classes
    Class - bunch of similar characteristics shared
        across different objects
        - A blueprint/template
        - Defines everything that is needed for an
            object during instantiation
            - Defines all of the characteristics
                that an object needs
    Objects - something that you make
        - Defined from a class
        - Overarching data type from which everything
            inherits from
        - Has a bunch of characteristics
        - Almost everything is an object
        Python
        - Int, Boolean, String, Float, List, Dict, Set,
        Tuple

    Encapsulation
    - Grouping all items into a single unit
    ex. all of the characteristics of a class
    ex. putting everything into a single class

    Inheritance
    - Acquires properties of another class

    Polymorphism
    Abstraction
"""
class Animal(object):
    def __init__(self):
        # run whenever the object instance is created
        # characteristics
        self.numLegs = 4
        self.color = "brown"

    def eat(self):
        print("Om nom. I just ate.")

anAnimal = Animal()
print(anAnimal)
print(Animal)
# print(anAnimal.eat())
anAnimal.eat() # -> 1. anAnimal 2. eat 3. ()

"""

    Inheritance

    Animal
    - Birds
    - Dogs
    - Cats
    - Fish
    - Reptiles

# Animal = parent class
# Cat = child class
"""
print()
class Cat(Animal):
    pass

aCat = Cat()
print(aCat)
aCat.eat()
print(aCat.color)
blueCat = Cat()
blueCat.color = "blue"
print(blueCat.color)

print()
"""
    Polymorphism
    - takes many forms
    - changing an existing function to suit
        subclass/child class requirements

    Override
    - taking a function and making it do something
        completely different

    Overloading (not present in Python)
    - defining a function with the same name with
        different functionality
    - allowed by different function definitions
        - different parameters
"""
class Dog(Animal):

    def eat(self):
        print("Om nom. I just ate dog food.")

    # def eat(self, food):
    #     print("Om nom. I just ate, but I ate {0} instead."
    #           .format(food))

aDog = Dog()
aDog.eat()

"""
    Abstraction
    - being able to hide all of the details of how
        something works

    print() - we know how to use it, what it does,
        but not how it works
"""
class Calc(object):
    def __init__(self):
        pass

    def generateNum(self, num):
        num += 2
        num = num * num
        num -= 5
        num = num + 3 * 4 - 2 + 1 ** 2 >> 5
        return num

aCalc = Calc()
print(aCalc.generateNum(10))

import math

print(math.pow(2,2))

"""
    Getter and setter methods
"""
class Person(object):
    def __init__(self):
        self.numLegs = None
        self.eyeColor = None
        self.abs = None

    # setter method
    def setNumLegs(self, numLegs):
        self.numLegs = numLegs

    # getter method
    def getNumLegs(self):
        self.numLegs -= 1
        return self.numLegs

a = Person()
a.setNumLegs(4)
print(a.getNumLegs(), "legs")

a.numLegs = 3 # setting
print(a.numLegs) # getting