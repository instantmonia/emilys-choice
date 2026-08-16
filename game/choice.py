class Choice:
    def __init__(
            self,
            text:str,
            target_scene:str = None,
            target_dialogue:str = None,
            item_to_add = None,
            sanity_delta: int = 0,
            flags_delta: list = None,
            category: str = "action",
            response_text: str = None,
    ):
        self.text = text
        self.target_scene = target_scene
        self.target_dialogue = target_dialogue
        self.item_to_add = item_to_add
        self.sanity_delta = sanity_delta
        self.flags_delta = flags_delta if flags_delta is not None else []
        self.category = category
        self.response_text = response_text