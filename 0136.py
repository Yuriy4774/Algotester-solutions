n = int(input())
sp = list(input())
sp = [int(i) for i in sp]
res = 0
#if sum(sp) == n*7:
    #print(0)
    #exit()
c = True
for i in range(n):
    if sp[i] == 7 and c:
        c = False
        #print(i)
    elif sp[i] == 4:
        if not c:
            res+=1
            c = True

print(res)