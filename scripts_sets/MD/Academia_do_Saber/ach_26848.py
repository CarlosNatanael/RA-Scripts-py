from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=26848, title="Alistamento Militar")

# 1. ALIASES DE MEMÓRIA
mem_state   = byte(0x001a5e) # 0x09 = Em Missão/Minijogo
mem_mission = byte(0x001a6b) # 0=Swamp, 1=Caatinga, 2=Jungle
mem_rank    = byte(0x001a6a)
mem_mg_id   = byte(0x005bcb)
mem_timer   = word(0x001a66)

cond_in_mission = (mem_state == 0x09)

# 2. PATENTES (RANKS)
ranks_data = [
    (623939, "Earning Your Stripes", "Reach the rank of Sergeant", 1, "709333", 0x03, AchievementType.STANDARD),
    (623940, "Officer Material", "Reach the rank of Warrant Officer", 1, "709334", 0x04, AchievementType.STANDARD),
    (623941, "Tactical Command", "Reach the rank of First Lieutenant", 2, "709335", 0x07, AchievementType.STANDARD),
    (623942, "Leading the Charge", "Reach the rank of Captain", 5, "709336", 0x08, AchievementType.STANDARD),
    (623943, "Field Commander", "Reach the rank of Major", 5, "709337", 0x09, AchievementType.STANDARD),
    (623944, "Superior Officer", "Reach the rank of Lieutenant Colonel", 5, "709338", 0x0a, AchievementType.STANDARD),
    (623945, "The Colonel", "Reach the rank of Colonel", 5, "709339", 0x0b, AchievementType.STANDARD),
    (623946, "One-Star General", "Reach the rank of Brigade General", 5, "709340", 0x0c, AchievementType.STANDARD),
    (623947, "Two-Star General", "Reach the rank of Division General", 5, "709341", 0x0d, AchievementType.STANDARD),
    (623948, "Supreme Commander", "Reach the maximum rank of Army General and beat the game", 10, "709342", 0x0e, AchievementType.WIN_CONDITION),
]

for r_id, title, desc, pts, badge, rank_val, a_type in ranks_data:
    ach = Achievement(id=r_id, title=title, description=desc, points=pts, badge=badge, type=a_type)
    ach.add_core([
        cond_in_mission,
        (mem_rank == rank_val),
        (mem_rank.delta() != rank_val),
    ])
    my_set.add_achievement(ach)

# 3. MISSÕES (PROGRESSÃO)
missions_data = [
    (623936, "Swamp Survivor", "Successfully complete all minigames in the Swamp mission", 1, "709330", 0x00, byte(0x005b4a)),
    (623937, "Drylands Explorer", "Successfully complete all minigames in the Caatinga mission", 2, "709331", 0x01, byte(0x00572a)),
    (623938, "Jungle Operative", "Successfully complete all minigames in the Jungle mission", 2, "709332", 0x02, byte(0x0054af)),
]

for m_id, title, desc, pts, badge, mission_val, mem_flag in missions_data:
    ach = Achievement(id=m_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_mission == mission_val),
        cond_in_mission,
        (mem_mg_id == 0x05),
        (mem_flag == 0x00),
        (mem_flag.delta() == 0x01),
    ])
    my_set.add_achievement(ach)

# 4. MINIJOGOS - SEM ERROS (FLAWLESS)
flawless_data = [
    (623950, "Sharp Eye", "Complete the Swamp Odd One Out minigame without any mistakes during a mission", 2, "709344", 0x00, 0x02, byte(0x005840), 0x05, byte(0x00583e)),
    (623951, "Swamp Mathematician", "Complete the Swamp Math Equations minigame without any mistakes during a mission", 10, "709345", 0x00, 0x04, byte(0x0055d0), 0x05, byte(0x0055ce)),
    (623952, "Perfect Fit", "Complete the Swamp Shape Fit minigame without any mistakes during a mission", 5, "709346", 0x00, 0x05, byte(0x005b4c), 0x0a, byte(0x005b4a)),
    (623953, "Box Counter", "Complete the Caatinga Count the Boxes minigame without any mistakes during a mission", 5, "709347", 0x01, 0x01, byte(0x005498), 0x05, byte(0x005496)),
    (623954, "Logical Flow", "Complete the Caatinga Complete the Sequence minigame without any mistakes during a mission", 5, "709348", 0x01, 0x02, byte(0x0058a2), 0x05, byte(0x0058a0)),
    (623955, "Memory of the Drylands", "Complete the Caatinga Card Recall minigame without any mistakes during a mission", 5, "709349", 0x01, 0x03, byte(0x005a0c), 0x05, byte(0x005a0a)),
    (623956, "Quick Calculator", "Complete the Caatinga Quick Math minigame without any mistakes during a mission", 25, "709350", 0x01, 0x04, byte(0x00551c), 0x05, byte(0x00551a)),
    (623957, "Shadow Tracker", "Complete the Caatinga Shadow Matching minigame without any mistakes during a mission", 25, "709351", 0x01, 0x05, byte(0x00572c), 0x05, byte(0x00572a)),
    (623958, "Spatial Awareness", "Complete the Jungle Cube Folding minigame without any mistakes during a mission", 5, "709352", 0x02, 0x01, byte(0x005b76), 0x05, byte(0x005b74)),
    (623960, "Jungle Memory", "Complete the Jungle Memory Match minigame without any mistakes during a mission", 10, "709354", 0x02, 0x03, byte(0x00591c), 0x0a, byte(0x00591a)),
    (623961, "Division Expert", "Complete the Jungle Missing Digits minigame without any mistakes during a mission", 10, "709355", 0x02, 0x04, byte(0x00563e), 0x05, byte(0x00563c)),
    (623962, "Eagle Eye", "Complete the Jungle Object Counting minigame without any mistakes during a mission", 10, "709356", 0x02, 0x05, byte(0x0054b1), 0x05, byte(0x0054af)),
]

for f_id, title, desc, pts, badge, mission_val, mg_val, mem_meas, target_val, mem_error in flawless_data:
    ach = Achievement(id=f_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        cond_in_mission,
        (mem_mission == mission_val),
        (mem_mg_id == mg_val),
        measured(mem_meas == target_val),
        (mem_error == 0x00),
        (mem_error.delta() != 0x00),
    ])
    my_set.add_achievement(ach)

# 5. MINIJOGOS - TEMPO (SPEED)
# Picture Perfect Pace
ach = Achievement(id=623949, title="Picture Perfect Pace", description="Complete the Swamp Picture Puzzle minigame in 59 seconds or less during a mission", points=2, badge="709343")
ach.add_core([
    cond_in_mission,
    (mem_mission == 0x00),
    (mem_mg_id == 0x01),
    (mem_timer <= 0x3b),
    trigger(byte(0x00127f) == 0x05),
    trigger(byte(0x00127f).delta() == 0x04),
])
my_set.add_achievement(ach)

# Rapid Knight
ach = Achievement(id=623959, title="Rapid Knight", description="Complete the Jungle Knight's Tour minigame in 104 seconds or less during a mission", points=5, badge="709353")
ach.add_core([
    cond_in_mission,
    (mem_mission == 0x02),
    (mem_mg_id == 0x02),
    (mem_timer <= 0x68),
    trigger(byte(0x00186d) == 0x05),
    (byte(0x00186d).delta() != 0x05),
])
my_set.add_achievement(ach)

my_set.save()