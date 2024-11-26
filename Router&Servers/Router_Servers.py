from random import sample

class Server:
    ip_val = sample(range(1,10000),9998)
    
    def __init__(self):
        self.buffer = []
        self.router = None
        self.ip = self.ip_val.pop()
        
    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)
        
    def get_data(self):
        buffer2 = self.buffer.copy()
        self.buffer = []
        return buffer2
    
    def get_ip(self):
        return self.ip

class Router:
    def __init__(self):
        self.buffer = []
        self.dct = dict()
        
    def link(self, server):
        self.dct[server.ip] = server
        server.router = self
        
    def unlink(self, server):
        server.router = None
        del self.dct[server.ip]
    
    def send_data(self):
        for obj in self.buffer:
            if obj.ip in self.dct:
                self.dct[obj.ip].buffer.append(obj)
        self.buffer = []
        
class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
