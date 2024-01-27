n = int(input())
pattern = [["." for i in range(n)]]
pattern[0][0] = "*"
a, b = 0, 0

while True:
    m = input()
    if m == "END":
        break
    if m == "R":
        b = min(b+1, n-1)
    elif m == "L":
        b = max(b-1, 0)
    elif m == "B":
        a += 1
    if a == len(pattern):
        pattern.append(["."for i in range(n)])
    pattern[a][b] = "*"
for row in pattern:
    print(" ".join(row))
if a != len(pattern)-1 or b != n-1:
    print("There's no way out!")





