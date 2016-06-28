"""
The Odd One
6.24.2016

It's a hot day out and everybody's in the mood for ice cream. Word on the street is there's a new ice cream startup in town that's supposedly run by Oddity Kelpy.
When you go over to see what the hype is all about, you see Oddity Kelpy outside of the ice cream store frantically running about. She sees you and rushes over to
see if you can help her with her problem.

There are too many people lining up at the door for the big opening of her ice cream shop, Creamtel, because there aren't enough workers to make the cones for all
ice cream being sold.

Oddity Kelpy's trade secret is that her cones are made of 0's and 1's, and the extra work needed to make these cones keeps her from being able
to mass produce these cones quickly. She needs a program that will help her make cones on demand and allows her to be able to input the biggest width of a cone, and
print out a schematic for what that would look like. She can then use a 3-D printer to print out the cone.

For example, if she wanted a cone with a width of 5, then her desired cone schematic would be:
    01010
     010
      0

Each layer of the cone will start with a 0 and alternate between 1's and 0's from there. The output will be centered as shown with spaces as filler.
"""

widthOfCone = int(input("What is your desired cone width?"))


x = [[(i+j)%2 for i in range(widthOfCone)]for j in range (widthOfCone-2)] #generates random 0s and 1s with the width

for row in x:
    for cell in row:
        print (cell, end=' ')
    print()
#for

"""
one = [1]
zero = [0]

for i in range (0, widthOfCone):
    for j
"""
# -1 from both sides and increases
