
import math

class Meetwiel:

    def __init__(self, straal, omwenteling) -> None:
        self.__straal = straal
        self.__omwenteling = omwenteling

    def __str__(self):
        return "meetwiel met straal " + str(self.__straal) + " aantal omwentelingen " + str(self.__omwenteling) + " de omtrek is " + str(self.omtrek) + " de afgelegde afstand is " + str(self.afstand)
    @property
    def straal(self):
        return self.__straal

    @straal.setter
    def straal(self, waarde):
        self.__straal = waarde

    @property
    def omtrek(self):
        return self.__straal * 2 * math.pi

    @property
    def omwenteling(self):
        return self.__omwenteling

    @omwenteling.setter
    def omwenteling(self, waarde):
        self.__omwenteling = waarde

    @property
    def afstand(self):
        return self.omtrek * self.__omwenteling

