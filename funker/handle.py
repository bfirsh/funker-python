import json
import socketserver


class HandleHandler(socketserver.StreamRequestHandler):
    def handle(self):
        kwargs = json.loads(str(self.rfile.read(), "utf-8"))
        return_value = self.server.func(**kwargs)
        return_str = json.dumps(return_value)
        self.wfile.write(return_str.encode("utf-8"))
        self.wfile.close()


def handle(func):
    server = socketserver.TCPServer(("0.0.0.0", 9999), HandleHandler)
    server.request_queue_size = 1  # drop any connections except from the first
    server.timeout = None
    server.func = func
    server.handle_request()
    server.server_close()
