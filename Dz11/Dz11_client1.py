import socket
i=0
while True:
    m = int(input("введіть число"))
    if m in range(5):
        massage = str(m)
        break
    else:
        i=i+1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
sock.send(bytes(massage, encoding = 'UTF-8'))
data = sock.recv(1024)
print("тип даних ----", type(data))
sock.close()
print(data)
