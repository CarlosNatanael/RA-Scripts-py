from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=1179, title="Spider-Man and Venom: Maximum Carnage")

# 1. ALIASES DE MEMÓRIA
mem_stage      = word(0x000a0e)
mem_game_state = byte(0x00088e)
mem_score_10k  = byte(0x000980)
mem_score_100k = byte(0x000982)

mem_boss_hp    = word(0x000dc0)
mem_p1_lives   = word(0x000990)
mem_p2_lives   = word(0x000992)
mem_continues  = word(0x000994)
mem_char       = byte(0x0009a8)
mem_demo_mode  = byte(0x0019cd)

mem_acc_trig   = byte(0x001cca)
mem_accuracy   = word(0x001ccc)

# 2. PROGRESSÃO DE FASES
prog_data = [
    (18214, "Swinging Into Action", "Clear Level 1 - New York Streets", 5, "712398", 0x04, [0x02]),
    (18216, "Scaling the Streets", "Clear Level 2 - Climb", 5, "712399", 0x06, [0x04]),
    (18218, "Double Trouble", "Clear Level 3 - Rooftop", 5, "712400", 0x08, [0x06]),
    (18219, "Back Alley Brawler", "Clear Level 4 - Alleyway", 5, "712401", 0x0a, [0x08]),
    (18220, "Unlikely Allies", "Clear Level 5 - The Hall", 5, "712402", 0x0c, [0x0a]),
    (18227, "Frisco Throwdown", "Clear Level 6 - San Francisco", 5, "712403", 0x12, [0x10]),
    (18222, "Mayhem in Manhattan", "Clear Level 7 - Times Square or Central Park as either character", 5, "712404", 0x14, [0x12, 0x0e]),
    (18229, "Concrete Chaos", "Clear Level 8 - New York Streets 2", 5, "712405", 0x16, [0x14]),
    (18231, "Clubbed to Death", "Clear Level 9 - The Deep", 5, "712406", 0x18, [0x16]),
    (18252, "Breaking & Entering", "Clear Level 10 - Fantastic 4 HQ", 5, "712407", 0x1a, [0x18]),
    (18254, "Dogged Determination", "Clear Level 11 - Fantastic 4 Lab", 5, "712408", 0x1c, [0x1a]),
    (18256, "Rooftop Rumble", "Clear Level 12 - Rooftop 2", 5, "712409", 0x1e, [0x1c]),
    (18277, "Brooklyn Bust-Up", "Clear Level 13 - Prospect Park", 5, "712410", 0x20, [0x1e]),
    (18279, "The Fearsome Five", "Clear Level 13 - Prospect Park 2", 5, "712411", 0x22, [0x20]),
    (18283, "Streets Run Red", "Clear Level 17 - Manhattan Street 2", 10, "712412", 0x32, [0x30]),
    (18296, "United Against Carnage", "Clear Level 18 - The End...", 10, "712413", 0x34, [0x32]),
]

for a_id, title, desc, pts, badge, stage, prevs in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.PROGRESSION)
    logic = []
    
    if len(prevs) > 1:
        logic.append(or_next(mem_stage.delta() == prevs[0]))
        logic.append(mem_stage.delta() == prevs[1])
    else:
        logic.append(mem_stage.delta() == prevs[0])
        
    logic.extend([
        (mem_stage == stage),
        (mem_game_state == 0x00)
    ])
    ach.add_core(logic)
    my_set.add_achievement(ach)

# 3. PRECISÃO (Accuracy)
acc_data = [
    (18215, "Big Apple Bullseye", "Clear Level 1 - New York Streets with an accuracy of 80% or higher", 10, "712420", 0x02, 0x80),
    (18228, "Symbiotic Sharpshooter", "Clear Level 6 - San Francisco with an accuracy of 80% or higher", 25, "712422", 0x10, 0x80),
    (18223, "Perfect Timing", "Clear Level 7 - Times Square with an accuracy of 80% or higher", 25, "712423", 0x0e, 0x80),
    (18230, "Concrete Precision", "Clear Level 8 - New York Streets 2 with an accuracy of 80% or higher", 25, "712424", 0x14, 0x80),
    (18232, "Flawless Footwork", "Clear Level 9 - The Deep with an accuracy of 80% or higher", 25, "712425", 0x16, 0x80),
    (18253, "Plaza Perfection", "Clear Level 10 - Fantastic 4 HQ with an accuracy of 80% or higher", 25, "712426", 0x18, 0x80),
    (18255, "Fantastic Heist", "Clear Level 11 - Fantastic 4 Lab with an accuracy of 80% or higher", 25, "712427", 0x1a, 0x80),
    (18257, "Against All Odds", "Clear Level 12 - Rooftop 2 with an accuracy of 80% or higher", 25, "712428", 0x1c, 0x80),
    (18278, "Brooklyn Bullseye", "Clear Level 13 - Prospect Park with an accuracy of 70% or higher", 25, "712429", 0x1e, 0x70),
    (18280, "Jail Cell Jostle", "Clear Level 14 - Police Station with an accuracy of 80% or higher", 25, "712430", 0x22, 0x80),
    (18281, "Shrieking Violet", "Clear Level 15 - Manhattan Rooftop with an accuracy of 80% or higher", 25, "712431", 0x26, 0x80),
    (18282, "Rogue Reinforcements", "Clear Level 16 - Manhattan Street with an accuracy of 80% or higher", 25, "712432", 0x2c, 0x80),
    (18297, "Method to the Madness", "Clear Level 18 - The End... with an accuracy of 50% or higher", 25, "712434", 0x32, 0x50),
]

for a_id, title, desc, pts, badge, stage, req_acc in acc_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    logic = [
        (mem_stage == stage),
        (mem_acc_trig == 0xff).with_hits(1),
        (mem_accuracy >= req_acc), (mem_accuracy.delta() < req_acc),
        reset_if(mem_stage != stage),
        reset_if(mem_demo_mode == 0x80)
    ]
    if a_id != 18297:
        logic.append(reset_if(mem_p1_lives == 0x00))
    if a_id == 18230:
        logic.append(reset_if(mem_accuracy == 0xffff))
        
    ach.add_core(logic)
    my_set.add_achievement(ach)

# 4. SALAS SECRETAS
secret_data = [
    (18217, "Web of Secrets", "Discover the first secret room in Climb", 2, "716324", [0x3a], 0x04),
    (629398, "West Coast Connection", "Discover the first secret room in San Francisco", 2, "716325", [0x3a, 0x38], 0x10),
    (629399, "Marvel's First Family", "Discover the secret room in the Fantastic 4 Lab", 2, "716326", [0x36], 0x1a),
    (629400, "To Protect and Serve", "Discover the secret room in the Police Station", 2, "716327", [0x3c], 0x22),
    (629401, "Skyline Scavenger", "Discover the secret room on the Manhattan Rooftop", 2, "716329", [0x3e], 0x26),
    (629402, "Ruins of Hope", "Discover the secret room in the Ruined Boy's Home", 2, "716330", [0x3c], 0x34),
]

for a_id, title, desc, pts, badge, trigger_stages, delta_stage in secret_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.MISSABLE)
    logic = []
    
    if len(trigger_stages) > 1:
        logic.append(or_next(mem_stage == trigger_stages[0]))
        logic.append(trigger(mem_stage == trigger_stages[1]))
    else:
        logic.append(trigger(mem_stage == trigger_stages[0]))
        
    logic.extend([
        (mem_stage.delta() == delta_stage),
        (mem_game_state == 0x00)
    ])
    ach.add_core(logic)
    my_set.add_achievement(ach)

ach = Achievement(id=629406, title="Liberty's Gift", description="Discover the secret room at the Statue of Liberty", points=5, badge="716328", type=AchievementType.MISSABLE)
ach.add_core([(mem_stage == 0x2a), (mem_game_state == 0x00), (word(0x000b7c) >= 0x01), (word(0x000b7c).delta() == 0x00)])
my_set.add_achievement(ach)

# 5. PONTUAÇÃO E DESAFIOS GERAIS
ach = Achievement(id=18314, title="Neighbourhood Watch", description="Reach a score of 10,000 points", points=5, badge="712415")
ach.add_core([(mem_score_10k >= 0x01), (mem_score_10k.delta() < 0x01), (mem_game_state == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=18315, title="Downtown Defenders", description="Reach a score of 50,000 points", points=10, badge="712416")
ach.add_core([(mem_score_10k >= 0x05), (mem_score_10k.delta() < 0x05), (mem_game_state == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=18316, title="Ultimate Alliance", description="Reach a score of 100,000 points", points=25, badge="712417")
ach.add_core([(mem_score_100k >= 0x01), (mem_score_100k.delta() < 0x01), (mem_game_state == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=18306, title="Maximum Spider", description="Reach the maximum number of lives", points=25, badge="712418")
ach.add_core([(mem_p1_lives >= 0x09), (mem_p1_lives.delta() < 0x09), (mem_game_state == 0x00), reset_next_if(mem_stage == 0x00), pause_if((byte(0x0019cf) == 0x05).with_hits(1))])
my_set.add_achievement(ach)

ach = Achievement(id=18221, title="Web Slinging Sinner", description="During The Chase, land at least one hit on Demogoblin", points=10, badge="712421", type=AchievementType.MISSABLE)
ach.add_core([(mem_stage == 0x0c), (mem_game_state == 0x00), trigger((word(0x000966) > 0x3c6).with_hits(1)), reset_if(mem_stage != 0x0c)])
my_set.add_achievement(ach)

# 6. ENDGAME & CONDIÇÕES DE VITÓRIA
ach = Achievement(id=18302, title="Maximum Carnage", description="Complete the game", points=10, badge="712414", type=AchievementType.WIN_CONDITION)
ach.add_core([
    (mem_stage == 0x34), (mem_game_state == 0x00),
    trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x64).with_hits(1),
    and_next(mem_p2_lives == 0x00), reset_if(mem_p1_lives == 0x00),
    reset_if(mem_stage == 0x00), reset_if(mem_stage == 0x3c)
])
my_set.add_achievement(ach)

ach = Achievement(id=18284, title="Maximum Responsibility", description="Defeat Carnage in the 'The End' stage playing exclusively as Spider-Man", points=25, badge="716319", type=AchievementType.MISSABLE)
ach.add_core([
    trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x3c).with_hits(1),
    (mem_stage == 0x32), and_next(mem_stage == 0x32),
    and_next((mem_boss_hp == 0x3c).with_hits(1)),
    pause_if((mem_char == 0x02).with_hits(1))
])
ach.add_alt([reset_if(mem_stage == 0x00), reset_if(mem_p1_lives == 0x00)])
my_set.add_achievement(ach)

ach = Achievement(id=18304, title="Wallcrawler's Resolve", description="Complete the game with 4 or more lives remaining on the active character", points=25, badge="712436")
ach.add_core([
    (mem_stage == 0x34), (mem_game_state == 0x00),
    (mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x64).with_hits(1),
    (mem_p1_lives >= 0x04),
    reset_if(mem_p1_lives == 0x00),
    reset_if(mem_stage == 0x00),
    reset_if(mem_accuracy == 0x10),
    reset_if(byte(0x0019cf) == 0x05),
    reset_if(byte(0x0019d1) == 0x05),
    reset_if(mem_demo_mode == 0x80),
    reset_if(mem_stage == 0x3c)
])
my_set.add_achievement(ach)

ach = Achievement(id=18303, title="Resilient Duo", description="Complete the game with 1 or more continues remaining", points=25, badge="712435")
ach.add_core([
    (mem_stage == 0x34), (mem_game_state == 0x00),
    trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x64).with_hits(1),
    (mem_continues >= 0x01),
    and_next(mem_p1_lives == 0x00), reset_if(mem_p2_lives == 0x00),
    reset_if(mem_stage == 0x00), reset_if(byte(0x0019cf) == 0x05),
    reset_if(byte(0x0019d1) == 0x05), reset_if(mem_demo_mode == 0x80),
    reset_if(mem_stage == 0x3c)
])
my_set.add_achievement(ach)

ach = Achievement(id=18305, title="Unbreakable Duo", description="Complete the game with 3 or more continues remaining", points=50, badge="712437")
ach.add_core([
    (mem_stage == 0x34), (mem_game_state == 0x00),
    trigger(mem_boss_hp == 0x00), (mem_boss_hp.delta() == 0x64).with_hits(1),
    (mem_continues >= 0x03),
    and_next(mem_p1_lives == 0x00), reset_if(mem_p2_lives == 0x00),
    reset_if(mem_stage == 0x00), reset_if(byte(0x0019cf) == 0x05),
    reset_if(byte(0x0019d1) == 0x05), reset_if(mem_demo_mode == 0x80),
    reset_if(mem_stage == 0x3c)
])
my_set.add_achievement(ach)

my_set.save()