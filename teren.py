__author__ = 'illmoded'
import copy
import random as r


class Teren(object):
    def __init__(self, pozycja=0, energia=0):
        self.pozycja = pozycja
        self.energia = energia
        self.szansa_na_wzrost = 0

    # @property
    def rosnie_drzewo(self):
        self.energia += 10


class Pustynia(Teren):
    def __init__(self, pozycja=0):
        Teren.__init__(self, pozycja=0)
        self.pozycja = pozycja
        self.szansa_na_wzrost = 0.01


class Dzunkla(Teren):
    def __init__(self, pozycja=0):
        Teren.__init__(self, pozycja=0)
        self.pozycja = pozycja
        self.szansa_na_wzrost = 5

p = Pustynia()
d = Dzunkla()


def generuj_teren(rozmiar):
    ziemia = [[0 for x in range(rozmiar)] for y in range(rozmiar)]
    for x in range(rozmiar):
        for y in range(rozmiar):
            if 60 > x > 40 and 60 > y > 40:
                ziemia[x][y] = (copy.deepcopy(d))
                ziemia[x][y].pozycja = x, y
            else:
                ziemia[x][y] = (copy.deepcopy(p))
                ziemia[x][y].pozycja = x, y
                # print(ziemia[x][y].pozycja)
    return ziemia


def tworzenie_lasow(ziemia):
    rozmiar = len(ziemia)
    for x in range(rozmiar):
        for y in range(rozmiar):

            los = r.uniform(0, 100)

            if ziemia[x][y].szansa_na_wzrost > los:
                ziemia[x][y].rosnie_drzewo()
