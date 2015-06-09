__author__ = 'illmoded'

import zwierza
import teren
import copy
import random as r

p= teren.Pustynia()
d= teren.Dzunkla()

rozmiar=100
ziemia = [[0 for x in range(rozmiar)] for y in range(rozmiar)]

#nie wiem po co takie cos, ale jest...
for x in range(rozmiar):
    for y in range(rozmiar):
        if 60 > x >40 and 60 > y > 40:
            ziemia[x][y]=(copy.deepcopy(d))
            ziemia[x][y].pozycja=x,y
        else:
            ziemia[x][y]=(copy.deepcopy(p))
            ziemia[x][y].pozycja=x,y
        # print(ziemia[x][y].pozycja)

listazwieraat = []
zwierz = zwierza.Zwierz()

#tu jeszcze while ogolny
while len(listazwieraat)<100: #generuje
    listazwieraat.append(zwierz)

for zwierze in listazwieraat: #modyfikuje

    zwierze.pozycja.x=r.randint(0,rozmiar)
    zwierze.pozycja.y=r.randint(0,rozmiar)

    #to powinno byc jako slownik, nie jako lista
    zwierze.id = zwierze #adres w pamieci, powinien byc unikatowy
    for i in xrange[8]:
        zwierze.genom.dl[i] = r.randint(-10, 10)


# tak wyglada wzrost drzew
los=0
for x in range(rozmiar):
    for y in range(rozmiar):

        los = r.randint(0,100)

        if ziemia[x][y].szansa_na_wzrost > los:
            ziemia[x][y].rosnie_drzewo()

        # print(los, ziemia[x][y].szansa_na_wzrost,ziemia[x][y].szansa_na_wzrost>los,ziemia[x][y].energia)

# ruch zwierzat
for zwierz in listazwieraat:
    wybor = r.choice(zwierz.genom.kierunek)
    if wybor == 'N':
        zwierz.pozycja.x += 0
        zwierz.pozycja.y += zwierz.genom.dl[0]
    elif wybor == 'E':
        zwierz.pozycja.x += zwierz.genom.dl[1]
        zwierz.pozycja.y += 0
    elif wybor == 'W':
        zwierz.pozycja.x += zwierz.genom.dl[2]
        zwierz.pozycja.y += 0
    elif wybor == 'S':
        zwierz.pozycja.x += 0
        zwierz.pozycja.y += zwierz.genom.dl[3]
    elif wybor == 'NE':
        zwierz.pozycja.x += zwierz.genom.dl[4]
        zwierz.pozycja.y += zwierz.genom.dl[4]
    elif wybor == 'NW':
        zwierz.pozycja.x += zwierz.genom.dl[5]
        zwierz.pozycja.y += zwierz.genom.dl[5]
    elif wybor == 'SE':
        zwierz.pozycja.x += zwierz.genom.dl[6]
        zwierz.pozycja.y += zwierz.genom.dl[6]
    elif wybor == 'SW':
        zwierz.pozycja.x += zwierz.genom.dl[7]
        zwierz.pozycja.y += zwierz.genom.dl[7]

