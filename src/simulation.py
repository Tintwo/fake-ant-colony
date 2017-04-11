#!/usr/bin/python

from sys import argv, exit

# default configuration part
worldWidth = 4
worldHeight = 6

# usage text
usage = """Usage: %s [-h|--help]""" % argv[0]

# help!
if "--help" in argv or "-h" in argv:
    print(usage)
    exit()

class World:
    def __init__(self, w, h):
        self.map = [Chunk(i) for i in range(w*h)]

    def get_tuple_from_number(self, number):
        global worldWidth
        x = number % worldWidth
        y = int(number / worldWidth)
        coord = (x, y)
        return coord

    def get_i_from_tuple(self, tuple):
        global worldWidth
        x, y = tuple
        i = y * worldWidth + x
        return i

class Chunk:
    def __init__(self, pos):
        self.id = """case %s""" % pos

    def add_ressource(self, rsc):
        pass

test = "World size : %sx%s" % (worldWidth, worldHeight)
print(test)

# world = [Chunk(i) for i in range(worldWidth*worldHeight)]
# print(world[11].id)
world = World(worldWidth, worldHeight)
print(world.get_tuple_from_number(11))
print(world.get_i_from_tuple((3, 2)))
