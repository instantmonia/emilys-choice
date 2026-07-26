from game.player import Player
from game.scene import Scene
from data.scenes import Scene

class Game:
    def __init__(self, player:Player, scenes:dict[str, Scene]):
        self.player = player
        self.scenes = scenes
        self.current_scene_name = player.current_location

    @property
    def current_scene(self) -> Scene:
        return self.scenes[self.current_scene_name]
