# Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a
# képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban
# találhatóak!

a=int(input("Kérek egy számot: "))
b=int(input("masik szam: "))
if b<a:
    for io in range(b,a+1):
        if io%3==0:
            print(io)
if a<b:
    for io in range(b,a+1):
        if io%3==0:
            print(io)