
class Auto:
    #information hidng = ingen private zetten.
    #stap 1: consturctor aanmaken
    def _init_(self, paramerk, parakmstand):
        #propertie private zetten --> 2 underscores ervoor = private
        self.__kmstand = parakmstand
        self.__merk = paramerk

    #propertiemethode
        #hier vraag je een property op
        @property
        def kmstand (self):
            return self.__kmstand - 2000  #wat geef je terug

        #hier geef je een nieuwe waarde aan een propertie
        @kmstand .setter
        def kmstand (self, value):
            self.__kmstand = value

        #de tostring metode
        # wordt ebruikt wanneer een auto wordt afgeprint
        def _str_(self):
            return self.__merk + "(" + str(self.kmafstand) + "km )"

    #methode in de klasse
   # def wijzig_kmstand(self, par_nieuw_kmstand):
    #    return self()