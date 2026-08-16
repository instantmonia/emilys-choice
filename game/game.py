from game.player import Player
from game.scene import Scene

class Game:
    def __init__(self, player:Player, scenes:dict[str, Scene]):
        self.player = player
        self.scenes = scenes
        self.current_dialogue_name = None
        self.current_scene_name = player.current_location

    @property
    def current_scene(self) -> Scene:
        return self.scenes[self.current_scene_name]

    @property
    def current_dialogue(self):
        if self.current_dialogue_name is None:
            return None
        return self.current_scene.dialogues[self.current_dialogue_name]

    def choose(self, choice_index: int):
        if self.current_dialogue is not None:
            choice = self.current_dialogue.choices[choice_index]
        else:
            choice = self.current_scene.choices[choice_index]

        if choice.item_to_add is not None:
            if choice.item_to_add not in self.player.inventory:
                self.player.inventory.append(choice.item_to_add)

        if choice.sanity_delta != 0:
            self.player.sanity += choice.sanity_delta

        if choice.flags_delta:
            self.player.flags.extend(choice.flags_delta)

        if choice.target_scene is not None:
            self.current_scene_name = choice.target_scene
            self.player.current_location = choice.target_scene
            self.current_dialogue_name = None

        if choice.target_dialogue is not None:
            self.current_dialogue_name = choice.target_dialogue

        return choice.response_text
