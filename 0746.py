n,m = map(int,input().split())
sp = [False] * n

for i in range(m):
    a,b = map(int,input().split())
    c = b-a+1
    i = 0
    while i < n and c > 0:
        if sp[i] == False:
            sp[i] = True
            c-=1
        i+=1

print(res)