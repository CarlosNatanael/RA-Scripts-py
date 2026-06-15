from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=10708, title="Joe Montana Football")

# 1. ALIASES DE MEMÓRIA
target_value = byte(0x0866).bcd()
mem_diff     = byte(0x08d5)
mem_state    = byte(0x0891)
mem_p2_team  = byte(0x08bf)

# 2. DADOS DOS LEADERBOARDS
# Formato: (ID, "Nome da Dificuldade", Valor na Memória)
lb_data = [
    (165033, "Beginner",    0),
    (165034, "Normal",      1),
    (165035, "Professional", 2),
]

# 3. GERAÇÃO DINÂMICA
for lb_id, diff_name, diff_val in lb_data:
    
    lb_start = [
        reset_if(mem_state == 0x08),
        (mem_p2_team == 0xff).with_hits(1),
        (mem_diff == diff_val),
        (byte(0x0891).delta() != value(32)),
        (byte(0x0891) == value(32)),
    ]

    lb = Leaderboard(
        id=lb_id,
        title=f"Highest Score - {diff_name}",
        description=f"Finish a match with the highest score possible playing on {diff_name} difficulty",
        format=LeaderboardFormat.VALUE,
        lower_is_better=False
    )

    lb.start = [lb_start]
    lb.cancel = [[always_false()]]
    lb.submit = [[always_true()]]
    lb.value = [[measured(target_value)]]
    my_set.add_leaderboard(lb)

my_set.save()