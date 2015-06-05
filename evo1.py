__author__ = 'illmoded'

import numpy as np

mapa = np.array[100, 100]


class Drzewo(object):
    def __init__(self):
        self.id = 0
        self.pozycja = (1, 1)
        self.energia = 100


class Zwierz(object):
    def __init__(self):
        self.id = 0
        self.energia = 100
        self.czas_zycia = 0
        self.pozycja = (1, 1)  # moze niekoniecznie jako tuple
        self.genom = (1, 2, 3, 4, 5, 6, 7, 8)

    def rozmnazaj_sie(self):  # cos tu ma byc...
        pass  # pass to odpowiednik NULL dla funkcji btw

    def rusz_sie(self):
        # self.pozycja
        pass
        # cos z pozycja

    def zycie_jest_nowela(self):
        self.rusz_sie()
        self.energia -= 1
        if self.czas_zycia > 100 and self.energia > 200:
            self.rozmnazaj_sie()

    def jedz(self, drzewo):
        # to by tez dzialalo na zjadanie innych stworow, bo maja energie!!!
        self.energia += drzewo.energia
        drzewo.energia = 0
        # cos z energia z drzewa
