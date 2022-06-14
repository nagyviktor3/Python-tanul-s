nev1 = input("Kérek egy nevet: ")
nev2 = input("Kérek egy másik nevet: ")
for i in range(nev1,nev2):

    if nev1 > nev2:
        print("Az első név hosszabb mint a második.")
    elif nev1 < nev2:
        print("A második név hosszabb mint az első.")
