from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=14286, title="Imported Set")

# ==========================================
# 1. ALIASES DE MEMÓRIA
# ==========================================
mem_stage = byte(0x1a93)
mem_state = byte(0x1d22)
mem_diff  = byte(0x1d0f)
mem_hp    = byte(0x0320) 

# ==========================================
# 2. PROGRESSÃO (Stages Completos)
# ==========================================
prog_data = [
    (606954, "First Assembly", "Complete Stage 1", 2, "00000", 0x06, AchievementType.PROGRESSION),
    (606955, "The Plot Thickens", "Complete Stage 2", 3, "00000", 0x0c, AchievementType.PROGRESSION),
    (606956, "Into the Depths", "Complete Stage 3", 5, "00000", 0x11, AchievementType.PROGRESSION),
    (606957, "Moon Base Mayhem", "Complete Stage 4", 5, "00000", 0x17, AchievementType.PROGRESSION),
    (606958, "Red Skull's Demise", "Defeat Red Skull and complete the game", 10, "00000", 0x1d, AchievementType.WIN_CONDITION),
]

for a_id, title, desc, pts, badge, target_stage, a_type in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=a_type)
    ach.add_core([
        (mem_stage == target_stage),
        (mem_stage.delta() == (target_stage - 1)),
        (mem_state == 0x07)
    ])
    my_set.add_achievement(ach)

# ==========================================
# 3. CHEFES SEM DANO (Missables)
# ==========================================
damageless_data = [
    (606970, "Laser Focus", "Defeat Living Laser in Stage 1 without taking any damage on Normal or Challenge difficulty", 10, "00000", 0x02),
    (606971, "Whirlwind Warning", "Defeat Whirlwind in Stage 2 without taking any damage on Normal or Challenge difficulty", 10, "00000", 0x05),
    (606972, "Unstoppable Force", "Defeat Juggernaut in Stage 3 without taking any damage on Normal or Challenge difficulty", 10, "00000", 0x08),
    (606973, "Mechanical Menace", "Defeat Ultron in Stage 4 without taking any damage on Normal or Challenge difficulty", 25, "00000", 0x16),
    (606974, "Bones to Pick", "Defeat Crossbones in Stage 5 without taking any damage on Normal or Challenge difficulty", 25, "00000", 0x19),
]

for a_id, title, desc, pts, badge, boss_stage in damageless_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.MISSABLE)
    
    ach.add_core([
        pause_if((mem_hp < 0x140).with_hits(1)), # 0x140 equivale a 320 em decimal
        (mem_stage.delta() == boss_stage),
        (mem_diff >= 0x01),
        trigger(mem_stage == (boss_stage + 1))
    ])
    
    # Condições de reset e proteção no Alt 1
    ach.add_alt([
        or_next(mem_state == 0x01),
        reset_if(mem_hp == 0x00)
    ])
    
    my_set.add_achievement(ach)

my_set.save()