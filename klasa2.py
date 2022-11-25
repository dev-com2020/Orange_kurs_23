class Human2:
    '''
    Klasa Human, opisująca człowieka jako obiekt w Pythonie
    autor: Tomasz
    '''

    def __init__(self, imie, wiek=0, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        '''
        Metoda w klasie Human, która zwraca
        :return: print z imieniem
        '''
        print("Cześć,jestem...", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")
