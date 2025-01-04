n = input()
a = n[0]
c = 1
res = ""
for i in range(1,len(n)):
    if n[i] == a:
        c+=1
    else:
        res+=str(c)
        res+=a
        c = 1
        a = n[i]
res+=str(c)
res+=a
print(res)
