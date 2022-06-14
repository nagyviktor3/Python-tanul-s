import random

vsz1 = random(1,100)
vsz2 = random(100,200)

for i in range(vsz1,vsz2):
    print(i)

    if vsz1 % vsz2 == 0 and vsz2 % vsz1 == 0:
        print(i)
else:
    print(vsz2,"%", vsz1,"=", vsz2%vsz1)