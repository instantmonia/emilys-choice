class Item:
    def __init__(self, name:str, description:str, can_pick_up:bool):
        self.name = name
        self.description = description
        self.can_pick_up = can_pick_up

    def __str__(self):
        return f"{self.name}: {self.can_pick_up}"