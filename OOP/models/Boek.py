#Boek.py

class Boek: #alt insert --> bjecten toeveolgen
    def __init__(self, titel: str, auteur: str) -> None:
        super().__init__() #je maakt gebruik van de hoofd klasse
        self.__titel = titel #__ aanwijzing om aan te geven dat iets privaat is

#properties
    @property
    def titel(self):
        return self.__titel

    @titel.setter
    def titel(self, waarde):
        self.__titel = waarde

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, value):
        self.__auteur = value

# methodes
    def __str__(self) -> str:
        return self().__auteur + "van boek" + self.__titel

