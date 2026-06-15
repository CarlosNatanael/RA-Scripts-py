from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=10708, title="Joe Montana Football")

# 1. ALIASES DE MEMÓRIA
mem_state         = byte(0x0891)
mem_action        = byte(0x03db)

mem_p1_team       = byte(0x08be)
mem_p2_team       = byte(0x08bf)

mem_p1_score      = byte(0x0866)
mem_p2_score      = byte(0x0868)
mem_p1_score_bcd  = byte(0x0866).bcd()
mem_p2_score_bcd  = byte(0x0868).bcd()

mem_interceptions = byte(0x08b1)
mem_sacks         = byte(0x08b4)
mem_sacks_allowed = byte(0x08b3)
mem_pass_yards    = word(0x08a7)
mem_rush_yards    = word(0x08a3)
mem_first_downs   = byte(0x08af)

mem_play_type     = byte(0x0889)
mem_diff          = byte(0x08d5)

# 2. BLOCOS REUTILIZÁVEIS
cond_in_match = [
    reset_if(mem_state == 0x08),
    (mem_p2_team == 0xff).with_hits(1),
]

cond_match_end = [
    (mem_state.delta() != 0x20),
    trigger(mem_state == 0x20),
]

# 3. ESTATÍSTICAS E ACUMULADORES (MEASURED)
stats_data = [
    (617228, "Ball Hawk", "Perform 3 interceptions on defense in a single match", 10, [mem_state <= 0x02, (mem_interceptions.delta() == 0x02), measured(mem_interceptions == 0x03)]),
    (617229, "Air Raid Siren", "Accumulate 300 or more passing yards in a single match", 10, [mem_state == 0x01, (mem_pass_yards.delta() < 300), measured(mem_pass_yards >= 300)]),
    (617230, "Ground and Pound", "Accumulate 150 or more rushing yards in a single match", 10, [mem_state == 0x01, (mem_rush_yards.delta() < 150), measured(mem_rush_yards >= 150)]),
    (617231, "Chain Mover", "Achieve 15 or more First Downs in a single match", 10, [mem_state == 0x01, (mem_first_downs.delta() < 15), measured(mem_first_downs >= 15)]),
]

for a_id, title, desc, pts, logic_list in stats_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts)
    ach.add_core([*cond_in_match, *logic_list])
    my_set.add_achievement(ach)

# 4. AÇÕES ESPECÍFICAS DE JOGO
ach = Achievement(id=617223, title="Call It in the Air", description="Guess the coin toss correctly at the start of a match", points=1)
ach.add_core([
    reset_if(mem_state == 0x08),
    (mem_state == 0x40).with_hits(1),
    (mem_action.delta() == 0x00),
    trigger(mem_action == 0x10),
])
my_set.add_achievement(ach)

ach = Achievement(id=617225, title="Pickpocket", description="Intercept a pass on defense", points=2)
ach.add_core([
    *cond_in_match,
    (mem_state <= 0x02),
    (mem_interceptions.delta() < mem_interceptions),
])
my_set.add_achievement(ach)

ach = Achievement(id=617226, title="Lumberjack", description="Sack the opposing Quarterback", points=2)
ach.add_core([
    *cond_in_match,
    (mem_state <= 0x02),
    (mem_sacks.delta() == 0x00),
    (mem_sacks == 0x01),
])
my_set.add_achievement(ach)

ach = Achievement(id=617227, title="It's Good!", description="Successfully kick a Field Goal by selecting the option from the play menu", points=2)
ach.add_core([
    *cond_in_match,
    (mem_state == 0x01),
    (mem_play_type == 0x02),
    sub_source(mem_p1_score.delta()),
    (mem_p1_score_bcd == 0x03),
])
my_set.add_achievement(ach)

ach = Achievement(id=617235, title="End Zone Trap", description="Score a Safety", points=25)
ach.add_core([
    *cond_in_match,
    (mem_state == 0x01),
    sub_source(mem_p1_score.delta()),
    (mem_p1_score_bcd == 0x02),
])
my_set.add_achievement(ach)

# 5. VITÓRIAS E DESAFIOS DE FIM DE JOGO
ach = Achievement(id=617224, title="First Down", description="Win a match on any difficulty", points=5, type=AchievementType.WIN_CONDITION)
ach.add_core([
    *cond_in_match,
    (mem_state == 0x20),
    (mem_state.delta() == 0x02),
    (mem_p1_score > mem_p2_score),
])
my_set.add_achievement(ach)

ach = Achievement(id=617232, title="Super Bowl XXIV Revenge", description="Win a match as Denver against San Francisco on Professional difficulty", points=25)
ach.add_core([
    *cond_in_match,
    (mem_p1_team == 0x12),
    (mem_p2_team == 0x00),
    (mem_diff == 0x02),
    *cond_match_end,
    trigger(mem_p1_score > mem_p2_score),
])
my_set.add_achievement(ach)

ach = Achievement(id=617233, title="California Heavyweights", description="Win a match as the LA Rams against the LA Raiders", points=5)
ach.add_core([
    *cond_in_match,
    (mem_p1_team == 0x02),
    (mem_p2_team == 0x14),
    *cond_match_end,
    trigger(mem_p1_score > mem_p2_score),
])
my_set.add_achievement(ach)

ach = Achievement(id=617234, title="Mile High Clubbed", description="Win a match against Denver on Professional difficulty by a margin of 30 points or more", points=25)
ach.add_core([
    *cond_in_match,
    (mem_p2_team == 0x12),
    (mem_diff == 0x02),
    *cond_match_end,
    sub_source(mem_p2_score_bcd),
    trigger(mem_p1_score_bcd >= 30),
])
my_set.add_achievement(ach)

ach = Achievement(id=617236, title="Impenetrable Line", description="Win a match on Professional difficulty without allowing your Quarterback to be sacked", points=25)
ach.add_core([
    *cond_in_match,
    (mem_diff == 0x02),
    (mem_sacks_allowed == 0x00),
    *cond_match_end,
    trigger(mem_p1_score_bcd > mem_p2_score_bcd),
])
my_set.add_achievement(ach)

my_set.save()