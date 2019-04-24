class Par:
    def __init__(self, id, url):
        self.id = id
        self.url = url

    def to_string(self):
        return str(self.id) + "|" + self.url

    def to_object(self, cadena):
        a,b = cadena.decode().split("|")
        self.id = int(a)
        self.url = str(b)