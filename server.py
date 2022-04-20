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
            answer = ''
            if decoded == '1000':
                answer = 'Left'
                print('Left')
            elif decoded == '0100':
                answer = 'Right'
                print('Right')
            elif decoded == '0010':
                answer = 'Up'
                print('Up')
            elif decoded == '0001':
                answer = 'Down'
                print('Down')
            elif decoded == '1010':
                answer = 'Left & Up'
                print('Left & Up')
            elif decoded == '1001':
                answer = 'Left & Down'
                print('Left & Down')
            elif decoded == '0110':
                answer = 'Right & Up'
                print('Right & Up')
            elif decoded == '0101':
                answer = 'Left & Down'
                print('Left & Down')
            elif decoded == '0000':
                answer = 'Center'
                print('Center')
            client.send(answer)
except:
    print("Closing socket")
    client.close()
    s.close()