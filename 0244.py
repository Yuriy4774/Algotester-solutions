n = int(input())
a = 0
    
for _ in range(n):
    b = input().strip()
        
    if b == "In":
        a += 1
    elif b == "Out":
        if a == 0:
            print("Error")
            exit()
        a -= 1
    
if a > 0:
    print("Cunning elector")
else:
    print("Just a fantasy")
