sp = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
res = [0] * 7
day = input()
n = int(input())
min_num = n // 7
n = n % 7
pos = sp.index(day)
for i in range(0,len(res)):
    res[i] = min_num
for j in range(n):
    res[pos]+=1
    pos = (pos + 1) % 7
print(*res)

