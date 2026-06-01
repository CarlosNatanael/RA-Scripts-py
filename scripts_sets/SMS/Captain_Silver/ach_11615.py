from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=11615, title="Captain Silver")

# 1. ALIASES DE MEMÓRIA
mem_pause = byte(0x0002)
mem_stage = byte(0x0025)
mem_lives = byte(0x0028)
mem_power = byte(0x0029)
mem_time_m = byte(0x002c)
mem_time_s = byte(0x002b)
mem_gold_100k = byte(0x0024)
mem_gold_1k = byte(0x0023)
mem_gamestate = byte(0x03d5)
mem_endgame = byte(0x0107)

# 2. PROGRESSÃO
prog_data = [
    (613397, "Defeating the Sorceress", "Clear Level 1, The Town of Barsend", 2, 1),
    (613398, "Captain Cahbad's Defeat", "Clear Level 2, The Ship", 2, 2),
    (613399, "Blinding the Cyclops", "Clear Level 3, The Boat", 5, 3),
    (613400, "Slaying the Dragon", "Clear Level 4, The Cave", 5, 4),
    (613401, "Peeling Top Banana", "Clear Level 5, The Jungle", 5, 5),
]

for a_id, title, desc, pts, stage in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_stage.delta() == stage),
        (mem_stage == stage + 1),
        (mem_gamestate == 0xff),
    ])
    my_set.add_achievement(ach)

# Level 6 / Win Condition
ach_win = Achievement(id=613402, title="Ghost of Captain Silver", description="Clear Level 6, The Mountain, and beat the game", points=10, type=AchievementType.WIN_CONDITION)
ach_win.add_core([
    (mem_stage == 0x06),
    (mem_endgame.delta() == 0x00),
    (mem_endgame == 0xff),
])
my_set.add_achievement(ach_win)

# 3. FLAWLESS (BOSSES SEM DANO/VIDA PERDIDA)
flawless_data = [
    (613403, "Flawless Barsend", "Clear Level 1 without losing a life", 5, 1),
    (613404, "Flawless Ship", "Clear Level 2 without losing a life", 10, 2),
    (613405, "Flawless Boat", "Clear Level 3 without losing a life", 10, 3),
    (613406, "Flawless Cave", "Clear Level 4 without losing a life", 25, 4),
    (613407, "Flawless Jungle", "Clear Level 5 without losing a life", 25, 5),
]

for a_id, title, desc, pts, stage in flawless_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        reset_next_if(mem_lives == 0x00),
        pause_if((mem_lives < mem_lives.delta()).with_hits(1)),
        (mem_stage.delta() == stage),
        trigger(mem_stage == stage + 1),
        (mem_gamestate == 0xff),
    ])
    my_set.add_achievement(ach)

# Flawless Mountain (Lógica de trigger diferente)
ach_flaw_mt = Achievement(id=613408, title="Flawless Mountain", description="Clear Level 6 without losing a life", points=50)
ach_flaw_mt.add_core([
        reset_next_if(mem_lives == 0x00),
        pause_if((mem_lives < mem_lives.delta()).with_hits(1)),
        (mem_stage == 0x06),
        (mem_endgame.delta() == 0x00),
        trigger(mem_endgame == 0xff),
])
my_set.add_achievement(ach_flaw_mt)

# 4. SWIFT LOOTER (TIME ATTACK)
swift_data = [
    (613416, "Swift Looter I", "Clear Level 1 with at least 40 seconds remaining", 2, 1),
    (613417, "Swift Looter III", "Clear Level 3 with at least 40 seconds remaining", 5, 3),
    (613418, "Swift Looter V", "Clear Level 5 with at least 40 seconds remaining", 10, 5),
]

for a_id, title, desc, pts, stage in swift_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_stage.delta() == stage),
        trigger(mem_stage == stage + 1),
        (mem_gamestate == 0xff),
        or_next(mem_time_m >= 0x01),
        (mem_time_s >= 0x40), # 0x40 representa 40 em BCD
    ])
    my_set.add_achievement(ach)

# 5. MISC (COLETÁVEIS, UPGRADES, DESAFIOS)
ach = Achievement(id=613409, title="A Prosperous Life", description="Clear the game without using any continues", points=50)
ach.add_core([
    reset_next_if(mem_time_m == 0x99),
    pause_if((mem_lives == 0x00).with_hits(1)),
    (mem_gamestate == 0xff),
    (mem_endgame.delta() == 0x00),
    trigger(mem_endgame == 0xff),
])
my_set.add_achievement(ach)

ach = Achievement(id=613410, title="A Ring Worth", description="Accumulate 50,000 gold", points=5)
ach.add_core([
    (mem_gamestate == 0xff),
    (mem_gold_100k == 0x00),
    (mem_gold_1k.delta() < 0x50),
    (mem_gold_1k >= 0x50),
])
my_set.add_achievement(ach)

ach = Achievement(id=613411, title="A Crown Worth", description="Accumulate 100,000 gold", points=10)
ach.add_core([
    (mem_gamestate == 0xff),
    (mem_gold_100k.delta() == 0x00),
    (mem_gold_100k >= 0x01),
])
my_set.add_achievement(ach)

ach = Achievement(id=613412, title="Brave Young Lad", description="Gain an extra life", points=1)
ach.add_core([
    (mem_gamestate == 0xff),
    (mem_lives > mem_lives.delta()),
])
my_set.add_achievement(ach)

letters_conds = [add_source(byte(addr).delta()) for addr in range(0x00f3, 0x00ff)]

ach = Achievement(id=613413, title="Changing Letters", description="Collect all the letters to spell CAPTAIN SILVER", points=2)
ach.add_core([
    (mem_gamestate == 0xff),
    *letters_conds,
    (byte(0x00ff).delta() == 12),
    (mem_lives > mem_lives.delta()),
])
my_set.add_achievement(ach)

ach = Achievement(id=613414, title="Five Magic Stars", description="Reach Power Level 3", points=5)
ach.add_core([
    (mem_gamestate == 0xff),
    (mem_power.delta() != 0x03),
    measured(mem_power == 0x03),
])
my_set.add_achievement(ach)

ach = Achievement(id=613415, title="Sword vs. Sorceress", description="Clear Level 1 staying at the default power level", points=5, type=AchievementType.MISSABLE)
ach.add_core([
    (mem_stage.delta() == 0x01),
    (mem_power == 0x00),
    (mem_stage == 0x02),
    trigger(mem_gamestate == 0xff),
])
my_set.add_achievement(ach)

my_set.save()