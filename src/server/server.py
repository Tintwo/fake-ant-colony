from sys import argv, exit
import os

from common import config


class Server:
    def __init__(self, addresses=['localhost'], port=config.port):
        self.addresses = addresses
        self.port = port
