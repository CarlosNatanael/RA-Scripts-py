from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=2428, title="Batman: The Animated Series")

# 1. ALIASES DE MEMÓRIA
mem_mode         = byte(0x003d9c) # 0x13 In-Game / 0x14 Menus
mem_level        = byte(0x003da8) # Level ID
mem_adv_mode     = byte(0x003db8) # Advanced Mode Flag

mem_boss_hp_a    = byte(0x004332) # HP do Chefe (Normal)
mem_boss_hp_b    = byte(0x004260) # HP do Chefe (Final / Blimp)

mem_player_hp    = byte(0x004331) # HP do Batman
mem_robin_dmg    = byte(0x0000e8) # Flag de Dano do Robin
mem_dmg_flag     = byte(0x00426e) # Flag de Dano Geral (Veículos)
mem_state_22     = byte(0x000022) # Flag de Estado Extra

mem_timer_m      = byte(0x004312) # Tempo - Minutos
mem_timer_s10    = byte(0x004311) # Tempo - Segundos (Dezenas)
mem_timer_s1     = byte(0x004310) # Tempo - Segundos (Unidades)

mem_timer_b_m    = byte(0x0000ec) # Tempo Alternativo - Min
mem_timer_b_s10  = byte(0x0000eb) # Tempo Alternativo - Seg 10

mem_batcrawler_st = byte(0x0000e5)
mem_batcrawler_pw = byte(0x00033d)
mem_bat_flag_1   = byte(0x0000e0)
mem_bat_flag_2   = byte(0x0000e9)
mem_bat_flag_3   = byte(0x000210)

mem_batarangs    = byte(0x000021)
mem_batarangs2   = byte(0x0000e1)

mem_no_punch     = byte(0x003e13)
mem_no_charge    = byte(0x003e15) # Compartilhado (Charge e Shield)

# 2. BLOCOS REUTILIZÁVEIS
cond_mode = [
    or_next(mem_mode == 0x13),
    reset_if(mem_mode == 0x14)
]

cond_15s = [
    or_next(mem_timer_m.delta() >= 1),
    or_next(mem_timer_s10.delta() >= 2),
    and_next(mem_timer_s10.delta() == 1),
    (mem_timer_s1.delta() >= 5),
]

# 3. PROGRESSÃO (DERROTAR CHEFES)
prog_data = [
    (604738, "The Joker's Last Jest", "Complete levels 1 through 4 and defeat The Joker", 5, "686921", 0x00, 0x03, mem_boss_hp_a, 0x18, AchievementType.PROGRESSION),
    (604739, "Deep Freeze", "Complete levels 5 through 10 and defeat Mr. Freeze", 5, "686922", 0x04, 0x09, mem_boss_hp_a, 0x09, AchievementType.PROGRESSION),
    (604740, "Green Thumbs, Cold Hearts", "Complete levels 11 through 16 and defeat Poison Ivy", 5, "686923", 0x0a, 0x0f, mem_boss_hp_a, 0x08, AchievementType.PROGRESSION),
    (604741, "Vengeance in the Night", "Complete levels 17 through 21 and finish the game", 10, "686924", 0x10, 0x14, mem_boss_hp_b, 0x98, AchievementType.WIN_CONDITION),
]

for a_id, title, desc, pts, badge, l_start, l_end, boss_mem, max_hp, a_type in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=a_type)
    ach.add_core([
        *cond_mode,
        (mem_level == l_start).with_hits(1),
        (mem_level == l_end).with_hits(1),
        (boss_mem == max_hp).with_hits(1),
        (boss_mem == 0),
        (boss_mem.delta() != 0),
    ])
    my_set.add_achievement(ach)

# 4. CHEFES SEM DANO
boss_dl_data = [
    (604742, "An Unfunny Joke", "Defeat The Joker in level 4 without taking damage", 5, "686925", 0x03, mem_boss_hp_a, 0x18),
    (604743, "Absolute Zero", "Defeat Mr. Freeze in level 10 without taking damage", 10, "686926", 0x09, mem_boss_hp_a, 0x09),
    (604744, "Natural Selection", "Defeat Poison Ivy in level 16 without taking damage", 10, "686927", 0x0f, mem_boss_hp_a, 0x08),
    (604745, "Mad Love Overturned", "Defeat Harley Quinn in level 19 without taking damage", 25, "686928", 0x12, mem_boss_hp_a, 0x0a),
]

for a_id, title, desc, pts, badge, lvl, boss_mem, max_hp in boss_dl_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_level == lvl),
        (boss_mem == max_hp).with_hits(1),
        reset_if(mem_player_hp != 0x0c),
        trigger(boss_mem == 0),
        (boss_mem.delta() != 0),
    ])
    my_set.add_achievement(ach)

# 604746: Único porque verifica a delta do HP do jogador em vez do 0x0c fixo
ach = Achievement(id=604746, title="The Final Punchline", description="Defeat The Joker in level 20 without taking damage", points=50, badge="686929")
ach.add_core([
    (mem_level == 0x13),
    (mem_boss_hp_a == 0x18).with_hits(1),
    pause_if((mem_player_hp < mem_player_hp.delta()).with_hits(1)),
    trigger(mem_boss_hp_a == 0x00),
    (mem_boss_hp_a.delta() != 0x00),
])
ach.add_alt([
    or_next(mem_level != 0x13),
    reset_if(mem_player_hp == 0x00),
])
my_set.add_achievement(ach)

# 5. DYNAMIC DUO (ROBIN SEM DANO)
robin_dl_data = [
    (604747, "Dynamic Duo: Bridge Mission", "Complete level 6 as Robin without taking damage", 5, "686930", 0x05),
    (604748, "Dynamic Duo: Cold Pursuit", "Complete level 7 as Robin without taking damage", 10, "686931", 0x06),
    (604750, "Dynamic Duo: Ivy's Lair", "Complete level 14 as Robin without taking damage", 25, "686933", 0x0d),
]

for a_id, title, desc, pts, badge, lvl in robin_dl_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        and_next(mem_level == lvl),
        and_next(mem_level == mem_level.delta()),
        reset_next_if(mem_robin_dmg == 0),
        pause_if((mem_robin_dmg < mem_robin_dmg.delta()).with_hits(1)), # CORRIGIDO AQUI!
        trigger(mem_level == lvl + 1),
        (mem_level.delta() == lvl),
    ])
    my_set.add_achievement(ach)

# 6. BATCRAWLER (PASSWORDS SECRETOS)
batcrawler_data = [
    (604749, "One-Take Hacker", "Find the secret password on your first attempt in level 7 using the Batcrawler and without taking damage", 3, "686932", 0x06),
    (604751, "Root Access", "Find the secret password on your first attempt in level 14 using the Batcrawler and without taking damage", 5, "686934", 0x0d),
]

for a_id, title, desc, pts, badge, lvl in batcrawler_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        or_next(mem_bat_flag_1 == 1),
        and_next(mem_batcrawler_st == 0),
        pause_if((mem_robin_dmg < mem_robin_dmg.delta()).with_hits(1)),
        (mem_level == lvl),
        (mem_bat_flag_2 == 1).with_hits(1),
        (mem_batcrawler_pw == 0x7b).with_hits(1),
        trigger(mem_batcrawler_st == 0),
        (mem_batcrawler_st.delta() == 1),
    ])
    ach.add_alt([
        or_next(mem_bat_flag_3 == 0),
        reset_if(mem_robin_dmg == 0),
    ])
    my_set.add_achievement(ach)

# 7. DESAFIOS DE TEMPO
ach = Achievement(id=604752, title="Knight Rider", description="Complete level 3 with at least 20 seconds remaining", points=5, badge="686935")
ach.add_core([
    or_next(mem_timer_m.delta() >= 1),
    (mem_timer_s10.delta() >= 2),
    trigger(mem_level == 0x03),
    (mem_level.delta() == 0x02),
])
my_set.add_achievement(ach)

ach = Achievement(id=604753, title="Asphalt Vigilante", description="Complete level 8 with at least 15 seconds remaining", points=10, badge="686936")
ach.add_core([
    *cond_15s,
    trigger(mem_level == 0x08),
    (mem_level.delta() == 0x07),
])
my_set.add_achievement(ach)

ach = Achievement(id=604754, title="Bat out of Hell", description="Complete level 11 with at least 15 seconds remaining", points=10, badge="686937")
ach.add_core([
    or_next(mem_timer_m.delta() > 0),
    or_next(mem_timer_s10.delta() >= 2),
    and_next(mem_timer_s10.delta() == 1),
    (mem_timer_s1.delta() >= 5),
    trigger(mem_level == 0x0b),
    (mem_level.delta() == 0x0a),
])
my_set.add_achievement(ach)

ach = Achievement(id=604762, title="Dev Time: Binary Detective", description="Complete level 3 with at least 30 seconds remaining in Advanced Mode", points=10, badge="686945")
ach.add_core([
    (mem_adv_mode == 1),
    or_next(mem_timer_b_m.delta() > 0),
    (mem_timer_b_s10.delta() >= 3),
    trigger(mem_level == 0x18),
    (mem_level.delta() == 0x17),
])
my_set.add_achievement(ach)

# 8. FASES DE VEÍCULOS SEM DANO
ach = Achievement(id=604755, title="Skyline Protector", description="Complete level 5 without taking damage", points=10, badge="686938")
ach.add_core([
    or_next(mem_level != 0x04),
    reset_next_if(mem_dmg_flag == 0),
    pause_if((mem_dmg_flag < 0x0c).with_hits(1)),
    trigger(mem_level == 0x05),
    (mem_level.delta() == 0x04),
])
my_set.add_achievement(ach)

ach = Achievement(id=604756, title="Aerial Dominance", description="Complete level 13 without taking damage", points=25, badge="686939")
ach.add_core([
    or_next(mem_level != 0x0c),
    reset_next_if(mem_dmg_flag == 0),
    pause_if((mem_dmg_flag < 0x0c).with_hits(1)),
    trigger(mem_level == 0x0d),
    (mem_level.delta() == 0x0c),
])
my_set.add_achievement(ach)

ach = Achievement(id=604757, title="Punctured Punchline", description="Blow up The Joker's blimp without taking damage", points=5, badge="686940")
ach.add_core([
    pause_if((mem_dmg_flag < 0x0c).with_hits(1)),
    (mem_level == 0x14),
    (mem_boss_hp_b == 0x98).with_hits(1),
    trigger(mem_boss_hp_b == 0),
    (mem_boss_hp_b.delta() != 0),
])
ach.add_alt([
    or_next(mem_level != 0x14),
    reset_if(mem_dmg_flag == 0),
])
my_set.add_achievement(ach)

# 9. MODO AVANÇADO E MISC
adv_data = [
    (604758, "Data Retrieval: Rookie", "Complete levels 1 through 5 in Advanced Mode", 5, "686941", 0x15, 0x1a, 0x19),
    (604759, "Data Retrieval: Veteran", "Complete levels 6 through 10 in Advanced Mode", 10, "686942", 0x1a, 0x1f, 0x1e),
    (604760, "Data Retrieval: Master", "Complete levels 11 through 16 in Advanced Mode", 25, "686943", 0x1f, 0xff, 0x24),
]

for a_id, title, desc, pts, badge, l_start, l_end, l_delta in adv_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        *cond_mode,
        (mem_adv_mode == 1),
        (mem_level == l_start).with_hits(1),
        (mem_level == l_end),
        (mem_level.delta() == l_delta).with_hits(1),
    ])
    my_set.add_achievement(ach)

# Utility Belt Master
ach = Achievement(id=604761, title="Utility Belt Master", description="Reach the maximum capacity of 9 Batarangs", points=1, badge="686944")
ach.add_core([ (value(0x00) == 0x00) ])
ach.add_alt([
    (mem_batarangs == 9),
    (mem_batarangs.delta() < 9),
])
ach.add_alt([
    (mem_batarangs2 == 9),
    (mem_batarangs2.delta() < 9),
])
my_set.add_achievement(ach)

# 10. RESTRIÇÕES (SEM ATAQUE/TIRO)
ach = Achievement(id=604763, title="Shadow Ninja", description="Complete level 2 without punching or kicking in Story Mode", points=10, badge="686946")
ach.add_core([
    pause_if((mem_state_22 == 0xff)),
    pause_if((mem_no_punch == 1).with_hits(1)),
    (mem_adv_mode == 0),
    trigger(mem_level == 0x02),
    (mem_level.delta() == 0x01).with_hits(1),
])
ach.add_alt([
    and_next(mem_level != 0x01),
    reset_if(mem_level != 0x02),
    or_next(mem_mode == 0x14),
    reset_if(mem_mode == 0x13),
])
my_set.add_achievement(ach)

ach = Achievement(id=604764, title="Defensive Driving", description="Complete level 3 without firing your electric charge in Story Mode", points=3, badge="686947")
ach.add_core([
    pause_if((mem_no_charge == 1).with_hits(1)),
    (mem_adv_mode == 0),
    trigger(mem_level == 0x03),
    (mem_level.delta() == 0x02).with_hits(1),
])
ach.add_alt([
    and_next(mem_level != 0x02),
    reset_if(mem_level != 0x03),
    or_next(mem_mode == 0x14),
    reset_if(mem_mode == 0x13),
])
my_set.add_achievement(ach)

ach = Achievement(id=604765, title="Reckless Pilot", description="Complete level 5 without activating your shield in Story Mode", points=5, badge="686948")
ach.add_core([
    pause_if((mem_no_charge == 1).with_hits(1)),
    (mem_adv_mode == 0),
    trigger(mem_level == 0x05),
    (mem_level.delta() == 0x04).with_hits(1),
])
ach.add_alt([
    and_next(mem_level != 0x04),
    reset_if(mem_level != 0x05),
    or_next(mem_mode == 0x14),
    reset_if(mem_mode == 0x13),
])
my_set.add_achievement(ach)

my_set.save()