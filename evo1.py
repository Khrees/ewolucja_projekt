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
        self.pozycja = (1, 1)
        self.genom = (1, 2, 3, 4, 5, 6, 7, 8)

    def rusz_sie(self):
        pass
        # cos z pozycja

    def jedz(self, drzewo):
        # cos z energia z drzewa
        pass
