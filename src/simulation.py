#!/usr/bin/python

from sys import argv, exit

from common import config

# usage text
usage = """Usage: %s [-h|--help]""" % argv[0]

# help!
if "--help" in argv or "-h" in argv:
    print(usage)
    exit()

# defaults
addresses = ["localhost"]
port = config.port
language = "en"

test = "%s:%s" % (addresses[0], port)
print(test)
