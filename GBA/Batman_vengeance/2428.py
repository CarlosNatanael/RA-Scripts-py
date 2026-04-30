from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=2428, title="Imported Set")


# 1. ALIAS DE MEMÓRIA (O Fim dos Números Mágicos)
mem_screen   = byte(0x3d9c)
mem_mode     = byte(0x3db8)
mem_level    = byte(0x3da8)

boss_hp      = byte(0x4332)
boss_hp_alt  = byte(0x4260) # Usado pelo Joker's Blimp
player_hp    = byte(0x4331)
robin_hp     = byte(0x00e8)
batplane_hp  = byte(0x426e)

timer_min    = byte(0x4312)
timer_sec    = byte(0x4311)
timer_ms     = byte(0x4310)

adv_timer_s  = byte(0x00eb)
adv_timer_ms = byte(0x00ec)

belt_batman  = byte(0x0021)
belt_robin   = byte(0x00e1)

# 2. STORY MODE: PROGRESSÃO

progression_data = [
    (604738, "The Joker's Last Jest", "Complete levels 1 through 4 and defeat The Joker", 5, "686921", AchievementType.PROGRESSION, 0x00, 0x03, boss_hp, 0x18),
    (604739, "Deep Freeze", "Complete levels 5 through 10 and defeat Mr. Freeze", 5, "686922", AchievementType.PROGRESSION, 0x04, 0x09, boss_hp, 0x09),
    (604740, "Green Thumbs, Cold Hearts", "Complete levels 11 through 16 and defeat Poison Ivy", 5, "686923", AchievementType.PROGRESSION, 0x0a, 0x0f, boss_hp, 0x08),
    (604741, "Vengeance in the Night", "Complete levels 17 through 21 and finish the game", 10, "686924", AchievementType.WIN_CONDITION, 0x10, 0x14, boss_hp_alt, 0x98),
]

for a_id, title, desc, pts, badge, a_type, lvl_start, lvl_end, hp_addr, hp_max in progression_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=a_type)
    ach.add_core([
        or_next(mem_screen == 0x13),
        reset_if(mem_screen == 0x14),
        (mem_level == lvl_start).with_hits(1),
        (mem_level == lvl_end).with_hits(1),
        (hp_addr == hp_max).with_hits(1),
        (hp_addr == 0x00),
        (hp_addr.delta() != 0x00)
    ])
    my_set.add_achievement(ach)

# 3. STORY MODE: BOSSES SEM DANO

damageless_bosses = [
    (604742, "An Unfunny Joke", "Defeat The Joker in level 4 without taking damage", 5, "686925", 0x03, boss_hp, 0x18),
    (604743, "Absolute Zero", "Defeat Mr. Freeze in level 10 without taking damage", 10, "686926", 0x09, boss_hp, 0x09),
    (604744, "Natural Selection", "Defeat Poison Ivy in level 16 without taking damage", 10, "686927", 0x0f, boss_hp, 0x08),
    (604745, "Mad Love Overturned", "Defeat Harley Quinn in level 19 without taking damage", 25, "686928", 0x12, boss_hp, 0x0a),
    (604746, "The Final Punchline", "Defeat The Joker in level 20 without taking damage", 50, "686929", 0x13, boss_hp, 0x18),
]

for a_id, title, desc, pts, badge, lvl, hp_addr, hp_max in damageless_bosses:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_level == lvl),
        (hp_addr == hp_max).with_hits(1),
        reset_if(player_hp != 0x0c),
        trigger(hp_addr == 0x00),
        (hp_addr.delta() != 0x00)
    ])
    my_set.add_achievement(ach)

# 4. STORY MODE: ROBIN (DYNAMIC DUO)

robin_levels = [
    (604747, "Dynamic Duo: Bridge Mission", "Complete level 6 as Robin without taking damage", 5, "686930", 0x05, 0x06),
    (604748, "Dynamic Duo: Cold Pursuit", "Complete level 7 as Robin without taking damage", 10, "686931", 0x06, 0x07),
    (604750, "Dynamic Duo: Ivy's Lair", "Complete level 14 as Robin without taking damage", 25, "686933", 0x0d, 0x0f),
]

for a_id, title, desc, pts, badge, cur_lvl, next_lvl in robin_levels:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        and_next(mem_level == cur_lvl),
        and_next(mem_level == mem_level.delta()),
        reset_next_if(robin_hp == 0x00),
        pause_if((robin_hp < 0x0c).with_hits(1)),
        trigger(mem_level == next_lvl),
        (mem_level.delta() == cur_lvl)
    ])
    my_set.add_achievement(ach)

# 5. HACKERS (BATCRAWLER)

hackers = [
    (604749, "One-Take Hacker", "Find the secret password on your first attempt in level 7 using the Batcrawler and without taking damage", 3, "686932", 0x06),
    (604751, "Root Access", "Find the secret password on your first attempt in level 14 using the Batcrawler and without taking damage", 5, "686934", 0x0d)
]

for a_id, title, desc, pts, badge, lvl in hackers:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        or_next(byte(0x00e0) == 0x01),
        and_next(byte(0x00e5) == 0x00),
        pause_if((robin_hp < robin_hp.delta()).with_hits(1)),
        (mem_level == lvl),
        (byte(0x00e9) == 0x01).with_hits(1),
        (byte(0x033d) == 0x7b).with_hits(1),
        trigger(byte(0x00e5) == 0x00),
        (byte(0x00e5).delta() == 0x01)
    ])
    ach.add_alt([
        or_next(byte(0x0210) == 0x00),
        reset_if(robin_hp == 0x00)
    ])
    my_set.add_achievement(ach)

# 6. ADVANCED MODE: DATA RETRIEVAL

adv_progression = [
    (604758, "Data Retrieval: Rookie", "Complete levels 1 through 5 in Advanced Mode", 5, "686941", 0x15, 0x1a, 0x19),
    (604759, "Data Retrieval: Veteran", "Complete levels 6 through 10 in Advanced Mode", 10, "686942", 0x1a, 0x1f, 0x1e),
    (604760, "Data Retrieval: Master", "Complete levels 11 through 16 in Advanced Mode", 25, "686943", 0x1f, 0xff, 0x24),
]

for a_id, title, desc, pts, badge, hit_lvl, end_lvl, delta_lvl in adv_progression:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        or_next(mem_screen == 0x13),
        reset_if(mem_screen == 0x14),
        (mem_mode == 0x01),
        (mem_level == hit_lvl).with_hits(1),
        (mem_level == end_lvl),
        (mem_level.delta() == delta_lvl).with_hits(1)
    ])
    my_set.add_achievement(ach)

# 7. CONQUISTAS ESPECÍFICAS / TIMERS

def create_timer_ach(a_id, title, desc, pts, badge, trigger_lvl, delta_lvl, is_adv=False):
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    if not is_adv:
        # Lógica base do timer do Story Mode
        logic = [
            or_next(timer_min.delta() > 0x00) if a_id == 604754 else or_next(timer_min.delta() >= 0x01),
            or_next(timer_sec.delta() >= 0x02) if a_id != 604752 else (timer_sec.delta() >= 0x02)
        ]
        if a_id != 604752: # Asphalt e Bat out of Hell têm MS
            logic.extend([and_next(timer_sec.delta() == 0x01), (timer_ms.delta() >= 0x05)])
    else:
        # Lógica do Dev Time (Advanced Mode)
        logic = [(mem_mode == 0x01), or_next(adv_timer_ms.delta() > 0x00), (adv_timer_s.delta() >= 0x03)]
    
    logic.extend([trigger(mem_level == trigger_lvl), (mem_level.delta() == delta_lvl)])
    ach.add_core(logic)
    my_set.add_achievement(ach)

create_timer_ach(604752, "Knight Rider", "Complete level 3 with at least 20 seconds remaining", 5, "686935", 0x03, 0x02)
create_timer_ach(604753, "Asphalt Vigilante", "Complete leve 8 with at least 15 seconds remaining", 10, "686936", 0x08, 0x07)
create_timer_ach(604754, "Bat out of Hell", "Complete level 11 with at least 15 seconds remaining", 10, "686937", 0x0b, 0x0a)
create_timer_ach(604762, "Dev Time: Binary Detective", "Complete level 3 with at least 30 seconds remaining in Advanced Mode", 10, "686945", 0x18, 0x17, True)

# Veículos Sem Dano
for a_id, title, desc, pts, badge, lvl, delta_lvl in [(604755, "Skyline Protector", "Complete level 5 without taking damage", 10, "686938", 0x05, 0x04), (604756, "Aerial Dominance", "Complete level 13 without taking damage", 25, "686939", 0x0d, 0x0c)]:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([or_next(mem_level != delta_lvl), reset_next_if(batplane_hp == 0x00), pause_if((batplane_hp < 0x0c).with_hits(1)), trigger(mem_level == lvl), (mem_level.delta() == delta_lvl)])
    my_set.add_achievement(ach)

# Punctured Punchline
ach = Achievement(id=604757, title="Punctured Punchline", description="Blow up The Joker's blimp without taking damage", points=5, badge="686940")
ach.add_core([pause_if((batplane_hp < 0x0c).with_hits(1)), (mem_level == 0x14), (boss_hp_alt == 0x98).with_hits(1), trigger(boss_hp_alt == 0x00), (boss_hp_alt.delta() != 0x00)])
ach.add_alt([or_next(mem_level != 0x14), reset_if(batplane_hp == 0x00)])
my_set.add_achievement(ach)

# Utility Belt Master
ach = Achievement(id=604761, title="Utility Belt Master", description="Reach the maximum capacity of 9 Batarangs", points=1, badge="686944")
ach.add_core([(value(0x00) == 0x00)])
ach.add_alt([(belt_batman == 0x09), (belt_batman.delta() < 0x09)])
ach.add_alt([(belt_robin == 0x09), (belt_robin.delta() < 0x09)])
my_set.add_achievement(ach)

# Desafios de Restrição (Story Mode)
restr_data = [
    (604763, "Shadow Ninja", "Complete level 2 without punching or kicking in Story Mode", 10, "686946", byte(0x3e13), 0x02, True),
    (604764, "Defensive Driving", "Complete level 3 without firing your electric charge in Story Mode", 3, "686947", byte(0x3e15), 0x03, False),
    (604765, "Reckless Pilot", "Complete level 5 without activating your shield in Story Mode", 5, "686948", byte(0x3e15), 0x06, False)
]

for a_id, title, desc, pts, badge, action_mem, lvl, is_ninja in restr_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    core_logic = []
    if is_ninja:
        core_logic.append(pause_if((byte(0x0022) == 0xff)))
    
    core_logic.extend([
        pause_if((action_mem == 0x01).with_hits(1)),
        (mem_mode == 0x00),
        trigger(mem_level == lvl),
        (mem_level.delta() == (lvl - 1)).with_hits(1) if is_ninja else (mem_level.delta() == (lvl - 1) if lvl == 0x03 else mem_level.delta() == 0x04).with_hits(1)
    ])
    
    alt_logic = []
    if is_ninja:
        alt_logic.extend([and_next((mem_level != 0x01)), reset_if((mem_level != 0x02))])
    alt_logic.extend([or_next((mem_screen == 0x14)), reset_if((mem_screen == 0x13))])
    
    ach.add_core(core_logic)
    ach.add_alt(alt_logic)
    my_set.add_achievement(ach)

my_set.save()