import re
b = input()
b = re.sub(r' +',' ',b.strip())
b = re.sub(r"\\n","\n",b)

g = ""
b =list(b)
c = []
tmp = 0

for i in b:
    if i=="@":
        c.append('@')
        tmp+=1
    elif i=='#' and tmp>0:
        tmp-=1
    else:
        c.append(i)
for item in c:
    g+=str(item)
print('Formatted Text: '+g)