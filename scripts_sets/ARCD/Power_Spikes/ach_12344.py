from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=12344, title="Imported Set")

# 1. ALIASES DE MEMÓRIA
mem_mode       = byte(0x00002e)
mem_state      = word(0x000022)
mem_match_end  = byte(0x000024)
mem_diff       = byte(0x000044)
mem_cpu_team   = byte(0x0019c2)
mem_cpu_score  = word(0x001690)
mem_time       = word(0x0016b6)

# 2. PROGRESSÃO DE EQUIPAS
prog_data = [
    (611765, "Defeating the Red Dragon", "Win a match against China in Arcade mode", 2, 0x03, "694302"),
    (611766, "Rising Sun Down", "Win a match against Japan in Arcade mode", 2, 0x00, "694303"),
    (611767, "Eagle Down", "Win a match against the USA in Arcade mode", 5, 0x01, "694304"),
    (611768, "Caribbean Spike", "Win a match against Cuba in Arcade mode", 5, 0x0f, "694305"),
    (611769, "Breaking the Iron Curtain", "Win a match against the USSR in Arcade mode", 10, 0x02, "694306"),
]

for a_id, title, desc, pts, team_id, badge in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.PROGRESSION, badge=badge)
    ach.add_core([
        (mem_mode == 0x01),
        (mem_cpu_team == team_id),
        (mem_state == 0x07),
        (mem_match_end.delta() != 0x03),
        (mem_match_end == 0x03),
    ])
    my_set.add_achievement(ach)

# World Champion (Win Condition)
ach = Achievement(id=611770, title="World Champio", description="Clear the Arcade mode", points=25, type=AchievementType.WIN_CONDITION, badge="694307")
ach.add_core([
    (mem_mode == 0x01),
    (mem_cpu_team == 0x02),
    (mem_state == 0x07),
    (mem_match_end.delta() != 0x03),
    (mem_match_end == 0x03),
])
my_set.add_achievement(ach)


# 3. DESAFIOS AVANÇADOS
# Hardcore Spiker
ach = Achievement(id=611771, title="Hardcore Spiker", description="Clear the Arcade mode on Hard difficulty", points=25, badge="694316")
ach.add_core([
    and_next(mem_state == 0x07),
    pause_if((mem_match_end == 0x02).with_hits(1)),
    (mem_mode == 0x01),
    (mem_diff == 0x01),
    (mem_state.delta() != 0x08),
    trigger(mem_state == 0x08),
])
ach.add_alt([reset_if(mem_state == 0x05)])
my_set.add_achievement(ach)

# Coin Saver
ach = Achievement(id=611772, title="Coin Saver", description="Clear the Arcade mode without using any continues", points=50, badge="694317")
ach.add_core([
    and_next(mem_state == 0x07),
    pause_if((mem_match_end == 0x02).with_hits(1)),
    (mem_mode == 0x01),
    (mem_state.delta() != 0x08),
    trigger(mem_state == 0x08),
])
ach.add_alt([
    reset_if(mem_state == 0x03)
])
my_set.add_achievement(ach)

# Impenetrable Block
ach = Achievement(id=611773, title="Impenetrable Block", description="Win a set in Arcade mode without letting the CPU score a single point", points=10, badge="694318")
ach.add_core([
    (mem_mode == 0x01),
    pause_if((mem_cpu_score > mem_cpu_score.delta()).with_hits(1)),
    (mem_state == 0x06).with_hits(1),
    (mem_match_end.delta() != 0x03),
    trigger(mem_match_end == 0x03),
])
ach.add_alt([reset_if(mem_state == 0x05)])
my_set.add_achievement(ach)

# Time Attack Spiker
ach = Achievement(id=611774, title="Time Attack Spiker", description="Win a set in Arcade mode with at least 60 seconds remaining on the clock", points=10, badge="694319")
ach.add_core([
    reset_if(mem_state <= 0x05),
    (mem_mode == 0x01),
    (mem_time >= 0x01),
    (mem_state == 0x06).with_hits(1),
    (mem_match_end.delta() != 0x03),
    trigger(mem_match_end == 0x03),
])
my_set.add_achievement(ach)

my_set.save()