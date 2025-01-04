n = int(input())
sp = list(map(str,input().split()))

count = {}

for i in sp:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

a = []
m = ''

for char_c, count_c in count.items():
    a.append(char_c * (count_c // 2))
    if count_c % 2 == 1:
        if m == '':
           m = char_c
print("".join(a)+m+"".join(a[::-1]))
