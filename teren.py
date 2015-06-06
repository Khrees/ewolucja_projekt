__author__ = 'illmoded'


class Teren(object):
    def __init__(self, pozycja):
        self.pozycja = pozycja


class Pustynia(Teren):
    def __init__(self, pozycja):
        super(Pustynia, self).__init__(pozycja) #co to jest??????
        self.pozycja = pozycja
        self.sznsa_na_wzrost = 1
    pass


class Dzunkla(Teren):
    def __init__(self, pozycja):
        super(Dzunkla, self).__init__(pozycja)
        self.pozycja = pozycja
        self.szansa_na_wzrost = 20
    pass
