class Ressource:
    def __init__(self, rtype, density):
        self.type = rtype
        self.amount = density*1000  # should be a random number from density * quantity associated
