from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=1167, title="Sonic Blast Man")

# 1. ALIASES DE MEMÓRIA
mem_state     = byte(0x000062)
mem_stage     = byte(0x0000aa)
mem_mode      = byte(0x001852)
mem_diff      = byte(0x00185a)
mem_lives     = byte(0x000fa1)
mem_dpunch    = byte(0x000fa3)

# Pontuação
mem_score_h   = byte(0x001a0c)
mem_score_l   = byte(0x001a0b)

# Combate & Hit Stages
mem_power     = byte(0x0018f9)
mem_100t      = byte(0x001992)
mem_hit_id    = byte(0x0018e8)
mem_hit_state = byte(0x00199f)
mem_hit_score = byte(0x0019e9)


# 2. PROGRESSÃO (STAGES)
prog_data = [
    (608416, "Ghost Town Showdown", "Complete Stage 1 and clear out the dirty varmints", 2, 0),
    (608417, "Weapon Factory Assault", "Complete Stage 2 while soldiers are gunning for you", 5, 1),
    (608418, "Terror in the Eerie Light", "Complete Stage 3 and survive the alien ambush in the sewers", 5, 2),
    (608419, "Grim Castle Siege", "Complete Stage 4 and dismantle the horde of violent robot soldiers", 5, 3),
]

for a_id, title, desc, pts, stage_val in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.PROGRESSION)
    ach.add_core([
        reset_if(mem_state == 0x93),
        (mem_stage == stage_val),
        (mem_state.delta() == 0xdb).with_hits(1),
        (mem_state == 0xb6),
    ])
    my_set.add_achievement(ach)

# Win Condition:
ach = Achievement(id=608420, title="A New Breed", description="Complete Stage 5 aboard the space station and save the Earth", points=10, type=AchievementType.WIN_CONDITION)
ach.add_core([
    reset_if(mem_state == 0x93),
    (mem_stage.delta() == 0x04).with_hits(1),
    (mem_state.delta() == 0xdb).with_hits(1),
    (mem_state == 0xb6),
])
my_set.add_achievement(ach)


# 3. HIT STAGES (Desafios)
hit_stage_data = [
    (608422, "Street Justice", "Knock out the delinquent and save the woman in Hit Stage 1", 1, 0, byte(0x0018ea)),
    (608423, "Highway Hero", "Stop the runaway truck and save the child in Hit Stage 2", 2, 1, byte(0x0018eb)),
    (608424, "Controlled Demolition", "Demolish the building to save the city in Hit Stage 3", 2, 2, byte(0x0018ec)),
    (608425, "Monstrous Catch", "Take down the giant red crab monster in Hit Stage 4", 2, 3, byte(0x0018ed)),
    (608426, "Planetary Defense", "Destroy the meteor heading towards Earth in Hit Stage 5", 3, 4, byte(0x0018ee)),
]

for a_id, title, desc, pts, hit_id, flag_mem in hit_stage_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_hit_id == hit_id),
        (flag_mem.delta() == 0x01),
        (mem_hit_state == 0x03),
        (mem_hit_score > mem_hit_score.delta()),
    ])
    my_set.add_achievement(ach)


# 4. PONTUAÇÃO (SCORE)
score_data = [
    (608428, "Rookie Striker", "Reach 100,000 points", 5, 0x10),
    (608429, "Seasoned Fighter", "Reach 300,000 points", 5, 0x30),
    (608430, "Heavy Hitter", "Reach 500,000 points", 10, 0x50),
]

for a_id, title, desc, pts, target_low in score_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_score_h.delta() == 0x00),
        (mem_score_l.delta() < target_low),
        or_next(mem_score_h > 0x00),
        (mem_score_l >= target_low),
    ])
    my_set.add_achievement(ach)

# 1 Milhão (Blast Man Prime)
ach = Achievement(id=608431, title="Blast Man Prime", description="Reach 1,000,000 points", points=25)
ach.add_core([
    reset_if(mem_state == 0x93),
    (mem_state == 0xc7).with_hits(1),
    (mem_score_h.delta() == 0x00),
    (mem_score_h >= 0x01),
])
my_set.add_achievement(ach)


# 5. BOSS RUSH
boss_rush_data = [
    (608439, "The Outlaw Giant", "Defeat the first boss on Hard or Very Hard in Boss Rush mode", 10, 0, 1),
    (608440, "Razor-Sharp Duo", "Defeat the second boss on Hard or Very Hard in Boss Rush mode", 25, 1, 2),
    (608441, "Hatching Menace", "Defeat the third boss on Hard or Very Hard in Boss Rush mode", 10, 2, 3),
    (608442, "Missile Behemoth", "Defeat the fourth boss on Hard or Very Hard in Boss Rush mode", 10, 3, 4),
    (608443, "The Shadow Blast", "Defeat the fifth boss on Hard or Very Hard in Boss Rush mode", 25, 4, 5),
]

for a_id, title, desc, pts, prev_boss, next_boss in boss_rush_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        reset_if(mem_state == 0xcc),
        (mem_mode == 0x0a),
        (mem_diff >= 0x02),
        (mem_state == 0xdb).with_hits(1),
        (mem_stage.delta() == prev_boss),
        trigger(mem_stage == next_boss),
    ])
    my_set.add_achievement(ach)


# 6. ESPECÍFICOS & MISSABLES

# 1-UP Brawler
ach = Achievement(id=608427, title="1-UP Brawler", description="Collect a 1-UP item during normal stage gameplay", points=5)
ach.add_core([(mem_state == 0xc7), (mem_state.delta() == 0xc7), (mem_lives > mem_lives.delta())])
my_set.add_achievement(ach)

# No Alien Left Behind
ach = Achievement(id=608421, title="No Alien Left Behind", description="Reach and defeat the Stage 5 Boss by intentionally taking the most heavily guarded path (Normal or higher)", points=10, type=AchievementType.MISSABLE)
ach.add_core([
    (mem_diff >= 0x01),
    or_next((mem_stage == 0x05).with_hits(1)),
    pause_if((mem_stage == 0x06).with_hits(1)),
    (mem_stage == 0x04).with_hits(1),
    (mem_stage.delta() == 0x07).with_hits(1),
    trigger(mem_state == 0xb6),
])
ach.add_alt([
    or_next(mem_state == 0x93),
    reset_if(mem_state == 0xcc),
])
my_set.add_achievement(ach)

# Perfect Impact
ach = Achievement(id=608432, title="Perfect Impact", description="Land a 100% power punch", points=50)
ach.add_core([(mem_state == 0xd0), (mem_power == 0x6f), (mem_100t.delta() == 0x00), (mem_100t >= 0x01)])
my_set.add_achievement(ach)

# Triple Threat
ach = Achievement(id=608433, title="Triple Threat", description="Land three punches of 100t or more in any Hit Stage", points=10)
ach.add_core([
    reset_if(mem_state != 0xd0),
    or_next(byte(0x0018a8) == 0x01),
    (mem_mode == 0x09),
    (mem_state == 0xd0),
    and_next(mem_hit_state == 0x01),
    (mem_100t >= 0x01).with_hits(1),
    and_next(mem_hit_state.delta() == 0x02),
    (mem_100t >= 0x01).with_hits(1),
    and_next(mem_hit_state == 0x03),
    (mem_100t >= 0x01).with_hits(1),
])
my_set.add_achievement(ach)

# Unstoppable Force
ach = Achievement(id=608434, title="Unstoppable Force", description="Land three punches of 100t or more in Hit Stage 5", points=25)
ach.add_core([
    reset_if(mem_hit_id != 0x04),
    (byte(0x0018ee) == 0x01),
    and_next(mem_hit_state == 0x01),
    (mem_100t >= 0x01).with_hits(1),
    and_next(mem_hit_state.delta() == 0x02),
    (mem_100t >= 0x01).with_hits(1),
    and_next(mem_hit_state == 0x03),
    trigger((mem_100t >= 0x01).with_hits(1)),
])
my_set.add_achievement(ach)

# Conserving Energy
ach = Achievement(id=608435, title="Conserving Energy", description="Complete any level without using the D-Punch (Normal or higher)", points=10)
ach.add_core([
    pause_if((mem_dpunch < mem_dpunch.delta()).with_hits(1)),
    (mem_diff >= 0x01),
    (mem_state == 0xc7).with_hits(1),
    trigger((mem_state.delta() == 0xdb).with_hits(1)),
    trigger(mem_state == 0xb6),
])
ach.add_alt([
    or_next(mem_state == 0xcc),
    reset_if(mem_state == 0x93),
])
my_set.add_achievement(ach)

# Hardened Hero
ach = Achievement(id=608436, title="Hardened Hero", description="Complete the entire game on Hard mode or higher", points=25)
ach.add_core([
    (mem_diff >= 0x02),
    or_next(mem_stage.delta() == 0x08),
    (mem_stage.delta() == 0x06),
    trigger(mem_stage == 0x04),
])
my_set.add_achievement(ach)

# Funções auxiliares para os Desafios de Option Mode
def option_mode_ach(a_id, title, desc, pts, target_mode):
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        reset_if(mem_mode != target_mode),
        (mem_diff == 0x03),
        (mem_mode.delta() == 0x00).with_hits(1),
        (mem_mode == target_mode),
        trigger(mem_state == 0xb8),
    ])
    my_set.add_achievement(ach)

option_mode_ach(608437, "Mechanical Mayhem", "Complete Stage 4 on Very Hard mode starting from the Stage Select in Option Mode", 10, 0x03)
option_mode_ach(608438, "The Ultimate Blast", "Complete Stage 5 on Very Hard mode starting from the Stage Select in Option Mode", 25, 0x04)

my_set.save()