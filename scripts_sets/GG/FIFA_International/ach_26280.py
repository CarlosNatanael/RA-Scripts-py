from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=26280, title="FIFA International Soccer")

# 1. ALIASES DE MEMÓRIA
mem_comp_mode   = byte(0x0c9a)
mem_period      = byte(0x0af0)
mem_score_p1    = byte(0x0d85)
mem_score_cpu   = byte(0x0d93)
mem_match_end   = byte(0x0ad7)
mem_team_p1     = byte(0x0b11)
mem_team_cpu    = byte(0x0b12)
mem_game_state  = byte(0x0bb3)
mem_player_team = byte(0x0b0f)
mem_half_len    = byte(0x0af5)

# Passwords / Cheats
mem_pw_1 = byte(0x0c70)
mem_pw_2 = byte(0x0c71)
mem_pw_3 = byte(0x0c72)
mem_pw_4 = byte(0x0c73)
mem_pw_5 = byte(0x0c74)

# 2. VITÓRIAS EM AMIGÁVEIS (EXHIBITION)
# Helper para não repetir a lógica de vitória
def exhibition_win_ach(a_id, title, desc, pts, p1_team=None, cpu_team=None):
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    logic = [
        (mem_comp_mode == 0x00),
        (mem_period >= 0x01),
        (mem_score_p1 > mem_score_cpu),
        (mem_match_end.delta() == 0),
        trigger(mem_match_end == 0xff)
    ]
    
    # Adiciona as equipas à lógica se elas forem especificadas
    if p1_team is not None:
        logic.insert(1, (mem_team_p1 == p1_team))
    if cpu_team is not None:
        logic.insert(2, (mem_team_cpu == cpu_team))
        
    ach.add_core(logic)
    my_set.add_achievement(ach)

exhibition_win_ach(609896, "World Class Debut", "Win your first Exhibition match", 1)
exhibition_win_ach(609897, "Superclássico das Américas", "Playing as Brazil, defeat Argentina in an Exhibition match", 2, p1_team=0x06, cpu_team=0x01)
exhibition_win_ach(609898, "Low Countries Derby", "Playing as Germany, defeat Netherlands in an Exhibition match", 2, p1_team=0x11, cpu_team=0x1d)
exhibition_win_ach(609899, "Clásico de CONCACAF", "Playing as Mexico, defeat USA in an Exhibition match", 2, p1_team=0x1b, cpu_team=0x2f)

# Trajectory Madness (Vitória com Cheat Code ativado)
ach = Achievement(id=609905, title="Trajectory Madness", description="Win a match with the Crazy Ball option enabled in an Exhibition match", points=5)
ach.add_core([
    (mem_pw_1 == 0x01), (mem_pw_2 == 0x0c), (mem_pw_3 == 0x1e), (mem_pw_4 == 0x13), (mem_pw_5 == 0x12),
    (mem_comp_mode == 0x00), (mem_period >= 0x01), (mem_score_p1 > mem_score_cpu),
    (mem_match_end.delta() == 0x00), trigger(mem_match_end == 0xff)
])
my_set.add_achievement(ach)


# 3. LIGAS E TORNEIOS (CAMPANHA)
# League Champion
ach = Achievement(id=609900, title="League Champion", description="Complete the League mode and finish in 1st place", points=25)
ach.add_core([(mem_comp_mode == 0x01), (mem_game_state.delta() != 0x09), (mem_game_state == 0x09)])
my_set.add_achievement(ach)

# Cup Winners
ach = Achievement(id=609901, title="Cup Winners", description="Win the Tournament mode", points=25, type=AchievementType.WIN_CONDITION)
ach.add_core([(mem_comp_mode == 0x04), (mem_game_state.delta() != 0x04), (mem_game_state == 0x04)])
my_set.add_achievement(ach)

# The Azzurri Glory
ach = Achievement(id=609902, title="The Azzurri Glory", description="Playing as Italy, win the Tournament mode", points=10)
ach.add_core([
    or_next(mem_comp_mode == 0x03),
    (mem_comp_mode == 0x04),
    (mem_player_team == 0x18), # Italy
    (mem_game_state.delta() != 0x04),
    trigger(mem_game_state == 0x04)
])
my_set.add_achievement(ach)


# 4. ABSOLUTE DOMINANCE (Loop Dinâmico)
ach_dominance = Achievement(id=609903, title="Absolute Dominance", description="Win all 3 matches during the Group Stage of a Tournament", points=10)
ach_dominance.add_core([
    (mem_comp_mode.delta() == 0x03),
    trigger(mem_comp_mode == 0x04)
])

# Gera os 24 Alts automaticamente!
for i in range(24):
    base_addr = 0x0c9b + (i * 8)
    mem_team_id = byte(base_addr + 1)
    mem_wins    = byte(base_addr + 3)
    
    ach_dominance.add_alt([
        (mem_player_team == mem_team_id),
        trigger(mem_wins == 0x03)
    ])

my_set.add_achievement(ach_dominance)


# 5. DESAFIOS ESPECÍFICOS
# First-Half Blitz
ach = Achievement(id=609904, title="First-Half Blitz", description="Score at least 2 goals during the first half of an Exhibition match with the half length set to 2 minutes", points=5)
ach.add_core([
    (mem_half_len == 0x01),
    (mem_comp_mode == 0x00),
    (mem_player_team != 0xff),
    (mem_period == 0x00),
    or_next(mem_score_p1.delta() == 0x01),
    (mem_score_p1.delta() == 0x00),
    trigger(mem_score_p1 == 0x02)
])
my_set.add_achievement(ach)

my_set.save()