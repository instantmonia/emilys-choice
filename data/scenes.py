from game.scene import Scene
from game.npc import Npcs
from game.item import Item
from game.choice import Choice
from game.dialogue import DialogueNode

def load_scenes() -> dict[str, Scene]:
    father_daniel = Npcs(
        name="Daniel",
        identity=["priest", "teacher"],
        sanity=100,
        relationship=0,
        flags=[],
        dialogue=["Welcome, child.","Congratulation for your achievement!"]
    )

    oliver = Npcs(
        name="Oliver",
        identity=["orphan","student","exceptional_kid"],
        sanity=100,
        relationship=0,
        flags=[],
        dialogue=["..."]
    )

    astrolabe = Item(
        name="astrolabe",
        description="A gift from Royal Academy of Astrology, just for the best student.",
        can_pick_up=True
    )

    nave_ceremony = Scene(
        name="Monastery Nave - Ceremony",
        description=(
            "Father Daniel stands before the gathered students.\n\n"
            "\"This summer, Emily Field will enter Belharis Academy of Astrology as a new student. "
            "She is the first student from Saintfield ever to be accepted by Belharis.\"\n\n"
            "He then holds out a polished astrolabe to her."
        ),
        items=[],
        choices=[
            Choice(
                text="Accept the astrolabe",
                target_dialogue="daniel_after_award",
                item_to_add=astrolabe,
                flags_delta=["star-reader"]
            ),
            Choice(
                text="Refuse the astrolabe",
                target_dialogue="daniel_after_award",
                flags_delta=["commoner"]
            )
        ],
        npcs=[father_daniel],
        dialogues={
            "daniel_after_award": DialogueNode(
                npc_name="Daniel",
                text=(
                    "The applause fades.\n\n"
                    "Father Daniel says, \"To every student with ambition, let Emily be your example.\"\n\n"
                    "The ceremony ends, and the crowd gradually disperses."
                ),
                choices=[
                    Choice(
                        text="Leave for the garden",
                        target_scene="Monastery Garden"
                    )
                ]
            )
        }
    )

    garden = Scene(
        name="Garden",
        description="Emily arrived at the garden. Beautiful flowers bloomed throughout it, and a statue of a saint stood at its center. Suddenly, she saw a shadow dart through the flowers.",
        items=[],
        choices=[
            Choice(
                text="Follow it",
                target_dialogue="oliver_start",
                flags_delta=["approached_oliver"]
            ),
            Choice(
                text="Ignore it",
                target_scene="Monastery Gate",
                flags_delta=["ignored_oliver"]
            )
        ],
        npcs=[oliver],
        dialogues={
            "oliver_start": DialogueNode(
                npc_name="Narration",
                text="Oliver stands near the statue, pale and trembling. His eyes never meet Emily's, and tears keep streaming down his cheeks.",
                choices=[
                    Choice(
                        text="Ask him what happened",
                        target_dialogue="oliver_pleads",
                    ),
                    Choice(
                        text="Hold him gently",
                        target_dialogue="oliver_pleads",
                    )
                ]
            ),
            "oliver_pleads": DialogueNode(
                npc_name="Oliver",
                text="Don’t go... please... don’t go...",
                choices=[
                    Choice(
                        text="Reassure Oliver",
                        target_dialogue="oliver_asks_promise",
                    )
                ]
            ),
            "oliver_asks_promise": DialogueNode(
                npc_name="Narration",
                text="Emily says, \"The capital is not far from here. I will come back often to visit you. Don't be sad.\" Oliver looks up at her with red eyes and whispers, \"Promise?\"",
                choices=[
                    Choice(
                        text="Promise him",
                        target_dialogue="oliver_reassured",
                    )
                ]
            ),
            "oliver_reassured": DialogueNode(
                npc_name="Narration",
                text="Emily promises. Oliver nods quietly, though his fingers still hold her sleeve for a moment before letting go.",
                choices=[
                    Choice(
                        text="Two months later",
                        target_scene="Monastery Gate",
                        flags_delta=["promised_oliver"]
                    )
                ]
            )
        }
    )

    return {
        "Monastery Nave": nave_ceremony,
        "Monastery Garden": garden
    }

#description="The central hall of a church where the congregation gathers for worship, prayers, and hymns."