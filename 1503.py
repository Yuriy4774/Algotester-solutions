na = list(map(int,input().split()))
n,a = na[0],na[1]
min_val = []
for minn in range(n):
    min_val.append(0)
max_val = []
for maxx in range(n):
    max_val.append(0)
for i in range(n):
    inputs = list(map(int,input().split()))
    min_b,max_b = inputs[0],inputs[1]

    min_val[i]=min_b
    max_val[i]=max_b

max_all = 0
for j in max_val:
    max_all += j

min_all = 0
for k in min_val:
    min_all += k
if max_all < a:
    print("Impossible")
if max_all >= a:
    if min_all >= a:
        print("Certainly")
    else:
        print("Possibly")
