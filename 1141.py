n = input()
m = input()

res_n = 0
res = ""
for i in [n,m]:
    for j in range(1,len(i),2):
        if i[j] == 'u':
            res_n+=2
        elif i[j] == 'y':
            res_n+=1
        else:
            j+=1

ku,kyu = 0,0
ku = res_n // 2
kyu = res_n % 2
for i in range(ku):
    res+="ku"
for i in range(kyu):
    res+="kyu"
print(res)

