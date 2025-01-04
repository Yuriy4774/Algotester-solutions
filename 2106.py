n = int(input())
res = False
sp1 = list(input())
sp2 = list(input())

for i in range(0,len(sp1)):
    if sp1[i] == sp2[i] and int(sp1[i]) == 1:
        print("Yes")
        res = True
        break

if res == False:
    print("No")
        
