class Human:
    '''
    Klasa Human, opisująca człowieka jako obiekt w Pythonie
    autor: Tomasz
    '''
    imie = ""
    wiek = None
    plec = ""

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


