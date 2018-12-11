#Voer de nodige import-statements in!!!

def testVoertuig():
    voertuig = Voertuig("Mercedes",1998,100)
    print(voertuig.geef_detail_info())
    print(voertuig)

# testVoertuig()

def test_voertuigen():
    wagen1 = Personenwagen("Audi A4", 2010, 1200, 5)
    wagen2 = Personenwagen("Volkswagen sharon", 2016, 100, 7)
    print(wagen1)
    print(wagen2)

    wagen1.reisbestemming = "Gent"
    print(wagen1.geef_detail_info())
    print("Huidig aantal voertuigen: %d\n" % Voertuig.geef_aantal_voertuigen())

    vrachtwagen1 = Vrachtwagen("DAF", 2009, 12145, 120000)
    print(vrachtwagen1)
    print(vrachtwagen1.geef_detail_info())
    print("\nHuidig aantal voertuigen: %d\n" % Voertuig.geef_aantal_voertuigen())

# test_voertuigen()

def demoPolymorfisme():

    wagen1 = Personenwagen("Audi A4", 2010, 1200, 5)
    wagen2 = Personenwagen("Volkswagen sharon", 2016, 100, 7)
    vrachtwagen1 = Vrachtwagen("DAF", 2009, 12145, 120000)
    voertuigen = [wagen1, wagen2, vrachtwagen1]

    print("Dit zijn de beschikbare voertuigen:")
    for voertuig in voertuigen:
        print(voertuig)

    print("\nGeef de nieuwe reisbestemming voor elk voertuig op:")
    for voertuig in voertuigen:
        voertuig.reisbestemming = input("Voor %s:> " % voertuig)

    print("Detail info:")
    for voertuig in [wagen1, wagen2, vrachtwagen1]:
        print(voertuig.geef_detail_info())


# demoPolymorfisme()
