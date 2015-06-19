__author__ = 'illmoded'

import zwierza
import teren
import copy
import random as r

p = teren.Pustynia()
d = teren.Dzunkla()

rozmiar = 100
ziemia = [[0 for x in range(rozmiar)] for y in range(rozmiar)]

# nie wiem po co takie cos, ale jest...
for x in range(rozmiar):
    for y in range(rozmiar):
        if 60 > x > 40 and 60 > y > 40:
            ziemia[x][y] = (copy.deepcopy(d))
            ziemia[x][y].pozycja = x, y
        else:
            ziemia[x][y] = (copy.deepcopy(p))
            ziemia[x][y].pozycja = x, y
            # print(ziemia[x][y].pozycja)

listazwieraat = []
zwierz = zwierza.Zwierz()


while len(listazwieraat) < 1:  # generuje
    listazwieraat.append(copy.deepcopy(zwierz))

for zwierze in listazwieraat:  # modyfikuje

    zwierze.x = r.randint(0, rozmiar)
    zwierze.y = r.randint(0, rozmiar)

    zwierze.idz = r.randint(0,1000)

    for i in xrange(8):
        zwierze.genom.append(r.randint(0, 10))

# albo stworzyc konstruktor i gnerowac w taki sposob, w sumie bardziej pythonowe by bylo

# tu 
dzien = 0
while dzien < 1000:
    # tak wyglada wzrost drzew
    los = 0
    for x in range(rozmiar):
        for y in range(rozmiar):

            los = r.randint(0, 100)

            if ziemia[x][y].szansa_na_wzrost > los:
                ziemia[x][y].rosnie_drzewo()

                # print(los, ziemia[x][y].szansa_na_wzrost,ziemia[x][y].szansa_na_wzrost>los,ziemia[x][y].energia)

    # ruch zwierzat
    for krolik in listazwieraat:
        krolik.energia -= 1
        kierunek = r.randint(0,7)
        
        # ruszanie sie
        if kierunek == 0:
        	krolik.x += krolik.genom[kierunek]

        if kierunek == 1:
        	krolik.x += krolik.genom[kierunek]
        	krolik.y -= krolik.genom[kierunek]

        if kierunek == 2:
        	krolik.y -= krolik.genom[kierunek]

        if kierunek == 3:
        	krolik.x -= krolik.genom[kierunek]
        	krolik.y -= krolik.genom[kierunek]

        if kierunek == 4:
        	krolik.x -= krolik.genom[kierunek]

        if kierunek == 5:
        	krolik.x -= krolik.genom[kierunek]
        	krolik.y += krolik.genom[kierunek]

        if kierunek == 6:
        	krolik.y += krolik.genom[kierunek]

        if kierunek == 7:
        	krolik.x += krolik.genom[kierunek]
        	krolik.y += krolik.genom[kierunek]

        #sprawdzanie, czy nie wyszedl i ewentualne przemieszczenie
        if 0 > krolik.x:
        	krolik.x += rozmiar
        elif krolik.x > rozmiar:
        	krolik.x -= rozmiar

        if 0 > krolik.y:
        	krolik.y += rozmiar
        elif krolik.y > rozmiar:
        	krolik.y -= rozmiar


        # jedzenie!!!
    for krolik in listazwieraat:
        for x in xrange(0, rozmiar):
            for y in xrange(0, rozmiar):
                if krolik.x == x and krolik.y == y:
                    krolik.jedz(ziemia[x][y])

    for krolik in listazwieraat:
        if krolik.energia <= 0:

            # del krolik # http://stackoverflow.com/questions/2150108/efficient-way-to-shift-a-list-in-python
            # nowykrolik = zwierz
            # listazwieraat.append(nowykrolik)
            # # i atrybuty...

            # moze zamiast del po prostu resetowac krolika
            noweidz = r.randint(0,1000)

            krolik.idz = noweidz
            krolik.energia = 100
            krolik.czas_zycia = 0
            krolik.x = r.randint(0, rozmiar)
            krolik.y = r.randint(0, rozmiar)
            for g in xrange(len(krolik.genom)):
                krolik.genom[g] = r.randint(-10, 10)

        # rozmnazanie
    if len(listazwieraat) <= 500:
        for krolik in listazwieraat:
            dojrzalosc = 20
            libido = 50
            if krolik.czas_zycia >= dojrzalosc and krolik.energia >= libido:
                krolik.energia /= 2
                nowykrolik = copy.deepcopy(krolik)
                listazwieraat.append(nowykrolik)  # nie ma znaczenia czy nowy sie zmieni czy stary, nie?
                krolik.czas_zycia = 0
                krolik.energia = 100
                krolik.genom[r.randint(0, 7)] += r.randint(-2, 2)

    for krolik in listazwieraat:
        krolik.czas_zycia += 1

    if dzien % 10 == 0:
        for k in listazwieraat:
            print(dzien, len(listazwieraat))
            print(k.idz, k.x, k.y, k.energia,k.genom)
            print(k.czas_zycia)

    dzien += 1
    

