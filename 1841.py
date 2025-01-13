n = input()
if len(n) % 2 == 1:
    center = len(n) // 2
    a,b = n[:center],n[center+1:]
    a = a[::-1]
    for i in range(len(a)):
        if not(a[i] == b[i] or a[i] in '47' or b[i] in '47'):
            print("NO")
            exit()
else:
    center = len(n) // 2
    a,b = n[:center],n[center:]
    a = a[::-1]
    for i in range(len(a)):
        if not(a[i] == b[i] or a[i] in '47' or b[i] in '47'):
            print("NO")
            exit()
print("YES")