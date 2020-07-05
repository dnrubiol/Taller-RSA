## Taller RSA ##
## Desarrollador: Diego Nicolas Rubio Lopez ##

import random   ##modulo para numero aleatorio
from sympy import *  ##modulo para isprime()

##Funcion para calcular MCD
def mcd(x,y):
    mcd = 1
    if x % y == 0:
        return y
    for k in range (int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break
    return mcd

##Generar numero primo aleatorio entre 100 y 1000 (4 digitos)
n1 = 100
n2 = 1000
primes = [i for i in range(n1, n2) if isprime(i)]
p = random.choice(primes)
q = random.choice(primes)
print("Primo p: " + str(p))
print("Primo q: " + str(q))

##Asegurar que los primos sean diferentes (sirve tambien si son iguales)
while q == p:
    q = random.choice(primes)
n = p*q
fi = (p-1)*(q-1)

##Calcular número natural e tal que MCD(e,fi) == 1
for l in range(3, fi-2):
    if mcd(l,fi) == 1:
        e = l
        break

##Calcular d mediante el algoritmo extendido de Euclides
for y in range(1, fi):
    d = (((y * fi) + 1) / e)
    if ('.0' in str(d)):
        d = (int(d))
        break

##Imprimir claves de encriptacion
print("Clave publica:")
print("e=" + str(e) + " n=" + str(n))
print("Clave privada:")
print("d=" + str(d) + " n=" + str(n))

##Opcion de cifrado
print("Introduzca numero para proceso de cifrado")
m = input()
c = (int(m)**e) % n
print("Mensaje cifrado: " + str(c))

##Opcion de decifrado
print("Introduzca numero para proceso de decifrado")
c2 = input()
m2 = (int(c2)**d) % n
print("Mensaje decifrado: " + str(m2))


## Fuentes para el desarrollo del programa:
## https://www.youtube.com/watch?v=pBKQtPJE13U
## https://www.youtube.com/watch?v=gMVZdxyEg8g
## https://stackoverrun.com/es/q/7639854