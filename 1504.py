n = int(input())
sp = list(map(int,input().split()))
sp.sort()

for i in range(0,len(sp)-1,2):
    print(sp[i],sp[i+1])
