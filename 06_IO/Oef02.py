#oefening 02
import os


def lees_bestand_in_lijstnummer(bestand):
    f = open(bestand, "r", encoding="utf-8")
    line = f.readline()

    index = 1
    while(line):
        line = line.rstrip("\n")
        print("{0}: {1}".format(index,line))
        index += 1
        line = f.readline()
    f.close()

def shrijf_input_naar_bestand(bestand):
    f = open(bestand, "w")
    invoer = input("Wat wil je invoeren: ")
    while(invoer != "s"):
        f.write(invoer + "\n")
        invoer = input("wat wil je nog invoeren (sluit af met 's' : ")
    f.close()
if(os.path.exists("Tekst2.txt")):
    {
        lees_bestand_in_lijstnummer("Tekst2.txt")
    }
else:
    {
        shrijf_input_naar_bestand("Tekst2.txt")
    }