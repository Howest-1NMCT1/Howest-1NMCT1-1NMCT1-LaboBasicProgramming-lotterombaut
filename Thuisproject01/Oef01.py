#oef01

zin = input("Geef een zin in")

def count_word(invoer):
    teller = 0
    woordenList = invoer.split(" ")
    for i in woordenList:
        if( len(i) <= 3):
            teller+=1
    return teller

x=count_word(zin)
print("Er zitten {0} kleine woorden in de zin. ".format(x))

def count_numb(invoernum):
    teller = 0
    woordenlijst = str.split(invoernum)
    for n in woordenlijst:
        if(n.isdigit()):
            teller+=1
    return teller
y=count_numb(zin)
print("Er zitten {0} getallen in de zin. ".format(y))
