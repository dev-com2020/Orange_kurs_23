# fh = open('dane.txt', 'a')
# fh.write("Test nr 11\n")
# fh.write("Test nr 12\n")
# fh.write("Test nr 13\n")
# fh.close()
lista = [1, 2, 3, 4]
#
# with open('dane.txt') as fh:
#     for line in fh:
#         print(line.strip())

# with open('dane.txt', 'a') as fh:
#     fh.write(str(lista))


lista2 = []
with open('dane.txt', 'r') as fh:
    for line in fh:
        lista2.append(line.strip())
# print(lista2)
for i in lista2:
    print(i)

print(lista2[3])