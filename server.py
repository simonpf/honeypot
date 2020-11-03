"""
Example server application to demonstrate arbitrary code execution vulnerability
with pickle.
"""
import io
import socket
import pickle

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while(True):
        conn, addr = s.accept()
        with conn:
            data = io.BytesIO()
            while True:
                received = conn.recv(1024)
                data.write(received)
                if len(received) < 1024:
                    break

            try:
                print("trying to read data:")
                obj = pickle.loads(data.getvalue())
                print(obj)
                conn.sendall(f"Oh, you sent me an object. It looks like this:\n {obj}".encode())
            except Exception as e:
                conn.sendall(f"Hi {addr[0]}! I am still up and running :)".encode())
