import socket
import time


class RaspberryCommunication:

    def __init__(self, ip_address, port):
        try:
            self.timeout = 1
            self.raspberry_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.raspberry_socket.connect((str(ip_address), int(port)))
            self.raspberry_socket.settimeout(self.timeout)
        except:
            print("\n\nServer is not available!")

    def send(self, movement):
        self.raspberry_socket.send(bytes(movement, 'UTF-8'))
        # time.sleep(0.1)
        if not movement:
            self.raspberry_socket.close()

    def receive(self):
        received_data = self.raspberry_socket.recv(1024)
        return received_data.decode()
