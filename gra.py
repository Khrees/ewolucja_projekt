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

listazwieraat=[]
zwierz=zwierza.Zwierz()

#tu jeszcze while ogolny
while len(listazwieraat)<100: #generuje
    listazwieraat.append(zwierz)

for zwierze in listazwieraat: #modyfikuje
    zwierze.pozycja= [r.randint(0,100),r.randint(0,100)]

    N=r.randint(0,10)
    E=r.randint(0,10)
    W=r.randint(0,10)
    S=r.randint(0,10)
    NE=r.randint(0,10)
    NW=r.randint(0,10)
    SE=r.randint(0,10)
    SW=r.randint(0,10)

    zwierze.genom=[N,E,W,S,NE,NW,SE,SW] #to powinno byc jako slownik, nie jako lista
    zwierze.id = zwierze #adres w pamieci, powinien byc unikatowy


# tak wyglada wzrost drzew
los=0
for x in range(rozmiar):
    for y in range(rozmiar):

        los=r.randint(0,100)

        if ziemia[x][y].szansa_na_wzrost > los:
            ziemia[x][y].rosnie_drzewo()

        # print(los, ziemia[x][y].szansa_na_wzrost,ziemia[x][y].szansa_na_wzrost>los,ziemia[x][y].energia)


