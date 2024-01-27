def mahi():
    words = b.split(" ")
    words.sort(key=lambda x: int(x[1:]))
    for word in words:
        print(word[0], end="")
b = str(input())
mahi()
