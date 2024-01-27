a = int(input())
b = set()
for t in range(a):
    c = input()
    if "@" in c:
        i,e = c.split("@",1)
        b.add(e)
f = sorted(b)
for x in f:
    print(x)
