from communication import RaspberryCommunication
import pytest

ip_address = '192.168.1.162'
port = 9527

def test_data_match():
    raspberry_communication = RaspberryCommunication(ip_address, port)
    sended_data = "Hello World!"
    raspberry_communication.send(sended_data)
    recived_data = raspberry_communication.recive()
    print(recived_data)
    assert sended_data == recived_data




