from model_oef1.Persoon import Persoon


class Auto:
    def __init__(self, par_nummerplaat, par_eigenaar):
        self.__nummerplaat = par_nummerplaat
        self.__eigenaar = par_eigenaar

    @property
    def nummerplaat(self):
        return self.__nummerplaat

    @nummerplaat.setter
    def nummerplaat(self, value):
        self.__nummerplaat = value

    @property
    def eigenaar(self):
        return self.__eigenaar

    @eigenaar.setter
    def eigenaar(self, value):
        if isinstance(value, Persoon):
            self.__eigenaar = value
        else:
            raise ValueError("Geen object van de klasse Persoon")

    def __str__(self):
        return "Voertuig met kenteken %s heeft als eigenaar: %s" % (self.__nummerplaat, self.__eigenaar)
