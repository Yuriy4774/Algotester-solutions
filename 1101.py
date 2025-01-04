n,m,x = map(int,input().split())
sp1 = list(map(int,input().split()))
sp2 = list(map(int,input().split()))

sp1.sort()
sp2.sort()

i,j = 0,m-1
res = float('inf')

while i < n and j >= 0:
    summ = sp1[i] + sp2[j]
    delta = abs(summ - x)

    if delta < res:
        res = delta
    
    if summ < x:
        i += 1
    else:
        j -= 1

print(res)