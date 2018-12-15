from datetime import datetime


class Persoon:
    # klasse-attributen
    vereniging = "Howest"
    __aantal_personen = 0  # private!

    def __init__(self, par_naam, par_voornaam, par_geboortejaar=2016):
        self.naam = par_naam
        self.voornaam = par_voornaam
        self.geboortejaar = par_geboortejaar
        Persoon.__aantal_personen += 1

    def __del__(self):
        Persoon.__aantal_personen -= 1

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if (value != ""):
            self.__naam = value
        else:
            raise ValueError("Geen geldige naam")

    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        if (value != ""):
            self.__voornaam = value
        else:
            raise ValueError("Geen geldige voornaam")

    @property
    def geboortejaar(self):
        return self.__geboortejaar

    @geboortejaar.setter
    def geboortejaar(self, value):
        # controle of de nieuwe waarde wel degelijk een int is
        if isinstance(value, int) and value >= 1900 and value <= datetime.now().year:
            self.__geboortejaar = value
        else:
            raise ValueError("Geen geldig geboortejaar")

    # extra property-methode(s)
    @property
    def leeftijd(self):
        verschil = datetime.now().year - self.geboortejaar
        return verschil

    def __str__(self):
        info = str(self.naam).upper() + ", " + self.voornaam + " (" + str(self.geboortejaar) + ") "
        return info

    def __eq__(self, other):
        print("eq - Persoon")
        if (self.naam == other.naam) and (self.voornaam == other.voornaam) and (
                    self.geboortejaar == other.geboortejaar):
            return True
        else:
            return False

    # operator <
    def __lt__(self, other):
        if self.naam != other.naam:
            return self.naam < other.naam
        else:
            return self.voornaam < other.voornaam

    @staticmethod
    def geef_aantal_personen():
        return Persoon.__aantal_personen
