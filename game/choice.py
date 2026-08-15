from.player import Player

class Choice:
    def __init__(
            self,
            text:str,
            target_scene:str = None,
            item_to_add = None,
            sanity_delta: int = 0,
            flags_delta: list = None,
    ):
        self.text = text
        self.target_scene = target_scene
        self.item_to_add = item_to_add
        self.sanity_delta = sanity_delta
        self.flags_delta = flags_delta if flags_delta is not None else []