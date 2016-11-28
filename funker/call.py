import json
import six
import socket


def call(name, **kwargs):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((name, 9999))
        sock.sendall(json.dumps(kwargs).encode("utf-8"))
        sock.shutdown(socket.SHUT_WR)
        buf = six.binary_type()
        while True:
            data = sock.recv(4096)
            if not data:
                break
            buf += data
        return json.loads(six.text_type(buf, "utf-8"))
    finally:
        sock.close()
