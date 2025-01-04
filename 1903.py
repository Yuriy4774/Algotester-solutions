n = int(input())
sp = list(map(int, input().split()))
sp.sort()

res,j = 1,1
for i in range(1,n):
    if sp[i] != sp[i-1]:
        j+=1
    res+=j
print(res)
