import socket
import io
import pickle

HOST = '129.16.35.44'  # The server's hostname or IP address
PORT = 8000        # The port used by the server

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#
#    all_data = io.BytesIO(b'Hello, world' * 1000)
#    while True:
#        data = all_data.read(1024)
#        s.sendall(data)
#        if len(data) < 1024:
#            break
#    data = s.recv(1024)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    all_data = io.BytesIO(pickle.dumps(":)"))
    while True:
        data = all_data.read(1024)
        s.sendall(data)
        if len(data) < 1024:
            break
    data = s.recv(1024)

print('Received', repr(data))
