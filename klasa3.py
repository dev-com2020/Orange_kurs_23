from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "Startuje i lecę z prędkością:", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie!")

    def wydajOdglos(self):
        print("piiiiii")


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 1)
        self.__gatunek = gatunek


    def dziobianie(self):
        print("Tu", self.__gatunek, "Ja sobie będę dziobać!")

    def lataj(self):
        print("Tu", self.__gatunek, "Ja nie latam!")

    def wydajOdglos(self):
        print("kokokok")


ptak1 = Orzel('Orzeł', 100)
ptak1.lataj()
ptak1.poluj()

ptak2 = Kura('Kura')
ptak2.dziobianie()
ptak2.lataj()
