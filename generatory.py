# lista = []
# for n in range(10): lista.append(n ** 2)
# print(lista)
#
# squares = list(map(lambda n: n ** 2, range(10)))
# print(squares)
#
# sq = [n ** 2 for n in range(10)]
# print(sq)
import random


def get_squares(n):  # classic function approach
    return [x ** 2 for x in range(n)]


# print(get_squares(10))


def get_squares_gen(n):  # generator approach
    for x in range(n):
        yield x ** 2  # we yield, we don't return


# print(list(get_squares_gen(4)))
# sq = get_squares_gen(4)
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))

def licznik(start=0):
    n = start
    while True:
        yield n
        n += 1


# c = licznik()
# print(next(c))
# print("Wynik losowania:", random.randint(1, 6))
# print(next(c))
# print("Wynik losowania 2:", random.randint(1, 6))
# print(next(c))

def minimum(*n):
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum()
minimum(2)
minimum(2, -3)
minimum(2, -3, 33, 545, -50, -11)


#
# def func(**kwargs):
#     print(kwargs)

#
# func()
# func(a=44)
# func(a=44, b=433, c=44444)

def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)


connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')


def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 5, 7, 9, A='a', B='b')
