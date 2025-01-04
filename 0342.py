a,b,c,r = map(int,input().split())
res = []

p = (a + b + c) / 2

S = (p * (p - a) * (p - b) * (p - c))**0.5

R = (a * b * c) / (4 * S)

if R <= r:
    res.append('+')
else:
    res.append('-')

p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c))**0.5
r1 = S / p
if r1 >= r:
    res.append('+')
else:
    res.append('-')
print(res[0],res[1],sep="")