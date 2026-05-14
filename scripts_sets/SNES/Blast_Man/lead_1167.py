from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=1167, title="Sonic Blast Man")

# 1. ALIASES DE MEMÓRIA
mem_state = byte(0x0062)
mem_stage = byte(0x00aa)
mem_mode  = byte(0x1852)
mem_diff  = byte(0x185a)

# 2. DADOS DOS LEADERBOARDS
# Formato: (ID, "Nome da Dificuldade", Valor na Memória)
lb_data = [
    (162921, "Easy",      0),
    (162922, "Normal",    1),
    (162923, "Hard",      2),
    (162924, "Very Hard", 3),
]

# 3. GERAÇÃO DINÂMICA
for lb_id, diff_name, diff_val in lb_data:
    
    lb_start = [
        (mem_diff == diff_val),
        (mem_mode.delta() == 0),
        (mem_mode == 10),
        (mem_stage == 0),
    ]
    
    lb_cancel = [
        or_next(mem_state == 204),
        (mem_state == 147),
    ]
    
    lb_submit = [
        (mem_mode == 10),
        (mem_stage.delta() == 4),
        (mem_stage == 5),
    ]

    lb_value = [
        measured(value(0) == value(0)),
    ]
    
    lb = Leaderboard(
        id=lb_id,
        title=f"Fastest Fists [{diff_name}]",
        description="Defeat all bosses in Boss Rush mode in the shortest time",
        format=LeaderboardFormat.FRAMES,
        lower_is_better=True
    )
    
    lb.set_start(lb_start)
    lb.set_cancel(lb_cancel)
    lb.set_submit(lb_submit)
    lb.set_value(lb_value)
    my_set.add_leaderboard(lb)
my_set.save()