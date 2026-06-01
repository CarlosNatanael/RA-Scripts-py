from pycheevos.core.helpers import *
from pycheevos.core.constants import LeaderboardFormat
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=11615, title="Imported Leaderboards")

# 1. ALIASES DE MEMÓRIA
mem_stage = byte(0x0025)
mem_endgame = byte(0x0107)

mem_gold_100k = byte(0x0024).bcd()
mem_gold_1k = byte(0x0023).bcd()
mem_gold_10 = byte(0x0022).bcd()

# 2. LEADERBOARDS
lb_wealthiest = Leaderboard(
    id=163827,
    title="Wealthiest Pirate",
    description="Highest amount of gold accumulated upon defeating the Ghost of Captain Silver and beating the game",
    format=LeaderboardFormat.VALUE,
    lower_is_better=False
)

# Gatilho instantâneo no fim do jogo
lb_wealthiest.start = [[
    (mem_stage == 0x06),
    (mem_endgame.delta() == 0x00),
    (mem_endgame == 0xff),
]]

# Submissão e Cancelamento imediatos
lb_wealthiest.cancel = [[always_false()]]
lb_wealthiest.submit = [[always_true()]]

# Valor com multiplicadores para restaurar o cálculo real de ouro
lb_wealthiest.value = [[
    add_source(mem_gold_100k * 100000),
    add_source(mem_gold_1k * 1000),
    measured(mem_gold_10 * 10)
]]

my_set.add_leaderboard(lb_wealthiest)

my_set.save()