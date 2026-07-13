from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=286, title="International Superstar Soccer Deluxe")

# 1. ALIASES DE MEMÓRIA
mem_screen       = byte(0x000032)
mem_cpu_active   = byte(0x000052)
mem_p1_ctrl      = byte(0x0011e6)
mem_match_active = byte(0x002f1f)
mem_match_state  = byte(0x001d08)
mem_game_mode    = byte(0x001e5e)
mem_world_mode   = byte(0x00de13)
mem_difficulty   = byte(0x001f9c)

mem_p1_team      = byte(0x000da0)
mem_p2_team      = byte(0x000ea0)
mem_p1_score     = byte(0x000da2)
mem_p2_score     = byte(0x000ea2)

mem_scenario_idx = byte(0x00e52a)
mem_train_type   = byte(0x00e52c)
mem_train_diff   = byte(0x00e52e)
mem_ws_wins      = byte(0x001652)
mem_ws_match_st  = bit3(0x000057)

# Stats
mem_shots        = byte(0x000daa)
mem_corners      = byte(0x000dac)
mem_fouls_given  = byte(0x000dab)
mem_yellow_cards = byte(0x000dae)
mem_red_cards    = byte(0x000daf)

# 2. CONDIÇÕES COMUNS
cond_match_valid = [
    (mem_cpu_active == 0x00),
    (mem_p1_ctrl == 0x00),
    (mem_match_active == 0x01),
]

cond_no_99_goals = pause_if((mem_p1_score == 0x63).with_hits(1))

def goal_trigger(hits=1):
    return (mem_p1_score > mem_p1_score.delta()).with_hits(hits)

# 3. CENÁRIOS (Normal & Hardcore)
scenario_flags = [
    # (Idx, Func, Addr, P2_Max_Goals)
    (0,  bit7, 0x00d88d, 2),  (1,  bit6, 0x00d88d, 3),
    (2,  bit5, 0x00d88d, 3),  (3,  bit4, 0x00d88d, 0),
    (4,  bit3, 0x00d88d, 1),  (5,  bit2, 0x00d88d, 1),
    (6,  bit1, 0x00d88d, 1),  (7,  bit0, 0x00d88d, 0),
    (8,  bit7, 0x00d706, 1),  (9,  bit6, 0x00d706, 2),
    (10, bit5, 0x00d706, 3),  (11, bit4, 0x00d706, 1),
]

scen_normal = [
    (424029, "Ciao", 3, "708394"), (424030, "Hallo", 4, "708395"),
    (424031, "Hello", 5, "708396"), (424032, "Guten Tag", 3, "708397"),
    (424033, "Merhaba", 2, "708398"), (424034, "Bonjour", 3, "708399"),
    (424035, "Buna Ziua", 4, "708400"), (424036, "Halò", 2, "708401"),
    (424037, "Olá", 4, "708402"), (424038, "Hola", 3, "708403"),
    (424039, "Goedendag", 5, "708404"), (424040, "Cheerio", 5, "708405")
]

scen_hard = [
    (10240, "Azzurri's Last Stand", 10, "708406"), (10241, "Germany's Escape", 10, "708407"),
    (10242, "Never Underestimate Pride", 10, "708408"), (10243, "Breaking the Tie", 10, "708409"),
    (10244, "Historic Victory", 10, "708410"), (10245, "Making Things Even", 10, "708411"),
    (10246, "The Best Team Always Wins", 10, "708412"), (10247, "Ticket to England", 10, "708413"),
    (10248, "Lusitanian Focus", 10, "708414"), (10249, "The Best Team in South America", 10, "708415"),
    (10250, "A Real Struggle", 10, "708416"), (10251, "Avoiding Embarrassment", 10, "708417")
]

for i in range(12):
    idx, bit_fn, addr, max_goals = scenario_flags[i]
    
    # --- Cenários Normais (Level 3+) ---
    n_id, n_title, n_pts, n_badge = scen_normal[i]
    ach_norm = Achievement(id=n_id, title=n_title, description=f"Clear Scenario No. {i+1} on Game Level 3 or above", points=n_pts, badge=n_badge, type=AchievementType.PROGRESSION)
    ach_norm.add_core([
        (mem_difficulty >= 0x02),
        (mem_p1_score > mem_p2_score),
        (mem_scenario_idx == idx),
        (mem_game_mode == 0x04),
        (bit_fn(addr) == 0x01),
        (bit_fn(addr).delta() == 0x00),
        cond_no_99_goals
    ])
    ach_norm.add_alt([reset_if((mem_game_mode == 0x00))])
    my_set.add_achievement(ach_norm)

    # --- Cenários Hardcore (Level 5 + No Goals Conceded) ---
    h_id, h_title, h_pts, h_badge = scen_hard[i]
    ach_hard = Achievement(id=h_id, title=h_title, description=f"Clear Scenario No. {i+1} on Game Level 5 without conceding a goal", points=h_pts, badge=h_badge)
    ach_hard.add_core([
        (mem_difficulty == 0x04),
        trigger(mem_p1_score > mem_p2_score),
        (mem_game_mode == 0x04),
        (mem_scenario_idx == idx),
        trigger(bit_fn(addr) == 0x01),
        (bit_fn(addr).delta() == 0x00),
        cond_no_99_goals,
        and_next(mem_scenario_idx == idx),
        pause_if((mem_p2_score > max_goals).with_hits(1)),
    ])
    ach_hard.add_alt([reset_if((mem_game_mode == 0x00))])
    my_set.add_achievement(ach_hard)

# The True Ending (All Scenarios in 1 Attempt)
ach = Achievement(id=10312, title="The True Ending", description="Clear every Scenario on the first attempt on Game Level 4 or above", points=25, badge="708458")
ach.add_core([
    (byte(0x00d88d) == 0xff).with_hits(1),
    (byte(0x00d706) == 0xf1).with_hits(1),
    (mem_game_mode == 0x04),
    (mem_difficulty >= 0x03),
    trigger(byte(0x0013e1) == 0x01),
    (byte(0x0013e1).delta() == 0x00),
    *(reset_if(byte(0x00d88e + j) > 1) for j in range(12)) # Laço embutido para limpar as 12 linhas repetidas!
])
my_set.add_achievement(ach)

# 4. TREINOS (Records)
training_data = [
    # Dribble (0)
    (10252, "Dribble Learner", 0, 0, 0x1e5, 0x00d8c4, 1, "708431"),
    (10253, "Dribble Teacher", 0, 1, 0x1ec, 0x00d906, 1, "708432"),
    (10254, "Dribble Expert", 0, 2, 0x1df, 0x00d948, 5, "708433"),
    (10255, "Dribble Master", 0, 3, 0x1d8, 0x00d98a, 5, "708434"),
    # Pass (1)
    (10256, "So You Think You Can Pass?", 1, 0, 0x1e0, 0x0008cf, 1, "708435"),
    (10257, "Long Way to Go Yet", 1, 1, 0x1df, 0x000911, 1, "708436"),
    (10258, "Assist King", 1, 2, 0x1dd, 0x000953, 3, "708437"),
    (10259, "Assist Master", 1, 3, 0x1e7, 0x000995, 5, "708438"),
    # Shoot (2)
    (10260, "Rookie Shooter", 2, 0, 0x226, 0x0008da, 1, "708439"),
    (10261, "Still Couldn't Score in a League Game", 2, 1, 0x21c, 0x00091c, 1, "708440"),
    (10262, "Tournament Pressure", 2, 2, 0x20c, 0x00095e, 3, "708441"),
    (10263, "World Class Striker", 2, 3, 0x20e, 0x0009a0, 5, "708442"),
    # Defend (3)
    (10264, "You are Still Learning to Defend", 3, 0, 0x207, 0x0008e5, 1, "708443"),
    (10265, "Rookie Defender", 3, 1, 0x1f9, 0x000927, 1, "708444"),
    (10266, "Local League Defender", 3, 2, 0x209, 0x000969, 3, "708445"),
    (10267, "World Class Defender", 3, 3, 0x20b, 0x0009ab, 5, "708446"),
    # Corner (4)
    (10268, "Corner Rookie", 4, 0, 0x206, 0x0008f0, 1, "708447"),
    (10269, "Where is the Bend?", 4, 1, 0x1fe, 0x000932, 1, "708448"),
    (10270, "First Picked For Corners", 4, 2, 0x1f8, 0x000974, 3, "708449"),
    (10271, "Curving expert", 4, 3, 0x1de, 0x0009b6, 5, "708450"),
    # Free Kick (5)
    (10272, "Bend It Like Victoria Beckham", 5, 0, 0x202, 0x0008fb, 1, "708451"),
    (10273, "Can't Score From A Free Kick", 5, 1, 0x1fe, 0x00093d, 1, "708452"),
    (10274, "Goals From 20 Yards", 5, 2, 0x200, 0x00097f, 3, "708453"),
    (10275, "Goals from Anywhere!", 5, 3, 0x21e, 0x0009c1, 5, "708454"),
]

for t_id, title, type_val, diff_val, target, addr, pts, badge in training_data:
    ach = Achievement(id=t_id, title=title, description=f"Break the training record", points=pts, badge=badge)
    ach.add_core([
        (mem_train_type == type_val),
        (mem_train_diff == diff_val),
        (mem_game_mode == 0x06),
        trigger(word(addr) > target),
        (word(addr).delta() <= target),
    ])
    my_set.add_achievement(ach)

# 5. WORLD SERIES & TORNEIOS
ws_data = [
    (623460, "International Superstar", "Win the International on Game Level 4 or above", 10, [or_next(mem_game_mode == 0x01), (mem_world_mode == 0x02), (mem_difficulty >= 0x03)]),
    (623461, "The World Is Yours", "Win the World Series with any team on Difficulty 4 or above", 10, [(mem_ws_wins == 0x23).with_hits(1), or_next(mem_game_mode == 0x02), reset_if(mem_world_mode != 0x03), (mem_difficulty >= 0x03)]),
    (10280, "World Champion", "Win the World Series without a single loss in the season", 25, [trigger((mem_ws_wins == 0x23).with_hits(1)), reset_if(byte(0x00dc60) != 0x00), or_next(mem_game_mode == 0x02), (mem_world_mode == 0x03)]),
    (10281, "Defying the Impossible", "Win every match in the World Series as Morocco", 25, [trigger((mem_ws_wins == 0x23).with_hits(1)), reset_if(byte(0x00dc60) != 0x00), (mem_p1_team == 0x3a), or_next(mem_game_mode == 0x02), (mem_world_mode == 0x03)]),
    (10282, "It Will Take Something Special", "Win every match in the World Series on Game Level 5", 50, [trigger((mem_ws_wins == 0x23).with_hits(1)), (mem_difficulty == 0x04), reset_if(byte(0x00dc60) != 0x00), or_next(mem_game_mode == 0x02), (mem_world_mode == 0x03)]),
]

for w_id, title, desc, pts, conds in ws_data:
    ach = Achievement(id=w_id, title=title, description=desc, points=pts, type=AchievementType.WIN_CONDITION if pts==10 else AchievementType.STANDARD)
    ach.add_core([
        *conds,
        trigger(mem_ws_match_st == 0x01),
        (mem_ws_match_st.delta() != 0x01)
    ])
    my_set.add_achievement(ach)

# Short Tournaments
ach = Achievement(id=623462, title="Fast Track to Glory", description="Win a Short Tournament on Game Level 4 or above", points=2, badge="708388")
ach.add_core([(mem_difficulty >= 0x03), (byte(0x00167c) == 0x01), (byte(0x001654) == 0x05), (bit5(0x00a23e) == 0x01), (bit5(0x00a23e).delta() != 0x01)])
my_set.add_achievement(ach)

ach = Achievement(id=623463, title="Sprint Champion", description="Win a Short League on Game Level 4 or above", points=2, badge="708389")
ach.add_core([(mem_difficulty >= 0x03), (byte(0x00167c) == 0x01), (byte(0x001654) == 0x04), (bit5(0x00a23e) == 0x01), (bit5(0x00a23e).delta() == 0x00)])
my_set.add_achievement(ach)

# 6. ESTATÍSTICAS E CONQUISTAS DE PARTIDA
goals_data = [
    (534, "Yes! GOALLLL!!!", "Score your first goal in any game mode", 1, 1, []),
    (9370, "Hat Trick!", "Score 3 goals in a match", 3, 3, []),
    (535, "GOALLLL!!!! GOALLLLLL!!!!", "Score 10 goals in a match", 5, 10, []),
    (9371, "I Don't Believe It", "Score 20 goals in a match", 10, 20, []),
]

for m_id, title, desc, pts, hits, extra in goals_data:
    ach = Achievement(id=m_id, title=title, description=desc, points=pts)
    ach.add_core([
        goal_trigger(hits),
        (mem_screen != 0x03),
        *cond_match_valid,
        cond_no_99_goals,
        *extra
    ])
    if hits > 1: ach.add_alt([reset_if(mem_match_active == 0x00)])
    my_set.add_achievement(ach)

# Cartões e Faltas
ach = Achievement(id=10276, title="Word of Warning", description="Receive a Yellow Card", points=1, badge="708423")
ach.add_core([(mem_yellow_cards > value(0)).with_hits(1), *cond_match_valid, cond_no_99_goals])
ach.add_alt([reset_if(mem_match_active == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=10277, title="You're Off!", description="Receive a Red Card", points=1, badge="708424")
ach.add_core([(mem_red_cards > value(0)).with_hits(1), *cond_match_valid, cond_no_99_goals])
ach.add_alt([reset_if(mem_match_active == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=10362, title="Must Score Now", description="Accumulate at least 10 Corner Kicks in a single match", points=5, badge="708429")
ach.add_core([measured((mem_corners > value(0)).with_hits(10)), *cond_match_valid, cond_no_99_goals])
ach.add_alt([reset_if(mem_match_active == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=10363, title="Luck of the Irish", description="Giveaway 10 free kicks to the opposing team without receiving a card in a single match", points=10, badge="708430")
ach.add_core([measured((mem_fouls_given > value(0)).with_hits(10)), *cond_match_valid, cond_no_99_goals, pause_if((mem_yellow_cards > 0x00).with_hits(1))])
ach.add_alt([reset_if(mem_match_active == 0x00)])
my_set.add_achievement(ach)

# Condições de Vitória Específicas
ach = Achievement(id=10278, title="First Taste of Success", description="Win a full match in any game mode", points=5, badge="708422")
ach.add_core([(mem_p1_score > mem_p2_score), *cond_match_valid, (mem_match_state == 0x14), (mem_match_state.delta() != 0x14), cond_no_99_goals])
ach.add_alt([reset_if(mem_match_active == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=10355, title="Shotless", description="Win a match in Open Game mode without ever shooting the ball", points=5, badge="708426")
ach.add_core([(mem_shots == 0x00), (mem_p1_score > mem_p2_score), *cond_match_valid, (mem_match_state == 0x14), (mem_match_state.delta() != 0x14), cond_no_99_goals])
ach.add_alt([reset_if(mem_match_active == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=10360, title="One Tough Line Up", description="Beat the All-Star team in a match in Open Game mode", points=5, badge="708459")
ach.add_core([(mem_p2_team == 0x48), *cond_match_valid, trigger(mem_p1_score > mem_p2_score), trigger(mem_match_state == 0x14), (mem_match_state.delta() != 0x14), reset_next_if(mem_match_active == 0x00), cond_no_99_goals])
my_set.add_achievement(ach)

ach = Achievement(id=10361, title="Don't Underestimate Us", description="Beat the All-Star team in a match in Open Game mode while playing as Morocco on Game Level 5 with Game Time set to 7", points=25, badge="708460")
ach.add_core([(mem_p1_team == 0x3a), (mem_p2_team == 0x48), *cond_match_valid, (byte(0x001f88) == 0x02), (mem_difficulty == 0x04), trigger(mem_p1_score > mem_p2_score), trigger(mem_match_state == 0x14), (mem_match_state.delta() != 0x14), reset_next_if(mem_match_active == 0x00), cond_no_99_goals])
my_set.add_achievement(ach)

ach = Achievement(id=10357, title="Made Easy", description="Win a match in Open Game mode with fouls, offisde, and cards disabled", points=5, badge="708425")
ach.add_core([(mem_p1_score > mem_p2_score), (mem_cpu_active == 0x00), (mem_p1_ctrl == 0x00), (mem_match_active == 0x01), (byte(0x001f92) == 0x01), (byte(0x001f98) == 0x01), (byte(0x001f9a) == 0x01), (mem_match_state == 0x14), (mem_match_state.delta() != 0x14), cond_no_99_goals])
ach.add_alt([reset_if(mem_match_active == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=623464, title="Man's Best Referee", description="Win a match officiated by the dog referee without committing any fouls on Game Level 4 or above", points=5, badge="708390")
ach.add_core([(byte(0x00d854) == 0x01), (mem_match_state == 0x48).with_hits(1), (byte(0x001f98) == 0x00), (mem_difficulty >= 0x03), (mem_cpu_active == 0x00), pause_if((byte(0x000eab) > 0x00).with_hits(1)), trigger(mem_match_state == 0x14), (mem_match_state.delta() != 0x14)])
ach.add_alt([reset_if(mem_match_active == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=10358, title="Super Goalie", description="Win a match in Penalty Kick mode without allowing a goal", points=5, badge="708427")
ach.add_core([(mem_game_mode == 0x05), (byte(0x00d443) == 0x00), (mem_cpu_active == 0x00), (mem_p1_ctrl == 0x00), trigger(mem_match_state == 0x14), (mem_match_state.delta() != 0x14), cond_no_99_goals])
ach.add_alt([reset_if(mem_game_mode == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=10359, title="The Unbreakable Wall", description="Win a match in Penalty Kick mode on Game Level 5 and while keeping a clean sheet", points=10, badge="708428")
ach.add_core([(mem_difficulty == 0x04), (mem_game_mode == 0x05), (byte(0x00d443) == 0x00), (mem_cpu_active == 0x00), (mem_p1_ctrl == 0x00), trigger(mem_match_state == 0x14), (mem_match_state.delta() != 0x14), cond_no_99_goals])
ach.add_alt([reset_if(mem_game_mode == 0x00)])
my_set.add_achievement(ach)

# Golos Especiais
ach = Achievement(id=623466, title="Jogo Bonito", description="Score a goal with a bicycle kick on Game Level 4 or above", points=2, badge="708392")
ach.add_core([goal_trigger(), (mem_difficulty >= 0x03), *cond_match_valid, (mem_match_state == 0x11).with_hits(1), or_next(mem_match_state == 0x45), or_next(mem_match_state == 0x2f), (mem_match_state == 0x46), reset_if(mem_match_state == 0x02), reset_if(mem_match_state == 0x2c), reset_if(mem_match_state == 0x03), reset_if(mem_match_state == 0x01)])
my_set.add_achievement(ach)

ach = Achievement(id=623467, title="Smooth Operator", description="Score a goal immediately after performing a feint on Game Level 4 or above", points=5, badge="708393")
ach.add_core([trigger(goal_trigger()), (mem_difficulty >= 0x03), *cond_match_valid, or_next((mem_match_state == 0x3d).with_hits(1)), (mem_match_state == 0x1d).with_hits(1), or_next(mem_match_state == 0x45), or_next(mem_match_state == 0x2f), trigger(mem_match_state == 0x46), reset_if(mem_match_state == 0x02), reset_if(mem_match_state == 0x03), reset_if(mem_match_state == 0x01), reset_if(mem_match_state == 0x1f), reset_if(mem_match_state == 0x18)])
my_set.add_achievement(ach)

ach = Achievement(id=623465, title="Dead Ball Specialist", description="Score a goal from a free kick during a full match", points=2, badge="708391")
ach.add_core([trigger(goal_trigger()), (mem_match_state == 0x04).with_hits(1), or_next((mem_match_state == 0x46).with_hits(1)), (mem_match_state == 0x2f).with_hits(1), (mem_cpu_active == 0x00), (mem_p1_ctrl == 0x00), reset_if(mem_match_state == 0x02), reset_if(mem_match_state == 0x2c), reset_if(mem_match_state == 0x03), reset_if(mem_match_state == 0x11)])
my_set.add_achievement(ach)

my_set.save()