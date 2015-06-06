__author__ = 'illmoded'


class Teren(object):
    def __init__(self, pozycja=0):
        self.pozycja = pozycja


class Pustynia(Teren):
    def __init__(self, pozycja=0):
        Teren.__init__(self, pozycja=0)
        self.pozycja = pozycja
        self.sznsa_na_wzrost = 5


class Dzunkla(Teren):
    def __init__(self, pozycja=0):
        Teren.__init__(self, pozycja=0)
        self.pozycja = pozycja
        self.szansa_na_wzrost = 20

