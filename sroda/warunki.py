# haslo = input("Podaj hasło:")
#
# if haslo == '12345':
#     print("Hasło ok!")
# elif haslo == 'tomek34':
#     print("Hasło prawie dobre...")
# else:
#     print("Hasło nie jest prawidłowe!")
#
# print("Reszta programu.....")
# print("Reszta programu.....")
# print("Reszta programu.....")
# print("Reszta programu.....")
# print("Reszta programu.....")
#
# temp = 24
#
# if temp < 0:
#     print("mróz")
# elif temp == 0:
#     print("przymrozek")
# elif 10 < temp < 20:
#     print("dodatnia")
# elif temp >= 20:
#     print("upał")
#
# if temp < 10 or temp > 15:
#     print('wiosna')
#
#
# lista = []
# lang = input("Wpisz znany Ci język programowania:")
#
# match lang:
#     case "Python":
#         lista.append(lang)
#     case "PHP":
#         lista.append(lang)
#     case "Java":
#         lista.append(lang)
#     case _:
#         print("nie znam takiego języka")
#
# print(lista)


#
# if __name__ == '__main__':
#     print("czekam...")

temp = -24
alert = False

if temp < 0:
    print("mróz")
    if temp < -10:
        alert = True
        print("Alert pogodowy!")
        if temp < -100:
            pass
elif temp == 0:
    print("przymrozek")
elif 10 < temp < 20:
    print("dodatnia")
elif temp >= 20:
    print("upał")


