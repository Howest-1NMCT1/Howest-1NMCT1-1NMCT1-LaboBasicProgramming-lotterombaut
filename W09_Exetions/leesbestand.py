
def lees_bestand():
    try:
        bestandsnaam = input("lees de getallen in van het bestand. ")
        fo = open(bestandsnaam)
        line = fo.readline()
        som = 0
        while(line):
            som += int(line)
            line = fo.readline()
        print(som)
        return som
    except FileNotFoundError as fo:
        print("File {0} is niet gevonden.".format())
    except ValueError:
        print("Je hebt een letter(combinatie) ingevoerd.")



