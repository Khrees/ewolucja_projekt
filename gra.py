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

# tu jeszcze while ogolny
while len(listazwieraat) < 100:  # generuje
    listazwieraat.append(copy.deepcopy(zwierz))

for zwierze in listazwieraat:  # modyfikuje

    zwierze.x = r.randint(0, rozmiar)
    zwierze.y = r.randint(0, rozmiar)

    zwierze.id = zwierze  # adres w pamieci, powinien byc unikatowy!!!!!!!!!!!!!

    for i in xrange(8):
        zwierze.genom.append(r.randint(-10, 10))

# albo stworzyc konstruktor i gnerowac w taki sposob, w sumie bardziej pythonowe by bylo

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
    # to jest tak glupie ze nie moge. jak to zrobic inaczej?

    wrrr = r.randint(0, 7)
    if wrrr == 0:
        if 0 > krolik.x - krolik.genom[wrrr] > rozmiar:
            krolik.x -= krolik.genom[wrrr] % rozmiar
        else:
            krolik.x -= krolik.genom[wrrr]
        if 0 > krolik.y + krolik.genom[wrrr] > rozmiar:
            krolik.y += krolik.genom[wrrr] % rozmiar
        else:
            krolik.y += krolik.genom[wrrr]

    if wrrr == 1:
        if 0 > krolik.x - 0 > rozmiar:
            krolik.x -= 0 % rozmiar
        else:
            krolik.x -= 0
        if 0 > krolik.y + krolik.genom[wrrr] > rozmiar:
            krolik.y += krolik.genom[wrrr] % rozmiar
        else:
            krolik.y += krolik.genom[wrrr]

    if wrrr == 2:
        if 0 > krolik.x + krolik.genom[wrrr] > rozmiar:
            krolik.x += krolik.genom[wrrr] % rozmiar
        else:
            krolik.x += krolik.genom[wrrr]
        if 0 > krolik.y + krolik.genom[wrrr] > rozmiar:
            krolik.y += krolik.genom[wrrr] % rozmiar
        else:
            krolik.y += krolik.genom[wrrr]

    if wrrr == 3:
        if 0 > krolik.x + krolik.genom[wrrr] > rozmiar:
            krolik.x += krolik.genom[wrrr] % rozmiar
        else:
            krolik.x += krolik.genom[wrrr]
        if 0 > krolik.y + 0 > rozmiar:
            krolik.y += 0 % rozmiar
        else:
            krolik.y += 0

    if wrrr == 4:
        if 0 > krolik.x + krolik.genom[wrrr] > rozmiar:
            krolik.x += krolik.genom[wrrr] % rozmiar
        else:
            krolik.x += krolik.genom[wrrr]
        if 0 > krolik.y - krolik.genom[wrrr] > rozmiar:
            krolik.y -= krolik.genom[wrrr] % rozmiar
        else:
            krolik.y -= krolik.genom[wrrr]

    if wrrr == 5:
        if 0 > krolik.x - 0 > rozmiar:
            krolik.x -= 0 % rozmiar
        else:
            krolik.x -= 0
        if 0 > krolik.y - krolik.genom[wrrr] > rozmiar:
            krolik.y -= krolik.genom[wrrr] % rozmiar
        else:
            krolik.y -= krolik.genom[wrrr]

    if wrrr == 6:
        if 0 > krolik.x - krolik.genom[wrrr] > rozmiar:
            krolik.x -= krolik.genom[wrrr] % rozmiar
        else:
            krolik.x -= krolik.genom[wrrr]
        if 0 > krolik.y - krolik.genom[wrrr] > rozmiar:
            krolik.y -= krolik.genom[wrrr] % rozmiar
        else:
            krolik.y -= krolik.genom[wrrr]

    if wrrr == 7:
        if 0 > krolik.x - krolik.genom[wrrr] > rozmiar:
            krolik.x -= krolik.genom[wrrr] % rozmiar
        else:
            krolik.x -= krolik.genom[wrrr]
        if 0 > krolik.y + 0 > rozmiar:
            krolik.y += 0 % rozmiar
        else:
            krolik.y += 0

#teraz smierc i nowe zycie

for krolik in listazwieraat:
    if krolik.energia <= 0:

        # del krolik
        # nowykrolik = zwierz
        # listazwieraat.append(nowykrolik)
        # # i atrybuty...

        # moze zamiast del po prostu resetowac krolika
        noweidz = r.random()

        krolik.idz = noweidz
        krolik.energia = 100
        krolik.czas_zycia = 0
        krolik.x = r.randint(0,rozmiar)
        krolik.y = r.randint(0,rozmiar)
        for g in xrange(len(krolik.genom)):
            krolik.genom[g]=r.randint(-10,10)
