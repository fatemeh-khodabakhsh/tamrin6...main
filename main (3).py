n = int(input())
for i in range(n):
    for j in range(1 , n-i+1):
        print(end='')
    temp = 1   
    for j in range(i+1):
        if (j == 0 or i == j):
            temp = 1
        else:
            temp = temp * (i-j+1) // j
        print(temp, end=" ")
    print()
