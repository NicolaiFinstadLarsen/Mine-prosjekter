def lobby():
    path = "0"
    print("Lobby text")
    while path != "1" or path != "2":
        print("lobby choise")
        path = input()
        if path == "1":
            print("path 1 text")
            pathRoom1 = "0"
        return pathRoom1
        if path == "2":
            print("path 2 text")
            pathRoom2 = "0"
        return pathRoom2

    
def room1(pathRoom1):
    print("room1 text")
    while pathRoom1 != "1" or pathRoom1 != "2":
        print("room1 choise text")
        pathRoom1 = input()
        if pathRoom1 == "1":
            print("room1 choise 1 text")
            pathRoom2 = "0"
            return pathRoom2
        if pathRoom1 == "2":
            print("room 1 choise 2 text (death)")        
    

def room2(pathRoom2):
    print("room 2 text")
    while pathRoom2 != "1" or pathRoom2 != "2":
        print("room 2 choise text")
        if pathRoom2 == "1":
            print("room 2 path 1 text(Win)")
        if pathRoom2 == "2":
            print("room 2 path 2 text(death)")
    