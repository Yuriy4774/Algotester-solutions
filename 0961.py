x,y,z = map(int, input().split())

if z > x+y:
    print(x+y)
else:
    if z < x-y:
        print(-1)
    else:
        print(z)
