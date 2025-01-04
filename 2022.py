def fill(n):
    s1,s2 = "",""
    for i in range(n):
        if i % 2 == 0:
            s1+="/"
            s2+="\\"
        else:
            s2+="/"
            s1+="\\"
    return s1,s2

n = int(input())
sp = input()
res1,res2 = 0,0
sp1,sp2 = fill(n)
for i in range(n):
    if sp[i] != sp1[i]:
        res1+=1
    if sp[i] != sp2[i]:
        res2+=1
print(min(res1,res2))
