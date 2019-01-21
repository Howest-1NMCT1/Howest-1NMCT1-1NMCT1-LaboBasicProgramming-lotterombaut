from W11_ExamenOefening.Models.Handelszaak import Handelszaak
from W11_ExamenOefening.Models.Adres import Adres
import logging

#is een = overerven (klasse met () erachter is erven)
class Huisartspraktijk(Handelszaak):

    #heeft een ... = compositie (klasse gebruiken)
    def __init__(self, praktijktype:str, telefoonnummer:Handelszaak, adres:Adres):
        self.lijst_huisarts = []
        self.praktijktype = praktijktype
        super(Huisartspraktijk, self).__init__(telefoonnummer, adres)


    @property
    def praktijktype(self):
        return self.__prakrijktype

    @praktijktype.setter
    def praktijktype(self, new_praktijktype):
        if(isinstance(new_praktijktype,str )):
            self.__praktijktype = new_praktijktype
        else:
            raise ("er is iets mis bij het ingeven van het praktijktype")

    def __str__(self):
        info = "praktijktype: {0}, telefoonnummer: {1}, adres: {2}".format(self.praktijktype, self.telefoonnummer, self.adres)
        return info

#methode
    def voeg_huisarts_toe(self,par_huisarts):
        self.lijst_huisarts.append(par_huisarts)

    @staticmethod
    def inlezen_huisarts(bestand):
        fo = open(bestand, "r")
        line = fo.readline()#controlleer hoeveel commentaar lijnen er staan (als er 2 lijnen commentaar zijn doe je deze lijn 2 maal)

        while line:
            #zolang er lijnen zijn in het csv bestand worden de lijnen uitgelezen
            line.f.readline()
            naam = line.split(";")[1]
            telefoon = line.split(";")[8]
            straat = line.split(";")[2]
            nummer = line.split(";")[4]
            postcode = line.split(";")[5]
            gemeente = line.split(";")[6]
            #bestaat de huisarts al?
            adres = Adres(straat, nummer, postcode, gemeente )
            af_te_printen = "Naam: {0}, telefoon: {1}, adres: {2}".format(naam, telefoon, adres)
            Huisartspraktijk.lijst_huisarts.append(af_te_printen)
        fo.close()

