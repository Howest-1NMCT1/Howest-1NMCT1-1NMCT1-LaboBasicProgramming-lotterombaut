#oef02
import random

invoer = int(input("Hoeveel nummerplaten wenst u?"))
teken = " - "

def get_nummerplaat(aantal):
    nummerplaten =""
    for i in range(0,aantal):
        start = random.randint(0, 9)
        letters = "azertyuiopqsdfghjklmwxcvbn"
        randletters = ""
        randcijfers = ""
        for k in range(0,3):
            randomLetter1 = random.choice(letters)
            randomcijfer = random.randint(0, 9)
            randletters += randomLetter1
            randcijfers += str(randomcijfer)
        x = str(start) + teken + randletters + teken + randcijfers + '\n'
        nummerplaten+=x
    return nummerplaten

uitvoer = get_nummerplaat(invoer)
print(uitvoer)

