import random
number = random.randint(0,100)
guesses = 0
gissa = 0
while gissa != number:
    guesses += 1
    gissa=int(input('Skriv gissning'))

    if gissa < number:
        print (f'För litet')
    elif gissa > number:
        print (f'För stort')
print('Grattis du gissade rätt')