n,m,k = map(int,input().split())
res = 0
def c(a,k):
    if a % k != 0:
        return a // k +1
    else:
        return a // k
for i in range(n):
    s = input()
    a = s.count('*')
    res+=c(a,k)

print(res)
