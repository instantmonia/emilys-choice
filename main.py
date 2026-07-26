from game.player import Player
from game.game import Game
from data.scenes import load_scenes

def main():
    player = Player()
    scenes = load_scenes()
    game = Game(player, scenes)

    print(game.current_scene.name)
    print(game.current_scene.description)

    for npc in game.current_scene.npcs:
        print(npc.name)

    print(game.current_scene)

if __name__ == '__main__':
    main()
