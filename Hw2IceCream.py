

w=int(input("Width: "))
x=""

for i in range(w,0,-2):
    for j in range((w-i)//2,0,-1):  #(w-i)=5-5=0   (w-i)=5-3=2//2=1  (w-i)=5-1=4//2=2
         x = " " + x
    for t in range(0,i):        # 1s & 0s
        if (t%2==0):
            x=x+"0"
        else:
            x=x+"1"
    print(x)
    x=""











