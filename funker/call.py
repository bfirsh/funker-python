import json
import socket


def call(name, **kwargs):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((name, 9999))
        sock.sendall(bytes(json.dumps(kwargs) + "\n", "utf-8"))
        sock.shutdown(socket.SHUT_WR)
        buf = ''
        while True:
            data = sock.recv(4096)
            if not data:
                break
            buf += str(data, "utf-8")
        return json.loads(buf)
    finally:
        sock.close()
