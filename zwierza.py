__author__ = 'illmoded'


class Zwierz(object):
    def __init__(self,pozycja=0,x=0,y=0,idz=0, energia=100, czas_zycia=0):
        self.idz = idz
        self.energia = energia
        self.czas_zycia = czas_zycia
        self.pozycja =pozycja
        self.pozycja.x = x
        self.pozycja.y = y
        # self.genom
        self.genom.kierunek =['N','E','W','S','NE','NW','SE','SW']
        self.genom.dl = []

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
            self.energia /= 2
            self.rozmnazaj_sie()

    def jedz(self, drzewo):
        # to by tez dzialalo na zjadanie innych stworow, bo maja energie!!! (prawdopodobnie)
        self.energia += drzewo.energia
        drzewo.energia = 0
        # cos z energia z drzewa
