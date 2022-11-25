from klasa1 import Human as h
from klasa2 import Human2 as h2

czlowiek1 = h()
czlowiek1.imie = "Tomek"
czlowiek1.plec = 'm'
czlowiek1.wiek = 39
czlowiek1.powitanie()
czlowiek1.ruszaj()

czlowiek2 = h()
czlowiek2.imie = "Ewa"
czlowiek2.plec = 'k'
czlowiek2.wiek = 29
czlowiek2.powitanie()
czlowiek2.ruszaj()

czlowiek3 = h2("Jacek", 25, 'm')
czlowiek3.powitanie()
czlowiek3.ruszaj()

czlowiek4 = h2("Kasia")
czlowiek4.powitanie()
czlowiek4.ruszaj()
czlowiek4.wiek = 20
print(czlowiek4.wiek)
