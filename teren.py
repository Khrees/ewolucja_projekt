__author__ = 'illmoded'


class Teren(object):
    def __init__(self, pozycja =0, energia =0):
        self.pozycja = pozycja
        self.energia = energia


    # @property
    def rosnie_drzewo(self):
        self.energia += 10
        return 1


class Pustynia(Teren):
    def __init__(self, pozycja=0):
        Teren.__init__(self, pozycja=0)
        self.pozycja = pozycja
        self.szansa_na_wzrost = 5


class Dzunkla(Teren):
    def __init__(self, pozycja=0):
        Teren.__init__(self, pozycja=0)
        self.pozycja = pozycja
        self.szansa_na_wzrost = 20
