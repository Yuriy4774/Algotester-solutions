n = input()
lenght = len(n)
y_s,b_s = "",""
blue = False
for i in range(lenght):
    if blue == False:
        y_s += 'B'
        b_s += 'Y'
        blue = True
    else:
        y_s += 'Y'
        b_s += 'B'
        blue = False

r_y,r_b = 0,0
for j in range(lenght):
    if n[j] != y_s[j]:
        r_y+=1
    if n[j] != b_s[j]:
        r_b+=1
print(min(r_y,r_b))