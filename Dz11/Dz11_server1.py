import socket
season = {1:"winter", 2:"spring", 3:"summer", 4:"autumn"}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    d = int(data)
    print('повідомлення, яке буде надіслане - ', season[d])
    f = bytes(season[d], encoding='UTF-8')

    conn.send(f)
conn.close()