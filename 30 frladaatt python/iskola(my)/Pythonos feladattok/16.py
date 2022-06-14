# . Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap egy egész
# számot és eldönti a számról, hogy osztható-e 2-vel és 3-mal is egyszerre! A programodban hívd
# is meg ezt az alprogramot!

a=int(input("szam: "))
def oszthato(a):
        if a%2==0 and a%3==0:
            print("osztható")
        else:
            print("Nem osztható")
oszthato(a)