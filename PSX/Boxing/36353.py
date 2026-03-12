from pycheevos.core.helpers import *
from pycheevos.core.constants import AchievementType
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet
import operator
from functools import reduce

my_set = AchievementSet(game_id=36353, title="Boxing Achievements")

# 1. ALIAS DE MEMÓRIA GLOBAIS
mem_screen  = byte(0x1feff0)
mem_menu    = byte(0x1fef74)
mem_champ   = byte(0x1fef70)
mem_char    = byte(0x1fef66)
mem_rank    = byte(0x1fef68)
mem_p1_ctrl = byte(0x1fef84)
mem_p2_ctrl = byte(0x1fef88)
mem_p1_vs   = byte(0x1fedb0)
mem_p2_vs   = byte(0x1fede8)
mem_diff    = word(0x1fe564)

ptr_base    = tbyte(0x1fe480)
win_match   = ptr_base >> bit0(0x0000c8)
match_state = ptr_base >> byte(0x000018)
in_fight    = (mem_screen == 0x0e) | (mem_screen == 0x0d)

OFFSET_CHAR = 0x50

# 2. FEATHERS / IMPACTS / LEGENDS (Títulos de Campeonato)
champ_data = [
    (589160, 0,  "Heavyweight Impact", "Win the Local Championship in the Heavyweight weight class", 10, "670388", AchievementType.PROGRESSION),
    (589156, 1,  "Local Impact", "Win the Local Championship in the Middleweight weight class", 2, "670386", AchievementType.PROGRESSION),
    (589152, 2,  "Bronze Feather", "Win the Local Championship in the Lightweight weight class", 2, "670383", AchievementType.PROGRESSION),
    (589161, 3,  "Titan of the Nation", "Win the National Championship in the Heavyweight weight class", 10, "670389", AchievementType.PROGRESSION),
    (589157, 4,  "National Pride", "Win the National Championship in the Middleweight weight class", 5, "669866", AchievementType.PROGRESSION),
    (589153, 5,  "Silver Feather", "Win the National Championship in the Lightweight weight class", 2, "670384", AchievementType.PROGRESSION),
    (589162, 6,  "Heavyweight Legend", "Win the World Championship in the Heavyweight weight class", 10, "670390", AchievementType.PROGRESSION),
    (589158, 7,  "Global Domination", "Win the World Championship in the Middleweight weight class", 10, "670387", AchievementType.PROGRESSION),
    (589154, 8,  "Gold Feather", "Win the World Championship in the Lightweight weight class", 5, "670385", AchievementType.PROGRESSION),
    (589163, 9,  "The Final Challenge", "Win the Secret Championship in the Heavyweight weight class", 25, "670392", AchievementType.WIN_CONDITION),
    (589159, 10, "Middleweight Enigma", "Win the Secret Championship in the Middleweight weight class", 10, "669868", AchievementType.PROGRESSION),
    (589155, 11, "Platinum Feather", "Win the Secret Championship in the Lightweight weight class", 10, "670391", AchievementType.PROGRESSION),
]

for a_id, champ_val, title, desc, pts, badge, a_type in champ_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=a_type)
    ach.add_core([
        in_fight,
        win_match == 1,
        match_state == 0x13,
        mem_champ == champ_val,
        mem_champ.delta() == champ_val
    ])
    my_set.add_achievement(ach)

# 3. UNLOCKS DE PERSONAGENS
unlock_data = [
    (589149, 0x1fe6d3, "Son of a Legend", "Unlock the fighter B.T.", 2, "669846"),
    (589140, 0x1fe6d4, "Lightning Counter", "Unlock the fighter Puma", 2, "669847"),
    (589141, 0x1fe6d5, "The Prince's Ambition", "Unlock the fighter Prince", 2, "669848"),
    (589142, 0x1fe6d6, "Precise Intuition", "Unlock the fighter Misha", 5, "669849"),
    (589143, 0x1fe6d7, "The Living Legend", "Unlock the fighter Silver Man", 5, "669850"),
    (589144, 0x1fe6d8, "Devastating Reach", "Unlock the fighter Gio", 5, "669851"),
    (589145, 0x1fe6d9, "From Dohyo to the Ring", "Unlock the fighter Kojiromaru", 5, "669852"),
    (589146, 0x1fe6da, "The Ring Spy", "Unlock the fighter Spice", 5, "669853"),
    (589147, 0x1fe6db, "Warrior of the Sun", "Unlock the fighter Asteka", 10, "669854"),
    (589148, 0x1fe6dc, "The Disguised Champion", "Unlock the fighter Mr. Crown", 10, "669855"),
]
for a_id, addr, title, desc, pts, badge in unlock_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([mem_menu == 1, byte(addr).delta() == 0, byte(addr) == 1])
    my_set.add_achievement(ach)

# 4. RING ENCYCLOPEDIA & MASTER OF TECHNIQUES
# Ring Encyclopedia (589139)
encyc_addrs = range(0x1fe6d0, 0x1fe6dd)
core_encyc = [add_hits((byte(addr) == 2).with_hits(1)) for addr in encyc_addrs]
core_encyc.append(measured((value(0) == 1).with_hits(13)))
core_encyc.extend([add_hits((byte(addr).delta() == 1)) for addr in encyc_addrs])
core_encyc.extend([add_hits((byte(addr) == 2)) for addr in encyc_addrs])
core_encyc.extend([(value(0) == 1).with_hits(1), reset_if(mem_menu != 1)])

ach_encyc = Achievement(id=589139, title="Ring Encyclopedia", description="Unlock every bio note and secret for every fighter", points=25, badge="670227")
ach_encyc.add_core(core_encyc)
my_set.add_achievement(ach_encyc)

# Master of Techniques (589151)
tech_addrs = [0x1fe6dd, 0x1fe6de, 0x1fe6df, 0x1fe6e3, 0x1fe6e4, 0x1fe6e5, 0x1fe6e9, 0x1fe6ea, 0x1fe6ef, 0x1fe6f0, 0x1fe6f1, 0x1fe6f2, 0x1fe6f5, 0x1fe6fb, 0x1fe6fc, 0x1fe6fd, 0x1fe701, 0x1fe702, 0x1fe707, 0x1fe70d, 0x1fe70e, 0x1fe70f, 0x1fe713, 0x1fe714, 0x1fe719, 0x1fe71a, 0x1fe71b, 0x1fe71f, 0x1fe725, 0x1fe726]
core_tech = [add_hits((byte(addr) == 1).with_hits(1)) for addr in tech_addrs]
core_tech.append(measured((value(0) == 1).with_hits(30)))
core_tech.extend([add_hits((byte(addr).delta() == 1).with_hits(1)) for addr in tech_addrs])
core_tech.extend([(value(0) == 1).with_hits(29), reset_if(mem_menu != 4)])

ach_tech = Achievement(id=589151, title="Master of Techniques", description="Successfully perform the special move of each of the 13 characters", points=10, badge="670229")
ach_tech.add_core(core_tech)
my_set.add_achievement(ach_tech)

# 5. CONQUISTAS "CHAMPION'S RETIREMENT" E "TRUE VETERAN" (Alts Automáticos)
# Champion's Retirement (589309)
ach = Achievement(id=589309, title="Champion's Retirement", description="Win the World Championship in all three weight classes with the same fighter", points=10, badge="670230")
ach.add_core([mem_screen != 0x13, add_address(tbyte(0x1fe480)), trigger((byte(0x000018) == 0x13))])
for char_id in range(13):
    t_light = word(0x1fe768 + (char_id * OFFSET_CHAR))
    t_mid   = word(0x1fe770 + (char_id * OFFSET_CHAR))
    t_heavy = word(0x1fe778 + (char_id * OFFSET_CHAR))
    ach.add_alt([mem_char == char_id, t_light.delta() == 0, t_light > 0, t_mid > 0, t_heavy > 0])
    ach.add_alt([mem_char == char_id, t_light > 0, t_mid.delta() == 0, t_mid > 0, t_heavy > 0])
    ach.add_alt([mem_char == char_id, t_light > 0, t_mid > 0, t_heavy.delta() == 0, t_heavy > 0])
my_set.add_achievement(ach)

# True Veteran (589821)
ach = Achievement(id=589821, title="True Veteran", description="Reach Veteran level with any character", points=10, type=AchievementType.PROGRESSION, badge="669877")
ach.add_core([mem_screen != 0x13])
for char_id in range(13):
    char_rank = byte(0x1fe733 + (char_id * OFFSET_CHAR))
    ach.add_alt([mem_char == char_id, char_rank.delta() < 0x63, char_rank >= 0x64])
my_set.add_achievement(ach)


# 6. GRUPO "WITHOUT LOSING A MATCH"
no_loss_data = [
    (589308, "Neighborhood Hero", "Win the Local Championship in Middleweight weight class or higher without losing a match", "670239", lambda c: c <= 1, 10),
    (589810, "National Idol", "Win the National Championship in Middleweight weight class or higher without losing a match", "670240", lambda c: (c == 3) | (c == 4), 25),
    (589812, "Living Legend", "Win the World Championship in Middleweight weight class or higher without losing a match", "670241", lambda c: (c == 6) | (c == 7), 25),
    (589814, "Beyond the Limit", "Win the Secret Championship in Middleweight weight class or higher without losing a match", "670242", lambda c: (c == 9) | (c == 10), 25),
]

match_win_flag = bit0(0x1fef6a)

for a_id, title, desc, badge, champ_cond, pts in no_loss_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.MISSABLE, badge=badge)
    ach.add_core([champ_cond(mem_champ), mem_rank == 1, match_win_flag.delta() == 0, match_win_flag == 1, add_address(tbyte(0x1fe480)), trigger(byte(0x000018) == 0x13), mem_menu == 0])
    for char_id in range(13):
        ach.add_alt([mem_char == char_id, word(0x1fe738 + (char_id * OFFSET_CHAR)) == 0])
    my_set.add_achievement(ach)

# Unshakable Perfection (A escada mágica do OrNext com reduce)
ach = Achievement(id=589818, title="Unshakable Perfection", description="Win all Championships across all weight classes without ever losing a match", points=50, type=AchievementType.MISSABLE, badge="670251")
ach.add_core([mem_screen != 0x13, mem_rank == 1, match_win_flag.delta() == 0, match_win_flag == 1])

for char_id in range(13):
    losses_pers = word(0x1fe75c + (char_id * OFFSET_CHAR))
    belts = [word(0x1fe764 + (char_id * OFFSET_CHAR) + (i * 2)) for i in range(12)]
    
    # Cria os 12 OrNext automaticamente
    or_next_deltas = reduce(operator.or_, [b.delta() == 0 for b in belts])
    current_checks = [b > 0 for b in belts]
    
    ach.add_alt([mem_char == char_id, losses_pers == 0, or_next_deltas] + current_checks)
my_set.add_achievement(ach)


# 7. CONDIÇÕES ESPECÍFICAS EM COMBATE
combat_data = [
    (589836, "Don't Blink!", "Score a KO in the first round", 1, "670253", [
        mem_screen != 0x13, mem_p1_ctrl == 1, mem_p2_ctrl == 0, in_fight,
        add_address(tbyte(0x1fe480)), dword(0x00002c) == 1, 
        add_address(tbyte(0x1fe480)), win_match.delta() == 0, 
        add_address(tbyte(0x1fe480)), win_match == 1
    ]),
    (589843, "Clean Code", "Win a fight without being knocked down", 2, "670761", [
        mem_screen != 0x13, mem_p1_ctrl == 1, mem_p2_ctrl == 0, in_fight,
        add_address(tbyte(0x1fe480)), byte(0x0000ac) == 0, 
        add_address(tbyte(0x1fe480)), byte(0x0000b0) > 0,
        add_address(tbyte(0x1fe480)), byte(0x0000c0) == 1,
        add_address(tbyte(0x1fe480)), match_state.delta() != 0x0f, 
        add_address(tbyte(0x1fe480)), match_state == 0x0f
    ]),
    (589908, "Human Dynamometer", "Knock down your opponent with a strike that registers 100kg or more of force on the impact panel", 2, "670762", [
        mem_screen != 0x13, in_fight, mem_p2_ctrl == 0, mem_p1_ctrl == 1,
        (word(0x1fee54) >= 0x1f4) | (word(0x1fee58) >= 0x1f4) | (word(0x1fee5c) >= 0x1f4),
        add_address(tbyte(0x1fe480)), byte(0x0000c0).delta() == 0, 
        add_address(tbyte(0x1fe480)), byte(0x0000c0) == 1
    ]),
    (589930, "Optimized Defense", "Win a fight while maintaining over 50% HP", 2, "670763", [
        in_fight, mem_p2_ctrl == 0, mem_p1_ctrl == 1,
        add_source(word(0x1fedd8)), sub_source(word(0x1feddc)), word(0x1fedd8) > 0,
        add_address(tbyte(0x1fe480)), byte(0x0000b0) > 0,
        add_address(tbyte(0x1fe480)), byte(0x0000c0) == 1,
        add_address(tbyte(0x1fe480)), match_state.delta() != 0x0f, 
        add_address(tbyte(0x1fe480)), match_state == 0x0f
    ]),
    (589932, "Human Projectile", "Land 5 consecutive hits without the opponent blocking", 2, "670765", [
        in_fight, mem_p2_ctrl == 0, mem_p1_ctrl == 1,
        reset_if(word(0x1fedd8) < word(0x1fedd8).delta()),
        add_address(tbyte(0x1fe480)), pause_if(bit0(0x0000d4) == 1),
        reset_if((word(0x1fee10) == word(0x1fee10).delta()).with_hits(120)),
        (word(0x1fee10) < word(0x1fee10).delta()).with_hits(5)
    ]),
    (591285, "Feline Reflex", "Block or evade 5 consecutive attacks", 5, "670803", [
        in_fight, mem_p2_ctrl == 0, mem_p1_ctrl == 1,
        reset_if(word(0x1fedd8) < word(0x1fedd8).delta()),
        and_next(word(0x1fee60) != 0), add_hits(word(0x1fee60) != word(0x1fee60).delta()),
        and_next(word(0x1fee64) != 0), add_hits(word(0x1fee64) != word(0x1fee64).delta()),
        and_next(word(0x1fee68) != 0), (word(0x1fee68) != word(0x1fee68).delta()).with_hits(5)
    ]),
    (591418, "Floor Sweeper", "K.O your opponent using a special move", 5, "670804", [
        mem_p2_ctrl == 0, mem_p1_ctrl == 1, in_fight, reset_if(mem_screen == 0x09),
        add_address(tbyte(0x1fe480)), (byte(0x0000b0) > byte(0x0000b0).delta()).with_hits(1),
        add_address(tbyte(0x1fe480)), and_next(tbyte(0x000148) == 2),
        add_address(tbyte(0x1fe480)), reset_if(byte(0x0000b0) > byte(0x0000b0).delta()),
        add_address(tbyte(0x1fe480)), bit0(0x0000c8).delta() == 0, 
        add_address(tbyte(0x1fe480)), bit0(0x0000c8) == 1
    ])
]

for a_id, title, desc, pts, badge, logic in combat_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core(logic)
    my_set.add_achievement(ach)

# Ring Dance (Alt Groups)
ach = Achievement(id=589933, title="Ring Dance", description="Survive an entire round without being hit", points=5, badge="670801")
ach.add_core([in_fight, mem_p2_ctrl == 0, (mem_p1_ctrl == 1).with_hits(1), word(0x1feddc) > 0, reset_if(word(0x1fedd8) < word(0x1feddc))])
ach.add_alt([add_address(tbyte(0x1fe480)), byte(0x0000b0) > 0, add_address(tbyte(0x1fe480)), byte(0x0000c0) == 1, add_address(tbyte(0x1fe480)), match_state.delta() != 0x0f, add_address(tbyte(0x1fe480)), trigger(match_state == 0x0f)])
ach.add_alt([add_address(tbyte(0x1fe480)), and_next(dword(0x00002c).delta() > 0), add_address(tbyte(0x1fe480)), trigger(dword(0x00002c).delta() < dword(0x00002c))])
my_set.add_achievement(ach)

# The Amazing Chicken
ach = Achievement(id=589934, title="The Amazing Chicken", description="Run away for an entire round without attacking and win the fight afterward", points=5, badge="670802")
ach.add_core([
    in_fight, mem_p2_ctrl == 0, mem_p1_ctrl == 1,
    (mem_screen == 0x0a) | reset_next_if(mem_screen == 0x09),
    add_address(tbyte(0x1fe480)), and_next(dword(0x00002c) == 1),
    pause_if((word(0x1fee10) < word(0x1fee10).delta()).with_hits(1)),
    add_address(tbyte(0x1fe480)), byte(0x00002c) > 1,
    add_address(tbyte(0x1fe480)), and_next(byte(0x0000b0) > 0),
    add_address(tbyte(0x1fe480)), and_next(byte(0x0000c0) == 1),
    add_address(tbyte(0x1fe480)), and_next(match_state.delta() != 0x0f),
    add_address(tbyte(0x1fe480)), trigger(match_state == 0x0f)
])
my_set.add_achievement(ach)


# 8. PARTIDAS DE HISTÓRIA / RIVAIS
rivals_data = [
    (591419, "Noble Final Act", "Win the World Championship as Prince in any weight class", 5, "671053", 
     [mem_char == 5, byte(0x1fe8bf) == 2, byte(0x1fe8c1).delta() == 1, byte(0x1fe8c1) == 0, add_address(tbyte(0x1fe480)), match_state.delta() != 0x13, add_address(tbyte(0x1fe480)), match_state == 0x13]),
    (591420, "Sparring of a Lifetime", "As Tanaka, defeat Silver Man on Hard difficulty or higher", 2, "671069",
     [in_fight, mem_menu == 2, (mem_diff == 0x4b) | (mem_diff == 0x64), mem_p2_ctrl == 0, mem_p1_ctrl == 1, mem_p1_vs == 0, mem_p2_vs == 7]),
    (591421, "The Script Changed", "As Ryoko, defeat her father Tanaka on Hard difficulty or higher", 5, "671070",
     [in_fight, mem_menu == 2, (mem_diff == 0x4b) | (mem_diff == 0x64), mem_p2_ctrl == 0, mem_p1_ctrl == 1, mem_p1_vs == 1, mem_p2_vs == 0]),
    (591422, "End of the Shadow", "As Red, finally defeat his colleague Ryoko on Hard difficulty or higher", 5, "671071",
     [in_fight, mem_menu == 2, (mem_diff == 0x4b) | (mem_diff == 0x64), mem_p2_ctrl == 0, mem_p1_ctrl == 1, mem_p1_vs == 2, mem_p2_vs == 1]),
    (591423, "Number One Fan", "As Misha, defeat her hero Asteka on Hard difficulty or higher", 10, "671086",
     [in_fight, mem_menu == 2, (mem_diff == 0x4b) | (mem_diff == 0x64), mem_p2_ctrl == 0, mem_p1_ctrl == 1, mem_p1_vs == 6, mem_p2_vs == 11]),
    (591424, "Childhood Pact", "As Prince, defeat his friend Gio on Hard difficulty or higher", 3, "671087",
     [in_fight, mem_menu == 2, (mem_diff == 0x4b) | (mem_diff == 0x64), mem_p2_ctrl == 0, mem_p1_ctrl == 1, mem_p1_vs == 5, mem_p2_vs == 8]),
    (591425, "Final Service", "As Spice, defeat Mr. Crown on Hard difficulty or higher", 10, "671088",
     [in_fight, mem_menu == 2, (mem_diff == 0x4b) | (mem_diff == 0x64), mem_p2_ctrl == 0, mem_p1_ctrl == 1, mem_p1_vs == 10, mem_p2_vs == 12]),
    (591426, "Master of Evasion", "Win a fight on Very Hard difficulty", 5, "671090",
     [in_fight, mem_menu == 2, mem_diff == 0x64, mem_p1_ctrl == 1, mem_p2_ctrl == 0]),
    (591427, "Shadow Boxing", "Win a fight in Exhibition mode against the same character you are using on Very Hard difficulty", 10, "671091",
     [in_fight, mem_menu == 2, mem_diff == 0x64, mem_p2_ctrl == 0, mem_p1_ctrl == 1, mem_p1_vs == mem_p2_vs])
]

# Injeta a lógica de finalização do combate para todas as conquistas de rivais
for a_id, title, desc, pts, badge, logic in rivals_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    
    if a_id != 591419:
        logic.extend([
            add_address(tbyte(0x1fe480)), and_next(byte(0x0000b0) > 0),
            add_address(tbyte(0x1fe480)), and_next(byte(0x0000c0) == 1),
            add_address(tbyte(0x1fe480)), and_next(match_state.delta() != 0x0f),
            add_address(tbyte(0x1fe480)), trigger(match_state == 0x0f)
        ])
        
    ach.add_core(logic)
    my_set.add_achievement(ach)

my_set.save()