import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficent b: "))
c = float(input("Enter coefficient c: "))

x =(cmath.sqrt((b**2)-(4*a*c)))

ans1= (-b+x)/(2*a)
ans2= (-b-x)/(2*a)
print(ans1,ans2)