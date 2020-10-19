print('Dina alternativ är: \n\t Åsele\n\t Umeå')
vars = input('Var är du? ')

if vars == 'Umeå':
    Umeå = input('Är det en vardag?[Ja/Nej]')
    if Umeå == 'Ja':
        print('Dra till skolan')
    else:
        print('Dra raggen i stan')

else:
    Åsele=input('Är det tredje helgen i Juli? [Ja/Nej]')
    if Åsele == 'Ja':
        print('Far på Åsele marknad å gör något roligt! ')
    else:
        print('Va me boisen å ströga')