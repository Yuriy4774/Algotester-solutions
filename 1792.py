n = int(input())
sp = list(map(int,input().split()))
sp.sort()

for i in sp:
    if i < 51:
        print("Zabud pro stypendiiu")
        exit()
    elif i < 90:
        print("Zvychaina")
        exit()
    
print("Pidvyshchena")
