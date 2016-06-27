coneWidth = 9
number = int(coneWidth/2+1)
um = int(coneWidth/2+1)
x = 1
for l in range(0,um,1):
    h = ""
    all ="0"
    for i in range(1,x,1):
        h = h+" "
    for k in range(1,number,1):
        all= all+"1"+"0"
    x=x+1
    number=number-1
    print(h+all+h)

