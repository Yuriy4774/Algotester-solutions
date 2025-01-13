n = int(input())
sp = list(map(int,input().split()))
one,two = 0,0
for i in sp:
    if i == 1:
        one+=1
    else:
        two+=1

if (one % 2 == 0 and two % 2 == 0) or (one % 2 == 0 and two % 2 == 1):
    print("YES")
    exit()
print("NO")