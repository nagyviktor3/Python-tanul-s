
with open("temp.txt") as f:
    for inline in f:
        words=inline.split()
        for i in range(len(words)):    
            if i%2!=0:
                print (words[i])
            

        