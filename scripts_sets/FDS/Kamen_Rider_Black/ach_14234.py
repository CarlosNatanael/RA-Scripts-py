from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=14234, title="Kamen Rider Black - Refactored")

# 1. ALIASES DE MEMÓRIA (Chega de números mágicos)
mem_stage      = byte(0x0560)
mem_substage   = byte(0x055e)
mem_game_state = byte(0x0111)
mem_hp         = byte(0x0066)
mem_boss_hp    = byte(0x0067)
mem_timer      = byte(0x0065)
mem_score      = tbyte(0x0060)

mem_opt1       = byte(0x0557)
mem_opt2       = byte(0x0559)
mem_opt3       = byte(0x055b)

# 2. PROGRESSÃO PADRÃO (Stages 1 a 5)
prog_data = [
    (630457, "Flea Eradication", "Defeat the Flea Mutant and clear Stage 1", 2, 0x02, 0x83, "723518"),
    (630458, "Horn Snapped", "Defeat the Rhinoceros Mutant and clear Stage 2", 3, 0x06, 0x83, "723519"),
    (630459, "Shell Shocked", "Defeat the Tortoise Mutant and clear Stage 3", 3, 0x0a, 0x83, "723520"),
    (630460, "Approaching the Sanctuary", "Defeat the Crab Mutant and clear Stage 4", 5, 0x0c, 0x82, "723521"),
    (630461, "The High Priests Fall", "Defeat the Evil Lords and clear Stage 5", 5, 0x10, 0x82, "723522"),
]

for a_id, title, desc, pts, stage_val, sub_val, badge in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_stage == stage_val),
        (mem_game_state == 0x80),
        (mem_substage == sub_val),
        (mem_substage.delta() == 0x03),
    ])
    my_set.add_achievement(ach)

# Century King
ach = Achievement(id=630462, title="Century King", description="Defeat Shadow Moon and complete the game", points=5, badge="723523", type=AchievementType.WIN_CONDITION)
ach.add_core([(mem_stage == 0x14), (mem_game_state == 0x80), (mem_substage == 0x01), (mem_substage.delta() == 0x00)])
my_set.add_achievement(ach)

# 3. DESAFIOS DE SCORE
score_data = [
    (630472, "Earning Your Stripes", "Reach a score of 5,000 points", 2, 0x5000),
    (630473, "Gorgom's Nightmare", "Reach a score of 10,000 points", 2, 0x10000),
    (630474, "Child of the Sun", "Reach a score of 30,000 points", 5, 0x30000),
]

for a_id, title, desc, pts, tgt_score in score_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_score >= tgt_score),
        (mem_score.delta() < tgt_score),
        (mem_hp >= 0x01),
    ])
    my_set.add_achievement(ach)

# 4. DESAFIOS DE HP DOS CHEFES (Sturdy Armor, etc.)
hp_data = [
    (630511, "Sturdy Armor", "Defeat the Rhinoceros Mutant finishing with at least 50% of your maximum HP", 10, 0x06, None, 0x2d, 0x20),
    (630512, "Cracking the Shell", "Defeat the Tortoise Mutant finishing with at least 50% of your maximum HP", 10, 0x0a, None, 0x30, 0x20),
    (630513, "Pincer Movement", "Defeat the Crab Mutant finishing with at least 50% of your maximum HP", 10, 0x0c, 0x02, 0x30, 0x20),
    (630514, "Resisting Temptation", "Defeat High Priestess Bishum finishing with at least 50% of your maximum HP", 10, 0x10, 0x00, 0x40, 0x20),
    (630515, "Defying Gravity", "Defeat High Priest Darom finishing with at least 50% of your maximum HP", 25, 0x10, 0x01, 0x40, 0x20),
    (630516, "Breaking the Tusks", "Defeat High Priest Baraom finishing with at least 50% of your maximum HP", 25, 0x10, 0x02, 0x40, 0x20),
]

for a_id, title, desc, pts, stage, substage, max_bhp, min_hp in hp_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.MISSABLE)
    logic = [(mem_stage == stage)]
    
    if substage is not None:
        logic.append((mem_substage == substage))
        
    logic.extend([
        trigger(mem_boss_hp == 0x00),
        (mem_boss_hp.delta() == max_bhp).with_hits(1),
        (mem_hp >= min_hp),
        reset_if(mem_hp == 0x00),
    ])
    
    if substage is not None:
        logic.extend([and_next(mem_stage == stage), reset_if(mem_substage != substage)])
    else:
        logic.append(reset_if(mem_stage != stage))
        
    ach.add_core(logic)
    my_set.add_achievement(ach)

# 5. CONQUISTAS ÚNICAS
# The King of Creation
ach = Achievement(id=630463, title="The King of Creation", description="Complete the game without getting a Game Over to witness the True Ending", points=50, badge="723524", type=AchievementType.MISSABLE)
ach.add_core([
    and_next((mem_game_state == 0x80)),
    pause_if((mem_hp == 0x00).with_hits(1)),
    trigger((mem_stage == 0x14)),
    trigger((mem_substage == 0x01)),
    trigger((mem_substage.delta() == 0x00)),
])
ach.add_alt([
    and_next((mem_score == 0x00)),
    and_next((mem_hp == 0x00)),
    and_next((mem_timer == 0x00)),
    reset_if((mem_stage == 0x00)),
])
my_set.add_achievement(ach)

# Raw Strength
ach = Achievement(id=630464, title="Raw Strength", description="Defeat the Spider Mutant without using any Power Stripes", points=3, badge="723525", type=AchievementType.MISSABLE)
ach.add_core([
    (mem_stage == 0x00), (mem_substage == 0x40),
    trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x2d).with_hits(1),
    and_next(mem_game_state == 0xa0), and_next(byte(0x00e9) == 0x02), and_next((bit4(0x0073) == 0x01).with_hits(1)),
    reset_if(bit4(0x0073) == 0x00), reset_if(mem_hp == 0x00),
])
my_set.add_achievement(ach)

# Full Arsenal
ach = Achievement(id=630465, title="Full Arsenal", description="Defeat the Flea Mutant with all Option Charges at maximum", points=10, badge="723526")
ach.add_core([
    (mem_stage == 0x02), (mem_opt1 == 0x0e), (mem_opt2 == 0x0e), (mem_opt3 == 0x0e),
    trigger(mem_substage == 0x83), (mem_substage.delta() == 0x03),
])
my_set.add_achievement(ach)

# Blind Faith
ach = Achievement(id=630466, title="Blind Faith", description="Defeat the Crab Mutant without using any Option Charges", points=10, badge="723527", type=AchievementType.MISSABLE)
ach.add_core([
    trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x30).with_hits(1),
    (mem_stage == 0x0c), (mem_substage == 0x02),
    reset_if(mem_opt1 != 0x00), reset_if(mem_opt2 != 0x00), reset_if(mem_opt3 != 0x00), reset_if(mem_hp == 0x00),
])
my_set.add_achievement(ach)

# Bike Challenges (Road Warrior & Highway Star)
bike_data = [
    (630467, "Road Warrior", "Reach the boss in Stage 2-1 without taking damage or falling off the Battle Hopper", 10, "723528", 0x00),
    (630468, "Highway Star", "Reach the boss in Stage 2-3 without taking damage or falling off the Battle Hopper", 10, "723529", 0x02),
]
for a_id, title, desc, pts, badge, sub in bike_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.MISSABLE)
    ach.add_core([
        (mem_stage == 0x04), (mem_substage == sub),
        trigger(mem_boss_hp == 0x30), (mem_boss_hp.delta() == 0x00),
        and_next(mem_stage == 0x04), and_next(mem_substage == sub),
        pause_if((mem_hp < 0x42).with_hits(1)),
    ])
    ach.add_alt([reset_if(mem_hp == 0x00)])
    my_set.add_achievement(ach)

# Speedruns (Boss Battle Timer)
timer_data = [
    (630469, "Time is of the Essence", "Defeat the Bombyx Mutant in Stage 1-3 with at least 25 remaining on the Boss Battle Timer", 5, "723530", 0x42, 0x00, 0x19, 0x2d),
    (630470, "Rushed Extinction", "Defeat the Rhinoceros Mutant in Stage 2-4 with at least 25 remaining on the Boss Battle Timer", 10, "723531", 0x03, 0x06, 0x19, 0x2d),
    (630471, "No Time for Prayers", "Defeat High Priestess Bishum in Stage 5-1 with at least 20 remaining on the Boss Battle Timer", 10, "723532", 0x00, 0x10, 0x14, 0x40),
]
for a_id, title, desc, pts, badge, sub, stage, min_time, max_bhp in timer_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_substage == sub), (mem_stage == stage),
        reset_if(mem_timer < min_time),
        trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == max_bhp).with_hits(1),
        reset_if(mem_hp == 0x00),
    ])
    my_set.add_achievement(ach)

my_set.save()