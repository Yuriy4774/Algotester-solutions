sp = list(input())
s = list(input())

for i in range(0,len(sp)-len(s)+1):
    a = sp[i:i+len(s)]
    b = True
    for i in range(0,len(s)):
        #print(a[i],s[i])
        if (a[i] == s[i] or a[i] == '?') == False:
            b = False
    if b:
        print("YES")
        exit()
print("NO")
