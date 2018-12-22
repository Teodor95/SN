import ssl
from socket import *
from threading import Thread

clients = []


class Socket:
    def __init__(self):
        self._socket = socket(AF_INET,SOCK_STREAM)
        self.context = ssl.create_default_context()


def clientHandler(c, addr):
    global clients
    print(addr, "is Connected")
    try:
        while True:
            data = c.recv(1024)
            if not data:
                break
            for client in clients:
                if addr != client:
                    c.sendto(data, client)
    except:
        print("Error. Data not sent to all clients.")


HOST = ''  # localhost
PORT = 8000

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Server is running on " + str(PORT))

# Thread(target=clientHandler).start()
# Thread(target=clientHandler).start()
# Thread(target=clientHandler).start()
trds = []

for i in range(5):
    c, addr = s.accept()
    clients.append(addr)
    t = Thread(target=clientHandler, args=(c, addr))
    trds.append(t)
    t.start()

for t in trds:
    t.join()

s.close()
