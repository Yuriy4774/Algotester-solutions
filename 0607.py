m,n = map(int, input().split())
sp=  list(map(int, input().split()))

def can(x):
    crav = 0
    for i in range(len(sp)):
        crav += sp[i]//x
    return crav>=m

a,b = 1e-9,max(sp)+1
while (b-a)>=10**-7:
    c = (a+b)/2
    if can(c):
        a = c
    else:
        b = c
print(round((a+b)/2,7))
