import socket

backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9527))
s.listen(backlog)
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)

        if len(data) == 4:
            decoded = data.decode('utf-8')
            if decoded == '1000':
                print('Left')
            elif decoded == '0100':
                print('Right')
            elif decoded == '0010':
                print('Up')
            elif decoded == '0001':
                print('Down')
            elif decoded == '1010':
                print('Left & Up')
            elif decoded == '1001':
                print('Left & Down')
            elif decoded == '0110':
                print('Right & Up')
            elif decoded == '0101':
                print('Left & Down')
            elif decoded == '0000':
                print('Center')
            client.send(data)
except:
    print("Closing socket")
    client.close()
    s.close()
