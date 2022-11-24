# import locale
#
# locale.setlocale(locale.LC_NUMERIC, 'pl_PL')

# name = "Tomek"
# if name == "Tomek":
#     print(f"Twoje imię to {name}")

# if name := "Tomek":
#     print(f"Twoje imię to {name}")

# przekaski = ['hotdog', 'pizza', 'hamburger', 'frytki']
# prompt = "Wybierz swoją przekąskę:"
# print(przekaski)
# while True:
#     choice = input(prompt)
#     if choice in przekaski:
#         break
#     print(f"Przepraszamy, ale '{choice}' jest niepoprawny")
# print(f"Twój wybór '{choice}'")

# przekaski = ['hotdog', 'pizza', 'hamburger', 'frytki']
# prompt = "Wybierz swoją przekąskę:"
# print(przekaski)
# while (choice := input(prompt)) not in przekaski:
#     print(f"Przepraszamy, ale '{choice}' jest niepoprawny")
# print(f"Twój wybór '{choice}'")

user = "Tomek"
wiek = 39
wersja = 3.90001
liczba = 134632344532
# print('Witaj %s masz teraz %d lat' % (user, wiek))
# print('Witaj %(user)s masz teraz %(wiek)d lat' % {'user': user, "wiek": wiek})
# print('Witaj {} masz teraz {} lat'.format(user, wiek))
# print('Witaj {user} masz teraz {wiek} lat'.format(user=user, wiek=wiek))
# print(f'Witaj {user} masz teraz {wiek} lat')
print("Używamy wersji Python %i" % 3)
print("Używamy wersji Python %f" % 3.9)
print("Używamy wersji Python %.1f" % 3.9)
print("Używamy wersji Python %.f" % 3.9)
print("Używamy wersji Python {}".format(wersja))
print(f"Używamy wersji Python {wersja:.1f}")
print(f"{user:>10}")
print(f"{user:>20}")
print(f"{user:>30}")
print('Nasza duża liczba: {:,}'.format(liczba).replace(',', '.'))
print('Nasza duża liczba: {:,}'.format(liczba).replace(',', ' '))
