from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=26225, title="Kenyuu Densetsu Yaiba")

# 1. ALIASES DE MEMÓRIA
mem_stage       = byte(0x0013)
mem_stage_flag  = byte(0x1e42)
mem_hp          = byte(0x0b77)
mem_continues   = byte(0x00c3)
mem_score       = word(0x000d)
mem_lives       = byte(0x0016)
mem_spirit      = byte(0x0009)
mem_sword_pwr   = byte(0x00f7)

# 2. BLOCOS REUTILIZÁVEIS
# Várias conquistas falham se o jogador usar um Continue ou voltar ao ecrã inicial
alt_no_continue = [
    or_next(mem_continues < mem_continues.delta()),
    reset_if(mem_stage == 0x00),
]

# 3. PROGRESSÃO DA HISTÓRIA
prog_data = [
    (622152, "The Raijin Awakens", "Complete Stage 1", 1, 0x0a, AchievementType.PROGRESSION),
    (622153, "Trials of the Dragon Orb", "Complete Stage 2", 2, 0x1d, AchievementType.PROGRESSION),
    (622154, "Infiltrating Onimaru's Fortress", "Complete Stage 3", 2, 0x25, AchievementType.PROGRESSION),
    (622155, "Kenyuu Densetsu", "Complete Stage 4", 5, 0x30, AchievementType.WIN_CONDITION),
]

for a_id, title, desc, pts, st_val, a_type in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=a_type)
    ach.add_core([
        (mem_stage == st_val),
        (mem_stage.delta() == st_val - 1),
        (mem_stage_flag == 0x01),
    ])
    my_set.add_achievement(ach)

# 4. CHEFES SEM DANO (MISSABLES)
boss_data = [
    (622156, "Dodging the Swallow Cut", "Defeat Kojiro Sasaki without taking any damage", 5, 0x09),
    (622157, "Taming the One-Eyed Wolf", "Defeat Jubei without taking any damage", 10, 0x1a),
    (622158, "Conquering the Fujin Sword", "Defeat Takeshi Onimaru without taking any damage", 25, 0x30),
]

for a_id, title, desc, pts, st_val in boss_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.MISSABLE)
    ach.add_core([
        trigger(mem_stage == st_val),
        (mem_stage.delta() == st_val - 1),
        and_next(mem_stage == st_val - 1),
        pause_if((mem_hp < mem_hp.delta()).with_hits(1)),
    ])
    ach.add_alt(alt_no_continue)
    my_set.add_achievement(ach)

# 5. DESAFIOS DOS MINIJOGOS (MISSABLES)
mini_data = [
    (622159, "Mastering the Toad", "Complete the Geroda minigame with at least 3 blocks of health remaining", 10, 0x04, (mem_hp == 0x02).with_hits(1)),
    (622160, "Riding the Fierce Tiger", "Complete the Kagetora minigame flawlessly", 5, 0x06, (mem_hp < mem_hp.delta()).with_hits(2)),
    (622161, "Deflecting the Wind", "Complete the Gekko vs Takeshi Onimaru with at least 3 blocks of health remaining", 10, 0x20, (mem_hp == 0x02).with_hits(1)),
    (622162, "Soaring with Shonosuke", "Complete the Shonosuke minigame flawlessly", 5, 0x2c, (mem_hp < mem_hp.delta()).with_hits(2)),
]

for a_id, title, desc, pts, st_val, hit_cond in mini_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.MISSABLE)
    ach.add_core([
        trigger(mem_stage == st_val),
        (mem_stage.delta() == st_val - 1),
        and_next(mem_stage == st_val - 1),
        pause_if(hit_cond), # CORRIGIDO AQUI!
    ])
    ach.add_alt(alt_no_continue)
    my_set.add_achievement(ach)

# 6. MARCOS DE PONTUAÇÃO (SCORE)
score_data = [
    (622163, "Jungle Boy", "Reach a score of 5,000", 2, 0x0500),
    (622164, "Kendo Prodigy", "Reach a score of 15,000", 3, 0x1500),
    (622165, "The Legendary Samurai", "Reach a score of 50,000", 5, 0x5000),
]

for a_id, title, desc, pts, score_val in score_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        (mem_score >= score_val),
        (mem_score.delta() < score_val),
        (mem_stage != 0x00),
    ])
    my_set.add_achievement(ach)

# 7. DESAFIOS DIVERSOS (MISC)
ach = Achievement(id=622166, title="Kurogane Resilience", description="Accumulate 5 extra lives at the same time", points=2)
ach.add_core([
    (mem_lives == 0x05),
    (mem_lives.delta() == 0x04),
    (mem_stage != 0x00),
])
my_set.add_achievement(ach)

ach = Achievement(id=622167, title="Samurai Damashii", description="Reach a Fighting Spirit of 60 or higher", points=5)
ach.add_core([
    (mem_spirit >= 0x60),
    (mem_spirit.delta() != 0x60),
    (mem_stage != 0x00),
])
my_set.add_achievement(ach)

ach = Achievement(id=622168, title="Bare Blade", description="Defeat Kojiro Sasaki with the Sword Power set to No Power", points=2)
ach.add_core([
    trigger(mem_stage == 0x09),
    (mem_stage.delta() == 0x08),
    (mem_sword_pwr == 0x00),
])
my_set.add_achievement(ach)

ach = Achievement(id=622169, title="Sayaka's True Hero", description="Choose to save your friends instead of taking the Power Orb in Stage 2", points=1)
ach.add_core([
    (mem_stage == 0x1d),
    (mem_stage.delta() == 0x1c),
    and_next(mem_stage == 0x1c),
    pause_if((mem_lives < mem_lives.delta()).with_hits(1)), # CORRIGIDO AQUI!
])
ach.add_alt(alt_no_continue)
my_set.add_achievement(ach)

ach = Achievement(id=622174, title="Heir of the Dragon God", description="Complete the game without getting a Game Over", points=25)
ach.add_core([
    trigger(mem_stage == 0x30),
    (mem_stage.delta() != 0x30),
    reset_next_if(mem_stage == 0x00),
    pause_if((mem_continues < mem_continues.delta()).with_hits(1)), # CORRIGIDO AQUI!
])
my_set.add_achievement(ach)

# 8. SPEEDRUNS
speed_data = [
    (622170, "Swift as a Jungle Boy I", "Speedrun Stage 1-1 and beat the Developer time", 2, 0x02, 2300),
    (622171, "Swift as a Jungle Boy II", "Speedrun Stage 2-2 and beat the Developer time", 2, 0x0d, 600),
    (622172, "Swift as a Jungle Boy III", "Speedrun Stage 2-4 and beat the Developer time", 2, 0x11, 600),
    (622173, "Swift as a Jungle Boy IV", "Speedrun Stage 2-6 and beat the Developer time", 2, 0x15, 1100),
]

for a_id, title, desc, pts, st_val, ticks in speed_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([
        trigger(mem_stage == st_val),
        (mem_stage.delta() == st_val - 1),
        reset_next_if(mem_stage == 0x00),
        pause_if((mem_stage == st_val - 1).with_hits(ticks)),
    ])
    my_set.add_achievement(ach)

my_set.save()