s = input()
x,y = map(int, input().split())
res_x,res_y = 0,0
for i in s:
    if i == 'R':
        res_x+=1
    else:
        res_y+=1

if res_x >= x and res_y >= y:
    print("YES")
else:
    print("NO")

