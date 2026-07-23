from pycheevos.core.helpers import *
from pycheevos.core.constants import LeaderboardFormat
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=14452, title="Yu Yu Hakusho: Spirit Detective")

# 1. ALIASES DE MEMÓRIA
mem_difficulty = byte(0x001a)
mem_boss_id    = byte(0x0e20)
mem_boss_state = byte(0x0100)
mem_score      = word(0x0010)
mem_game_state = byte(0x0022)
mem_stage      = byte(0x0150)
mem_p1_hp      = byte(0x0b19)
mem_boss_hp    = byte(0x0e2a)

# 2. HIGH SCORE
lb_score = Leaderboard(
    id=167761,
    title="High Score",
    description="Achieve the highest score clearing the game",
    format=LeaderboardFormat.VALUE,
    lower_is_better=False
)

lb_score.start = [[
    (mem_difficulty == 1),
    (mem_boss_id == 5),
    (mem_boss_state != 10),
    (mem_boss_state.delta() == 10),
]]
lb_score.cancel = [[always_false()]]
lb_score.submit = [[always_true()]]
lb_score.value  = [[measured(mem_score)]]

my_set.add_leaderboard(lb_score)

# 3. FASTEST CLEAR (TIME TRIALS)
# Dados: (ID do LB, Nome do Mapa, Valor da Memória do Mapa)
tt_data = [
    (167762, "Map A", 0),
    (167763, "Map B", 1),
    (167764, "Map C", 2),
    (167765, "Map D", 3),
]

for lb_id, map_name, map_val in tt_data:
    lb = Leaderboard(
        id=lb_id,
        title=f"Fastest Clear: {map_name}",
        description=f"Clear {map_name} as fast as possible",
        format=LeaderboardFormat.FRAMES,
        lower_is_better=True
    )
    
    lb.start = [[
        (mem_boss_state == 10),
        (mem_game_state == 0),
        (mem_stage == map_val),
        (mem_p1_hp == 80),
    ]]
    
    lb.cancel = [[
        (mem_boss_state == 0),
        (mem_p1_hp == 0),
    ]]
    
    lb.submit = [[
        (mem_boss_hp == 80),
        (mem_boss_hp.delta() == 0),
    ]]
    
    lb.value = [[measured(always_true())]]
    
    my_set.add_leaderboard(lb)

my_set.save()