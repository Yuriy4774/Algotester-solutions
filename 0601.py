n = int(input())
sp = list(map(int,input().split()))

res = 0
for i in sp:
    if i > 47:
        res+=4
    elif i >= 8:
        res+=3
    elif i>=3:
        res+=2
    else:
        res+=1
print(res)