class Locatie:
    def __init__(self, parastraat:str, paralatitude:float, paralongitude:float):
        self.__straat = parastraat
        self.__latitude = paralatitude
        self.__longitude = paralongitude

    @property
    def straat(self):
        return self.__straat    #straat xordt weergegeven

    @straat.setter
    def straat(self, value):
        if isinstance(value, str) and value != "":
            self.__straat = value
        else:
            raise ValueError("Straat ongeldig")

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if isinstance(value, float):
            self.__latitude
        else:
            raise ValueError("Latitude ongeldig")

    @property
    def lognitude(self):
        return self.__longitude

    @lognitude.setter
    def lognitude(self, value):
        if isinstance(value, float):
            self.__longitude
        else:
            raise ValueError("longitude ongelding")

    def __str__(self):
        return self.straat  #geen haakjes --> we maken gebruik van de property

    def __eq__(self, other):
        if self.straat.lower() == other.straat.lower() and self.latitude == other.latitude and self.lognitude == other.longitude:
           return True
        else:
            return False

    def __lt__(self, other):
        return self.straat.lower() < other.straat.lower()
