n = int(input())
sp = list(map(int,input().split()))
res = 0

if sp[0]>sp[1]:
    zmin=False
else:
    zmin=True
for i in range(1,len(sp)):
    if sp[i]>sp[i-1]:
        if zmin == False:
            zmin=True
            res+= 1
    if sp[i]<sp[i-1]:
        if zmin == True:
            zmin=False
            res+= 1

print(res)
