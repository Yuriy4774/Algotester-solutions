sp = list(map(int, input().split()))
n = sp[0]
sp = sp[1:]

yes = True
for i in range(1,len(sp)):
    if sp[i] <= sp[i-1]:
        yes = False
        break

mnoz = {0}
if yes:
    for i in range(n):
        if sp[i] in mnoz:
            yes = False
        
        temp = set()
        for j in mnoz:
            temp.add(sp[i] + j)
        mnoz.update(temp)
        #print(mnoz)
        mnoz.discard(0)

if yes == True:
    print("Yes")
else:
    print("No")
