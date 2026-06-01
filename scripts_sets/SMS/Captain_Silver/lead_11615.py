from pycheevos.core.helpers import *
from pycheevos.core.constants import LeaderboardFormat
from pycheevos.models.set import AchievementSet
from pycheevos.models.leaderboard import Leaderboard

my_set = AchievementSet(game_id=11615, title="Captain Silver - All Leaderboards")

# 1. ALIASES DE MEMÓRIA
mem_stage = byte(0x0025)
mem_gamestate = byte(0x03d5)
mem_endgame = byte(0x0107)
mem_timebonus = byte(0x0134)

# Tempo
mem_time_m = byte(0x002c).bcd()
mem_time_s = byte(0x002b).bcd()

# Ouro
mem_gold_100k = byte(0x0024).bcd()
mem_gold_1k = byte(0x0023).bcd()
mem_gold_10 = byte(0x0022).bcd()

# 2. CÁLCULOS DE VALOR (VALUES)
time_value = [
    add_source(mem_time_m * 100),
    measured(mem_time_s)
]

gold_value = [
    add_source(mem_gold_100k * 100000),
    add_source(mem_gold_1k * 1000),
    measured(mem_gold_10 * 10)
]

# 3. LEADERBOARDS: FASTEST CLEAR (FASES 1 A 6)
lb_data = [
    (1, "Fastest Clear: Town of Barsend", "Highest time remaining upon clearing Level 1"),
    (2, "Fastest Clear: The Ship", "Highest time remaining upon clearing Level 2"),
    (3, "Fastest Clear: The Boat", "Highest time remaining upon clearing Level 3"),
    (4, "Fastest Clear: The Cave", "Highest time remaining upon clearing Level 4"),
    (5, "Fastest Clear: The Jungle", "Highest time remaining upon clearing Level 5"),
    (6, "Fastest Clear: The Mountain", "Highest time remaining upon defeating the Ghost of Captain Silver Level 6"),
]

for stage, title, desc in lb_data:
    lb = Leaderboard(
        id=0,
        title=title,
        description=desc,
        format=LeaderboardFormat.VALUE,
        lower_is_better=False
    )
    
    lb.start = [[
        (mem_stage == stage),
        (mem_gamestate == 0xff),
        (mem_timebonus.delta() == 0),
        (mem_timebonus == 1),
    ]]
    lb.cancel = [[always_false()]]
    lb.submit = [[always_true()]]
    lb.value = [time_value]
    
    my_set.add_leaderboard(lb)

# 4. LEADERBOARD: WEALTHIEST PIRATE
lb_wealthiest = Leaderboard(
    id=163827,
    title="Wealthiest Pirate",
    description="Highest amount of gold accumulated upon defeating the Ghost of Captain Silver and beating the game",
    format=LeaderboardFormat.VALUE,
    lower_is_better=False
)

lb_wealthiest.start = [[
    (mem_stage == 0x06),
    (mem_endgame.delta() == 0x00),
    (mem_endgame == 0xff),
]]
lb_wealthiest.cancel = [[always_false()]]
lb_wealthiest.submit = [[always_true()]]
lb_wealthiest.value = [gold_value]

my_set.add_leaderboard(lb_wealthiest)

my_set.save()