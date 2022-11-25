import sqlite3

conn = sqlite3.connect("database.sqlite")

c = conn.cursor()

# c.execute('''
#             CREATE TABLE klienci
#             (data TEXT, klient_id INTEGER, zakupy REAL)
# ''')
# c.execute('''
#             INSERT INTO klienci VALUES
#             ('2022-11-24', 11, 1587.50)
# ''')
# c.execute('''
#             INSERT INTO klienci VALUES
#             ('2022-11-23', 10, 15237.20)
# ''')
lista = []
for row in c.execute('SELECT * FROM klienci ORDER BY zakupy'):
    lista.append(row)

conn.commit()
conn.close()
print(lista)