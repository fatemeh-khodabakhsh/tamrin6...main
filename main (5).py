n = input()
x = n.split()
b = int(input())
f = {}

for i,j in enumerate(x):
     f[(int(j))] = i
c={}
for k in f.keys():
    t = b-k
    if t in f and t != k:
        d = f[k]+f[t]
        if (t, k) not in c.keys():
            c[(k, t)] = d
r = sorted(c.values())
if not c:
    print("Not Found!")
else:
    for h in r:
        print(h)