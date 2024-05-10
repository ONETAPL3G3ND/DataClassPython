from dataclasses import dataclass

@dataclass(frozen=True)
class Client:
    name: str
    ip: str
    port: int

class Server:
    def __init__(self):
        self.clients = []

    def AddClient(self, client: Client):
        self.clients.append(client)


if __name__ == '__main__':
    client = Client(name="Sergii", ip="192.168.2.1", port=25565)
    server = Server()
    server.AddClient(client)
    client.name = "Vasya" #dataclasses.FrozenInstanceError: cannot assign to field 'name'