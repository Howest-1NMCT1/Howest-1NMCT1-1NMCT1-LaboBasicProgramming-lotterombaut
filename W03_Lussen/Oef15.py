#oef13

def check_email_format(email):
    # 1 staat er een @ in?

    position_at = email.find("@")
    if(position_at < 3):
        return False

    #2 eindigt op "stundent.howest.be
    if( email[position_at +1 :] != "student.howest.be"):
        return False

    #3 een punt met naam.voornaam
    position_punt = email[0:position_at].find(".")
    if(position_punt == -1): return False
    voornaam= email[0:position_punt]
    naam = email[position_punt: position_at]
    if(voornaam == ""): return False
    if(naam == ""): return False

    #4
    return True

if check_email_format("lotte.rombaut@student.howest.be"):
    print("dit is een geldig emailadres")
else:
    print("ongeldig")