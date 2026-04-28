from pycheevos.core.helpers import byte, or_next, and_next, reset_if, reset_next_if, pause_if, trigger, value
from pycheevos.core.constants import AchievementType
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=2428, title="Imported Set")


# 1. ALIAS DE MEMÓRIA (Chega de números mágicos)

mem_screen   = byte(0x3d9c)
mem_mode     = byte(0x3db8)
mem_level    = byte(0x3da8)

boss_hp      = byte(0x4332)
boss_hp_alt  = byte(0x4260)
player_hp    = byte(0x4331)
robin_hp     = byte(0x00e8)
batplane_hp  = byte(0x426e)

timer_min    = byte(0x4312)
timer_sec    = byte(0x4311)
timer_ms     = byte(0x4310)

adv_timer_s  = byte(0x00eb)
adv_timer_ms = byte(0x00ec)


# 2. STORY MODE: PROGRESSÃO (Bosses)

# (ID, Title, Desc, Pts, Type, lvl_start, lvl_end, hp_addr, hp_max)
progression_data = [
    (604738, "Joker's Last Jest", "Complete levels 1-4 and defeat the Joker on the bridge", 5, AchievementType.PROGRESSION, 0x00, 0x03, boss_hp, 0x18),
    (604739, "Deep Freeze", "Complete levels 5-10 and defeat Mr. Freeze", 5, AchievementType.PROGRESSION, 0x04, 0x09, boss_hp, 0x09),
    (604740, "Green Thumbs, Cold Hearts", "Complete levels 11-16 and defeat Poison Ivy", 5, AchievementType.PROGRESSION, 0x0a, 0x0f, boss_hp, 0x08),
    (604741, "Vengeance in the Night", "Complete levels 17-21 and finish the game", 10, AchievementType.WIN_CONDITION, 0x10, 0x14, boss_hp_alt, 0x98),
]

for a_id, title, desc, pts, a_type, lvl_start, lvl_end, hp_addr, hp_max in progression_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=a_type)
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


# 3. STORY MODE: BOSSES SEM TOMAR DANO

# (ID, Title, Desc, Pts, Level, hp_addr, hp_max)
damageless_bosses = [
    (604742, "Unfunny Joke", "Defeat the Joker in Level 4 without taking damage", 5, 0x03, boss_hp, 0x18),
    (604743, "Absolute Zero", "Defeat Mr. Freeze in Level 10 without taking damage", 10, 0x09, boss_hp, 0x09),
    (604744, "Natural Selection", "Defeat Poison Ivy in Level 16 without taking damage", 10, 0x0f, boss_hp, 0x08),
    (604745, "Mad Love Overturned", "Defeat Harley Quinn in Level 19 without taking damage", 25, 0x12, boss_hp, 0x0a),
    (604746, "The Final Punchline", "Defeat the final Joker in Level 20 without taking damage", 50, 0x13, boss_hp, 0x18),
]

for a_id, title, desc, pts, lvl, hp_addr, hp_max in damageless_bosses:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_level == lvl),
        (hp_addr == hp_max).with_hits(1),
        reset_if(player_hp != 0x0c),
        trigger(hp_addr == 0x00),
        (hp_addr.delta() != 0x00)
    ])
    my_set.add_achievement(ach)


# 4. STORY MODE: ROBIN (Dynamic Duo)

# (ID, Title, Desc, Pts, cur_lvl, next_lvl)
robin_levels = [
    (604747, "Dynamic Duo: Bridge Mission", "Complete Level 6 as Robin without taking damage", 5, 0x05, 0x06),
    (604748, "Dynamic Duo: Cold Pursuit", "Complete Level 7 as Robin without taking damage", 10, 0x06, 0x07),
    (604750, "Dynamic Duo: Ivy's Lair", "Complete Level 14 as Robin without taking damage", 25, 0x0d, 0x0f),
]

for a_id, title, desc, pts, cur_lvl, next_lvl in robin_levels:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        and_next(mem_level == cur_lvl),
        and_next(mem_level == mem_level.delta()),
        reset_next_if(robin_hp == 0x00),
        pause_if((robin_hp < 0x0c).with_hits(1)),
        trigger(mem_level == next_lvl),
        (mem_level.delta() == cur_lvl)
    ])
    my_set.add_achievement(ach)


# 5. BATCRAWLER: HACKERS (Mesma lógica do Alt)

hackers = [
    (604749, "One-Take Hacker", "Retrieve the secret password using the Batcrawler on your first attempt without taking damage in Level 7", 3, 0x06),
    (604751, "Root Access", "Retrieve the secret password using the Batcrawler on your first attempt without taking damage in Level 14", 5, 0x0d)
]

for a_id, title, desc, pts, lvl in hackers:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
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

# (ID, Title, Desc, Pts, hit_lvl, end_lvl, delta_lvl)
adv_progression = [
    (604758, "Data Retrieval: Rookie", "Complete Advanced Mode Levels 1 through 5", 5, 0x15, 0x1a, 0x19),
    (604759, "Data Retrieval: Veteran", "Complete Advanced Mode Levels 6 through 10", 10, 0x1a, 0x1f, 0x1e),
    (604760, "Data Retrieval: Master", "Complete Advanced Mode Levels 11 through 16", 25, 0x1f, 0xff, 0x24),
]

for a_id, title, desc, pts, hit_lvl, end_lvl, delta_lvl in adv_progression:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        or_next(mem_screen == 0x13),
        reset_if(mem_screen == 0x14),
        (mem_mode == 0x01),
        (mem_level == hit_lvl).with_hits(1),
        (mem_level == end_lvl),
        (mem_level.delta() == delta_lvl).with_hits(1)
    ])
    my_set.add_achievement(ach)


# 7. MANUAIS: TIMERS, VEÍCULOS E DESAFIOS ESPECÍFICOS

# Knight Rider
ach = Achievement(id=604752, title="Knight Rider", description="Complete Level 3 with 20 seconds...", points=5)
ach.add_core([or_next(timer_min.delta() >= 0x01), (timer_sec.delta() >= 0x02), trigger(mem_level == 0x03), (mem_level.delta() == 0x02)])
my_set.add_achievement(ach)

# Asphalt Vigilante
ach = Achievement(id=604753, title="Asphalt Vigilante", description="Complete Level 8 with 15 seconds...", points=10)
ach.add_core([or_next(timer_min.delta() >= 0x01), or_next(timer_sec.delta() >= 0x02), and_next(timer_sec.delta() == 0x01), (timer_ms.delta() >= 0x05), trigger(mem_level == 0x08), (mem_level.delta() == 0x07)])
my_set.add_achievement(ach)

# Bat-Out-of-Hell
ach = Achievement(id=604754, title="Bat-Out-of-Hell", description="Complete Level 11 with 15 seconds...", points=10)
ach.add_core([or_next(timer_min.delta() > 0x00), or_next(timer_sec.delta() >= 0x02), and_next(timer_sec.delta() == 0x01), (timer_ms.delta() >= 0x05), trigger(mem_level == 0x0b), (mem_level.delta() == 0x0a)])
my_set.add_achievement(ach)

# Skyline Protector
ach = Achievement(id=604755, title="Skyline Protector", description="Complete Level 5 without taking damage", points=10)
ach.add_core([or_next(mem_level != 0x04), reset_next_if(batplane_hp == 0x00), pause_if((batplane_hp < 0x0c).with_hits(1)), trigger(mem_level == 0x05), (mem_level.delta() == 0x04)])
my_set.add_achievement(ach)

# Aerial Dominance
ach = Achievement(id=604756, title="Aerial Dominance", description="Complete Level 13 without taking damage", points=25)
ach.add_core([or_next(mem_level != 0x0c), reset_next_if(batplane_hp == 0x00), pause_if((batplane_hp < 0x0c).with_hits(1)), trigger(mem_level == 0x0d), (mem_level.delta() == 0x0c)])
my_set.add_achievement(ach)

# Punctured Punchline
ach = Achievement(id=604757, title="Punctured Punchline", description="Destroy the Joker's dirigible without taking damage", points=5)
ach.add_core([pause_if((batplane_hp < 0x0c).with_hits(1)), (mem_level == 0x14), (boss_hp_alt == 0x98).with_hits(1), trigger(boss_hp_alt == 0x00), (boss_hp_alt.delta() != 0x00)])
ach.add_alt([or_next(mem_level != 0x14), reset_if(batplane_hp == 0x00)])
my_set.add_achievement(ach)

# Utility Belt Master
ach = Achievement(id=604761, title="Utility Belt Master", description="Reach the maximum capacity of 9 Batarangs", points=1)
ach.add_core([(value(0) == 0)])
ach.add_alt([(byte(0x21) == 0x09), (byte(0x21).delta() < 0x09)])
ach.add_alt([(byte(0xe1) == 0x09), (byte(0xe1).delta() < 0x09)])
my_set.add_achievement(ach)

# Dev Time: Binary Detective
ach = Achievement(id=604762, title="Dev Time: Binary Detective", description="Complete Adv Level 3 with 30s+", points=10)
ach.add_core([(mem_mode == 0x01), or_next(adv_timer_ms.delta() > 0x00), (adv_timer_s.delta() >= 0x03), trigger(mem_level == 0x18), (mem_level.delta() == 0x17)])
my_set.add_achievement(ach)

# Shadow Ninja
ach = Achievement(id=604763, title="Shadow Ninja", description="Level 2 without throwing a punch/kick", points=2)
ach.add_core([pause_if((byte(0x3e13) == 0x01).with_hits(1)), (mem_mode == 0x00), trigger(mem_level == 0x02), (mem_level.delta() == 0x01).with_hits(1)])
ach.add_alt([or_next(mem_screen == 0x14), reset_if(mem_screen == 0x13)])
my_set.add_achievement(ach)

# Defensive Driving
ach = Achievement(id=604764, title="Defensive Driving", description="Level 3 without electric charge", points=3)
ach.add_core([pause_if((byte(0x3e15) == 0x01).with_hits(1)), (mem_mode == 0x00), trigger(mem_level == 0x03), (mem_level.delta() == 0x02).with_hits(1)])
ach.add_alt([or_next(mem_screen == 0x14), reset_if(mem_screen == 0x13)])
my_set.add_achievement(ach)

# Reckless Pilot
ach = Achievement(id=604765, title="Reckless Pilot", description="Level 5 without shield", points=5)
ach.add_core([pause_if((byte(0x3e15) == 0x01).with_hits(1)), (mem_mode == 0x00), trigger(mem_level == 0x06), (mem_level.delta() == 0x04).with_hits(1)])
ach.add_alt([or_next(mem_screen == 0x14), reset_if(mem_screen == 0x13)])
my_set.add_achievement(ach)

my_set.save()