n,m = map(int,input().split())

count = n

sp = [i for i in range(n + 1)]
size = [1] * (n + 1)
color = [i for i in range(n + 1)]

def find(a):
    if sp[a] == a:
        return a
    sp[a] = find(sp[a])
    return sp[a]

def unite(a,b):
    a = find(a)
    b = find(b)
    if (a==b):
        return 0
    
    if size[a] < size[b]:
        sp[a] = b
        size[b]+=size[a]
    else:
        sp[b] = a
        size[a] += size[b]
        color[a] = color[b]

def build_road(a,b,count):
    if (find(a) != find(b)):
        unite(a,b)
        count-=1
    return count


for i in range(m):
    a,b = map(int,input().split())
    count = build_road(a,b,count)
    print(count)

