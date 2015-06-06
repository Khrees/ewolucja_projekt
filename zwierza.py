__author__ = 'illmoded'


class Zwierz(object):
    def __init__(self, id, pozycja, genom, energia=0, czas_zycia=0):
        self.id = id
        self.energia = energia
        self.czas_zycia = czas_zycia
        self.pozycja = pozycja  # moze niekoniecznie jako tuple
        self.genom = genom

    def rozmnazaj_sie(self):  # cos tu ma byc...
        pass  # pass to odpowiednik NULL dla funkcji btw

    def rusz_sie(self):
        # cos z pozycja
        # self.pozycja
        pass

    def zycie_jest_nowela(self):
        self.rusz_sie()
        self.energia -= 1
        if self.czas_zycia > 100 and self.energia > 200:
            self.czas_zycia = 0
            self.rozmnazaj_sie()

    def jedz(self, drzewo):
        # to by tez dzialalo na zjadanie innych stworow, bo maja energie!!!
        self.energia += drzewo.energia
        drzewo.energia = 0
        # cos z energia z drzewa
