n = input()
#MYKHAILO
for i in range(0, len(n), 8):
    if n[i:i + 8] != "MYKHAILO":
        print("NI")
        exit()
print("TAK")
