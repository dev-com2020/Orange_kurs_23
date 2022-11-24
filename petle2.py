licznik = 0
# while True:
#     licznik += 1
#     print("Komunikat...")
#     if licznik == 10:
#         break

# while licznik < 10:
#     print("Komunikat 2...")
#     licznik += 1

# lista = []
# while True:
#     wejscie = input("Wprowadź liczbę:")
#     if wejscie == "s":
#         break
#     lista.append(int(wejscie))
#
# print("Twoja lista:", lista)

lista = [4, 6, 8, 10]
people = ["Tomek", "Kuba", "Maciej", "Agata"]
pos = 0
while pos < len(people):
    person = people[pos]
    liczba = lista[pos]
    print(person, liczba)
    pos += 1
