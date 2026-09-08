from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=41205, title="Pokémon - Refactored")

# 1. ALIASES DE MEMÓRIA (Chega de espalhar endereços)
ptr_battle    = tbyte(0x005008)
ptr_badges    = tbyte(0x005010)

mem_trainer   = word(0x0406ae)
mem_map       = word(0x008004)
mem_b_state   = word(0x00801c)
mem_win_flag  = byte(0x02be8a)
mem_badge_flg = byte(0x0051fc)
mem_game_clr  = dword(0x02bfe8)

def get_party_levels():
    """Retorna os endereços de level de toda a party"""
    return [byte(addr) for addr in (0x02c2d8, 0x02c33c, 0x02c3a0, 0x02c404, 0x02c468, 0x02c4cc)]

# 2. GYM LEADERS (PROGRESSÃO)
gym_data = [
    (631785, "Rock-Solid Immunity", "Defeat Brock", 5, "723053", 0x19e, bit0),
    (631786, "Hydrotherapy", "Defeat Misty", 5, "723054", 0x19f, bit1),
    (631787, "Shock Treatment", "Defeat Lt. Surge", 5, "723055", 0x1a0, bit2),
    (631788, "Alternative Medicine", "Defeat Erika", 5, "723056", 0x1a1, bit3),
    (631789, "Venom Tolerance", "Defeat Koga", 5, "723057", 0x1a2, bit4),
    (631790, "Psychological Evaluation", "Defeat Sabrina", 5, "723058", 0x1a4, bit5),
    (631791, "Third-Degree Burns", "Defeat Blaine", 5, "723059", 0x1a3, bit6),
    (631792, "The Final Prescription", "Defeat Head Nurse Joy at the Viridian Gym", 10, "723060", 0x15e, bit7),
]

for a_id, title, desc, pts, badge, trainer_id, bit_func in gym_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_trainer == trainer_id),
        add_address(ptr_badges), (bit_func(0x0051fc) == 0x01),
        add_address(ptr_badges), (bit_func(0x0051fc).delta() == 0x00),
        add_address(ptr_battle), (mem_b_state == 0x03),
    ])
    my_set.add_achievement(ach)

# 3. LEVEL CAPS (MISSABLES)
cap_data = [
    (631793, "Triage", "Defeat Brock while only using Pokémon that are level 15 or less", 10, "723061", 0x19e, 15),
    (631794, "First Aid", "Defeat Misty while only using Pokémon that are level 23 or less", 10, "723062", 0x19f, 23),
    (631795, "Defibrillator", "Defeat Lt. Surge while only using Pokémon that are level 26 or less", 10, "723063", 0x1a0, 26),
    (631796, "Herbal Remedy", "Defeat Erika while only using Pokémon that are level 31 or less", 10, "723064", 0x1a1, 31),
    (631797, "Toxicology", "Defeat Koga while only using Pokémon that are level 43 or less", 10, "723065", 0x1a2, 43),
    (631798, "Psychiatry", "Defeat Sabrina while only using Pokémon that are level 45 or less", 10, "723066", 0x1a4, 45),
    (631799, "Burn Treatment", "Defeat Blaine while only using Pokémon that are level 50 or less", 10, "723067", 0x1a3, 50),
    (631800, "Discharged!", "Survive against Head Nurse Joy while only using Pokémon that are level 50 or less", 25, "723068", 0x15e, 50),
]

for a_id, title, desc, pts, badge, trainer_id, cap in cap_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.MISSABLE)
    
    logic = [
        (mem_trainer == trainer_id),
        trigger(mem_win_flag == 0x01),
        (mem_win_flag.delta() == 0x00),
    ]
    for lvl_mem in get_party_levels():
        logic.append((lvl_mem <= cap))
        
    logic.extend([
        add_address(ptr_battle),
        (mem_b_state == 0x03),
    ])
    
    ach.add_core(logic)
    my_set.add_achievement(ach)

# 4. ELITE FOUR, CHEFES E SECRET TRAINERS
boss_data = [
    (631802, "Contraband Confiscated", "Defeat Head Nurse Joy in the Game Corner Hideout", 10, "723069", 0x15c, 0x2d01),
    (631803, "Autopsy Report", "Defeat the RESEARCHER in the Pokémon Tower and expel Team Rocket", 25, "723070", 0x173, 0x5e01),
    (631804, "Patent Denied", "Defeat Head Nurse Joy at Silph Co. and prevent the corporate monopoly", 25, "723071", 0x15d, 0x3901),
    (631805, "Malpractice Ended", "Defeat the Admin on Five Island and shut down Team Rocket's last illegal clinic", 10, "723072", 0x220, 0x7201),
    (631809, "Patient Zero", "Defeat Lorelei", 10, "723074", 0x19a, 0x4b01),
    (631811, "Blunt Force Trauma", "Defeat Bruno", 10, "723075", 0x19b, 0x4c01),
    (631810, "Cryogenics", "Defeat Agatha", 10, "723076", 0x19c, 0x4d01),
    (631812, "Terminal Diagnosis", "Defeat Lance", 10, "723077", 0x19d, 0x4e01),
    (631807, "Unethical Origins", "Defeat the Geneticist in Cerulean Cave", 10, "723079", 0x2ee, 0x4a01),
    (631818, "General Practitioner", "Discover the whereabouts of Team Rocket's true creator", 10, "723085", 0x2ed, 0x7a01),
    (631819, "The Amphibian Anomaly", "Defeat the secret trainer obsessed with frogs", 25, "723086", 0x2ec, 0x5701),
    (631820, "Reviewer", "Defeat the engineer hidden somewhere on the map", 25, "723087", 0x2eb, 0x1403),
    (631821, "The Sprite Artist", "Defeat the master of custom art", 25, "723088", 0x2e7, 0x1203),
    (631822, "Chaotic Results", "Survive the chaos of the secret trainer", 25, "723089", 0x2e8, 0x503),
    (631823, "Malevolent Intent", "Defeat the trainer with a malevolent aura", 25, "723090", 0x2ea, 0x5f01),
    (631824, "Moonlight Sonata", "Defeat the secret trainer isolated in the shadows", 25, "723091", 0x2e9, 0x2302),
]

for a_id, title, desc, pts, badge, trainer_id, map_id in boss_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_trainer == trainer_id),
        add_address(ptr_battle), (mem_map == map_id),
        add_address(ptr_battle), (mem_b_state == 0x03),
        trigger(mem_win_flag == 0x01),
        (mem_win_flag.delta() == 0x00),
    ])
    my_set.add_achievement(ach)

# 5. CONQUISTAS ESPECÍFICAS E COMPLEXAS

# --- Survival of the Fittest (Rival Route 22) ---
ach = Achievement(id=631801, title="Survival of the Fittest", description="Defeat your rival on Route 22", points=5, badge="723052", type=AchievementType.MISSABLE)
ach.add_core([
    add_address(ptr_battle), (mem_map == 0x2903),
    or_next((mem_trainer == 0x149)), or_next((mem_trainer == 0x14a)), (mem_trainer == 0x14b),
    trigger(mem_win_flag == 0x01), (mem_win_flag.delta() == 0x00),
    add_address(ptr_battle), (mem_b_state == 0x03),
])
my_set.add_achievement(ach)

# --- Open-Heart Surgeon (Rival Champion) ---
ach = Achievement(id=631813, title="Open-Heart Surgeon", description="Defeat your rival in the Pokémon League", points=25, badge="723078", type=AchievementType.WIN_CONDITION)
ach.add_core([
    or_next((mem_trainer == 0x1b6)), or_next((mem_trainer == 0x1b7)), (mem_trainer == 0x1b8),
    add_address(ptr_battle), (mem_map == 0x4f01),
    add_address(ptr_battle), (mem_b_state == 0x03),
    trigger(mem_win_flag == 0x01), (mem_win_flag.delta() == 0x00),
])
my_set.add_achievement(ach)

# --- Board Certification (E4 Rematch) ---
ach = Achievement(id=631814, title="Board Certification", description="Defeat the Pokémon League during a rematch", points=25, badge="723082")
ach.add_core([
    or_next((mem_trainer == 0x2e3)), or_next((mem_trainer == 0x2e4)), (mem_trainer == 0x2e5),
    add_address(ptr_battle), (mem_map == 0x4f01),
    add_address(ptr_battle), (mem_b_state == 0x03),
    trigger(mem_win_flag == 0x01), (mem_win_flag.delta() == 0x00),
])
my_set.add_achievement(ach)

# --- Gene Therapy (Mewtwo) ---
ach = Achievement(id=631808, title="Gene Therapy", description="Capture Mewtwo in Cerulean Cave", points=10, badge="723080")
ach.add_core([
    (word(0x02bc3c) == 0x96),
    add_address(ptr_battle), (mem_map == 0x4a01),
    trigger((mem_win_flag == 0x07)), (mem_win_flag.delta() == 0x00),
])
my_set.add_achievement(ach)

# --- Perfect Immunity (National Dex) ---
ach = Achievement(id=631816, title="Perfect Immunity", description="Obtain the National Pokédex", points=5, badge="723081")
ach.add_core([
    add_address(ptr_badges), (bit0(0x005200) == 0x01).with_hits(1),
    add_address(ptr_badges), (bit0(0x005200).delta() == 0x00),
    reset_if((ptr_badges != ptr_badges.delta())),
    add_address(ptr_battle), reset_if((mem_map != 0x304)),
])
my_set.add_achievement(ach)

# --- Second Opinion (Level 90) ---
# Usando Python para simplificar os 12 'or_next'
party = get_party_levels()
ach_631815_logic = [or_next((p >= 0x5a)) for p in party[:-1]] + [(party[-1] >= 0x5a)]
ach_631815_logic += [or_next((p.delta() < 0x5a)) for p in party[:-1]] + [(party[-1].delta() < 0x5a)]
ach_631815_logic += [
    or_next((mem_game_clr == 0x00)),
    (mem_game_clr == 0x2000010),
    add_address(ptr_battle), (mem_b_state == 0x03),
]
ach = Achievement(id=631815, title="Second Opinion", description="Reach Level 90", points=5, badge="723083")
ach.add_core(ach_631815_logic)
my_set.add_achievement(ach)

# --- Medical History (Fame Checker) ---
ach = Achievement(id=631806, title="Medical History", description="Gather all of Head Nurse Joy's medical records in the Fame Checker", points=5, badge="723073")
ach.add_core([
    reset_if((ptr_battle != ptr_battle.delta())),
    (mem_game_clr == 0x00).with_hits(1),
    add_address(ptr_battle), add_source(bit2(0x00ba90)),
    add_address(ptr_battle), add_source(bit3(0x00ba90)),
    add_address(ptr_battle), add_source(bit4(0x00ba90)),
    add_address(ptr_battle), add_source(bit5(0x00ba90)),
    add_address(ptr_battle), add_source(value(0)),
])
ach.add_alt([
    value(0),
    add_address(ptr_battle), measured((bit7(0x00ba90) == 0x06)),
    add_address(ptr_battle), measured_if((mem_map != 0x00)),
    add_address(ptr_battle), add_source(bit2(0x00ba90).delta()),
    add_address(ptr_battle), add_source(bit3(0x00ba90).delta()),
    add_address(ptr_battle), add_source(bit4(0x00ba90).delta()),
    add_address(ptr_battle), add_source(bit5(0x00ba90).delta()),
    add_address(ptr_battle), add_source(value(0).delta()),
])
ach.add_alt([
    value(0), add_address(ptr_battle), (bit7(0x00ba90).delta() == 0x05),
])
my_set.add_achievement(ach)

# --- Extensive Research (HM Gym Challenge) ---
def generate_hm_checks(hm_slot, is_and=False):
    """Gera a lista de or_next para validar se o slot possui um HM"""
    hm_ids = [0x0f, 0x13, 0x39, 0x46, 0x7f, 0x94]
    checks = [or_next((hm_slot == hm)) for hm in hm_ids]
    if is_and:
        checks.append(and_next((hm_slot == 0xf9)))
    else:
        checks.append((hm_slot == 0xf9))
    return checks

ach = Achievement(id=631817, title="Extensive Research", description="Defeat a Gym Leader with at most one Pokémon in the party, who knows at least 3 HM moves", points=10, badge="723084", type=AchievementType.MISSABLE)
ach.add_core([
    (byte(0x02c029) == 0x01), (mem_game_clr == 0x2000010),
    trigger(mem_win_flag == 0x01), (mem_win_flag.delta() == 0x00),
    or_next((mem_trainer == 0x19e)), or_next((mem_trainer == 0x19f)),
    or_next((mem_trainer == 0x1a0)), or_next((mem_trainer == 0x1a1)),
    or_next((mem_trainer == 0x1a2)), or_next((mem_trainer == 0x1a3)),
    or_next((mem_trainer == 0x1a4)), (mem_trainer == 0x15e),
])

# Os 4 slots de ataques do primeiro Pokémon
moves = [word(0x02bbf0), word(0x02bbf2), word(0x02bbf4), word(0x02bbf6)]

# Alt 1: Moves 0, 1 e 2
ach.add_alt(generate_hm_checks(moves[0], True) + generate_hm_checks(moves[1], True) + generate_hm_checks(moves[2], False))
# Alt 2: Moves 0, 1 e 3
ach.add_alt(generate_hm_checks(moves[0], True) + generate_hm_checks(moves[1], True) + generate_hm_checks(moves[3], False))
# Alt 3: Moves 0, 2 e 3
ach.add_alt(generate_hm_checks(moves[0], True) + generate_hm_checks(moves[2], True) + generate_hm_checks(moves[3], False))
# Alt 4: Moves 1, 2 e 3
ach.add_alt(generate_hm_checks(moves[1], True) + generate_hm_checks(moves[2], True) + generate_hm_checks(moves[3], False))

my_set.add_achievement(ach)

my_set.save()