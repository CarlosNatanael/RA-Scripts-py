from pycheevos.core.helpers import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=36353, title="Boxing Achievements")

tech_addrs = [
    0x1fe6dd, 0x1fe6de, 0x1fe6df, 0x1fe6e3, 0x1fe6e4, 0x1fe6e5, 
    0x1fe6e9, 0x1fe6ea, 0x1fe6ef, 0x1fe6f0, 0x1fe6f1, 0x1fe6f2, 
    0x1fe6f5, 0x1fe6fb, 0x1fe6fc, 0x1fe6fd, 0x1fe701, 0x1fe702, 
    0x1fe707, 0x1fe70d, 0x1fe70e, 0x1fe70f, 0x1fe713, 0x1fe714, 
    0x1fe719, 0x1fe71a, 0x1fe71b, 0x1fe71f, 0x1fe725, 0x1fe726
]

mem_menu = byte(0x1fef74)

ach_tech = Achievement(id=589151, title="Master of Techniques", description="Successfully perform the special move of each of the 13 characters", points=10, badge="670229")
ach_tech.add_core([
    *[add_source(byte(addr).delta()) for addr in tech_addrs[:-1]],
    byte(tech_addrs[-1]).delta() < 30,
    measured_if(mem_menu == 4),
    *[add_source(byte(addr)) for addr in tech_addrs[:-1]],
    measured(byte(tech_addrs[-1]) == 30),
    reset_if(mem_menu != 4)
])
my_set.add_achievement(ach_tech)

my_set.save()