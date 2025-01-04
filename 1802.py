n,m = map(int,input().split())

if (m - n) % 12 == 0:
    print(int(((m+n)*13)/2))
else:
    print(-1)
