pris = float(input('grundpris')) #Frågar grundpriset på produkten
ålder = int(input('Ålder?')) #Frågar hur gammal man är
if ålder < 12: # om man är yngre än 12 så är prisat hälften än vad grundpriset är
    pris = pris * 0.5
else: # om man är äldre än 12 så är priset en tiondel av grundpriset
    pris = pris * 0.9
print (f'pris{pris:.2f} kr')