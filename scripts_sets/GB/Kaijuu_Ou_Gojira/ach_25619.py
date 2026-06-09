from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=25619, title="Kaijuu Ou Gojira")

# 1. ALIASES DE MEMÓRIA
mem_debug       = byte(0x00df05)
mem_stage       = byte(0x00da2c)
mem_continues   = byte(0x00db37)
mem_hp          = byte(0x00ffb9)
mem_beam_attack = bit0(0x00da02)

# Endereços de "Estado" do Chefe (Atualizados)
mem_boss_state_a = byte(0x00dd34)
mem_boss_state_b = byte(0x00dc34)

# 2. PROGRESSÃO
prog_data = [
    (614165, "Battle for Osaka", "Defeat Mothra and clear Level 1", 2, "696649", 0x00, 0x01),
    (614166, "Battle for Lake Ashino", "Defeat Biollante and clear Level 2", 2, "696650", 0x01, 0x02),
    (614167, "Battle for Mt. Fuji", "Defeat Hedorah and clear Level 3", 2, "696651", 0x02, 0x03),
    (614168, "Battle for Nagoya", "Defeat Mecha-King Ghidorah and clear Level 4", 5, "696652", 0x03, 0x04),
]

for a_id, title, desc, pts, badge, st_from, st_to in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_debug == 0x00),
        (mem_stage.delta() == st_from),
        (mem_stage == st_to),
    ])
    my_set.add_achievement(ach)

# Battle for Tokyo (Win Condition) - Atualizado com Reset no HP
ach = Achievement(id=614169, title="Battle for Tokyo", description="Defeat Super Mechagodzilla and clear Level 5", points=10, badge="696653", type=AchievementType.WIN_CONDITION)
ach.add_core([
    reset_if(mem_hp == 0x00),
    (mem_debug == 0x00),
    (mem_stage.delta() == 0x04).with_hits(1),
    (mem_stage == 0x00),
])
my_set.add_achievement(ach)

# 3. CONDIÇÕES ESPECIAIS E HP
ach = Achievement(id=614170, title="King of the Monsters", description="Complete the entire game without using any continues", points=50, badge="696661")
ach.add_core([
    (mem_debug == 0x00),
    (mem_continues == 0x00),
    trigger(mem_stage.delta() == 0x04),
    trigger(mem_stage == 0x00),
])
my_set.add_achievement(ach)

hp_data = [
    (614171, "Apex of Osaka", "Clear Level 1 maintaining at least 50% HP", 5, "696662", 0x00, 0x01),
    (614172, "Ashino's True Alpha", "Clear Level 2 maintaining at least 50% HP", 5, "696656", 0x01, 0x02),
    (614173, "Fuji's Invincible Menace", "Clear Level 3 maintaining at least 50% HP", 10, "696658", 0x02, 0x03),
    (614174, "Nagoya's Absolute God", "Clear Level 4 maintaining at least 50% HP", 10, "696659", 0x03, 0x04),
    (614175, "Unstoppable in Tokyo", "Clear Level 5 maintaining at least 50% HP", 25, "696660", 0x04, 0x00),
]

for a_id, title, desc, pts, badge, st_from, st_to in hp_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_debug == 0x00),
        (mem_hp >= 0x80),
        (mem_stage.delta() == st_from),
        trigger(mem_stage == st_to),
    ])
    my_set.add_achievement(ach)

# 4. DESAFIOS FÍSICOS (NO BEAM ATTACK)
phys_data = [
    (614176, "Wing Breaker", "Defeat Battra using only physical attacks", 5, "696691", 0x00, mem_boss_state_a, 0x84),
    (614177, "Scrap Metal", "Defeat Jet Jaguar using only physical attacks", 10, "696692", 0x03, mem_boss_state_b, 0x19),
    (614178, "Cyborg Smasher", "Defeat Gigan using only physical attacks", 10, "696693", 0x03, mem_boss_state_a, 0x92),
    (614179, "The Real Deal", "Defeat Fake Godzilla using only physical attacks", 10, "696694", 0x04, mem_boss_state_a, 0x96),
]

for a_id, title, desc, pts, badge, stage, mem_boss, state_val in phys_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    
    # Lógica Central
    ach.add_core([
        and_next(mem_boss == state_val),
        pause_if((mem_beam_attack == 0x01).with_hits(1)),
        (mem_debug == 0x00),
        (mem_stage == stage),
        (mem_boss.delta() == state_val),
        trigger(mem_boss == 0x00),
    ])
    
    # Grupo Alt para Resetar
    ach.add_alt([
        reset_if(mem_stage != stage),
    ])
    
    my_set.add_achievement(ach)

my_set.save()