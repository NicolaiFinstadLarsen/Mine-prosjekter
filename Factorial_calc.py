

def driver(n):
    total = []
    # print(n)
    for i in range(1,n+1):
        total.append(i)
        # print(total)
    print(str(n)+"! er:")
    return total
    
def factorial(total):
    x = 1   
    summering = []
    
    for i in total:
        x *= i
        summering.append(x)

    # print(summering)

    return summering



opprettet_liste = driver(int(input("What number do you want a factorial for? ")))
utregning = factorial(opprettet_liste)

print(max(utregning))
