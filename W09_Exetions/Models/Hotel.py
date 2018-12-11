# hotel
from W09_Exetions.Models.Hotelkamer import Hotelkamer
from W09_Exetions.Models.Hotelgast import Hotelgast


class Hotel:
    def __init__(self, kamers=[]) -> None:
        self.__dict_kamers = {}
        for kamer in kamers:
            self.__dict_kamers[kamer] = Hotelkamer(kamer)

    def __str__(self) -> str:
        return str(self)

    @property
    def dicht_kamers(self):
        return self.__dict_kamers

    @dicht_kamers.setter
    def dicht_kamers(self, value):
        pass

    def kamer_is_vrij(self):


    def get_kamer(selfself, kamernummer):
        if (kamernummer in self.__dict_kamers):


    def add_gast(self,hotelgast:Hotelgast, kamer_nr:str):
        line_to_print = ""
        hotelkamer = self.dicht_kamers[kamer_nr]
        if hotelkamer.kamer_is_vrij:
            hotelkamer.add_gast(hotelgast)
            line_to_print += "Kamer {0} is gereserveerd.".format(kamer_nr)
        else:
             line_to_print += "Kamer {0} is niet vrij.".format(kamer_nr)
        return line_to_print

    def show_bezetting_hotel(self):
        line_to_print = ""
        for kamer_obj in self.__dict_kamers.values():
            if(kamer_obj.kamer_is_vrij):
               line_to_print += kamer_obj.nummer
               for hotelgast_obj in kamer_obj.lijst_gasten:
                   line_to_print += "\t{0}".format()

