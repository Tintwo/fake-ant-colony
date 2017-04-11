from threading import Thread


class Ant(Thread):
    def __init__(self, init_location):
        Thread.__init__(self)
        self.init_location = init_location

    def run(self):
        pass

    def smell(self):
        pass

    def do_action(self):
        pass
