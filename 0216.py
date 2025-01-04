n,m = map(int,input().split())
if n*m == 0:
    print(0)
    exit()
a = 1/(n*m)
print(f"{a:.6f}")

