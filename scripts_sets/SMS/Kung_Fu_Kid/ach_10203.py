from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=10203, title="Kung Fu Kid")

mem_lives = byte(0x000081)
mem_state = byte(0x000004)
mem_round = byte(0x000080)

ach_lives = Achievement(id=48208, title="Extra Lifes", description="Get 5 Lifes", points=10)
ach_lives.add_core([
    (mem_lives == 5),
    (mem_lives.delta() == 4),
    (mem_state == 0)
])
my_set.add_achievement(ach_lives)


ach_win = Achievement(id=48223, title="Kung Fu Master", description="Finish the Game", points=25, type=AchievementType.WIN_CONDITION)
ach_win.add_core([
    (mem_lives == 12),
    (mem_lives.delta() == 11),
    (mem_state == 0)
])
my_set.add_achievement(ach_win)

my_set.save()