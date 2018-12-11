def demo1():
    lijst_getallen = []
    print("geef een lijst van 10 getallen op")

#een static methode is een methode die je kan oproepen zonder dat

    try:
        getal = int(input("Geef een getal in: "))
        lijst_getallen.append(getal)
    except ValueError as ex:    #as ex hoeft er niet nij
        print("Geen geldige waarde. Probeer opnieuw")
        print("Detail fotmelding: %s" %str(ex))

    print("De opgegeven getallen zijn: %s" % str())

    #meerdere except blokken zijn mogelijk
    def meerdere_except_blokken():
        fo = file.txt
        try:
            print(8/ int(input("geef een getal in:")))
        except ZeroDivisionError:
            print("Je kunt niet delen door nul")
        except ValueError:
            print("Je gaf geen getal op.")
        except FileExistsError:
            print("")
        except FileNotFoundError:
            print("Ongeldige bestandsnaam")

        except:
            print("Iets nverxachts ging fout.")
        finally:
            print("ethode ten einde.")      #finally is noodzakelijk ij het gebruik van een database
            fo.close()                                # dient om een database te sluiten.


#examenvraag! Je krijgt een blok, de grbruiker krijgt een melding te zien, welke?