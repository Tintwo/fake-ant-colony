#!/usr/bin/python

from sys import argv, exit
from objects.ressources.ressource import Ressource
from objects.ressources.leave import Leave
from objects.ressources.wood import Wood

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
        self.width = w
        self.height = h
        self.size = w*h
        self.map = [Chunk(i) for i in range(self.size)]

    def get_coord_from_i(self, number):
        if number < self.size:
            x = number % self.width
            y = int(number / self.width)
            coord = (x, y)
            return coord
        else:
            return False

    def get_i_from_coord(self, coord):
        if tuple == coord.__class__:
            x, y = coord
            if x < self.width and x >= 0 and y >= 0:
                i = y * self.width + x
                return i
            else:
                return -1
        else:
            return False

    def get_neighbour_coord_positions(self, coord):
        if tuple == coord.__class__:
            x, y = coord
            # method 1 : quick & dirty, need to check the array to remove impossible neighbours
            neighbours = [(x+c[0], y+c[1]) for c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]]
            for n in neighbours[:]:  # wrote array[:] to make a remove on the right element and don't reorder during loop
                if self.get_i_from_coord(n) >= self.size or self.get_i_from_coord(n) < 0:
                    neighbours.remove(n)
            # method 2 : check each 8 possibilities one by one before to add as neighbour
            return neighbours
        else:
            return False


class Chunk:
    def __init__(self, pos):
        self.id = """case %s""" % pos

    def add_ressource(self, rsc):
        pass

test = "World size : %sx%s (%s px)" % (worldWidth, worldHeight, worldWidth*worldHeight)
print(test)

world = World(worldWidth, worldHeight)
# print(world.get_coord_from_i(17))
# print(world.get_i_from_coord((3, 2)))
print(world.get_neighbour_coord_positions(world.get_coord_from_i(19)))

test1 = Ressource()
test2 = Leave(6)
test3 = Wood(5)
# print(dir(objects))
# print(objects.ressources.__all__)
# print(test3.TYPE)
