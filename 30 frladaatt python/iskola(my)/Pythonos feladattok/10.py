# Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
# felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
# a megadott szám értéke!
a=int(input("Elso szam: "))
if a<20:
    print(a*" ","start")
