from model_oef1.Persoon import Persoon


class Docent(Persoon):
    def __init__(self, par_naam, par_voornaam, par_personeelsnummer, par_opleidingen, par_geboortejaar=2016):
        super().__init__(par_naam, par_voornaam, par_geboortejaar)
        self.__personeelsnummer = par_personeelsnummer
        self.__opleidingen = par_opleidingen  # list: in welke opleidingen geeft hij/zij les?


    @property
    def personeelsnummer(self):
        return self.__personeelsnummer

    @personeelsnummer.setter
    def personeelsnummer(self, value):
        if (isinstance(value, int)):
            self.__personeelsnummer = value
        else:
            raise ValueError("Geen geldig personeelsnummer!")

    @property
    def opleidingen(self):
        return self.__opleidingen

    def geeft_les(self, opleiding):
        if not opleiding in self.__opleidingen:
            self.__opleidingen.append(opleiding)

    def __str__(self):
        return "Docent " + super().__str__()

    def __eq__(self, other):
        print("eq - Docent")
        if (self.__personeelsnummer == other.__personeelsnummer):
            return True
        else:
            return False


