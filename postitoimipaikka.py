import http_pyynto


def etsi_toimipaikka(postinumero: str) -> str:
    '''
    Etsii ja palauttaa annettua postinumeroa vastaavan toimipaikan nimen. Jos nimeä ei löydy,
    palauttaa merkkijonon 'Tuntematon'.
    '''
    postinumerot = http_pyynto.hae_postinumerot()

    if postinumero in postinumerot:
        return postinumerot[postinumero]
    else:
        return 'Tuntematon'


def main():
    '''
    Pääohjelma, joka kysyy käyttäjältä postinumeroa, ja etsii verkosta 
    löytyvästä JSON-aineistosta sitä vastaavan toimipaikan nimen.
    '''
    numero = input('Kirjoita postinumero: ')

    print(etsi_toimipaikka(numero))


if __name__ == '__main__':
    main()