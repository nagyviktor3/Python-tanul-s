


with open("szamok.txt","w") as file:
    x=0
    counter=0
    
    while counter<100:
        if x%3==0:
            file.write(str(x))#("{x}\n")
            file.write('\n')
            counter+=1
            x+=1
        else:
            counter+=1
            x+=1