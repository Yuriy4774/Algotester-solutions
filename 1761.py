sp=list(map(int,input().split()))
sp.sort()
if sp[0]+sp[1] <= 47:
    print("YES")
else:
    print("NO")

