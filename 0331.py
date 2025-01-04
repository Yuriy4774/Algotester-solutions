sp = list(input())

count = {}

for i in sp:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

one = False
for char_c, count_c in count.items():
    if count_c % 2 == 1:
        if one:
            print("NO")
            exit()
        one = True

print("YES")
