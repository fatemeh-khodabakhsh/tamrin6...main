def lcd(a, b):
    return abs(a*b) // gcd(a,b)
    
def gcd(a, b):
    while b! = 0:
        a, b = b, a % b
    return a

n = input()
if n == "sum":
    total_sum = 0
    while True:
        a = input()
        if a == "end":
            break
        total_sum += int(a)
    print(total_sum)

elif n == "average":
    total_sum = 0
    count = 0
    while True:
        a = input()
        if a == "end":
            break
        total_sum += int(a)
        count += 1
    print(round(total_sum/count,2))
    
elif n == "lcd":
    numbers = []
    while True:
        a = input()
        if a == "end":
            break
        numbers.append(int(a))
    while len(numbers) != 1:
        kmm = lcd(numbers[0], numbers[1])
        x = numbers[0]
        y = numbers[1]
        numbers.remove(x)
        numbers.remove(y)
        numbers.append(kmm)
    print(numbers[0])
    
elif n == "gcd":
    numbers=[]
    while True:
        a = input()
        if a == "end":
            break
        numbers.append(int(a))
    while len(numbers) != 1:
        bmm = gcd(numbers[0],numbers[1])
        x=numbers[0]
        y=numbers[1]
        numbers.remove(x)
        numbers.remove(y)
        numbers.append(bmm)
    print(numbers[0])
elif n == "min":
    x = int()
    minimum = x
    while True:
        a = input()
        if a == "end":
            break
        a = int(a)
        if a < x or minimum == x:
            x = a
    print(x)

elif n == "max":
    x =int()
    maximum = x
    while True:
        a = input()
        if a == "end":
            break
        a = int(a)
        if a > x or maximum == x :
            x = a
    print(x)
else:
    print("Invalid command")
