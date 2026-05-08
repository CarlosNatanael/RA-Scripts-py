from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=14286, title="Imported Leaderboards")

# 1. ALIASES DE MEMÓRIA
mem_diff  = byte(0x1d0f)
mem_state = byte(0x1d22)

# 2. DADOS DOS LEADERBOARDS
#(ID, "Nome da Dificuldade", Valor na Memória)
lb_data = [
    (162570, "Practice",  0),
    (162571, "Normal",    1),
    (162572, "Challenge", 2),
]

# 3. GERAÇÃO DINÂMICA
for lb_id, diff_name, diff_val in lb_data:
    
    lb_start = [
        (mem_diff == diff_val),
        (mem_state.delta() == 2),
        (mem_state >= 3),
    ]
    
    lb_cancel = [
        (mem_state == 1),
    ]
    
    lb_submit = [
        (mem_state.delta() != 8),
        (mem_state == 8),
    ]
    
    lb_value = [
        add_source(low4(0x1d5b) * 10000000),
        add_source(low4(0x1d5a) * 1000000),
        add_source(low4(0x1d59) * 100000),
        add_source(low4(0x1d58) * 10000),
        add_source(low4(0x1d57) * 1000),
        add_source(low4(0x1d56) * 100),
        add_source(low4(0x1d55) * 10),
        measured(low4(0x1d54) * 1), 
    ]
    
    lb = Leaderboard(
        id=lb_id,
        title=f"Highest Score [{diff_name}]",
        description=f"Get the highest score possible on {diff_name} difficulty",
        format=LeaderboardFormat.VALUE,
        lower_is_better=False
    )
    
    lb.set_start(lb_start)
    lb.set_cancel(lb_cancel)
    lb.set_submit(lb_submit)
    lb.set_value(lb_value)
    
    my_set.add_leaderboard(lb)

my_set.save()