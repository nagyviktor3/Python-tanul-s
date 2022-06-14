szo = str(input("Kérek str: "))

lista = list((szo))
# print (lista)
lista.reverse()
# print (lista)
for i in range(len(lista)):
    print(lista[i],end=" ")
    