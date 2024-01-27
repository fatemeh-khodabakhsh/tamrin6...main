n = str(input())
def lcd(a,b):
    return abs(a*b)//gcd(a,b)
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
sum =0
if n == "sum":
    while (True):
        a = input()
        if(a=="end"):
            break
        a= int(a)
        sum += a
    print(sum)

elif n== "average":
    sum = 0
    count =0
    while (True):
        a = input()
        if(a=="end"):
            break
        a= int(a)
        sum += a
        count += 1
    print(round(sum/count,2))
elif n == "lcd":
    b = []
    while (True):
        a = input()
        if (a == "end"):
            break
        b.append(int(a))
    while len(b) != 1:
        kmm = lcd(b[0], b[1])
        x = b[0]
        y = b[1]
        b.remove(x)
        b.remove(y)
        b.append(kmm)
    print(b[0])
elif n=="gcd":
    b=[]
    while (True):
        a = input()
        if(a=="end"):
            break
        b.append(int(a))
    while len(b)!=1:
        bmm=gcd(b[0],b[1])
        x=b[0]
        y=b[1]
        b.remove(x)
        b.remove(y)
        b.append(bmm)
    print(b[0])
elif n == "min":
    x = int()
    min = x
    while (True):
        a = input()
        if (a == "end"):
            break
        a =int(a)
        if a < x or min==x:
            x=a
    print(x)

elif n=="max":
    x =int()
    max = x
    while(True):
        a = input()
        if (a == "end"):
            break
        a = int(a)
        if a > x or max==x :
            x =a
    print(x)
else:
    print("Invalid command")