
class Geboortedatum:
    def __init__(self, dag, maand, jaar):
        self.__jaar = jaar
        self.__maand = maand
        self.__dag = dag

    def __str__(self) -> str:
