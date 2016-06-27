import cmath
a = int(input("Type in a:"))
b = int(input("Type in b:"))
c = int(input("Type in c:"))

check = b*b-4*a*c
ans1 = (-b + cmath.sqrt(b*b - 4*a*c)/(2*a))
ans2 = (-b - cmath.sqrt(b*b - 4*a*c)/(2*a))

if check<0:
    print("error")
else:
    print("The roots are",ans1,"and",ans2)

