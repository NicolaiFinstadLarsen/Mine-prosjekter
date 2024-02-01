
def my_yield():
    x = int(input("What is your max capacity? "))
    y = int(input("What is your max price? "))
    

    a = int(input("What is your average capacity usage? "))
    b = int(input("What is your ATP(average ticket price? "))
    
    max_tot = x * y 
    avg_tot = a * b
    
    result = avg_tot / max_tot
    
    #print(result)
    print("Your yield is:", round(result,4)*100,"%")
    
my_yield()