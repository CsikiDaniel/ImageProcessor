import socket
import time


class RaspberryCommunication:

    def __init__(self, ip_address, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((str(ip_address), int(port)))

    def send(self, movement):
        self.s.send(bytes(movement, 'UTF-8'))
        #time.sleep(0.1)
        if not movement:
            self.s.close()
