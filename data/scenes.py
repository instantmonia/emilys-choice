from game.scene import Scene
from game.npc import Npcs
from game.item import Item
from game.choice import Choice

def load_scenes() -> dict[str, Scene]:
    father_Daniel = Npcs(
        name="Daniel",
        identity=["priest", "teacher"],
        sanity=100,
        relationship=0,
        flags=[],
        dialogue=["Welcome, child","Congratulation for your achievement!"]
    )

    oliver = Npcs(
        name="Oliver",
        identity=["orphan","student","exceptional_kid"],
        sanity=100,
        relationship=0,
        flags=[],
        dialogue=["Don’t go… please… don’t go…"]
    )

    astrolabe = Item(
        name="astrolabe",
        description="A gift from Royal Academy of Astrology, just for the best student.",
        can_pick_up=True
    )

    nave_ceremony = Scene(
        name="Monastery Nave - ceremony",
        description="Father Daniel holds out the astrolabe before the gathered students.",
        items=[astrolabe],
        choices=[
            Choice(
                text="Accept the astrolabe",
                target_scene="Monastery Nave - After Ceremony",
                item_to_add=astrolabe,
                flags_delta=["star-reader"]
            ),
            Choice(
                text="Refuse the astrolabe",
                target_scene="Monastery Nave - After Ceremony",
                flags_delta=["commoner"]
            )
        ],
        npcs=[father_Daniel]
    )

    after_ceremony = Scene(
        name="Monastery Nave - After Ceremony",
        description="The applause fades. Father Daniel lowers his voice and speaks to Emily before the hall begins to empty.",
        items=[],
        choices=[
            Choice(
                text="Listen to Father Daniel",
                target_scene="Monastery Garden",
                flags_delta=["heard_daniel_after_ceremony"]
            )
        ],
        npcs=[father_Daniel]
    )

    garden = Scene(
        name="Garden",
        description="A beautiful garden within the monastery. At its center stands a statue of a saint.",
        items=[],
        choices=[],
        npcs=[oliver]
    )

    return {
        "Monastery Nave": nave_ceremony,
        "Monastery Nave - After Ceremony": after_ceremony,
        "Monastery Garden": garden,
    }

#description="The central hall of a church where the congregation gathers for worship, prayers, and hymns."