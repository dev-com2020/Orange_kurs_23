lista = [5, 64, 3, 88, 5, 3]
zbior_liczb = set(lista)
zbior_liczb2 = {5, 88, 200, 456}
lista = list(zbior_liczb)
lista.sort()
krotka = tuple(lista)
# print(lista)
# print(zbior_liczb)
# print(krotka)
print(zbior_liczb2.difference(zbior_liczb))
print(zbior_liczb.difference(zbior_liczb2))
print(zbior_liczb.intersection(zbior_liczb2))