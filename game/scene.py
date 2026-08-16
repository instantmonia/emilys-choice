class Scene:
    def __init__(self, name: str, description: str,
                 items: list = None, choices: list = None, npcs: list = None, dialogues=None):
        self.name = name
        self.description = description
        self.items = items if items is not None else []
        self.choices = choices if choices is not None else []
        self.npcs = npcs if npcs is not None else []
        self.dialogues = dialogues if dialogues is not None else {}

    def __str__(self):
        items_str = ', '.join(str(item) for item in self.items)
        npcs_str = ', '.join(str(npc) for npc in self.npcs)
        return f"{self.name} — items: [{items_str}], npcs: [{npcs_str}], choices: {len(self.choices)}"