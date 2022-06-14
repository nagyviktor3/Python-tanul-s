szam= int(input("Kérek egy számot: "))
lista=[]
while szam > 0:
    lista.append(szam)
    szam= int(input("Kérek egy számot: "))
    if szam == 0:
        print(lista)
        break


    