from pycheevos.core.helpers import *
from pycheevos.core.constants import LeaderboardFormat
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=36560, title="Arch Rivals")

# 1. ALIASES DE MEMÓRIA
mem_period       = byte(0x01e2)
mem_p2_ctrl      = byte(0x0795)
mem_p1_score     = word(0x0216)
mem_match_end    = byte(0x8518)
mem_p1_ind_score = byte(0x0392)

# 2. LÓGICA COMPARTILHADA
start_match_end = [
    (mem_p2_ctrl == 0x00),
    or_next(mem_period == 0x04),
    (mem_period == 0x08),
    (mem_match_end.delta() == 0xff),
    (mem_match_end == 0x00),
]

# 3. LEADERBOARDS
lb_data = [
    (164725, "Individual High Score", "Highest points scored by Player 1 in a single match", mem_p1_ind_score),
    (164726, "Team High Score", "Highest total points scored by the Home Team in a single match", mem_p1_score),
]

for lb_id, title, desc, target_value in lb_data:
    lb = Leaderboard(
        id=lb_id,
        title=title,
        description=desc,
        format=LeaderboardFormat.VALUE,
        lower_is_better=False
    )
    
    lb.start = [start_match_end]
    lb.cancel = [[always_false()]]
    lb.submit = [[always_true()]]
    lb.value = [[measured(target_value)]]
    
    my_set.add_leaderboard(lb)

my_set.save()