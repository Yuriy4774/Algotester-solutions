n = int(input())
sp = list(map(int, input().split()))
p,n_p = 0,0
arr_p,arr_np,res = [],[],[]

for i in sp:
    if i % 2 == 0:
        p+=1
        arr_p.append(i)
    else:
        n_p+=1
        arr_np.append(i)

if abs(n_p - p) > 1:
    print(-1)
else:
    if n_p > p:
        n_p_bool = True
    else:
        n_p_bool = False
    for i in range(n):
        if n_p_bool:
            res.append(arr_np[0])
            arr_np.pop(0)
        else:
            res.append(arr_p[0])
            arr_p.pop(0)
        n_p_bool = not n_p_bool

    print(*res)

