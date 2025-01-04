n = int(input())
string = input()
redstone = 15
string = list(string)
for i in string:
    if i == "k":
        redstone = max(0,redstone-1)
    elif i == "p":
        if redstone >= 1:
            redstone = 15
        else:
            redstone = 0
    elif i == "z":
        if redstone >= 1:
            redstone = 0
        else:
            redstone = 15

print(redstone)
