print("""

    ************************
    *👻 Witaj w programie👻*
    ************************

""")
lista = []
wybor = input("Podaj swoje imię:")
lista.append(wybor)
print("Lista:", lista)
with open('czwartek/dane.txt', 'a') as fh:
    fh.write(str(lista))
input("Aby zakończyć wciśnij ENTER...")
