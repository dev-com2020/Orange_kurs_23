zmienna = lambda a, b: a + b
print(zmienna(5, 4))


def funkcja(f, liczba):
    return f(liczba)


def dodaj(x):
    return x + 1


print(funkcja(dodaj, 7))
print(funkcja(lambda x: x + 1, 7))

lista = [2, 4, 6, 8]

print(f"Zastosowanie filter {list(filter(lambda _: _ > 3, lista))}")

wiek = lambda x: "dziecko" if x < 10 else ("Nastolatek" if x < 18 else "Dorosły")
print(wiek(4))
print(wiek(15))
print(wiek(33))

print(sorted("tomek"))
print(sorted("tomek", reverse=True))

print(sorted("Alicja Kot ma psa ale nie ma kota".split(), key=str.lower))
