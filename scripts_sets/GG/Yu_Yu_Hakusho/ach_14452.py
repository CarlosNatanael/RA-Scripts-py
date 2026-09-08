from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=14452, title="Yu Yu Hakusho - Refactored")

# 1. ALIASES DE MEMÓRIA (E correção de escopo)
mem_stage      = byte(0x0150)
mem_boss_stage = byte(0x0e20)
mem_game_state = byte(0x0022)
mem_diff       = byte(0x001a)
mem_ending     = byte(0x0100)

mem_boss_state = byte(0x0e24)
mem_boss_hp    = byte(0x0e2a)
mem_player_hp  = byte(0x0e8b)
mem_spirit     = byte(0x0e8c)
mem_char       = byte(0x0016)
mem_continues  = byte(0x001e)
mem_score      = word(0x0010)

# 2. PROGRESSÃO DE MAPAS
prog_data = [
    (625647, "First Mission", "Clear Map A", 1, "711561", 0, bit0),
    (625648, "Urban Brawl", "Clear Map B", 2, "711562", 1, bit1),
    (625649, "City Limits", "Clear Map C", 2, "711563", 2, bit2),
    (625650, "Approaching the Stronghold", "Clear Map D", 3, "711564", 3, bit3),
]

for a_id, title, desc, pts, badge, stage_id, bit_func in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_stage == stage_id), (mem_boss_stage == stage_id),
        (bit_func(0x0155) == 0x01), (bit_func(0x0155).delta() == 0x00)
    ])
    my_set.add_achievement(ach)

# 3. ATAQUES ESPECIAIS NOS CHEFES (Bug do value(0) resolvido!)
boss_strike_data = [
    (625653, "Ooze Anatomy", "Strike the Slime Demon's Head with a Special Attack", 10, "711567", 0, 0x03),
    (625654, "Clipped Wings", "Strike the Bat Demon's Head with a Special Attack", 5, "711568", 1, 0x01),
    (625655, "System Override", "Strike the Giant Robot's Core with a Special Attack", 10, "711569", 2, 0x0b),
    (625656, "Extinguished", "Strike the Fire Demon's Head with a Special Attack", 5, "711570", 3, 0x01),
    (625657, "Green With Envy", "Strike the Green Demon's Head with a Special Attack", 5, "711571", 4, 0x03),
    (625658, "Regicide", "Strike the King Demon's Head with a Special Attack", 5, "711572", 5, 0x06),
]

for a_id, title, desc, pts, badge, stage_id, weak_point in boss_strike_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_game_state == 0x00), (mem_stage == stage_id), (mem_boss_stage == stage_id),
        reset_if(mem_boss_state != weak_point),
        trigger((mem_boss_hp < mem_boss_hp.delta()).with_hits(1)), 
        trigger((mem_spirit < mem_spirit.delta()).with_hits(1)),
    ])
    my_set.add_achievement(ach)

# 4. DESAFIOS DAMAGELESS & NO SPIRIT POWER
def get_map_win_condition(bit_func):
    return [trigger(bit_func(0x0155) == 0x01), (bit_func(0x0155).delta() == 0x00)]

dmg_spirit_data = [
    (625659, "Squeaky Clean", "Defeat the Slime Demon without taking any damage", 10, "711573", 0, mem_player_hp, get_map_win_condition(bit0)),
    (625660, "Echo Evasion", "Defeat the Bat Demon without taking any damage", 10, "711574", 1, mem_player_hp, get_map_win_condition(bit1)),
    (625661, "Perfect Dismantle", "Defeat the Giant Robot without taking any damage", 10, "711575", 2, mem_player_hp, get_map_win_condition(bit2)),
    (625662, "Unscorched", "Defeat the Fire Demon without taking any damage", 25, "711576", 3, mem_player_hp, get_map_win_condition(bit3)),
    (625665, "Brawler's Pride I", "Defeat the Slime Demon without using any Spiritual Power", 5, "711579", 0, mem_spirit, get_map_win_condition(bit0)),
    (625666, "Brawler's Pride II", "Defeat the Bat Demon without using any Spiritual Power", 10, "711580", 1, mem_spirit, get_map_win_condition(bit1)),
]

for a_id, title, desc, pts, badge, stage_id, mem_check, win_cond in dmg_spirit_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.MISSABLE if mem_check == mem_player_hp else AchievementType.STANDARD)
    ach.add_core([
        (mem_game_state == 0x00), (mem_stage == stage_id), (mem_boss_stage == stage_id),
        pause_if((mem_check < mem_check.delta()).with_hits(1)),
    ] + win_cond)
    ach.add_alt([reset_if(mem_player_hp == 0x00)])
    my_set.add_achievement(ach)

# Damageless especiais
special_dmg_data = [
    (625663, "Flawless Exorcism", "Defeat the Green Demon without taking any damage", 25, "711577", 4),
    (625664, "Absolute Dominance", "Defeat the King Demon without taking any damage", 50, "711578", 5),
]
for a_id, title, desc, pts, badge, stage_id in special_dmg_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.MISSABLE)
    logic = [
        trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x50).with_hits(1),
        (mem_boss_stage == stage_id) if stage_id == 4 else (mem_stage == stage_id),
    ]
    if stage_id == 5:
        logic.append((mem_diff == 0x01)) # King Demon exige Hard Mode
    else:
        logic.append((mem_game_state == 0x00))
        
    logic.append(pause_if((mem_player_hp < mem_player_hp.delta()).with_hits(1)))
    ach.add_core(logic)
    ach.add_alt([reset_if(mem_player_hp == 0x00)])
    my_set.add_achievement(ach)

# 5. PONTUAÇÃO (SCORE)
score_data = [
    (625669, "Spirit Trainee", "Reach 5,000 points", 1, "711583", 500),
    (625670, "Spirit Warrior", "Reach 10,000 points", 2, "711584", 1000),
    (625671, "Spirit Master", "Reach 30,000 points", 4, "711585", 3000),
]

for a_id, title, desc, pts, badge, target in score_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_score >= target), (mem_score.delta() < target), (mem_game_state == 0x00)
    ])
    my_set.add_achievement(ach)

# 6. ENDGAME E ESPECÍFICAS
ach = Achievement(id=625651, title="Storming the Castle", description="Clear the Castle stage", points=5, badge="711565", type=AchievementType.PROGRESSION)
ach.add_core([(mem_stage == 0x05), (mem_stage.delta() == 0x04), (mem_game_state == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=625652, title="The True Threat", description="Clear the Demon Realm and defeat the King Demon in Hard mode", points=10, badge="711566", type=AchievementType.WIN_CONDITION)
ach.add_core([(mem_diff == 0x01), (mem_stage == 0x05), (mem_ending != 0x0a), (mem_ending.delta() == 0x0a)])
my_set.add_achievement(ach)

ach = Achievement(id=625667, title="A Man's Code", description="Defeat the King Demon using only Kuwabara in Hard mode", points=10, badge="711581")
ach.add_core([
    trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x50).with_hits(1),
    (mem_diff == 0x01), (mem_stage == 0x05), (mem_char == 0x01), reset_if(mem_boss_stage != 0x05)
])
my_set.add_achievement(ach)

ach = Achievement(id=625668, title="Spirit Detective Elite", description="Clear the Demon Realm without using any continues", points=50, badge="711582")
ach.add_core([
    trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x50).with_hits(1),
    (mem_diff == 0x01), (mem_boss_stage == 0x05),
    pause_if((mem_continues < mem_continues.delta()).with_hits(1)) # <- Bug corrigido aqui também!
])
ach.add_alt([reset_if(mem_continues == 0x00)])
my_set.add_achievement(ach)

my_set.save()