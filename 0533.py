sp = list(input())
sp1,sp2,res = [],[],""

for i in range(0,len(sp)//2+1):
    sp1.append(sp[i])

for i in range(len(sp)-1,len(sp)//2,-1):
    sp2.append(sp[i])

#print(sp1,sp2)

for i in range(min(len(sp1),len(sp2))):
    res += sp1[i]
    res += sp2[i]
for i in range(len(sp1)-len(sp2)):
    res += sp[i+len(sp2)]
print(res)
