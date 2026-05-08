from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=14286, title="Imported Set")

# 1. ALIASES DE MEMÓRIA
mem_stage = byte(0x1a93)
mem_state = byte(0x1d22)
mem_diff  = byte(0x1d0f)
mem_cont  = byte(0x1d10)
mem_hp    = byte(0x0320)

# Endereços do Score (Nibbles/Low4)
score_high = low4(0x1d59)
score_low  = low4(0x1d58)


# 2. PROGRESSÃO (Stages Completos)
prog_data = [
    (606954, "First Assembly", "Complete Stage 1", 2, "00000", 0x06, AchievementType.PROGRESSION),
    (606955, "The Plot Thickens", "Complete Stage 2", 3, "00000", 0x0c, AchievementType.PROGRESSION),
    (606956, "Midway Battle", "Complete Stage 3", 5, "00000", 0x11, AchievementType.PROGRESSION),
    (606957, "Nearing the End", "Complete Stage 4", 5, "00000", 0x17, AchievementType.PROGRESSION),
    (606958, "Earth's Mightiest Heroes", "Complete Stage 5 and save the day", 10, "00000", 0x1d, AchievementType.WIN_CONDITION),
]

for a_id, title, desc, pts, badge, target_stage, a_type in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=a_type)
    ach.add_core([
        (mem_stage == target_stage),
        (mem_stage.delta() == (target_stage - 1)),
        (mem_state == 0x07)
    ])
    my_set.add_achievement(ach)


# 3. MISC & DESAFIOS GERAIS
# --- The Ultimate Challenge ---
ach = Achievement(id=606959, title="The Ultimate Challenge", description="Complete the game on Challenge difficulty", points=50, badge="00000")
ach.add_core([
    (mem_diff == 0x02),
    or_next(mem_state == 0x03),
    (mem_state == 0x07),
    trigger(mem_stage == 0x1d),
    trigger(mem_stage.delta() == 0x1c)
])
my_set.add_achievement(ach)

# --- True Avenger ---
ach = Achievement(id=606960, title="True Avenger", description="Complete the entire game without using any continues", points=25, badge="00000")
ach.add_core([
    pause_if((mem_cont < mem_cont.delta()).with_hits(1)),
    (mem_stage == 0x00).with_hits(1),
    (mem_state == 0x03).with_hits(1),
    (mem_state == 0x03),
    trigger(mem_stage.delta() == 0x1c),
    trigger(mem_stage == 0x1d)
])
ach.add_alt([reset_if(mem_state == 0x01)])
my_set.add_achievement(ach)

# --- Super Soldier ---
ach = Achievement(id=606961, title="Super Soldier", description="Reach the maximum health limit of 255 HP", points=5, badge="00000")
ach.add_core([(mem_state >= 0x03), (mem_hp.delta() < 0xff), (mem_hp == 0xff)])
my_set.add_achievement(ach)

# --- Heart of a Hero ---
ach = Achievement(id=606962, title="Heart of a Hero", description="Collect 1 extra hearts during a single session to extend your mission", points=1, badge="00000")
ach.add_core([
    reset_if(mem_state == 0x01),
    pause_if(mem_state != 0x03),
    (mem_cont > mem_cont.delta()).with_hits(1)
])
my_set.add_achievement(ach)


# 4. MARCOS DE PONTUAÇÃO (SCORE)
def create_score_ach(a_id, title, desc, pts, logic):
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge="00000")
    ach.add_core([(mem_state >= 0x03), (mem_state <= 0x07)] + logic)
    my_set.add_achievement(ach)

create_score_ach(606963, "Rookie Hero", "Reach 10,000 points", 2, [
    (score_high == 0x00), (score_low.delta() == 0x00), (score_low >= 0x01)
])
create_score_ach(606964, "Seasoned Fighter", "Reach 30,000 points", 3, [
    (score_high == 0x00), (score_low.delta() < 0x03), (score_low >= 0x03)
])
create_score_ach(606965, "Vibranium Tier", "Reach 50,000 points", 5, [
    (score_high == 0x00), (score_low.delta() < 0x05), (score_low >= 0x05)
])
create_score_ach(606966, "Avenger Prime", "Reach 100,000 points", 10, [
    (score_high.delta() == 0x00), (score_high >= 0x01)
])


# 5. CHEFES SEM DANO (Missables)
boss_data = [
    (606967, "Dodging Light", "Defeat Living Laser in Stage 1...", 5, 0x02),
    (606968, "Calming the Storm", "Defeat Whirlwind in Stage 1...", 5, 0x05),
    (606969, "Unstoppable Force, Untouchable Hero", "Defeat Juggernaut in Stage 2...", 10, 0x08),
    (606970, "Cheating Death", "Defeat Grim Reaper in Stage 2...", 10, 0x0b),
    (606971, "Lights Out", "Defeat Living Laser in Stage 3...", 10, 0x10),
    (606972, "The Juggernaut Falls", "Defeat Juggernaut in Stage 4...", 10, 0x13),
    (606973, "System Override", "Defeat Ultron in Stage 4...", 10, 0x16),
    (606974, "Bones to Pick", "Defeat Crossbones in Stage 5...", 25, 0x19),
    (606975, "Hail... Nothing!", "Defeat Red Skull in Stage 5...", 25, 0x1c),
]

for a_id, title, desc, pts, delta_stage in boss_data:
    ach = Achievement(id=a_id, title=title, description=desc.replace("...", " without taking any damage on Normal or Challenge difficulty"), points=pts, badge="00000", type=AchievementType.MISSABLE)
    ach.add_core([
        pause_if((mem_hp < mem_hp.delta()).with_hits(1)),
        (mem_stage.delta() == delta_stage),
        (mem_diff >= 0x01),
        trigger(mem_stage == (delta_stage + 1))
    ])
    ach.add_alt([
        or_next(mem_state == 0x01),
        reset_if(mem_hp == 0x00)
    ])
    my_set.add_achievement(ach)

my_set.save()