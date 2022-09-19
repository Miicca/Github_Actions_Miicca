import urllib.request
import json


def hae_postinumerot() -> dict:
    '''
    Tekee HTTP-pyynnön GitHubissa sijaitsevaan JSON-tiedostoon ja palauttaa Python-sanakirjan,
    jossa avaimina on postinumeroita, ja arvoina postitoimipaikkojen nimiä.
    '''
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        data = response.read()

    postinumerot = json.loads(data)
    return postinumerot
