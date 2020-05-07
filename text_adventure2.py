

def lobby():
    path = ""
    print("Lobby text")
    while path != "1" and path != "2":
        print("lobby choise")
        path = input("choose your path 1 or 2: ")
        if path == "1":
            print("lobby path 1 text")
            pathRoom1 = ""
            return pathRoom1
        if path == "2":
            print("lobby path 2 text")
            pathRoom2 = ""
            return pathRoom2

def room1(lobby):
    print("room1 text")
    while pathRoom1 != "1" and pathRoom1 != "2":
        print("room1 choise text")
        pathRoom1 = input("choose your path 1 or 2: ")
        if pathRoom1 == "1":
            print("room1 choise 1 text")
            pathRoom2 = ""
            return pathRoom2
        if pathRoom1 == "2":
            print("room 1 choise 2 text (death)")        
    

def room2(room1):
    print("room 2 text")
    while pathRoom2 != "1" and pathRoom2 != "2":
        print("room 2 choise text")
        pathRoom2 = input("choose your path 1 or 2: ")
        if pathRoom2 == "1":
            print("room 2 path 1 text(Win)")
        if pathRoom2 == "2":
            print("room 2 path 2 text(death)")
    
lobby()
