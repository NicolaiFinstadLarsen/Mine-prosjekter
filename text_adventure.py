print("intro")
print("intro2")

print("lobby, to veier")

def rom_1(self, path):
    
    while path != "1" and path != "2" and path != "3":
        path = input("Hvilken vei vil du gå? rom1")
    
    if path == "1":
        print("Rom1_vei1")
        path_rom1 = input("Hvilken vei? rom1_vei1 ") # rom 2 eller 3 
    if path == "2":
        print("Rom1_vei2")
        path_rom1 = input("Hvilken vei? rom1_vei2 ") # rom 2 eller 3 
    if path == "3":
        print("Død rom1_vei3")
    return path_rom1

main_path_rom1=rom_1("")
print(main_path_rom1)    
'''   
def rom_2(path_rom1):
    while path_rom1 != "1" and path_rom1 != "2":
        path_rom2 = input("Hvilken vei? rom2")
    
    
    if path_rom2 == "1":
        print("Død rom2_vei1")
       
    if path_rom2 == "2":
        print("win rom2_vei2")
    return path_rom2

#def rom_3(path_rom2):
    #while path_rom1 != "2"
print(path_rom2)
'''
rom_1("")
#rom_2("")
