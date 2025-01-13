n = int(input())

if n == 1:
    print(3)
    exit()
r,g,b = 1,1,1
for i in range(2,n+1):
    r,g,b = g+b,r+b,r+g
print(r+g+b)