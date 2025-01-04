n = input()
s  = ""
for i in range(0,len(n)):
    if i % 2 == 0:
        s+=str(int(n[i])*2)
    else:
        s+=n[i]
q = 0
for i in s:
    q+=int(i)
b = n[0]+n[1]
if q%10 == 0 and (b == '51' or b == '52' or b == '53' or b == '54' or b == '55'):
    print("VALID")
else:
    print("BAD")
