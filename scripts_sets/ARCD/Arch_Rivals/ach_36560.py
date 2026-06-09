from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=36560, title="Arch Rivals")

# 1. ALIASES DE MEMÓRIA
mem_period       = byte(0x01e2)
mem_p2_ctrl      = byte(0x0795)
mem_matchup      = byte(0x0371)

mem_p1_score     = word(0x0216)
mem_p2_score     = word(0x021a)
mem_match_end    = byte(0x8518)

mem_p1_char      = byte(0x0377)
mem_p1_ind_score = byte(0x0392)
mem_p1_steals    = byte(0x0396)
mem_p1_rebounds  = byte(0x0398)
mem_shots_att    = byte(0x039a)
mem_shot_clock   = byte(0x1f2b)

mem_teammate_req = byte(0x0c07)
mem_punch_flag   = byte(0x0465)

# Placar de outros jogadores na quadra
mem_p2_ind_score = byte(0x05a2)
mem_p3_ind_score = byte(0x07b2)
mem_p4_ind_score = byte(0x09c2)

# 2. BLOCOS REUTILIZÁVEIS
# Lógica comum: P2 é CPU, P1 ganha, Fim do 4º Quarto ou Morte Súbita, Tela de Resultado
cond_match_win = [
    (mem_p2_ctrl == 0x00),
    (mem_p1_score > mem_p2_score),
    or_next(mem_period == 0x04),
    (mem_period == 0x08),
    (mem_match_end.delta() == 0xff),
    (mem_match_end == 0x00),
]

# 3. VITÓRIAS POR CONFRONTO (MATCHUPS)
matchup_data = [
    (615363, "City of Angels", "Win a Los Angeles vs Chicago match", 5, 0x00, AchievementType.STANDARD),
    (615364, "State Rivalry", "Win a Brawl State vs Natural High match", 5, 0x01, AchievementType.STANDARD),
    (615365, "High Altitude, Low Blows", "Win a Natural High vs Los Angeles match", 5, 0x03, AchievementType.STANDARD),
    (615366, "Windy City Brawlers", "Win a Chicago vs Brawl State match", 5, 0x02, AchievementType.WIN_CONDITION),
]

for a_id, title, desc, pts, matchup_val, ach_type in matchup_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=ach_type)
    ach.add_core([
        reset_if(mem_period == 0x00),
        (mem_matchup == matchup_val).with_hits(1),
        *cond_match_win
    ])
    my_set.add_achievement(ach)

# 4. VITÓRIAS POR PERSONAGEM
char_data = [
    (615367, "Punk Rock Victory", "Win a match as Mohawk", 2, 0x06),
    (615368, "Sharpshooter", "Win a match as Lewis", 2, 0x04),
]

for a_id, title, desc, pts, char_id in char_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_p1_char == char_id),
        *cond_match_win
    ])
    my_set.add_achievement(ach)

# 5. CONQUISTAS ESPECÍFICAS
ach = Achievement(id=615369, title="The Real Star", description="Win a match with the highest individual score on the court", points=10)
ach.add_core([
    (mem_p1_ind_score > mem_p2_ind_score),
    (mem_p1_ind_score > mem_p3_ind_score),
    (mem_p1_ind_score > mem_p4_ind_score),
    *cond_match_win
])
my_set.add_achievement(ach)

ach = Achievement(id=615370, title="Sudden Death Survivor", description="Win a match in Sudden Death", points=10)
ach.add_core([
    (mem_p2_ctrl == 0x00),
    (mem_p1_score > mem_p2_score),
    (mem_period == 0x08),
    (mem_match_end.delta() == 0xff),
    trigger(mem_match_end == 0x00),
])
my_set.add_achievement(ach)

ach = Achievement(id=615371, title="Pickpocket", description="Perform 15+ steals in a single match", points=10)
ach.add_core([
    (mem_p2_ctrl == 0x00),
    (mem_period > 0x00),
    measured(mem_p1_steals >= 0x0f),
    (mem_p1_steals > mem_p1_steals.delta()),
])
my_set.add_achievement(ach)

ach = Achievement(id=615372, title="Board Crasher", description="Perform 10+ rebounds in a single match", points=5)
ach.add_core([
    (mem_p2_ctrl == 0x00),
    (mem_period > 0x00),
    measured(mem_p1_rebounds >= 0x0a),
    (mem_p1_rebounds > mem_p1_rebounds.delta()),
])
my_set.add_achievement(ach)

ach = Achievement(id=615373, title="Clutch Under Pressure", description="Score a 3-pointer with 3 seconds or less on the shot clock", points=10)
ach.add_core([
    (mem_p2_ctrl == 0x00),
    (mem_period > 0x00),
    reset_if(mem_p1_ind_score.delta() > mem_p1_ind_score),
    (mem_shot_clock <= 0x03).with_hits(1),
    sub_source(mem_p1_ind_score.delta()),
    trigger(mem_p1_ind_score == 0x03),
])
my_set.add_achievement(ach)

ach = Achievement(id=615374, title="Surgical Precision", description="Scoring 36+ points with a maximum of 20 total shots attempted in a single match", points=25, type=AchievementType.MISSABLE)
ach.add_core([
    reset_next_if(mem_period == 0x00),
    pause_if((mem_shots_att > 0x14).with_hits(1)),
    (mem_p2_ctrl == 0x00),
    (mem_period > 0x00),
    (mem_shots_att <= 0x14),
    measured(mem_p1_ind_score.delta() < 0x24),
    trigger(mem_p1_ind_score >= 0x24),
])
my_set.add_achievement(ach)

ach = Achievement(id=615375, title="Front Runner", description="Score the first points of the match, never trail on the scoreboard at any point, and win the game", points=25, type=AchievementType.MISSABLE)
ach.add_core([
    (mem_p2_ctrl == 0x00),
    (mem_p1_score > mem_p2_score),
    pause_if(mem_p2_score > mem_p1_score),
    (mem_period == 0x01).with_hits(1),
    trigger((mem_period == 0x02).with_hits(1)),
    trigger((mem_period == 0x03).with_hits(1)),
    trigger(mem_period == 0x04),
    (mem_match_end.delta() == 0xff),
    trigger(mem_match_end == 0x00),
])
ach.add_alt([reset_if(mem_period == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=615376, title="Silent Partner", description="Lead the 1st quarter without asking your CPU teammate for a pass", points=5)
ach.add_core([
    and_next(mem_teammate_req == 0x02),
    pause_if((mem_punch_flag == 0x20).with_hits(1)),
    (mem_p2_ctrl == 0x00),
    (mem_period.delta() == 0x01),
    trigger(mem_period == 0x02),
    (mem_p1_score > mem_p2_score),
])
ach.add_alt([reset_if(mem_period == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=615377, title="Pacifist Run", description="Win a match without throwing a single punch", points=25, type=AchievementType.MISSABLE)
ach.add_core([
    or_next(mem_teammate_req == 0x00),
    and_next(mem_teammate_req >= 0x03),
    pause_if((mem_punch_flag == 0x20).with_hits(1)),
    (mem_p2_ctrl == 0x00),
    (mem_p1_score > mem_p2_score),
    or_next(mem_period == 0x04),
    trigger(mem_period == 0x08),
    (mem_match_end.delta() == 0xff),
    trigger(mem_match_end == 0x00),
])
ach.add_alt([reset_if(mem_period == 0x00)])
my_set.add_achievement(ach)

my_set.save()