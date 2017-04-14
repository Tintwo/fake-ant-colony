from objects.ressources.ressource import *


class Leave(Ressource):

    TYPE = "leave"

    def __init__(self, qty):
        self.fiber = 0.21
        self.water = 0.7
        self.sugar = 0.09
        self.qty = qty
