x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
if bool(x1>0) == bool(x2>0) and bool(y1>0) == bool(y2>0):
    print("Yes")
else:
    print("No")
