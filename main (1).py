def binbasen(x, y):
    t = ""
    while x > 0:
        f = x % y
        t = str(f)+t
        x //= y
    return t
h = []    
while True:
    a, b = map(int, input().split())
    if [a, b] == [-1, -1]:
        break
    else:
        total_sum = 0
        if 2 <= b <= 9:
            for i in range(1, a + 1):
                if a % i == 0:
                    total_sum += i
            h.append(binbasen(total_sum,b))
        else:
            print("invalid base!")
            exit()
p = 0
for i in h:
    p += int(i)
print(p)










