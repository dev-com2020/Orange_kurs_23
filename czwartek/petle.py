lista = [4, 6, 8]
people = ["Tomek", "Kuba", "Maciej", "Agata"]
instr = ['gitara', 'bass', 'bębny', 'trąbka']

# for pos in range(len(lista)):
#     print("Element listy o indeksie", pos, "to:", lista[pos])
# print()
# for pos, liczba in enumerate(lista):
#     print("Element listy o indeksie", pos, "to:", liczba)
# print()
# for pos, liczba in enumerate(people):
#     cyfra = lista[pos]
#     print("Element listy o indeksie", pos, "to:", liczba, "i do tego cyfra", cyfra)

# for person, liczba, ins in zip(people, lista, instr):
#     print(person, liczba, ins)
# print()
# for data in zip(people, lista, instr):
#     person, liczba, ins = data
#     print(person, liczba, ins)

napis = "Tomek"
# for i in napis:
#     print(i)

# for i in range(-10,-2, 2):
#     print(i)
#
# for i in range(len(napis)-1, -1, -1):
#     print(napis[i])

slownik = {"imie": "Marek", "nazwisko": "Kowalski", "plec": "mezczyzna"}
#
# for k in slownik:
#     print(k)
#
# for k in slownik.values():
#     print(k)
#
# for k, v in slownik.items():
#     print(k, "=>", v)

for i in range(-1, -len(napis) - 1, -1):
    j = i + 1
    if j == 0:
        print(napis[i:])
    else:
        print(napis[i:j])
