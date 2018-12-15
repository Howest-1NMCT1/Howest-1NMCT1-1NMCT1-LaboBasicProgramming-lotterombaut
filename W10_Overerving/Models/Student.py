from W10_Overerving.Models.Persoon import Persoon


class Student(Persoon):
    def __init__(self, par_naam, par_voornaam, par_studentennummer, par_opleiding, par_geboortejaar=2016):
        Persoon.__init__(self, par_naam, par_voornaam, par_geboortejaar)
        self.__studentennummer = par_studentennummer
        self.__opleiding = par_opleiding

    @property
    def studentennummer(self):
        return self.__studentennummer

    @studentennummer.setter
    def studentennummer(self, value):
        if isinstance(value, int):
            self.__studentennummer = value
        else:
            raise ValueError("Geen geldig studentennummer!")

    @property
    def opleiding(self):
        return self.__opleiding

    @opleiding.setter
    def opleiding(self, value):
        if value != "":
            self.__opleiding = value
        else:
            raise ValueError("Geen geldige opleiding!")

    def __str__(self):
        return "Student " + super().__str__()

    def __eq__(self, other):
        print("eq - Student")
        if self.__studentennummer == other.__studentennummer:
            return True
        else:
            return False

