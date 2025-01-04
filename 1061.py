#m, n = map(int, input().split())
n = int(input())
sp,res,st = [],0,0

for i in range(n):
    a = int(input())
    if a == 1:
        st+=1
    else:
        if st <= 0:
            res+=1
        else:
            st-=1

print(res)
