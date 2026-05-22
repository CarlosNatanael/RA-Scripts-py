from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=10764, title="The Cyber Shinobi")

# 1. ALIASES DE MEMÓRIA
mem_pause    = byte(0x0001)
mem_state    = byte(0x0002)
mem_stage    = byte(0x000c)
mem_substage = byte(0x000d)
mem_lives    = byte(0x000e)
mem_power    = byte(0x0010)
mem_ninjutsu = byte(0x0011)
mem_weapon   = byte(0x0012)
mem_time_min = byte(0x0016)
mem_score_10k= byte(0x001b)
mem_score_100k= byte(0x001c)
mem_enemies  = byte(0x0025)
mem_hp       = byte(0x011c)

# 2. PROGRESSÃO DE FASES
prog_data = [
    (610591, "Construction Breach", "Complete Stage 1", 1, 0, AchievementType.PROGRESSION),
    (610592, "Plutonium Docks", "Complete Stage 2", 1, 1, AchievementType.PROGRESSION),
    (610593, "Corrupted Countryside", "Complete Stage 3", 2, 2, AchievementType.PROGRESSION),
    (610594, "Synthetic Jungle", "Complete Stage 4", 2, 3, AchievementType.PROGRESSION),
    (610595, "Toxic Waterfall", "Complete Stage 5", 2, 4, AchievementType.PROGRESSION),
    (610596, "Zeed's Downfall", "Complete Stage 6 Enemy Hideout and finish the game", 5, 5, AchievementType.WIN_CONDITION),
]

for a_id, title, desc, pts, stage, a_type in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=a_type)
    ach.add_core([
        (mem_stage == stage),
        (mem_state.delta() != 0x14),
        (mem_state == 0x14),
    ])
    my_set.add_achievement(ach)

# 3. SCORE (PONTUAÇÃO)
score_data = [
    (610597, "Ninja Apprentice", "Reach 10,000 points", 1, mem_score_10k, 1),
    (610598, "Zeed's Nightmare", "Reach 100,000 points", 2, mem_score_100k, 1),
    (610599, "Musashi's Legacy", "Reach 500,000 points", 5, mem_score_100k, 5),
]

for a_id, title, desc, pts, mem_addr, target in score_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        or_next(mem_state == 0x05),
        (mem_state == 0x14),
        (mem_addr >= target),
        (mem_addr.delta() < target),
    ])
    my_set.add_achievement(ach)

# 4. SWEEP
sweep_data = [
    (610600, "Site Sweep", "Defeat 21 enemies in Stage 1", 5, 0, 21),
    (610601, "Port Authority", "Defeat 55 enemies in Stage 2", 5, 1, 55),
    (610602, "Field Execution", "Defeat 6 enemies in Stage 3", 10, 2, 6),
    (610603, "Jungle Warfare", "Defeat 26 enemies in Stage 4", 10, 3, 26),
    (610604, "Waterfall Ambush", "Defeat 15 enemies in Stage 6", 10, 5, 15),
]

for a_id, title, desc, pts, stage, target in sweep_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.MISSABLE)
    ach.add_core([
        measured_if(mem_stage == stage),
        (mem_state == 0x05),
        measured(mem_enemies >= target),
        (mem_enemies.delta() < target),
    ])
    my_set.add_achievement(ach)

# 5. UPGRADES (LEVEL 8)
upgrade_data = [
    (610605, "Ancestral Blade", "Reach level 8 in Melee Power", 10, mem_power, 8),
    (610606, "Master of Elements", "Obtain the Earth Ninjutsu Level 8", 10, mem_ninjutsu, 8),
    (610607, "Shuriken Launcher", "Reach level 8 with the Shuriken", 1, mem_weapon, 8),
    (610608, "Laser Vulcan", "Reach level 8 with the Laser Vulcan", 2, mem_weapon, 16),
    (610609, "Supergrenade", "Reach level 8 with the Supergrenade", 5, mem_weapon, 24),
]

for a_id, title, desc, pts, mem_addr, target in upgrade_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_state == 0x05),
        measured(mem_addr == target) if a_id in (610605, 610606) else (mem_addr == target),
        (mem_addr.delta() < target),
    ])
    my_set.add_achievement(ach)

# The Cyber Shinobi
ach = Achievement(id=610610, title="The Cyber Shinobi", description="Reach level 8 in Power and Ninjutsu", points=25)
ach.add_core([
    (mem_state == 0x05),
    (mem_power == 0x08), (mem_power.delta() < 0x08),
    (mem_ninjutsu == 0x08), (mem_ninjutsu.delta() < 0x08),
])
my_set.add_achievement(ach)

# 6. FLAWLESS
# Os Bosses das Fases 3, 4, 5 e 6 usam a Área 2 (Substage = 1). As Fases 1 e 2 usam Área 3 (Substage = 2).
flawless_data = [
    (610611, "Flawless Blueprint", "Defeat the Stage 1 Boss without taking damage", 10, 0, 2),
    (610612, "Flawless Docking", "Defeat the Stage 2 Boss without taking damage", 10, 1, 2),
    (610613, "Flawless Field", "Defeat the Stage 3 Boss without taking damage", 10, 2, 1),
    (610614, "Flawless Tropics", "Defeat the Stage 4 Boss without taking damage", 25, 3, 1),
    (610615, "Flawless Flow", "Defeat the Stage 5 Boss without taking damage", 25, 4, 1),
    (610616, "Flawless Vengeance", "Defeat the Final Boss without taking damage", 50, 5, 1),
]

for a_id, title, desc, pts, stage, target_sub in flawless_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        and_next(mem_state.delta() == 0x05),
        and_next(mem_state == 0x05),
        pause_if((mem_hp < mem_hp.delta()).with_hits(1)),
        (mem_stage == stage),
        (mem_state.delta() != 0x14),
        trigger(mem_state == 0x14),
    ])
    ach.add_alt([
        or_next(mem_substage != target_sub),
        reset_if(mem_lives < mem_lives.delta()),
    ])
    my_set.add_achievement(ach)

# 7. DESAFIOS ESPECIAIS
# Conserving Chakra
ach = Achievement(id=610617, title="Conserving Chakra", description="Complete Stage 2 without using any Ninjutsu", points=10)
ach.add_core([
    pause_if((mem_state == 0x09).with_hits(1)),
    (mem_stage == 0x01),
    (mem_state.delta() != 0x14),
    trigger(mem_state == 0x14),
])
ach.add_alt([reset_if(mem_stage != 0x01)])
my_set.add_achievement(ach)

# Way of the Sword
ach = Achievement(id=610618, title="Way of the Sword", description="Defeat the Stage 1 Boss using only melee attacks, without firing your Sub-Weapon", points=10)
ach.add_core([
    pause_if((mem_weapon < mem_weapon.delta()).with_hits(1)),
    (mem_stage == 0x00),
    (mem_state.delta() != 0x14),
    trigger(mem_state == 0x14),
])
ach.add_alt([reset_if(mem_substage != 0x02)])
my_set.add_achievement(ach)

# Plutonium Rush
ach = Achievement(id=610619, title="Plutonium Rush", description="Complete Stage 1 with at least 04:00 time remaining on the clock", points=5)
ach.add_core([(mem_stage == 0x00), (mem_state.delta() != 0x14), trigger(mem_state == 0x14), (mem_time_min >= 0x04)])
my_set.add_achievement(ach)

# The only Hope (No Continues)
ach = Achievement(id=610620, title="The only Hope", description="Complete the game without using any Continues", points=50)
ach.add_core([
    pause_if((mem_state == 0x1a).with_hits(1)),
    or_next(mem_pause == 0x02),
    (mem_pause == 0x00),
    (mem_state.delta() != 0x16),
    trigger(mem_state == 0x16),
])
ach.add_alt([reset_if(mem_state == 0x01)])
my_set.add_achievement(ach)

my_set.save()