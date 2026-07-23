from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=14452, title="Yu Yu Hakusho: Spirit Detective")

# 1. ALIASES DE MEMÓRIA
mem_difficulty = byte(0x001a)
mem_character  = byte(0x0016)
mem_continues  = byte(0x001e)
mem_game_state = byte(0x0022)
mem_score      = word(0x0010)

mem_stage      = byte(0x0150)
mem_boss_id    = byte(0x0e20)
mem_boss_state = byte(0x0100)
mem_boss_weakp = byte(0x0e24)
mem_boss_hp    = byte(0x0e2a)

mem_player_hp  = byte(0x0e8b)
mem_player_sp  = byte(0x0e8c)

# Funções que validam as flags bit a bit para a progressão
flags_prog = {
    0: bit0(0x0155),
    1: bit1(0x0155),
    2: bit2(0x0155),
    3: bit3(0x0155)
}

# Blocos Alt Reutilizáveis
alt_hp_reset = [reset_if(mem_player_hp == 0x00)]

# 2. PROGRESSÃO DOS MAPAS
prog_data = [
    (625647, "First Mission", "Clear Map A", 1, 0),
    (625648, "Urban Brawl", "Clear Map B", 2, 1),
    (625649, "City Limits", "Clear Map C", 2, 2),
    (625650, "Approaching the Stronghold", "Clear Map D", 3, 3),
]

for a_id, title, desc, pts, st_val in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.PROGRESSION)
    flag_bit = flags_prog[st_val]
    ach.add_core([
        (mem_stage == st_val),
        (mem_boss_id == st_val),
        (flag_bit == 0x01),
        (flag_bit.delta() == 0x00),
    ])
    my_set.add_achievement(ach)

ach = Achievement(id=625651, title="Storming the Castle", description="Clear the Castle stage", points=5, type=AchievementType.PROGRESSION)
ach.add_core([
    (mem_stage == 0x05),
    (mem_stage.delta() == 0x04),
    (mem_game_state == 0x00),
])
my_set.add_achievement(ach)

ach = Achievement(id=625652, title="The True Threat", description="Clear the Demon Realm and defeat the King Demon in Hard mode", points=10, type=AchievementType.WIN_CONDITION)
ach.add_core([
    (mem_difficulty == 0x01),
    (mem_boss_id == 0x05),
    (mem_boss_state != 0x0a),
    (mem_boss_state.delta() == 0x0a),
])
my_set.add_achievement(ach)

# 3. ATAQUES ESPECIAIS (WEAKPOINTS)
weakpoint_data = [
    (625653, "Ooze Anatomy", "Strike the Slime Demon's Head with a Special Attack", 10, 0, 0x03),
    (625654, "Clipped Wings", "Strike the Bat Demon's Head with a Special Attack", 5, 1, 0x01),
    (625655, "System Override", "Strike the Giant Robot's Core with a Special Attack", 10, 2, 0x0b),
    (625656, "Extinguished", "Strike the Fire Demon's Head with a Special Attack", 5, 3, 0x01),
    (625657, "Green With Envy", "Strike the Green Demon's Head with a Special Attack", 5, 4, 0x10),
    (625658, "Regicide", "Strike the King Demon's Head with a Special Attack", 5, 5, 0x06),
]

for a_id, title, desc, pts, st_val, weak_val in weakpoint_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_game_state == 0x00),
        (mem_stage == st_val),
        (mem_boss_id == st_val),
        reset_if(mem_boss_weakp != weak_val),
        trigger((mem_boss_hp < mem_boss_hp.delta()).with_hits(1)),
        trigger((mem_player_sp < mem_player_sp.delta()).with_hits(1)),
    ])
    my_set.add_achievement(ach)

# 4. CHEFES SEM DANO (MISSABLES)
dl_data = [
    (625659, "Squeaky Clean", "Defeat the Slime Demon without taking any damage", 10, 0),
    (625660, "Echo Evasion", "Defeat the Bat Demon without taking any damage", 10, 1),
    (625661, "Perfect Dismantle", "Defeat the Giant Robot without taking any damage", 10, 2),
    (625662, "Unscorched", "Defeat the Fire Demon without taking any damage", 25, 3),
]

for a_id, title, desc, pts, st_val in dl_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.MISSABLE)
    flag_bit = flags_prog[st_val]
    ach.add_core([
        (mem_game_state == 0x00),
        (mem_stage == st_val),
        (mem_boss_id == st_val),
        pause_if((mem_player_hp < mem_player_hp.delta()).with_hits(1)),
        trigger(flag_bit == 0x01),
        (flag_bit.delta() == 0x00),
    ])
    ach.add_alt(alt_hp_reset)
    my_set.add_achievement(ach)

ach = Achievement(id=625663, title="Flawless Exorcism", description="Defeat the Green Demon without taking any damage", points=25, type=AchievementType.MISSABLE)
ach.add_core([
    trigger(mem_stage == 0x05),
    (mem_stage.delta() == 0x04),
    (mem_boss_id == 0x04),
    (mem_game_state == 0x00),
    pause_if((mem_player_hp < mem_player_hp.delta()).with_hits(1)),
])
ach.add_alt(alt_hp_reset)
my_set.add_achievement(ach)

ach = Achievement(id=625664, title="Absolute Dominance", description="Defeat the King Demon without taking any damage", points=50, type=AchievementType.MISSABLE)
ach.add_core([
    (mem_difficulty == 0x01),
    (mem_boss_id == 0x05),
    (mem_stage == 0x05),
    trigger(mem_boss_state != 0x0a),
    (mem_boss_state.delta() == 0x0a),
    pause_if((mem_player_hp < mem_player_hp.delta()).with_hits(1)),
])
ach.add_alt(alt_hp_reset)
my_set.add_achievement(ach)

# 5. SEM ATAQUE ESPECIAL (NO SP)
no_sp_data = [
    (625665, "Brawler's Pride I", "Defeat the Slime Demon without using any Spiritual Power", 5, 0),
    (625666, "Brawler's Pride II", "Defeat the Bat Demon without using any Spiritual Power", 10, 1),
]

for a_id, title, desc, pts, st_val in no_sp_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    flag_bit = flags_prog[st_val]
    ach.add_core([
        (mem_stage == st_val),
        (mem_boss_id == st_val),
        trigger(flag_bit == 0x01),
        (flag_bit.delta() == 0x00),
        pause_if((mem_player_sp < mem_player_sp.delta()).with_hits(1)),
    ])
    ach.add_alt(alt_hp_reset)
    my_set.add_achievement(ach)

# 6. DESAFIOS ESPECÍFICOS & MARCOS DE PONTOS
ach = Achievement(id=625667, title="A Man's Code", description="Defeat the King Demon using only Kuwabara in Hard mode", points=10)
ach.add_core([
    (mem_difficulty == 0x01),
    (mem_boss_id == 0x05),
    trigger(mem_boss_state != 0x0a),
    (mem_boss_state.delta() == 0x0a),
    (mem_character == 0x01),
])
my_set.add_achievement(ach)

ach = Achievement(id=625668, title="Spirit Detective Elite", description="Clear the Demon Realm without using any continues", points=50)
ach.add_core([
    trigger(mem_boss_id == 0x05),
    trigger(mem_boss_state != 0x0a),
    (mem_boss_state.delta() == 0x0a),
    pause_if((mem_continues < mem_continues.delta()).with_hits(1)),
])
ach.add_alt([reset_if(mem_continues == 0x00)])
my_set.add_achievement(ach)

score_data = [
    (625669, "Spirit Trainee", "Reach 5,000 points", 1, 500),
    (625670, "Spirit Warrior", "Reach 10,000 points", 2, 1000),
    (625671, "Spirit Master", "Reach 30,000 points", 4, 3000),
]

for a_id, title, desc, pts, score_val in score_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_score >= score_val),
        (mem_score.delta() < score_val),
        (mem_game_state == 0x00),
    ])
    my_set.add_achievement(ach)

my_set.save()