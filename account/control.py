import socket


class Control:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 12345

    def control(self, code):
        s = socket.socket()
        s.connect((self.host, self.port))
        s.send(code)
        result = s.recv()
        s.close()
        return result
