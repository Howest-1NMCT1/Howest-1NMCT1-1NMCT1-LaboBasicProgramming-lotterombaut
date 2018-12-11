#oefening 05

studenten = {}

def inlezen_scores(bestand):
    f = open(bestand,"r")
    line = f.readline()
    while line:
        naam = line.split(":", [0]) #eerste element van de lijst nl 0
        temp = line.split(":") [1:]
        punten = []
        for score in temp:
            punten.append(int(score))

        line = f.readline()
    f.close()

def zoek_student(persoon):
    for naam in studenten:
        if (naam.lower().find(persoon.lower())>=0):
            print("Naam gevonden: {0}".format(naam))
            print("Scores: {0}".format(studenten[naam]))
            print("gemiddelde punten: {0}".format)


inlezen_scores()