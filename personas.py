
import random


class Persona:  # cada usuario tiene su id, su nombre, y responden a su manera los mismos mensajes.
    def __init__(self, nombre, ids, jokes):
        self._ids = ids
        self._nombre = nombre
        self._jokes = jokes

    def tiene_id(self, id):
        return (self._ids.contain(id))

    def tiene_malasuerte(self):
        return random.randint(0,  10) > 1

    def get_joke(self):  # cada persona conoce las frases a las que usualmente son sujetos
        indiceRand = random.randint(0,  len(self.jokes) - 1)
        return self._jokes[indiceRand]


shaxi = Persona("Shaxi", [939515696503722035,931792716961038376,939213296031113217],
                ["qin ti priginti prrin", "who asked you, little doggie"])
