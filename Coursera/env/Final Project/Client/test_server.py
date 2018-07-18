import socket

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf8"))
                if data.decode("utf8").split(' ')[0] == 'get':
                    conn.send('ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'.encode('utf8'))

