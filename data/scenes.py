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
                text="Emily says, \"The capital is not far from here. I will come back often to visit you. Don't be sad.\" "
                     "Oliver looks up at her with red eyes and whispers, \"Promise?\"",
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
                        target_scene="Monastery Nave - At the Outbreak of War",
                        flags_delta=["promised_oliver"]
                    )
                ]
            )
        }
    )

    monastery_war = Scene(
        name="Monastery Nave - At the Outbreak of War",
        description="Two month later",
        choices=[
            Choice(target_dialogue="daniel_start")
        ],
        dialogues={
            "daniel_start": DialogueNode(
                npc_name="Daniel",
                text="\"The vampires’ war has spread to the area around the monastery… It’s no longer safe here.\n\n "
                     "News has arrived from the capital: for safety reasons, enrollment has been canceled this year as well.\n\n "
                     "I’ve contacted some families who are willing to adopt you. You now have a chance to leave this place and escape the danger.\n\n "
                     "Would you like to go?\"",
                choices=[
                    Choice(
                        text="Stay and care for the other orphans",
                        target_dialogue="emily_promise"
                    ),
                    Choice(
                        text="Leave and go to the adoptive family",
                        target_dialogue="be1_adopted"
                    ),
                    Choice(
                        text="Insist on enrolling at the Academy of Astrology",
                        target_dialogue="daniel_warning"
                    )
                ]
            ),
            "emily_promise": DialogueNode(
                npc_name="Daniel",
                text="\"If you stay at the monastery, you may never be able to leave.\" ",
                choices=[
                    Choice(
                        text="Saintfield is my home. It’s in danger, and I can’t abandon it.",
                        target_dialogue="From the Prologue to Chapter 1"
                    )
                ]
            ),
            "daniel_warning": DialogueNode(
                npc_name="Daniel",
                text="\"It's very dangerous. Do you still insist on going?\"",
                choices=[
                    Choice(
                        text="Yes.",
                        target_dialogue="be2_on the way"
                    ),
                    Choice(
                        text="Fine, I’ll take your advice.",
                        target_dialogue="From the Prologue to Chapter 1"
                    )
                ]

            ),
            "be1_adopted": DialogueNode(
                npc_name="Narration",
                # TODO: good part to link LLM
                text="Daniel says, \"May God watch over you, Emily, and guide you on the path ahead.\"\n\n "
                     "The adoptive family gave Emily a good life, and they spent many happy days together.\n\n "
                     "Unfortunately, the flames of war eventually reached their little home,\n\n "
                     "and with it, the fate Emily might have changed was lost forever."
            ),
            "be2_on the way": DialogueNode(
                npc_name="Narration",
                #TODO: good part to link LLM
                text="The road to the capital was already overrun by vampires.\n\n "
                     "Emily never made it to the capital, falling along the way with her dreams left unfulfilled."
            ),

            "From the Prologue to Chapter 1": DialogueNode(
                npc_name="Narration",
                text="111"
            )
        }
    )

    return {
        "Monastery Nave": nave_ceremony,
        "Monastery Garden": garden,
        "Monastery Nave - At the Outbreak of War": monastery_war
    }

#description="The central hall of a church where the congregation gathers for worship, prayers, and hymns."
#问题：运行程序时显示了NPC名字