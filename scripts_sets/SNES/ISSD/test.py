from pycheevos.core.helpers import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=286, title="International Superstar Soccer Deluxe")

# 1. ALIASES DE MEMÓRIA
mem_menu_opt  = byte(0x001e5e)
mem_chal_type = byte(0x00e52c)
mem_chal_diff = byte(0x00e52e)

# 2. DADOS DOS DESAFIOS (Nível, ID Nível, Memória Best Score, Target Score)
dribble_data = [
    ("Lv1", 0x00, word(0x00d8c4), 485),
    ("Lv2", 0x01, word(0x00d906), 492),
    ("Lv3", 0x02, word(0x00d948), 479),
    ("Lv4", 0x03, word(0x00d98a), 472),
]

pass_data = [
    ("Lv1", 0x00, word(0x00d8cf), 480),
    ("Lv2", 0x01, word(0x00d911), 479),
    ("Lv3", 0x02, word(0x00d953), 477),
    ("Lv4", 0x03, word(0x00d995), 487),
]

shoot_data = [
    ("Lv1", 0x00, word(0x00d8da), 550),
    ("Lv2", 0x01, word(0x00d91c), 540),
    ("Lv3", 0x02, word(0x00d95e), 524),
    ("Lv4", 0x03, word(0x00d9a0), 526),
]

defense_data = [
    ("Lv1", 0x00, word(0x00d8e5), 519),
    ("Lv2", 0x01, word(0x00d927), 505),
    ("Lv3", 0x02, word(0x00d969), 521),
    ("Lv4", 0x03, word(0x00d9ab), 523),
]

corner_data = [
    ("Lv1", 0x00, word(0x00d8f0), 518),
    ("Lv2", 0x01, word(0x00d932), 510),
    ("Lv3", 0x02, word(0x00d974), 504),
    ("Lv4", 0x03, word(0x00d9b6), 478),
]

free_data = [
    ("Lv1", 0x00, word(0x00d8fb), 514),
    ("Lv2", 0x01, word(0x00d93d), 510),
    ("Lv3", 0x02, word(0x00d97f), 478),
    ("Lv4", 0x03, word(0x00d9c1), 542),
]

# 3. GERAÇÃO DINÂMICA
for level_name, diff_val, mem_score, target_score in free_data:
    ach = Achievement(
        id=0,
        title=f"Dribble Master {level_name}",
        description=f"Beat the high score of {target_score} in the Dribble Challenge {level_name}",
        points=5
    )
    
    ach.add_core([
        (mem_chal_type == 0x05),
        (mem_chal_diff == diff_val),
        (mem_menu_opt == 0x06),
        trigger(mem_score > target_score),
        (mem_score.delta() <= target_score)
    ])
    
    my_set.add_achievement(ach)

my_set.save()