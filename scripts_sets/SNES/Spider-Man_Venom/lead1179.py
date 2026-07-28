from pycheevos.core.helpers import *
from pycheevos.core.constants import LeaderboardFormat
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=1179, title="Maximum Carnage - Leaderboards")

# 1. ALIASES DE MEMÓRIA
mem_stage   = word(0x000a0e)
mem_pause   = byte(0x00088e)
mem_boss_hp = word(0x000dc0)
mem_lives   = word(0x000990)
mem_clear   = byte(0x001cca)
mem_acc     = byte(0x001ccc)
mem_p1_hp   = word(0x000b7c)

# 2. HIGH SCORE
lb_score = Leaderboard(
    id=167942,
    title="High Score",
    description="Complete the game with the highest score possible",
    format=LeaderboardFormat.SCORE,
    lower_is_better=False
)

lb_score.start = [[
    (mem_stage == 52),
    (mem_pause == 0),
    (mem_boss_hp == 0),
    (mem_boss_hp.delta() == 100).with_hits(1),
    reset_if(mem_stage == 0),
    or_next(mem_lives == 0),
    reset_if(mem_acc == 16),
]]
lb_score.cancel = [[always_false()]]
lb_score.submit = [[always_true()]]
lb_score.value = [[
    add_source(byte(0x00097a)),
    add_source(byte(0x00097c)),
    add_source(byte(0x00097e)),
    add_source(byte(0x000980)),
    measured(byte(0x000982)),
]]

my_set.add_leaderboard(lb_score)

# 3. TIME TRIALS (SPEEDRUNS)
# Formato: (ID, "Nome", Stage ID, [Salas Secretas para Cancelar], Tipo_Submit, Proximo_Stage)
tt_data = [
    (167964, "New York Street", 2, [], 'A', None),
    (167965, "Climb", 4, [58], 'B', 6),
    (167966, "Rooftop", 6, [], 'B', 8),
    (167967, "Alleyway", 8, [], 'B', 10),
    (167968, "The Hall", 10, [], 'B', 12),
    (167969, "Times Square", 14, [], 'A', None),
    (167970, "San Francisco", 16, [56, 58], 'A', None),
    (167971, "Central Park", 18, [], 'B', 20),
    (167972, "New York Street 2", 20, [], 'A', None),
    (167973, "The Deep", 22, [], 'A', None),
    (167974, "Fantastic 4 HQ", 24, [], 'A', None),
    (167975, "Fantastic 4 Lab", 26, [54], 'A', None),
    (167976, "Rooftop 2", 28, [], 'A', None),
    (167977, "Prospect Park", 30, [], 'A', None),
    (167978, "Prospect Park 2", 32, [], 'B', 34),
    (167979, "Police Station", 34, [60], 'A', None),
    (167980, "Manhattan Rooftop", 38, [], 'A', None),
    (167981, "Manhattan Street 1", 44, [], 'A', None),
    (167982, "Manhattan Street 2", 48, [], 'A', None),
    (167983, "Ruined Boys Home", 52, [60], 'C', None),
]

for lb_id, name, st_id, cancel_stages, sub_type, next_st in tt_data:
    lb = Leaderboard(
        id=lb_id,
        title=f"Fastest Clear - {name}",
        description=f"Complete the {name} stage as fast as possible.",
        format=LeaderboardFormat.FRAMES,
        lower_is_better=True
    )
    
    # START
    start_hp_cond = (mem_p1_hp == 48) if st_id == 2 else (mem_p1_hp >= 1)
    lb.start = [[
        start_hp_cond,
        (mem_p1_hp.delta() == 0),
        (mem_stage == st_id),
    ]]
    
    # CANCEL
    lb_cancel_logic = [[mem_lives == 0]]
    for secret_stage in cancel_stages:
        lb_cancel_logic.append([mem_stage == secret_stage])
    lb.cancel = lb_cancel_logic
    
    # SUBMIT
    if sub_type == 'A':
        lb.submit = [[
            (mem_stage == st_id),
            (mem_clear == 255),
            (mem_clear.delta() == 0),
        ]]
    elif sub_type == 'B':
        lb.submit = [[
            (mem_stage == next_st),
            (mem_stage.delta() == st_id),
            (mem_pause == 0),
        ]]
    elif sub_type == 'C':
        lb.submit = [[
            (mem_stage == st_id),
            (mem_boss_hp == 0),
            (mem_boss_hp.delta() == 100).with_hits(1),
            reset_if(mem_lives == 0),
        ]]
    
    # VALUE
    lb.value = [[measured(always_true())]]
    
    my_set.add_leaderboard(lb)

my_set.save()