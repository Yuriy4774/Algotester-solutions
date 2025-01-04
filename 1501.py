xy = list(map(int,input().split()))
axy = list(map(int,input().split()))
x,y = xy[0],xy[1]
a_x,a_y = axy[0],axy[1]
res = abs(x-a_x)+abs(y-a_y)
print(res)
