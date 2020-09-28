milnu = input('Vad är mätarställningen idag?')
milinnan = input('Vad är mätarställningen för ett år sedan?')
literår = input('Hur många liter har gått i år')

milnu = int(milnu)
milinnan = int(milinnan)
körtdettaår = milnu-milinnan
literår = float(literår)
literpermil = literår/körtdettaår

print(f'Så här många mil har du kört i år:{körtdettaår:.0f}')
print(f'Så här många liter har det dragit per mil {literpermil:.2f}')