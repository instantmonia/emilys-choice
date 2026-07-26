class Player:
    def __init__(self):
        self.name = "Emily"
        self.current_location = "Monastery Nave"
        self.identity = ["orphan", "student"]
        self.sanity = 100
        self.inventory = []
        self.flags = []

    def __str__(self):
        return f"{self.name} ({', '.join(self.identity)}) - {self.current_location}, sanity: {self.sanity}"