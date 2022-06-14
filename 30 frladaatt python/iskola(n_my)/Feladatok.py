from curses import pair_content
from optparse import Values
from pydoc import pager
import random

nev1 = input("Kérek egy nevet: ")
nev2 = input("Kérek egy másik nevet: ")
for i in range(nev1(),nev2()):

    if nev1 > nev2:
        print("Az első név hosszabb mint a második.")
    elif nev1 < nev2:
        print("A második név hosszabb mint az első.")

vsz1 = random.randint(1,100)
vsz2 = random.randint(100,200)

for i in range(vsz1,vsz2):

    if vsz1 % vsz2 == 0 and vsz2 % vsz1 == 0:
        print(i)
else:
    print(vsz2,"%", vsz1,"=", vsz2%vsz1)