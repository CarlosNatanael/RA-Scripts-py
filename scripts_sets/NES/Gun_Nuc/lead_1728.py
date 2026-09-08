from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=1728, title="Imported Leaderboards")

# 1. ALIASES DE MEMÓRIA (LEADERBOARDS)
mem_diff       = byte(0x004c)
mem_ricochet   = byte(0x004e)
mem_state_f1   = byte(0x00f1)
mem_state_be   = byte(0x01be)

mem_alt1_trig  = byte(0x0180)
mem_alt2_trig  = byte(0x0188)

# 2. CÁLCULO DO PLACAR
val_logic = [
    add_source(byte(0x00e6)),
    add_source(byte(0x00e5)),
    add_source(byte(0x00e4)),
    add_source(byte(0x00e3)),
    add_source(byte(0x00e2)),
    add_source(byte(0x00e1)),
    measured(byte(0x00e0)),
]

# 3. ESTRUTURA GERAL DOS LEADERBOARDS
# (LB_ID, Title, Diff_Val, Rico_Val, Rico_Desc)
lb_data = [
    (171566, "High Score - Expert 1", 3, 255, "Ricochet on"),
    (171567, "High Score - Expert 2", 3, 0,   "Ricochet off"),
    (171568, "High Score - Advanced 1", 2, 255, "Ricochet on"),
    (171569, "High Score - Advanced 2", 2, 0,   "Ricochet off"),
    (171570, "High Score - Intermediate 1", 1, 255, "Ricochet on"),
    (171571, "High Score - Intermediate 2", 1, 0,   "Ricochet off"),
    (171572, "High Score - Novice 1", 0, 255, "Ricochet on"),
    (171573, "High Score - Novice 2", 0, 0,   "Ricochet off"),
]

for lb_id, title, diff_val, rico_val, rico_desc in lb_data:
    lb = Leaderboard(
        title=title,
        description=f"{rico_desc}, speed priority",
        id=lb_id,
        format=LeaderboardFormat.SCORE,
        lower_is_better=False
    )
    
    # Condições de Início
    start_core = [
        (mem_diff == diff_val),
        (mem_ricochet == rico_val),
        (mem_state_f1 == 255),
        (mem_state_be == 0),
    ]
    start_alt1 = [
        (mem_alt1_trig == 9),
        (mem_alt1_trig.delta() == 8),
    ]
    start_alt2 = [
        (mem_alt2_trig == 127),
        (mem_alt2_trig.delta() == 255),
    ]
    lb.set_start(start_core, start_alt1, start_alt2)
    
    # Cancelamento e Submissão
    lb.set_cancel([(value(0) == value(1))])
    lb.set_submit([(value(1) == value(1))])
    
    # Aplica o cálculo
    lb.set_value(val_logic)
    
    my_set.add_leaderboard(lb)

my_set.save()