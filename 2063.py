n,k = map(int,input().split())
sp = list(map(int,input().split()))

res = 0
a = []
prev = float('-inf')
for i in range(n):
    if (sp[i] > prev and (sp[i] - prev == 1 or i == 0)):
        prev = sp[i]
        a.append(sp[i])
    else:
        res+=1
        #print(a)
        a = [sp[i]]
        prev = sp[i]
if len(a) > 0:
    res+=1
    #print(res)
if res > k:
    print("No")
else:
    print("Yes")