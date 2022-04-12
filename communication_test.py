import pytest
import socket
from communication import RaspberryCommunication

ip_address = '127.0.0.1'
port = 9527


def test_sended_data_match():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((str(ip_address), int(port)))
    RaspberryCommunication.send()


