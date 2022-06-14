# Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
# képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok
# összege!



oszzeg=0
a=int(input("Szám ami pozitiv: "))
list=list((range(a)))
for i in range(1,a):
    oszzeg+=list[i]
print( oszzeg)