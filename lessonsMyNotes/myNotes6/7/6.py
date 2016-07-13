"""
Object Oriented Programming

Making objects from a piece of code
Objects - something that you can make
Class  - similar characteristics for objects

Easier to organize, logical flow(their's a structure)

why do we use this system?
    -to modularize code:
            break up code into reasonable snippets
            -Allowing us to plug in and out code (add function)
    - Easier to maintain and modify code
    - Encourages abstraction to hide complicated code
    - Give user clearly defined interface

Why wouldn't we use OOP?
    - NOT FIT FOR JOB (not most efficient way)
    - May be other programming paradigms right for job
        -DAta-driven
        - functional Programming


Programming Paradigm
    -A way of programming
    -Similar to how we classify (TAXONOMY)


Objects and Classes (object born from a class)
Classes -bunch of similar charcteristics shared across
        different objects
    -A bluepint/template
    - Defines all of charact. that objects needs
    - Defines everything that is needed for an
        object during instantation
Objects - something you make
    - Defined from a class
    -Overarching data type from whih everything
            inherits from
    - Has a bunch of characteristics, defined in class
    - Everything is an object
    Python (objects built into python)
    -Int, Boolean, String, Float, List, Dict, Set,
        Tuple,

Important parts of OOP OBJECT TAKES FROM CLASS)
    Encapsulation: big in OOP
        - BASE of OOP
        - Grouping all items into a single unit
        -i.e. all of the char. of a class
        -i.e. putting everything into single class

    Inheritance
    - Aquires properties of another class
    Polymorphism
    Abstraction
"""
class Animal (object): #build a new class, here there are two functions in this class
    def __init__(self): #Define initializer runs whenever obj instance is created

        #self: this object that you're working with

        #put characteristics
        self.numLegs = 4
        self.color = "brown" #object doesn't retain those if you don't put self

    def eat(self):  #function inside animal class
        print("Om nom. Just ate.")

anAnimal = Animal()#runs sort of like a function. instanciate an animal object
print(anAnimal)
print(Animal)
anAnimal.eat()  #already a print statement in def
        #-> 1. Goes to anAnimal object 2. eat 3. () tells it to run function

        #inheritance come from classes
"""
Inheritance
        Animal
            -Birds
            -felines
            -Reptiles

  Animal is parent class
    Cat is child class

"""
class Cat(Animal): #this is where you to ineritance, when you run cat you'll run animal argument
    pass            #you've defined it so you can use it

aCat = Cat()    #a cat object in memory
print(aCat)
aCat.eat()
print(anAnimal.color)
print(aCat.color)
blueCat = Cat()
blueCat.color = "blue"
print(blueCat.color)

"""
    Polymorphism
    - takes many forms
    - changing an existing funcitno to suit subclass/child
        class requriements

    Override
    - closely related to polymorphism
    - takes function and makes it do
        something different

    Overloading
    - defining function with the same name with different
        functionality
    - allowed by different function definitino
        - different arg parameters
"""
#new class, ref animal
print()
class Dog(Animal):
    def eat(self):
        print("Om nom. I just ate dog food.")

    def eat(self, food):
        print("Om nom. I just ate, but I ate {0} instead.".format(food))
aDog = Dog()
aDog.eat()

"""
Abstraction

print() - we know how to use it, what it does
            but not how it works
"""
class Calc(object):
    def __index__(self):
        pass

    def generateNum(self, num):
        num = num * num
aCalc = Calc()
print(aCalc.generateNum(5))

"""
Getter and setter methods
    object oriented guidelines
-
"""
class  Person(object):
    def __index__(self):
        self.numLegs = None
        self.eyeColor = None
        self.abs = None

        #setter method, takes info from user and put into attribute
        def setNumLegs(self, numbLegs):
            self.numLegs = numbLegs
#getter method, grabs attribute and returns it
def getNumLegs(self):
    return self.numLegs

a = Person()
a.setNumLegs(4)
print(a.getNumlegs(),"legs")

a.numLegs = 3 #setting
print(a.numLegs) #getting