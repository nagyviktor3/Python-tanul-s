# szo = str(input("Kérek str: "))
# # szo+=" "
# lista = list((szo))

# for i in range(len(lista)):
    
#     if i%3==0 :
#        print("+",end="")
#     else:
#         print("-",end="")
    
szam = int(input("Kérek int: "))
# szo+=" "
for i in range(szam):
    if i%3==0:
        print("+",end="")
    else:
        print("-",end="")
