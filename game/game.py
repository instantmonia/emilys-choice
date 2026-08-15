from game.player import Player
from game.scene import Scene

class Game:
    def __init__(self, player:Player, scenes:dict[str, Scene]):
        self.player = player
        self.scenes = scenes
        self.current_scene_name = player.current_location

    @property
    def current_scene(self) -> Scene:
        return self.scenes[self.current_scene_name]

    def choose(self, choice_index: int):
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
