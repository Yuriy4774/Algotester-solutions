n = int(input())
s= []
s = [*input()]
num_k,num_a,num_n,num_p = 0,0,0,0
for i in s:
    if i == 'k':
        num_k += 1
    elif i == 'a':
        num_a += 1
    elif i == 'n':
        num_n += 1
    elif i == 'p':
        num_p += 1

num_napka = min(num_k - 1,(num_a - 1) // 2,num_p,num_n)
print(num_napka)
