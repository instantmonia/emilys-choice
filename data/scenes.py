from game.scene import Scene
from game.npc import Npcs
from game.item import Item
from game.choice import Choice

def load_scenes() -> dict[str, Scene]:
    father_Danis = Npcs(
        name="Daniel",
        identity=["priest", "teacher"],
        sanity=100,
        relationship=0,
        flags=[],
        dialogue=["Welcome, child","Congratulation for your achievement!"]
    )

    astrolabe = Item(
        name="astrolabe",
        description="A gift from Royal Academy of Astrology, just for the best student.",
        can_pick_up=True
    )

    nave = Scene(
        name="Monastery Nave",
        description="The central hall of a church where the congregation gathers for worship, prayers, and hymns.",
        items=[astrolabe],
        choices=[
            Choice(
                text="Accept the astrolabe",
                item_to_add=astrolabe,
                flags_delta=["star-reader"]
            ),
            Choice(
                text="Refuse the astrolabe",
                flags_delta=["commoner"]
            )
        ],
        npcs=[father_Danis]
    )

    return {
        "Monastery Nave": nave,
    }