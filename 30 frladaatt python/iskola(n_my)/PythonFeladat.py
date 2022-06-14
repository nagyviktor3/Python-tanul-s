import os
from unicodedata import name


kernev = ["Márk", "Laci", "Milán", "Ákos"]
veznev = ["Török", "Szőke", "Varga", "Tóth"]
osztondij = [2000, 2500, 3000, 3500]

for i in range(len(kernev)):
    print(veznev[i], kernev[i], osztondij[i])

kernev.sort()
print("Az abc-ben a legutolsó:",kernev[0])

kernev.reverse()
print("Az abc-ben a legelső:",kernev[0])

#osszeg = osztondij[i]