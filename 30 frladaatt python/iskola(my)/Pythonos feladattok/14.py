# 4. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós
# számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott
# értékek között helyezkednek el!

b=int(input("Szám ami pozitiv: "))
a=int(input("Szám ami pozitiv2: "))
list=list((range(a)))
for i in range(b+1,a):
    print(i)
