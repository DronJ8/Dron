import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # створюємо сокет
sock.connect(('localhost', 55000))  # підключамося
sentence = input('введіть речення') # вводимо речення
sock.send(bytes(sentence, encoding = 'UTF-8'))  # відправляємо повідомлення
data = sock.recv(1024)  # читаємо відповідь з сервера
print("В реченні є " + str(data) + "слів") # пишемо, скільки слів в речення, вставляємо отримане з сервера значення
sock.close()  # закриваємо
