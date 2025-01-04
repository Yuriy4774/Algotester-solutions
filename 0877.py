n = int(input())
sp = list(map(int, input().split()))
min_n ,res= sp[0],0
for i in range(1,n):
    if sp[i] <= min_n:
        res+=1
        min_n = sp[i]
print(res+1)
