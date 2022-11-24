# from pakiet.fun2 import przywitaj, policz, policz2
from pakiet.fun2 import *
from pakiet.fun3 import przywitaj as p

f1 = przywitaj
f2 = policz()
print(f2)
print(policz2(2, 2))
p()

lista = [policz2(2, 2), policz2(3, 9), policz2(3, 22)]
print(lista)

for i in range(2):
    f1()
