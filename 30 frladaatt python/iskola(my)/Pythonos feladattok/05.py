# Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
# hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!

a=int(input('1: '))
b=int(input('2: '))
c=int(input('3: '))

if a +b ==c:
    print("1. és 2. szám összege egyenlő-e a harmadik számmal!")
if c +b ==a:
    print("2. és 3. szám összege egyenlő-e a harmadik számmal!")
if a +c ==b:
    print("1. és 3. szám összege egyenlő-e a harmadik számmal!")
