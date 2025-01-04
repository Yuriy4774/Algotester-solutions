a = input()
a = [char for char in a]
min_n = a.copy()
max_n = a.copy()

for i in range(0,len(a)):
    if a[i] == "*":
        if i == 0:
            min_n[i] = "1"
        else:
            min_n[i] = "0"
        max_n[i] = "9"


min_n,max_n = ''.join(min_n),"".join(max_n)
print(min_n,max_n)
