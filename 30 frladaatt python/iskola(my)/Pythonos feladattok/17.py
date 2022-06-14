# 17. Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap három számot
# és eldönti, hogy az összes paramétere pozitív-e! A programodban hívd is meg ezt az
# alprogramot!
a=int(input("1: "))
b=int(input("2: "))
c=int(input("3: "))
def visszatérő():
    if 0<a and 0<b and 0<c:
        print("Pozitiv")
    else: print("Negatív")
visszatérő(a,b,c)