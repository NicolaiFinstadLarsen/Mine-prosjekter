with open("historie.txt","r") as file:
    
    story = file.read()
    
counts = story.count("PlaceHolder")
#print(counts)    

Adj=[]
for element in range(counts):
    Adj.append(input("Skriv adjektiv: "))
    
               
print(Adj)









    

#print(A)
#print(c)