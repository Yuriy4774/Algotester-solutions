n = int(input())
sp = list(map(int, input().split()))
sp.sort()

res = 1
for i in range(n-1):
    if sp[i] != sp[i+1]:
        res+=1
print(res)
