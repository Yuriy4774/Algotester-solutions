n,m = map(int, input().split())
sp,num = [],0
for i in range(n):
    a = list(map(int, input().split()))
    sp.append(a)

for i in range(len(sp)-1,-1,-1):
    for j in range(len(sp[i])-1,-1,-1):
        num += sp[i][j]
print(num)
while sp[0][0] > 0:
    for i in range(len(sp)-1,-1,-1):
        for j in range(len(sp[i])-1,-1,-1):
            if sp[i][j] > 0:
                print(i+1,j+1,sp[i][j])
                sp[i][j]-=1


