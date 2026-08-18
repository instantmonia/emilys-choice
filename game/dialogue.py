class DialogueNode:
    def __init__(self, npc_name:str, text:str, choices: list = None, prompt: str = None):
        self.npc_name = npc_name
        self.text = text
        self.choices = choices if choices is not None else []
        self.prompt = prompt