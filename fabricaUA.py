import random
from random import choice

def getPalabra(cantidadA):  # utilizar clases para ua estaria mejor
    pal = "u"
    i = 0
    while i < cantidadA:  # ua, uaaa, uaaa
        pal = pal + "a"
        i += 1
    return pal


def getUa():
    pal = getPalabra(random.randint(1, 5))  # largo palabra
    return getMayusculasRandom(pal)


def getMayusculasRandom(pal):  # devuelve mayus arbitrarias "hola" hOlA hoLA
    eleccionMayus = zip(pal.lower(), pal.upper())  # ("H","h"), ("O","o")
    # que eliga entre cada una y luego pase a string con join
    return "".join(map(choice, eleccionMayus))

