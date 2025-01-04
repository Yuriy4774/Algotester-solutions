n = input()
n = list(n)
res = 0
for i in range(0,len(n)-1):
    if n[i] == n[i+1]:
        res+=1
print(res)

