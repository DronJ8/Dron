import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # сстворюємо сокет
sock.bind(('', 55000))  # поєднуємо порт і сокет
sock.listen(10)  # вказуємо період прослуховування
print('Сервер працює') # виводимо повідомлення що сервер працює
while True: # нескінченний цикл
    conn, addr = sock.accept()  # зєднання
    print('connected:', addr)  # інфа про підключення
    data = conn.recv(1024)  # дані від клієнта
    result = len(data.split()) # підраховуємо кількість слів в реченні
    print("There are " + str(result) + " words.") # виводимо інфу про кількість слів в серв.част
    ff=str(result) # перетв тип даних
    f = bytes(ff, encoding='UTF-8') #  кодування
    #     print("отримана інфа з клієнта", str(result)) # виводим інфу, яку отримали від клієнта
    conn.send(f)  # відправляємо кієнту відповідь
conn.close()  # закриваємо