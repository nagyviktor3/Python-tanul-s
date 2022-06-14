szam = int(input())
szam1 = szam > 0 and szam < 21

if szam > 20:
    print("A szám nagyobb mint 20.")
else:
    for i in range(szam1-1,szam):
        print(szam1*" ","START")