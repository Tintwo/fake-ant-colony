#!/usr/bin/python

from sys import argv, exit
import json
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
    def __init__(self, filemap=None):
        if filemap is None:
            global worldWidth, worldHeight
            print("Starting an empty world...")
            self.width = worldWidth
            self.height = worldHeight
            self.size = self.width * self.height
            self.map = [Chunk({'type': 'grass', 'ressources': {'leave': 150, 'wood': 10}}) for i in range(self.size)]
            print("The world is made of %d chunks (%dx%s)" % (self.size, self.width, self.height))
        else:
            print("Starting a world")
            self.build_map_from_file(filemap)
            print("The world is made of %d chunks (%dx%s)" % (self.size, self.width, self.height))

    def build_map_from_file(self, file):
        """Load a JSON file which contains all ressources and quantities"""
        h = open(file)
        jr = json.load(h)
        h.close()
        self.width = jr["width"]
        self.height = jr["height"]
        self.size = self.width * self.height
        self.map = []
        for c in jr["map"]:
            self.map.append(Chunk(c))

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
            all_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            # method 1 : quick & dirty, need to check the array to remove impossible neighbours
            # neighbours = [(x + c[0], y + c[1]) for c in all_directions]
            # for n in neighbours[:]:  # wrote array[:] to make a remove on the right element and don't reorder during loop
            #     if self.get_i_from_coord(n) >= self.size or self.get_i_from_coord(n) < 0:
            #         neighbours.remove(n)
            # method 2 : check each 8 possibilities one by one before to add as neighbour
            neighbours = []
            for n in all_directions[:]:
                possible_neighbour = (x + n[0], y + n[1])
                possible_neighbour_id = self.get_i_from_coord(possible_neighbour)
                if 0 <= possible_neighbour_id < self.size:
                    neighbours.append(possible_neighbour)
            return neighbours
        else:
            return False

    def get_chunk_infos(self, number):
        if number < self.size:
            self.map[number].get_infos()
        else:
            return False


class Chunk:
    def __init__(self, data):
        self.type = data['type']
        self.ressources = data['ressources']

    def get_infos(self):
        elements = []
        for e in self.ressources:
            elements.append("%s(%d)" % (e, self.ressources[e]))
        infos = "Chunk details: type '%s' with %s" % (self.type, ', '.join(elements))
        print(infos)

    def add_ressource(self, rsc):
        pass

# test = "World size : %sx%s (%s px)" % (worldWidth, worldHeight, worldWidth*worldHeight)
# print(test)

# world = World()
world = World("test_map.json")
# print(world.get_coord_from_i(17))
# print(world.get_i_from_coord((3, 2)))
# print(world.get_neighbour_coord_positions(world.get_coord_from_i(19)))
world.get_chunk_infos(19)

# test1 = Ressource()
# test2 = Leave(6)
# test3 = Wood(5)
# print(dir(objects))
# print(objects.ressources.__all__)
# print(test3.TYPE)
