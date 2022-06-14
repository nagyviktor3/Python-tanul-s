# Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a
# képernyőre, hogy mind a három páros szám-e (igen/nem)!
a=int(input("Kérek egy egész számot!: "))
b=int(input("Kérek egy egész számot!: "))
c=int(input("Kérek egy egész számot!: "))
paros=a%2 or b%2 or c%2
if paros==0:
    print("Igen")
else:
    print("Nem")










