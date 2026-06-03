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

mem_boss_hp_a   = byte(0x00dd43)
mem_boss_hp_b   = byte(0x00dc43)

# 2. PROGRESSÃO
prog_data = [
    (614165, "Battle for Osaka", "Defeat Mothra and clear Level 1", 2, 0, 1),
    (614166, "Battle for Lake Ashino", "Defeat Biollante and clear Level 2", 2, 1, 2),
    (614167, "Battle for Mt. Fuji", "Defeat Hedorah and clear Level 3", 2, 2, 3),
    (614168, "Battle for Nagoya", "Defeat Mecha-King Ghidorah and clear Level 4", 5, 3, 4),
]

for a_id, title, desc, pts, st_from, st_to in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_debug == 0x00),
        (mem_stage.delta() == st_from),
        (mem_stage == st_to),
    ])
    my_set.add_achievement(ach)

# Battle for Tokyo (Win Condition)
ach = Achievement(id=614169, title="Battle for Tokyo", description="Defeat Super Mechagodzilla and clear Level 5", points=10, type=AchievementType.WIN_CONDITION)
ach.add_core([
    (mem_debug == 0x00),
    (mem_stage.delta() == 0x04),
    (mem_stage == 0x00),
])
my_set.add_achievement(ach)

# 3. CONDIÇÕES ESPECIAIS E HP
ach = Achievement(id=614170, title="King of the Monsters", description="Complete the entire game without using any continues", points=25)
ach.add_core([
    (mem_debug == 0x00),
    (mem_continues == 0x00),
    trigger(mem_stage.delta() == 0x04),
    trigger(mem_stage == 0x00),
])
my_set.add_achievement(ach)

hp_data = [
    (614171, "Apex of Osaka", "Clear Level 1 maintaining at least 50% HP", 5, 0, 1),
    (614172, "Ashino's True Alpha", "Clear Level 2 maintaining at least 50% HP", 5, 1, 2),
    (614173, "Fuji's Invincible Menace", "Clear Level 3 maintaining at least 50% HP", 10, 2, 3),
    (614174, "Nagoya's Absolute God", "Clear Level 4 maintaining at least 50% HP", 10, 3, 4),
    (614175, "Unstoppable in Tokyo", "Clear Level 5 maintaining at least 50% HP", 25, 4, 0),
]

for a_id, title, desc, pts, st_from, st_to in hp_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_debug == 0x00),
        (mem_hp >= 0x80),
        (mem_stage.delta() == st_from),
        trigger(mem_stage == st_to),
    ])
    my_set.add_achievement(ach)

# 4. DESAFIOS FÍSICOS (NO BEAM ATTACK)
phys_data = [
    (614176, "Wing Breaker", "Defeat Battra using only physical attacks", 5, 0, mem_boss_hp_a, 0xc8),
    (614177, "Scrap Metal", "Defeat Jet Jaguar using only physical attacks", 10, 3, mem_boss_hp_b, 0x5e),
    (614178, "Cyborg Smasher", "Defeat Gigan using only physical attacks", 5, 3, mem_boss_hp_a, 0xb8),
]

for a_id, title, desc, pts, stage, mem_boss, max_hp in phys_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_debug == 0x00),
        (mem_stage == stage),
        (mem_boss == max_hp).with_hits(1),
        reset_if(mem_beam_attack == 0x01),
        (mem_boss.delta() != 0x00),
        trigger(mem_boss == 0x00),
    ])
    my_set.add_achievement(ach)

# The Real Deal (Necessita de validação dupla no HP: 0xe0 e 0xf0)
ach = Achievement(id=614179, title="The Real Deal", description="Defeat Fake Godzilla using only physical attacks", points=10)
ach.add_core([
    (mem_debug == 0x00),
    (mem_stage == 0x04),
    (mem_boss_hp_a == 0xe0).with_hits(1),
    (mem_boss_hp_a == 0xf0).with_hits(1),
    reset_if(mem_beam_attack == 0x01),
    (mem_boss_hp_a.delta() != 0x00),
    trigger(mem_boss_hp_a == 0x00),
])
my_set.add_achievement(ach)

my_set.save()