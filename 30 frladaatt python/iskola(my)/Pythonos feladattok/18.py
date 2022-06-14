a=int(input("Elso szam: "))
b=int(input("masodik szam: "))
oszzeg=0

list=list((range(b)))
for i in range(a+1,b):
    oszzeg+=list[i]
print( oszzeg)  


