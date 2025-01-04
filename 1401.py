n = int(input())
a = list(map(int, input(). split()))
p = a[0] % 2
res = 0
for i in range(1,len(a)):
    if a[i] % 2 != p:
        res+=1
        p = a[i] % 2

print(res)
