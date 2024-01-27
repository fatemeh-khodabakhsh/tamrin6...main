def mahi():
    a = b.split(" ")
    a.sort(key=lambda x: int(x[1:]))
    for x in a:
        print(x[0], end="")
b =str(input())
mahi()