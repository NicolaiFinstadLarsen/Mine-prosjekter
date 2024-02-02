import random
import time


adjektiver = []
i = 1
while len(adjektiver) <= 12:
    print("Ord ", i, "av", 13)
    nytt_ord = input("Skriv inn et adjektiv: ")
    adjektiver.append(nytt_ord)
    i += 1
    
# print(adjektiver)
    
random.shuffle(adjektiver)

# # print(adjektiver)

hovedtekst = ("Det var en gang en {} mann som var veldig {}, han hadde en {} bil og en {} bolig. "
              "En dag fant han en {} dame han likte veldig godt. Han tok frem en {} mobiltelefon og spurte om nummeret hennes. "
              "Dama hadde en {} veske, men mannen tenkte ikke så mye på det. Han hadde jo en {} lue på seg. "
              "Etter en {} pause ga kvinnen tilbake den {} mobilen til den {} mannen. Han var så {} for å ha fått telefon nummeret til en så {} kvinne".format(*adjektiver))
print()
print("Her kommer din histore!")
print()
time.sleep((1.5))
print(hovedtekst)