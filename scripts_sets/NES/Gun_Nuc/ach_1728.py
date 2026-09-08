from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=1728, title="Imported Set")

ach_6292_logic = [
    (byte(0x00e0) >= 0x01),
    (byte(0x00e0).delta() < 0x01),
    (byte(0x01be) == 0x00),
]
ach_6292 = Achievement(
    title="""Compiling Seven Digits""",
    description="""Score 1,000,000 points.""",
    points=5,
    id=6292, badge="387563"
)
ach_6292.add_core(ach_6292_logic)
my_set.add_achievement(ach_6292)

ach_6293_logic = [
    (byte(0x00e0) >= 0x04),
    (byte(0x00e0).delta() < 0x04),
    (byte(0x01be) == 0x00),
]
ach_6293 = Achievement(
    title="""Zanac Is So Last Light-Year!""",
    description="""Score 4,000,000 points.""",
    points=25,
    id=6293, badge="387564"
)
ach_6293.add_core(ach_6293_logic)
my_set.add_achievement(ach_6293)


my_set.save()