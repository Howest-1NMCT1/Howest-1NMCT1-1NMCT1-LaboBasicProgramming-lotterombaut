#oefening 01 Inlezen van tekst
import os
current_dir= os.getcwd()
print(current_dir)

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
lees_bestand_in_lijstnummer("Tekst.txt")

