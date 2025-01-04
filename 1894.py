n = int(input())
sp = list(map(int,input().split()))

res = 0
def d(a,b):
    if a < b and sp[a] > sp[b]:
        return True
    return False

for i in range(0,len(sp)):
    for j in range(0,len(sp)):
        if d(i,j):
            res+=1

print(res)
