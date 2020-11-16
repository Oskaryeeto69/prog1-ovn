pris = float(input('Vad är priset för årskortet?')) # frågar vad priset på årskortet är
pris0 = float(input('Vad är priset för en biljett=')) # frågar vad priset för en biljett är
besök = float(input('Hur ofta per år går du på gymmet?')) # frågar hur ofta du är på gymmet

dagskortperår = pris0 * besök # räknar ut hur mycket ett dagskort per gång du går på gymmet skulle kosta

if dagskortperår >= pris: # Säger att om dagskortperår är större än pris
    print ('Det blir billigare att köpa dagskort varenda gång') # så är det billigare att köpa dagskort
else: # annars
    print ('Det blir billigare att köpa årskort') # så är det billigare att köpa årskort