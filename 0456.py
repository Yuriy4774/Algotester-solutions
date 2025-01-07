n,m = map(int,input().split())
sp1 = set(list(map(int,input().split())))
sp2 = set(list(map(int,input().split())))

print(len(sp1.union(sp2)),len(sp1.intersection(sp2)))