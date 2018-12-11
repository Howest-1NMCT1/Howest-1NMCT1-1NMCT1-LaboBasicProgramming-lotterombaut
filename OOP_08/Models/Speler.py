
class Speler:
    def __init__(self, parnaam, parvoornaam, parscore) -> None:
        self.__naam = parnaam
        self.__voornaam = parvoornaam
        self.__score = parscore

    def __str__(self):
        return "de speler heet {0} {1}, de persoonlijke score bedraagd {2} punten.".format(self.__naam, self.__voornaam, str(self.score))

    #def bereken_teamscore(self):
    

    @property
    def naam(self):
        return self.__naam
#setter is om waarde aan te passen

    @property
    def voornaam(self):
        return self.__voornaam

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, nieuwescore):
        self.__scoree = nieuwescore