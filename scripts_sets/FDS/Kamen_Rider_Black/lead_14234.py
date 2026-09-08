from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=14234, title="Kamen Rider Black - Leaderboards")

# 1. ALIASES DE MEMÓRIA
mem_stage    = byte(0x0560)
mem_substage = byte(0x055e)
mem_score    = tbyte(0x0060)

# 2. LEADERBOARD: HIGH SCORE
lb = Leaderboard(
    id=169164,
    title="High Score",
    description="Complete the game by defeating Shadow Moon with the highest score possible",
    format=LeaderboardFormat.SCORE,
    lower_is_better=False
)

lb.start = [[
    (mem_stage == 0x14),
    (mem_substage == 0x01),
    (mem_substage.delta() == 0x00),
]]

lb.cancel = [[always_false()]]

lb.submit = [[always_true()]]

lb.value = [[
    measured(mem_score.bcd())
]]

my_set.add_leaderboard(lb)
my_set.save()