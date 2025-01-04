m,n,k = map(int, input().split())

t1,t2 = m / (k * 2),n / (0.5 * k)
if t1 < t2:
    print("Down")
elif t2 < t1:
    print("Up")
else:
    print("Never mind")
