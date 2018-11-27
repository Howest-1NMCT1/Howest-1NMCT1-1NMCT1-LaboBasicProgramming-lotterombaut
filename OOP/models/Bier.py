
class Bier:

#constructor
    def __init__(self, nr:int, naam:str, brouwerij:str, kleur:str, alcohol:str) -> None:
        self.__nr = nr
        self.__brouwerij = brouwerij
        self.__kleur = kleur
        self.__alcohol = alcohol

#properties
    @property
    def nr(self):
       return self.__nr

    @property
    def brouwerij(self):
        return self.__brouwerij

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, nieuwkleur):
        self.__kleur = nieuwkleur
    @property
    def alcohol(self):
        return self.__alcohol

    @alcohol.setter
    def alcohol(self, waardealcohol):
        self.__alcohol = waardealcohol

#methodes

    def __str__(self) -> str:
        return "Nummer: {0}, Naam: {1}, Brouwerij: {2}, kleur: {3}, alcohol percenage: {4}. ".format(self.__nr, self.__naam, self.__brouwerij, self.__kleur, self.__alcohol)