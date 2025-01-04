n, sp = input().split()

sp,n = [int(digit) for digit in sp],int(n)
#print(sp,n)
res = 1
for i in range(n):
        res *= 2
print(res)

