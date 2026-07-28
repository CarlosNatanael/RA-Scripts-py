from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=1179, title="Maximum Carnage")

# 1. ALIASES DE MEMÓRIA
mem_stage      = word(0x000a0e)
mem_pause      = byte(0x00088e)
mem_lives      = word(0x000990)
mem_conts      = word(0x000994)
mem_score_10k  = byte(0x000980) 
mem_score_100k = byte(0x000982) 
mem_hits       = word(0x000966)
mem_boss_hp    = word(0x000dc0)

mem_clear_flag = byte(0x001cca)
mem_accuracy   = byte(0x001ccc)

cheat_energy   = byte(0x0019cd)
cheat_lives    = byte(0x0019cf)
cheat_conts    = byte(0x0019d1)

# 2. PROGRESSÃO DE FASES
# (ID, Título, Descrição, Pontos, Badge, Fase Alvo, Fases Anteriores)
prog_data = [
    (18214, "Swinging Into Action", "Clear Level 1 - New York Streets", 5, "712398", 0x04, [0x02]),
    (18216, "Scaling the Streets", "Clear Level 2 - Climb", 5, "712399", 0x06, [0x04]),
    (18218, "Double Trouble", "Clear Level 3 - Rooftop", 5, "712400", 0x08, [0x06]),
    (18219, "Back Alley Brawler", "Clear Level 4 - Alleyway", 5, "712401", 0x0a, [0x08]),
    (18220, "Unlikely Allies", "Clear Level 5 - The Hall", 5, "712402", 0x0c, [0x0a]),
    (18227, "Frisco Throwdown", "Clear Level 6 - San Francisco", 5, "712403", 0x12, [0x10]),
    (18222, "Mayhem in Manhattan", "Clear Level 7 - Times Square or Central Park as either character", 5, "712404", 0x14, [0x12, 0x0e]), # Suporta os dois caminhos
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

for a_id, title, desc, pts, badge, target, prevs in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.PROGRESSION)
    conds = []
    
    # Tratamento para fases com múltiplos caminhos
    if len(prevs) > 1:
        for p in prevs[:-1]:
            conds.append(or_next(mem_stage.delta() == p))
            
    conds.append((mem_stage.delta() == prevs[-1]))
    conds.append((mem_stage == target))
    conds.append((mem_pause == 0x00))
    ach.add_core(conds)
    my_set.add_achievement(ach)

# 3. PRECISÃO NOS COMBATES (ACCURACY)
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

for a_id, title, desc, pts, badge, target_stage, target_acc in acc_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_stage == target_stage),
        (mem_clear_flag == 0xff).with_hits(1),
        (mem_accuracy >= target_acc),
        (mem_accuracy.delta() < target_acc),
        reset_if(mem_stage != target_stage),
        reset_if(cheat_energy == 0x80),
    ])
    my_set.add_achievement(ach)

# 4. PONTUAÇÃO (SCORE)
score_data = [
    (18314, "Neighbourhood Watch", "Reach a score of 10,000 points", 5, "712415", mem_score_10k, 0x01),
    (18315, "Downtown Defenders", "Reach a score of 50,000 points", 10, "712416", mem_score_10k, 0x05),
    (18316, "Ultimate Alliance", "Reach a score of 100,000 points", 25, "712417", mem_score_100k, 0x01),
]

for a_id, title, desc, pts, badge, mem_addr, target in score_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_addr >= target),
        (mem_addr.delta() < target),
        (mem_pause == 0x00),
    ])
    my_set.add_achievement(ach)

# 5. FINAIS (WIN CONDITIONS E DESAFIOS)
endings_data = [
    (18302, "Maximum Carnage", "Complete the game", 10, "712414", []),
    (18303, "Resilient Duo", "Complete the game with 1 or more continues remaining", 25, "712435", [
        reset_if(mem_conts < 0x01),
        reset_if(cheat_lives == 0x05),
        reset_if(cheat_conts == 0x05),
        reset_if(cheat_energy == 0x80)
    ]),
    (18304, "Wallcrawler's Resolve", "Complete the game with 4 or more lives remaining on the active character", 25, "712436", [
        reset_if(mem_lives < 0x04),
        reset_if(cheat_lives == 0x05),
        reset_if(cheat_conts == 0x05),
        reset_if(cheat_energy == 0x80)
    ]),
    (18305, "Unbreakable Duo", "Complete the game with 3 or more continues remaining", 50, "712437", [
        reset_if(mem_conts < 0x03),
        reset_if(cheat_lives == 0x05),
        reset_if(cheat_conts == 0x05),
        reset_if(cheat_energy == 0x80)
    ]),
]

for a_id, title, desc, pts, badge, restrictions in endings_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.WIN_CONDITION if not restrictions else AchievementType.STANDARD)
    ach.add_core([
        (mem_stage == 0x34),
        (mem_pause == 0x00),
        (mem_boss_hp == 0x00),
        (mem_boss_hp.delta() == 0x64).with_hits(1),
        reset_if(mem_stage == 0x00),
        or_next(mem_lives == 0x00),
        reset_if(mem_accuracy == 0x10),
        *restrictions
    ])
    my_set.add_achievement(ach)

# 6. MISCELÂNEA E MISSABLES
ach = Achievement(id=18306, title="Maximum Spider", description="Reach the maximum number of lives", points=25, badge="712418")
ach.add_core([
    (mem_lives >= 0x09),
    (mem_lives.delta() < 0x09),
    (mem_pause == 0x00),
    reset_next_if(mem_stage == 0x00),
    pause_if((cheat_lives == 0x05).with_hits(1)),
])
my_set.add_achievement(ach)

ach = Achievement(id=18217, title="Web of Secrets", description="Find a secret room", points=2, badge="712419", type=AchievementType.MISSABLE)
ach.add_core([
    trigger(mem_stage == 0x3a),
    (mem_stage.delta() == 0x04),
    (mem_pause == 0x00),
])
my_set.add_achievement(ach)

ach = Achievement(id=18221, title="Web Slinging Sinner", description="During The Chase, land at least one hit on Demogoblin", points=10, badge="712421", type=AchievementType.MISSABLE)
ach.add_core([
    (mem_stage == 0x0c),
    (mem_pause == 0x00),
    trigger((mem_hits > mem_hits.delta()).with_hits(1)),
    reset_if(mem_stage != 0x0c),
])
my_set.add_achievement(ach)

my_set.save()