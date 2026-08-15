from game.player import Player
from game.game import Game
from data.scenes import load_scenes

def main():
    player = Player()
    scenes = load_scenes()
    game = Game(player, scenes)

    while True:
        scene = game.current_scene

        print()
        print(scene.name)
        print(scene.description)

        if scene.npcs:
            print("\nNPCs:")
            for npc in scene.npcs:
                print(npc.name)

        if scene.items:
            print("\nItems:")
            for item in scene.items:
                print(item.name)

        print("\nChoices:")
        for index, choice in enumerate(scene.choices):
            print(f"{index}. {choice.text}")

        user_input = input("Choose: ")

        if user_input == "quit":
            break

        choice_index = int(user_input)
        game.choose(choice_index)


if __name__ == '__main__':
    main()
