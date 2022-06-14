a=int(input("Első szám: "))
b=int(input("Második szám: "))
c=int(input("Harmadik szám: "))

max=[a,b,c]

max.sort()
i=len(max)
i=i-1
print(max[i])