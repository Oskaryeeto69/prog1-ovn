pris = input ('Skriv priset på varan inkl. moms')

pris = float (pris)
exklmoms = pris * 0.8
delsmom = pris - exklmoms
print (f'priset exkl. moms är {exklmoms:6.2f} och moms i kronor är {delsmom:6.2f}')