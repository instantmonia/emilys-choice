class Npcs:
    def __init__(self, name:str, identity:list, sanity:int, flags:list, relationship:int, dialogue:list):
        self.name = name
        self.identity = identity
        self.sanity = sanity
        self.relationship = relationship
        self.flags = flags
        self.dialogue = dialogue

    def __str__(self):
        return f"{self.name} ({', '.join(self.identity)}) - {self.sanity}, relationship: {self.relationship}"