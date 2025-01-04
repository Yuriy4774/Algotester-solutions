n = int(input())
sp = list(map(int, input().split()))

total = sum(sp)

summ = 0
for k in range(1, n):
    summ += sp[k - 1]
    
    s_summ = total - summ
    
    if summ == s_summ:
        print("TAK")
        exit()

print("NI")
