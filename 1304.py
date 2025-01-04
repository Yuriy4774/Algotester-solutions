n = int(input())
sp = list(map(int,input().split()))

res = 0
ind = [0] * n
for i in range(n):
    ind[sp[i] - 1] = i

l_i,r_i = -1,n
for i in range(n):
    r_i = min(ind[i], r_i)
    l_i = max(ind[i],l_i)
    if l_i-r_i + 1 == i+1:
        res+=1
print(res)
