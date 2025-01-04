n,m,k = map(int,input().split())
sp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(n):
    a = ""
    b = i
    for j in range(m):
        a += sp[b % k]
        b //= k
    print(a[::-1]) 

