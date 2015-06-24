__author__ = 'illmoded'
import copy
import random as r


class Zwierz(object):
    def __init__(self, pozycja=0, x=0, y=0, energia=100, czas_zycia=0):
        self.energia = energia
        self.czas_zycia = czas_zycia
        self.pozycja = pozycja
        self.x = x
        self.y = y
        self.genom = []
        self.szybkosc = sum(self.genom)

    def rozmnazaj_sie(self, lista_zwierzat, dojrzalosc=25, libido=50):
        if self.czas_zycia >= dojrzalosc and self.energia >= libido:
                self.energia /= 2
                lista_zwierzat.append(copy.deepcopy(self))
                self.czas_zycia = 0
                self.energia = 100
                self.genom[r.randint(0, 7)] += r.randint(-2, 2)

    def rusz_sie(self, rozmiar=100):
        self.energia -= 3
        kierunek = r.randint(0, 7)

        if kierunek == 0:
            self.x += self.genom[kierunek]

        if kierunek == 1:
            self.x += self.genom[kierunek]
            self.y -= self.genom[kierunek]

        if kierunek == 2:
            self.y -= self.genom[kierunek]

        if kierunek == 3:
            self.x -= self.genom[kierunek]
            self.y -= self.genom[kierunek]

        if kierunek == 4:
            self.x -= self.genom[kierunek]

        if kierunek == 5:
            self.x -= self.genom[kierunek]
            self.y += self.genom[kierunek]

        if kierunek == 6:
            self.y += self.genom[kierunek]

        if kierunek == 7:
            self.x += self.genom[kierunek]
            self.y += self.genom[kierunek]

        # tu moglem zepsuc, mam nadzieje ze nie
        if 0 > self.x:
            self.x += rozmiar
        elif self.x > rozmiar:
            self.x -= rozmiar

        if 0 > self.y:
            self.y += rozmiar
        elif self.y > rozmiar:
            self.y -= rozmiar

    def czy_umrze(self, lista):
        if self.energia <= 0:
            lista.remove(self)

    def czy_ma_co_jesc(self, ziemia):
        rozmiar = len(ziemia)
        for x in xrange(0, rozmiar):
            for y in xrange(0, rozmiar):
                if self.x == x and self.y == y:
                    self.jedz(ziemia[x][y])

    def zycie_jest_nowela(self, lista_zwierzat, ziemia):
        self.czy_ma_co_jesc(ziemia)
        self.czy_umrze(lista_zwierzat)
        self.rozmnazaj_sie(lista_zwierzat)
        self.czas_zycia += 1

    def jedz(self, drzewo):
        if drzewo.energia >= 20:
            self.energia += 20 
            drzewo.energia -= 20


def generuj_zwierzeta(ilosc, rozmiar):
    lista_zwierzat = []
    zwierz = Zwierz()
    while len(lista_zwierzat) < ilosc:  # generuje
        lista_zwierzat.append(copy.deepcopy(zwierz))

    for zwierze in lista_zwierzat:  # modyfikuje

        zwierze.x = r.randint(0, rozmiar)
        zwierze.y = r.randint(0, rozmiar)

        for i in xrange(8):
            zwierze.genom.append(r.randint(0, 10))
    return lista_zwierzat
