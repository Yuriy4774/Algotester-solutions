import math

n = int(input())

def lcm(x1,x2):
    return (x1*x2) // math.gcd(x1,x2)

i,sp,res = 1,[],0
while i <= n:
    if n % i == 0:
        sp.append(i)
    i+=1
    
for i in sp:
    for j in sp:
        if lcm(i,j) == n:
            res+=1
print(res)

