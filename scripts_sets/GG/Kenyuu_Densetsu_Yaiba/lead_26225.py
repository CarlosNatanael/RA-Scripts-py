from pycheevos.core.helpers import *
from pycheevos.core.constants import LeaderboardFormat
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=26225, title="Kenyuu Densetsu Yaiba")

# 1. ALIASES DE MEMÓRIA
mem_stage      = byte(0x0013)
mem_stage_flag = byte(0x1e42)
mem_score      = word(0x000d).bcd()

# 2. HIGH SCORE (Kurogane's Legacy)
lb_score = Leaderboard(
    id=166521,
    title="High Score: Kurogane's Legacy",
    description="Submit your highest score achieved upon clearing the game",
    format=LeaderboardFormat.VALUE,
    lower_is_better=False
)

lb_score.start = [[
    (mem_stage == 0x30), # 48 em decimal
    (mem_stage.delta() != 0x30),
    (mem_stage > 0x00)
]]
lb_score.cancel = [[always_false()]]
lb_score.submit = [[always_true()]]
lb_score.value = [[measured(mem_score)]]

my_set.add_leaderboard(lb_score)

# 3. TIME TRIALS (SPEEDRUNS)
# Formato dos Dados: (ID, "Título", "Descrição", Fase_Inicial, Fase_Final)
tt_data = [
    (166522, "Time Trial: Stage 1-1", "Complete Stage 1-1 as fast as possible", 1, 2),
    (166523, "Time Trial: Stage 2-2 (First Power Orb)", "Complete the Stage 2-2 Power Orb minigame as fast as possible", 12, 13),
    (166524, "Time Trial: Stage 2-4 (Third Power Orb)", "Complete the Stage 2-4 Power Orb minigame as fast as possible", 16, 17),
    (166525, "Time Trial: Stage 2-6 (Fifth Power Orb)", "Complete the Stage 2-6 Power Orb minigame as fast as possible", 20, 21),
]

for lb_id, title, desc, st_start, st_submit in tt_data:
    lb = Leaderboard(
        id=lb_id,
        title=title,
        description=desc,
        format=LeaderboardFormat.FRAMES,
        lower_is_better=True
    )
    
    lb.start = [[
        (mem_stage == st_start),
        (mem_stage.delta() == st_start - 1),
        (mem_stage_flag == 1)
    ]]
    
    lb.cancel = [[
        (mem_stage == 0),
        (mem_stage_flag == 0)
    ]]
    
    lb.submit = [[
        (mem_stage == st_submit),
        (mem_stage.delta() == st_submit - 1),
        (mem_stage_flag == 1)
    ]]

    lb.value = [[
        measured(always_true())
    ]]
    
    my_set.add_leaderboard(lb)

my_set.save()