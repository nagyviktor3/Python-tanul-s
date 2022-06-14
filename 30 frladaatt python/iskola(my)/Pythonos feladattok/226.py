with open("temp.txt", "r") as f:
    io=0
    
    for line in f:
        
        words = line.split()
        if io%2==0:
            print(words[io])
            io +=1
        else:
            io +=1