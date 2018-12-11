import requests

def download():
    params = {'format': 'json', 'language': 'nl'}
    response = requests.get("https://datatank.stad.gent/4/cultuursportvrijetijd/sportclubs.json", params)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        return None


def inlezen_personen():
    resultaat = []
    list_json = download()
    for dict_element in list_json:  # fictief voorbeeldje
        naam = dict_element["Naam"]
        voornaam = dict_element["Voornaam"]
        leeftijd = int(dict_element["Leeftijd"])
        print("%s %s (%d)" %(voornaam, naam, leeftijd))
    return resultaat

def geef_namen_outdoor_location(json_data):
    set_namen = set()
    for sportcomplex in json_data:
        set_namen.add(sportcomplex["Benming"])
    return set_namen

json_data = download()
if json_data != None:
    for lijn in json_data:
        print(lijn)