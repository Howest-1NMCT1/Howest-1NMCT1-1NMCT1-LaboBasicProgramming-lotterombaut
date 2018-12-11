from W10_Overerving.Models.Auto import Auto
from W10_Overerving.Models.Docent import Docent
from W10_Overerving.Models.Persoon import Persoon
from W10_Overerving.Models.Student import Student


def start():
    try:
        # geen geldig geboortejaar
        persoon = Persoon("Walcarius", "Stijn", "geen idee")
        print(persoon)
    except ValueError as ex:
        print("Foutmelding: " + str(ex))


# start()


def sorteren_lijst():
    persoon1 = Persoon("Jansens", "Nick", 1992)
    persoon2 = Persoon("Claes", "Fien", 1994)
    persoon3 = Persoon("Claes", "Amber", 1992)

    personen = [persoon1, persoon2, persoon3]
    personen.sort()
    print("Gesorteerde lijst: ")
    for persoon in personen:
        print("- %s" % persoon)


# sorteren_lijst()

def test_auto():
    persoon1 = Persoon("Jansens", "Nick", 1992)
    auto1 = Auto("1-LVM-478", persoon1)
    print(auto1)

    # auto1.eigenaar = "Stijn Walcarius"            #Fout!
    # print(auto1)


# test_auto()


def test_student1():
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "NMCT", 1992)

    studenten = [student1, student2, student3]
    for student in studenten:
        print("- %s" % student)


# test_student1()

def test_student2():
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    student2 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    if student1 == student2:
        print("Gelijk!")
    else:
        print("Verschillend!")


# test_student2()


def testDocent():
    opleidingen = ["NMCT", "IPO", "Devine"]
    docent1 = Docent("Walcarius", "Stijn", 1234, opleidingen, 1977)
    docent2 = Docent("Laprudence", "Christophe", 1854, opleidingen, 1980)
    print(docent1)
    print(docent2)

    if (docent1 == docent2):
        print("Gelijk")
    else:
        print("verschillend")


# testDocent()


def werkt_dit():
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    student2 = Student("Baert", "Fien", 199510412, "NMCT", 1994)
    student3 = Student("Colpaert", "Barbara", 19931252, "IPO", 1993)
    docent1 = Docent("Walcarius", "Stijn", 1234, ["NMCT", "IPO", "Devine"], 1977)
    docent2 = Docent("Laprudence", "Christophe", 1854, ["NMCT", "IPO", "Devine"], 1980)

    # werkt dit? Verklaar!
    print(Docent.vereniging)
    print("Aantal: %d" % Persoon.geef_aantal_personen())

    # verklaar het resultaat van onderstaande regels
    for p in [docent1, student2, student3, docent1, student1]:
        print("%s heeft als leeftijd %d" % (p, p.leeftijd))


# werkt_dit()


def demoSom(x, y):
    return x + y


def demo_polymorphism():
    print(demoSom(10, 20))
    print(demoSom("1NMCT", "2NMCT"))
    print([1, 2, 3], [9, 8, 7])


# demo_polymorphism()


def testAuto():
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    docent1 = Docent("Walcarius", "Stijn", 1234, ["NMCT", "IPO", "Devine"], 1977)
    docent2 = Docent("Di Marco", "Mileto", 1854, ["NMCT", "DAE"], 1974)

    auto1 = Auto("How-001", docent1)
    auto2 = Auto("W8ZAAL", student1)
    auto3 = Auto("MoaHow", docent2)

    # verklaar output!
    for auto in [auto1, auto2, auto3]:
        print(auto)

# testAuto()
