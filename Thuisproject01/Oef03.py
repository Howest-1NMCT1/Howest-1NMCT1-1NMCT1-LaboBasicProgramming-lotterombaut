#oef03

invoer = "ABd1234@112"
#print(lst)

def is_paswoord_correct (wachtwoord):
    groot = 0
    klein = 0
    cijfer = 0
    spkarakter = 0
    listcijfers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lengte = 0
    lst = list(wachtwoord)
    for char in lst:
        if(char.isupper() == True):
            groot = True
        elif(char.islower() == True):
            klein = True
        elif char == "#" or char == "$" or char == "@":
            spkarakter = True
        else:
            for nummer in listcijfers:
                if (char == nummer):
                    cijfer = True
    if(len(wachtwoord) >= 10 and len(wachtwoord)<= 18):
        lengte= True
    if(groot == True and klein == True and cijfer ==True and spkarakter ==True and lengte ==True):
        return True
    else:
        return False

antwoord = is_paswoord_correct(invoer)
print(antwoord)



#  elif(char == listcijfers):
#     cijfer = True
