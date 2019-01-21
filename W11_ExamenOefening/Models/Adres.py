#klasse adres

class Adres:
    def __init__(self, parstraat:str, parnummer:str, parpostcode:str, pargemeente:str):
        self.straat = parstraat
        self.nummer = parnummer
        self.postcode = parpostcode
        self.gemeente = pargemeente


    @property
    def straat(self):
        return self.__straat

    @straat.setter
    def straat(self, new_straat):
        if(isinstance(new_straat, str)and new_straat != "" ):
         self.__straat = new_straat
        else:
            raise ("straat is niet correct")


    @property
    def nummer(self):
        return self.__nummer

    @nummer.setter
    def nummer(self, new_nummer):
        if (isinstance(new_nummer, str) and new_nummer != ""):
            self.__nummer = new_nummer
        else:
            raise ("er is iets misgegaan bij het huisnummer")

    @property
    def postcode(self):
        return self.__nummer

    @postcode.setter
    def postcode(self, new_postcode):
        if (isinstance(new_postcode, str) and new_postcode != ""):
            self.__postcode = new_postcode
        else:
            raise ("er is iets misgegaan bij de postcode")


    @property
    def gemeente(self):
        return self.__gemeente

    @gemeente.setter
    def gemeente(self, new_gemeente):
        if (isinstance(new_gemeente, str) and new_gemeente != ""):
            self.__gemeente = new_gemeente
        else:
            raise ("er is iets misgegaan bij de gemeente")


    def __str__(self):
        info = "straat: {0}, huisnummer: {1}, postcode: {2}, gemeente: {3}".format(self.straat, self.nummer, self.postcode, self.gemeente)
        return info


    def __eq__(self, other):
        if(self.straat.lower() == other.straat.lower() and self.nummer.lower() == other.nummer.lower() and self.postcode.lower() == other.postcode.lower() and self.gemeente.lower() == other.gemeente.lower()):
            return True
        else:
            return False
