import socket as sok
from threading import *

class Server:
    def __init__(self, host, port) -> None:
        self.server = sok.socket()
        self.host = host
        self.port = port
        self.server.bind((self.host, self.port))

    def run(self) -> None:
        ...