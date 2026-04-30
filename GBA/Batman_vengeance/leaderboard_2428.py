from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=2428, title="Imported Leaderboards")

mem_mode = byte(0x3db8)
mem_level = byte(0x3da8)

TIMERS = {
    "Batman":    (byte(0x002c), byte(0x002b), byte(0x002a)),
    "Batmobile": (byte(0x4312), byte(0x4311), byte(0x4310)),
    "Robin":     (byte(0x00ec), byte(0x00eb), byte(0x00ea)),
    "Batplane":  (byte(0x4272), byte(0x4271), byte(0x4270)),
}

# 2. DADOS DOS LEADERBOARDS
# Formato: (LB_ID, "Número", "Personagem", Level_Inicial)
leaderboard_data = [
    (162091, "01", "Batman", 21),
    (162093, "02", "Batmobile", 22),
    (162094, "03", "Robin", 23),
    (162095, "04", "Batplane", 24),
    (162096, "05", "Batmobile", 25),
    (162097, "06", "Robin", 26),
    (162098, "07", "Batplane", 27),
    (162099, "08", "Batman", 28),
    (162100, "09", "Batman", 29),
    (162101, "10", "Batplane", 30),
    (162102, "11", "Robin", 31),
    (162103, "12", "Batmobile", 32),
    (162104, "13", "Batman", 33),
    (162105, "14", "Batmobile", 34),
    (162106, "15", "Batman", 35),
    (162107, "16", "Robin", 36),
]

# 3. GERAÇÃO DINÂMICA
for lb_id, num, character, lvl in leaderboard_data:
    next_lvl = lvl + 1
    
    timer_min, timer_sec, timer_ms = TIMERS[character]

    lb_start = [
        (mem_mode == value(1)),
        (mem_level == value(lvl)),
        (mem_level.delta() != value(lvl)),
    ]
    
    lb_cancel = [
        (mem_level != value(lvl)),
        (mem_level != value(next_lvl)),
        (mem_level.delta() == value(lvl)),
    ]
    
    lb_submit = [
        (mem_mode == value(1)),
        (mem_level == value(next_lvl)),
        (mem_level.delta() == value(lvl)),
    ]
    
    lb_value = [
        add_source(timer_min * 60),
        add_source(timer_sec * 10),
        measured(timer_ms),
    ]
    
    lb = Leaderboard(
        id=lb_id,
        title=f"Advanced Trial {num} - {character}",
        description=f"Complete Advanced Mode Level {int(num)}. Ranked by the highest time remaining on the clock",
        format=LeaderboardFormat.VALUE,
        lower_is_better=False
    )
    
    lb.set_start(lb_start)
    lb.set_cancel(lb_cancel)
    lb.set_submit(lb_submit)
    lb.set_value(lb_value)
    
    my_set.add_leaderboard(lb)

my_set.save()