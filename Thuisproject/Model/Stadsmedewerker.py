from Thuisproject.Model.Melding import Melding


class Stadsmedewerker:
    def __init__(self, paranaam:str, paravoornaam:str ,paradienst:str):
        self.naam = paranaam
        self.voornaam = paravoornaam
        self.dienst = paradienst
        self.list_teverwerkenmeldingen = []

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if isinstance(value, str) and value != "":
            self.__naam = value
        else:
            raise ValueError("naam is ongeldig")
        
    @property
    def voornaam(self):
        return self.__voornaam
    
    @voornaam.setter
    def voornaam(self, value):
        if isinstance(value, str) and value != "":
            self.__voornaam =value
        else:
            raise ValueError("voornaam is ongeldig")

    @property
    def dienst(self):
        return self.__dienst

    @dienst.setter
    def dienst(self, value):
        if isinstance(value, str) and  value != "":
            self.__dienst = value
        else:
            raise ValueError("dienst is ongeldig")

    @property
    def meldingen(self):
        return self.list_teverwerkenmeldingen   #attribuut staat niet private (wil je wel private --> moet ze overal private staan

    def __str__(self):
        return "Medewerker {0} {1}".format(self.naam, self.voornaam)

    def __eq__(self, other):
        if self.naam == other.naam and self.voornaam == other.voornaam and self.dienst == other.dienst:
            return True
        else:
            return False

    def verwerk_nieuwe_melding(self, nieuwe_melding):
        if isinstance(nieuwe_melding, Melding):
            self.list_teverwerkenmeldingen.append(nieuwe_melding)
        else:
            raise  ValueError ("meldingswaarde ongeldig")

    def melding_verwerkt(self,de_verwerkte_melding):
        #behoort de melding tot deze medewerker? en zit ze in de list
        if de_verwerkte_melding in self.meldingen:
            self.meldingen.remove(de_verwerkte_melding)

    def selecteer_mijn_meldingen(self,meldingen, gezocht):
        for melding in meldingen:
            if gezocht.lower() in melding.categorie.lower():
                #melding specefiek voor die stadsmedewerker
                self.verwerk_nieuwe_melding(melding)