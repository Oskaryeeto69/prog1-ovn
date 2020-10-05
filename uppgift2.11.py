milnu = input('Vad är mätarställningen idag?') #ställer en fråga
milinnan = input('Vad är mätarställningen för ett år sedan?') #ställer en fråga
literår = input('Hur många liter har gått i år') #ställer en fråga

milnu = int(milnu) #säger att milen som är på mätaren nu är en int
milinnan = int(milinnan) #säger att milen som var på mätaren ett år sen är en int
körtdettaår = milnu-milinnan #räknar hur många mil bilen har kört detta år
literår = float(literår) #säger att liter
literpermil = literår/körtdettaår

print(f'Så här många mil har du kört i år:{körtdettaår:.0f}')
print(f'Så här många liter har det dragit per mil {literpermil:.2f}')