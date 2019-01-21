import json

from Thuisproject.Model.Locatie import Locatie


class Melding:
    def __init__(self, paralocatie, paracategorie, parasubcategorie, parasoortbinnenkomst, paradoorlooptijd, parameldingsdatum:str):
        self.locatie = paralocatie
        self.categorie = paracategorie
        self.subcategorie = parasubcategorie
        self.soortbinnenkomst = parasoortbinnenkomst
        self.doorlooptijd = paradoorlooptijd
        self.meldingsdatum = parameldingsdatum

    @property
    def locatie(self):
        return self.__locatie
    #geen underscores bij init ethode --> de property setter wordt opgeroepen en parlocatie wordt gebruikt als value
    #nuttig wanneer we controles toevoegen in de setters
    @locatie.setter
    def locatie(self, value):
        if isinstance(value, Locatie):
            self.__locatie = value
        else:
            raise ValueError("Locatie ongeldig")

    @property
    def categorie(self):
        return self.__categorie

    @categorie.setter
    def categorie(self, value):
        if isinstance(value, str) and value != "":
            self.__categorie = value
        else:
            raise ValueError("categorie ongeldig")

    @property
    def subcategorie(self):
        return self.__subcategorie

    @subcategorie.setter
    def subcategorie(self, value):
        if isinstance(value, str) and value != "":
            self.__subcategorie = value
        else:
            raise ValueError("Subcategorie ongeldig")

    @property
    def soortbinnenkomst(self):
        return self.__soortbinnenkomst

    @soortbinnenkomst.setter
    def soortbinnenkomst(self, value):
        if isinstance(value, str) and value != "":
            self.__soortbinnenkomst = value
        else:
            raise ValueError("ongeldige soort binnenkomst")

    @property
    def doorlooptijd(self):
        return self.__doorlooptijd

    @doorlooptijd.setter
    def doorlooptijd(self, value):
        if isinstance(value, int):
            self.__doorlooptijd = value
        else:
            raise ValueError("doorlooptijd ongeldig")

    @property
    def meldingsdatum(self):
        return self.__meldingsdatum

    @meldingsdatum.setter
    def meldingsdatum(self, value):
        if isinstance(value, str) and value != "":
            self.__meldingsdatum = value
        else:
            raise ValueError("meldingsdatum ongeldig")

    @property
    def info(self):
        return "{0} -> {1} ({2}) - {3}".format(self, self.categorie, self.subcategorie, self.soortbinnenkomst)

    def __str__(self):
        return "Melding  op {0} in {1}".format(self.meldingsdatum, self.locatie)
    def __eq__(self, other):
        if self.locatie == other.locatie and self.categorie == other.categorie and self.meldingsdatum == other.meldingsdatum:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.locatie.straat.lower() < other.locatie.straat.lower()

    @staticmethod
    def inlezen_jsonfile():
        lijst_meldingen =[]
        list_json = Melding.__inlezen_json()
        #elke dictionary wordt tap voor stap doorlopen
        for dict_element in list_json:
            try:
                #locatie aanmaken
                lat = dict_element["lat"]
                lon = dict_element["lon"]
                straat = dict_element["Straat"]
                locatie = Locatie(straat, lat, lon)

                #meldingsonbject aanmaken
                categorie = dict_element["categorie"]
                subcategorie = dict_element["subcategorie"]
                binnenkomst = dict_element["Soortbinnenkomst"]
                doorlooptijd = dict_element["Doorlooptijd"]
                #doorlooptijd converten naar int "21 dagen"
                #er wordt gesplitst op basis van de spatie en dan omgezet naar een int
                intdoorlooptijd = int(doorlooptijd.split(' ')[0])

                meldingsdatum = dict_element["dt_aangemeld"]
                melding = Melding(locatie , categorie, subcategorie, binnenkomst, intdoorlooptijd, meldingsdatum)

                #melding wordt toeevoegd aan de lijst met meldingen
                lijst_meldingen.append(melding)


            except Exception as ex:
                print(ex)
        #lijst wordt teruggegeven
        return lijst_meldingen

    @staticmethod
    def __inlezen_json():
        fo = open("data/meldingen_2016.json")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def select_categorie(meldingen, gezochte_categorie):
        lijst_resultaat = []
        for melding in meldingen:
            categorie = melding.categorie
            if categorie.lower() == gezochte_categorie.lower():
                lijst_resultaat.append(melding)
        return  lijst_resultaat

    @staticmethod
    def select_soortbinnenkomst(meldingen, gezochte_binnenkomst):
        lijst_resultaat = []
        for melding in meldingen:
            binnenkomst = melding.soortbinnenkomst
            if binnenkomst.lower() == gezochte_binnenkomst.lower():
                lijst_resultaat.append(melding)
        return lijst_resultaat

    @staticmethod
    def analyse_categorieen(meldingen):
        dict_resultaat ={}
        for melding in meldingen:
            categorie = melding.categorie
            #zit de categorie in de keys van de dictionary
            if categorie in dict_resultaat.keys():
                huidige_aantal = dict_resultaat[categorie]
                huidige_aantal = huidige_aantal + 1
                dict_resultaat[categorie] = huidige_aantal
            else:
                dict_resultaat[categorie] = 1
        return dict_resultaat