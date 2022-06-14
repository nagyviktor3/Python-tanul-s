szo = str(input("Kérek str: "))

for i in range(len(szo)):
    if szo[i] !=" ":
        print(szo[i],end="")
    else:
        continue