nev1 = input("Kérek egy nevet: ")
nev2 = input("Kérek egy másik nevet: ")

if nev1 > nev2:
        print("Az első név hosszabb mint a második.")
elif nev1 < nev2:
        print("A második név hosszabb mint az első.")

import random

vsz1 = random(1,100)
vsz2 = random(100,200)

for i in range(vsz1,vsz2):
    print(i)

    if vsz1 % vsz2 == 0 and vsz2 % vsz1 == 0:
        print(i)
else:
    print(vsz2,"%", vsz1,"=", vsz2%vsz1)

keruletek = [5,1,7,2,6,1,5,6,4,8,3,2,7,5,4,2,6,6,7,8,1,1,5,3,4,8,2,3,1,8,8,3,7,4,3,3,2,4,6,5]
szavazatok = [19,120,162,59,73,154,188,29,143,157,13,66,34,288,77,187,13,187,130,98,34,56,67,45,221,288,220,185,199,77,67,156,129,38,87,187,65,39,288,68]
nevek = ["Ablak Antal","Alma Dalma","Bab Zsuzsanna","Barack Barna","Birs Helga","Bors Botond","Brokkoli Gyula","Ceruza Zsombor","Fasirt Ferenc","Gomba Gitta","Halmi Helga","Hold Ferenc","Hurka Herold","Joghurt Jakab","Kajszi Kolos","Kapor Karola","Karfiol Ede","Kefir Ilona","Kupa Huba","Languszta Auguszta","Lila Lilla","Medve Rudolf","Meggy Csilla","Moly Piroska","Monitor Tibor","Narancs Edmond","Oldalas Olga","Pacal Kata","Petrezselyem Petra","Pokol Vidor","Ragu Ida","Retek Etelka","Sajt Hajnalka","Simon Simon","Szilva Szilvia","Tejes Attila","Tejfel Edit","Uborka Ubul","Vadas Marcell","Vagdalt Edit"]
partok = ["-","GYEP","ZEP","GYEP","GYEP","HEP","ZEP","-","HEP","TISZ","-","-","HEP","TISZ","GYEP","ZEP","ZEP","TISZ","-","-","-","-","GYEP","-","-","GYEP","HEP","HEP","ZEP","-","HEP","ZEP","TISZ","-","GYEP","TISZ","TISZ","ZEP","HEP","HEP"]

print("Képviselők száma: ",nevek)
print(random.choice)
print(keruletek + szavazatok + nevek + partok % 4)
