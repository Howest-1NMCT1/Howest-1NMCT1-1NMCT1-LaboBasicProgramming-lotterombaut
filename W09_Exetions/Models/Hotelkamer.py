class Hotelkamer:
    def __init__(self, nummer) -> None:
        self.__nummer = nummer

    def __str__(self):
        return f'kamer (self.__nummer} met {self.lijst_gasten_kamer} gasten.'

    @property
    def nummer(self):
        return self.__nummer

    @nummer.setter
    def nummer(self, nieuw_nummer):
        self.__nummer = nieuw_nummer

    @property
    def lijst_gasten_kamer(self):
        return self.__lijst_gasten_kamer

    @lijst_gasten_kamer.setter
    def lijst_gasten_kamer(self, nieuwelijst_gasten_kamer):
        self.__lijst_gasten_kamer = nieuwelijst_gasten_kamer

    @property
    def kamer_is_vrij(self):
        return len(self.lijst_gasten_kamer)

    @kamer_is_vrij.setter
    def kamer_is_vrij(self, value):
        pass