from game.player import Player
from game.game import Game
from data.scenes import load_scenes


def get_choice_index(choices):
    while True:
        user_input = input("Choose: ")

        if user_input == "quit":
            return None

        try:
            choice_index = int(user_input)
        except ValueError:
            print("Please enter a number, or type 'quit' to exit.")
            continue

        if not (0 <= choice_index < len(choices)):
            print(f"Please enter a number between 0 and {len(choices) - 1}.")
            continue

        return choice_index


def main():
    player = Player()
    scenes = load_scenes()
    game = Game(player, scenes)

    while True:
        scene = game.current_scene
        dialogue = game.current_dialogue

        if dialogue is not None:
            print()
            print(dialogue.npc_name)
            print(dialogue.text)
            choices = dialogue.choices
        else:
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

            choices = scene.choices

        if not choices:
            print("\nThe scene ends here.")
            break

        print("\nChoices:")
        for index, choice in enumerate(choices):
            print(f"{index}. {choice.text}")

        choice_index = get_choice_index(choices)

        if choice_index is None:
            break

        response_text = game.choose(choice_index)

        if response_text is not None and response_text != "":
            print()
            print(response_text)
            input("\nPress Enter to continue...")


if __name__ == '__main__':
    main()
