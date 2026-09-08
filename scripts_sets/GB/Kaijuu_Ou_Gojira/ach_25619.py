from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=25619, title="Godzilla - Refactored")

# 1. ALIASES DE MEMÓRIA
mem_demo      = byte(0x00df05)
mem_level     = byte(0x00da2c)
mem_hp        = byte(0x00ffb9)
mem_continues = byte(0x00db37)
mem_special   = bit0(0x00da02)

mem_boss_hp1  = byte(0x00dd34)
mem_boss_hp2  = byte(0x00dc34) # Usado especificamente pelo Jet Jaguar

# 2. PROGRESSÃO NORMAL (Stages 1 a 4)
prog_data = [
    (614165, "Battle for Osaka", "Defeat Mothra and clear Level 1", 2, "696649", 0x00, 0x01),
    (614166, "Battle for Lake Ashino", "Defeat Biollante and clear Level 2", 2, "696650", 0x01, 0x02),
    (614167, "Battle for Mt. Fuji", "Defeat Hedorah and clear Level 3", 2, "696651", 0x02, 0x03),
    (614168, "Battle for Nagoya", "Defeat Mecha-King Ghidorah and clear Level 4", 5, "696652", 0x03, 0x04),
]

for a_id, title, desc, pts, badge, prev_lvl, curr_lvl in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_demo == 0x00),
        (mem_level.delta() == prev_lvl),
        (mem_level == curr_lvl),
    ])
    my_set.add_achievement(ach)

# Battle for Tokyo
ach_tokyo = Achievement(id=614169, title="Battle for Tokyo", description="Defeat Super Mechagodzilla and clear Level 5", points=10, badge="696653", type=AchievementType.WIN_CONDITION)
ach_tokyo.add_core([
    reset_if(mem_hp == 0x00),
    (mem_demo == 0x00),
    (mem_level.delta() == 0x04).with_hits(1),
    (mem_level == 0x00),
])
my_set.add_achievement(ach_tokyo)

# King of the Monsters (No Continues)
ach_no_cont = Achievement(id=614170, title="King of the Monsters", description="Complete the entire game without using any continues", points=50, badge="696661")
ach_no_cont.add_core([
    (mem_demo == 0x00),
    (mem_continues == 0x00),
    trigger(mem_level.delta() == 0x04),
    trigger(mem_level == 0x00),
])
my_set.add_achievement(ach_no_cont)

# 3. DESAFIOS DE HP (>= 50% HP)
hp_data = [
    (614171, "Apex of Osaka", "Clear Level 1 maintaining at least 50% HP", 5, "696662", 0x00, 0x01),
    (614172, "Ashino's True Alpha", "Clear Level 2 maintaining at least 50% HP", 5, "696656", 0x01, 0x02),
    (614173, "Fuji's Invincible Menace", "Clear Level 3 maintaining at least 50% HP", 10, "696658", 0x02, 0x03),
    (614174, "Nagoya's Absolute God", "Clear Level 4 maintaining at least 50% HP", 10, "696659", 0x03, 0x04),
    (614175, "Unstoppable in Tokyo", "Clear Level 5 maintaining at least 50% HP", 25, "696660", 0x04, 0x00), # Nível 5 reseta para 0
]

for a_id, title, desc, pts, badge, prev_lvl, curr_lvl in hp_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_demo == 0x00),
        (mem_hp >= 0x80),
        (mem_level.delta() == prev_lvl),
        trigger(mem_level == curr_lvl),
    ])
    my_set.add_achievement(ach)

# 4. DESAFIOS FÍSICOS (No Special Attacks)
# Dados: (ID, Title, Desc, Pts, Badge, Enemy HP Address, Starting Boss HP, Level ID)
phys_data = [
    (614176, "Wing Breaker", "Defeat Battra using only physical attacks", 5, "696691", mem_boss_hp1, 0x84, 0x00),
    (614177, "Scrap Metal", "Defeat Jet Jaguar using only physical attacks", 10, "696692", mem_boss_hp2, 0x19, 0x03),
    (614178, "Cyborg Smasher", "Defeat Gigan using only physical attacks", 10, "696693", mem_boss_hp1, 0x92, 0x03),
    (614179, "The Real Deal", "Defeat Fake Godzilla using only physical attacks", 10, "696694", mem_boss_hp1, 0x96, 0x04),
]

for a_id, title, desc, pts, badge, hp_addr, boss_hp_val, lvl in phys_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    
    # Lógica base
    ach.add_core([
        and_next(hp_addr == boss_hp_val),
        pause_if((mem_special == 0x01).with_hits(1)),
        (mem_demo == 0x00),
        (mem_level == lvl),
        (hp_addr.delta() == boss_hp_val),
        trigger(hp_addr == 0x00),
    ])
    
    # Alt para reset se sair do nível
    ach.add_alt([
        reset_if(mem_level != lvl)
    ])
    
    my_set.add_achievement(ach)

my_set.save()