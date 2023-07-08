import socket as sok
from threading import *

class Server:
    def __init__(self, host, port) -> None:
        self.server = sok.socket()
        self.host = host
        self.port = port
        self.server.bind((self.host, self.port))

    def SetLogic(self, logics:dict):
        self.logics = logics

    def run(self) -> None:
        self.server.listen()
        while True:
            c,addr = self.server.accept()
            req = c.recv(1024)
            hdrs = req.split(b"\r\n")
            path = hdrs[0].split()[1]
            res = ""
            try:
                self.logics[path](res)
            except:
                print("Not write this logic ")
                res = b"HTTP/1.0 404 NOT FOUND\r\n\r\n Not logic"

            c.sendall(res)