s = input()
sp,res = [],[]

for i in range(0,len(s)):
    if s[i] == '(':
        sp.append(i+1)
    elif s[i]  == ')':
        open = sp[-1]
        sp.pop(-1)
        close = i+1
        res.append([open,close])

print(len(res))
for i in range(len(res)):
    print(res[i][0],res[i][1])