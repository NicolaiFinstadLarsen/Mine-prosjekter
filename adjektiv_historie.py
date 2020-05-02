with open("historie.txt","r") as file:
    
    story = file.read()
    
counts = story.count("PlaceHolder")
print(counts)  

for i in counts:
    adj = input("Adj: ")

