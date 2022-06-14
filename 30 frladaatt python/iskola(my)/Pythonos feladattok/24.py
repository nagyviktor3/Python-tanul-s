string1 = 'Debrecen'
f = open("temp.txt", "r")

flag = 0
index = 0
  
for line in f:  
    index += 1 
      
    if string1 in line:
      flag = 1
      break 

if flag == 1: 
   print(string1 , 'találtam a szövegben!') 
else: 
   print(string1, 'Nem találtam a szövegben!', index)

f.close() 