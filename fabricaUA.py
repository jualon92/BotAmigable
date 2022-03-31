import random
from random import choice


# que haga un ua de variable duracion y mayusculas
#uaa, ua,  uaAAa, uaAA, uaAa

# listaUA = ["ua","UaA", "UaA", "Uaa", "UAaA", "UAAaA", "UaaA", "UaaAA", "UaAaA", "uAaa", "uaAa", "uaaA", "uaaa"
# ] ##esta mejor que se genere por funciones, 1. se devuelve un uaa de random largo, y luego se vuelven mayusculas minusculas
 



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

