x = [i for i in range(15) if i % 2 == 0]
print(x)

slownik = {1: "Tomek", 2: "Andrzej", 3: "Kuba"}
print({value: key for key, value in slownik.items()})
