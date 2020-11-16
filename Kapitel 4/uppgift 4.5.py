meter = int(input('Släpp bollen från: '))

centimeter = 100 * meter
studs = 0
if meter < 0:
        break
while centimeter > 1:
    centimeter = centimeter * 0.7
    studs = studs + 1
    print (f'{centimeter:.2f}cm')
    
print(f'Bollen studsar {studs} gånger')