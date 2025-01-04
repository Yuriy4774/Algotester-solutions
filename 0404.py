s = input()
n = int(input())
sp = ""
for i in range(n):
    sp+=input()
res = 0
while True:
    #print(sp)
    for i in s:
        if i in sp:
            sp = sp.replace(i,'',1)
            #print(sp)
        else:
            print(res)
            exit()
    res+=1
