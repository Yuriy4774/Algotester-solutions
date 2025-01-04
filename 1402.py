n = int(input())

res = 0
for a in range(4, n+1):
    a_str = str(a)
    q_res = sum(int(i) for i in a_str)
    
    if all(i in '47' for i in str(q_res)):
        res += 1

print(res)
