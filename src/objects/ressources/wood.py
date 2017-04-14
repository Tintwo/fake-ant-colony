from objects.ressources.ressource import *


class Wood(Ressource):

    TYPE = "wood"

    def __init__(self, qty):
        self.fiber = 0.9
        self.water = 0.09
        self.sugar = 0.01
        self.qty = qty
