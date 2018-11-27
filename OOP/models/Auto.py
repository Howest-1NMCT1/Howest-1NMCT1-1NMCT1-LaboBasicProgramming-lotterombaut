#Auto.py

#contuctor
class Auto:
    def __init__(self, kleur:str, merk:str, brandstof:str, model:str, km_stand:int) -> None:       # geef aan wat je wil initialiseren
        self.__kleur = kleur
        self.__merk = merk
        self.__brandstof = brandstof
        self.__model = model
        self.__km_stand = km_stand

#properties

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, newcolor):
        self.__kleur = newcolor

    @property
    def merk(self):
        return self.__merk
    #merk mag niet aangepast worden, dus de setter moet weg

    @property
    def model(self):
        return self.__model

    @property
    def brandstof(self):
        return self.__brandstof

    @property
    def km_stand(self):
        return self.__km_stand

    @km_stand.setter
    def km_stand (self, newstand):
        self.__km_stand = newstand


#methode
    def rijden(self,extra_km):
        self.__km_stand += extra_km

#Tostring overwride

    def __str__(self) -> str:
        return "Merk: {0}, Model: {1}, Km stand: {2}. ".format(self.__merk, self.__model, self.__km_stand)