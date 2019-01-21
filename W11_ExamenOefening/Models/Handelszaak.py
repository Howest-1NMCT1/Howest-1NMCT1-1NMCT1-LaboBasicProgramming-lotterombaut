#klasse handelszaak
from W11_ExamenOefening.Models.Adres import Adres

class Handelszaak:
    def __init__(self, partelefoonnummer:str , adres:Adres):
        self.telefoonnummer = partelefoonnummer
        self.adres = adres

    @property
    def telefoonnummer(self):
        return self.__telefoonnummer

    @telefoonnummer.setter
    def telefoonnummer(self, new_telefoonnummer):
        if(isinstance(new_telefoonnummer, str)and new_telefoonnummer != "" ):
            self.__telefoonnummer = new_telefoonnummer
        else:
            raise ("incorrect telefoonnummer")

    @property
    def adres(self):
        return self.adres

    @adres.setter
    def adres(self, value):
        if isinstance(value, Adres):
            self.__adres = value
        else:
            raise ("oncorrect adres")

    def __str__(self):
        info = " telefoonnummer: {0}, Adres: {1}".format(self.telefoonnummer, self.adres)
        return info

    def __lt__(self, other):
        return self.telefoonnummer.lower() == other.telefoonnummer.lower() and self.adres == other.adres

