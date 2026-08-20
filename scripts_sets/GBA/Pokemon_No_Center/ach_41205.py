from pycheevos.core.helpers import *
from pycheevos.models.achievement import *
from pycheevos.models.set import *
from itertools import *

my_set = AchievementSet(game_id=41205, title="Pokémon FireRed - Refactored")

# 1. ALIASES DE MEMÓRIA E PONTEIROS
ptr_save1       = tbyte(0x005008)
ptr_party       = tbyte(0x005010)

mem_trainer_id  = word(0x0406ae)
mem_battle_out  = byte(0x02be8a)
mem_battle_flag = byte(0x02c029)
mem_game_state  = dword(0x02bfe8)
mem_map_id      = word(0x008004)
mem_last_heal   = word(0x00801c)
mem_wild_pkmn   = word(0x02bc3c)
mem_pokedex     = bit4(0x005200)

# 2. PROGRESSÃO DOS LÍDERES E HISTÓRIA
# Dados: (ID, Título, Descrição, Pontos, Trainer ID, Badge Bit / Condição Extra)
prog_data = [
    (631785, "Rock-Solid Immunity", "Defeat Brock", 5, 0x19e, bit0(0x0051fc)),
    (631786, "Hydrotherapy", "Defeat Misty", 5, 0x19f, bit1(0x0051fc)),
    (631787, "Shock Treatment", "Defeat Lt. Surge", 5, 0x1a0, bit2(0x0051fc)),
    (631788, "Alternative Medicine", "Defeat Erika", 5, 0x1a1, bit3(0x0051fc)),
    (631789, "Venom Tolerance", "Defeat Koga", 5, 0x1a2, bit4(0x0051fc)),
    (631790, "Psychological Evaluation", "Defeat Sabrina", 5, 0x1a4, bit5(0x0051fc)),
    (631791, "Third-Degree Burns", "Defeat Blaine", 5, 0x1a3, bit6(0x0051fc)),
    (631792, "The Final Prescription", "Defeat Head Nurse Joy at the Viridian Gym", 10, 0x15e, bit7(0x0051fc)),
]

for a_id, title, desc, pts, t_id, badge_func in prog_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.PROGRESSION)
    ach.add_core([
        (mem_trainer_id == t_id),
        add_address(ptr_party),
        (badge_func == 1),
        add_address(ptr_party),
        (badge_func.delta() == 0),
        add_address(ptr_save1),
        (mem_last_heal == 3),
    ])
    my_set.add_achievement(ach)

# 3. DESAFIOS DE LEVEL CAP (MISSABLES)
lvl_addresses = [byte(0x02c2d8), byte(0x02c33c), byte(0x02c3a0), byte(0x02c404), byte(0x02c468), byte(0x02c4cc)]

cap_data = [
    (631793, "Triage", "Defeat Brock while only using Pokémon that are level 15 or less", 10, 0x19e, 15),
    (631794, "First Aid", "Defeat Misty while only using Pokémon that are level 23 or less", 10, 0x19f, 23),
    (631795, "Defibrillator", "Defeat Lt. Surge while only using Pokémon that are level 26 or less", 10, 0x1a0, 26),
    (631796, "Herbal Remedy", "Defeat Erika while only using Pokémon that are level 31 or less", 10, 0x1a1, 31),
    (631797, "Toxicology", "Defeat Koga while only using Pokémon that are level 43 or less", 10, 0x1a2, 43),
    (631798, "Psychiatry", "Defeat Sabrina while only using Pokémon that are level 45 or less", 10, 0x1a4, 45),
    (631799, "Burn Treatment", "Defeat Blaine while only using Pokémon that are level 50 or less", 10, 0x1a3, 50),
    (631800, "Discharged!", "Survive against Head Nurse Joy while only using Pokémon that are level 50 or less", 25, 0x15e, 50),
]

for a_id, title, desc, pts, t_id, max_lvl in cap_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, type=AchievementType.MISSABLE)
    logic = [
        (mem_trainer_id == t_id),
        trigger(mem_battle_out == 1),
        (mem_battle_out.delta() == 0),
    ]
    # Adiciona a trava de level para todos os 6 slots
    for lvl_addr in lvl_addresses:
        logic.append((lvl_addr <= max_lvl))
        
    logic.extend([add_address(ptr_save1), (mem_last_heal == 3)])
    ach.add_core(logic)
    my_set.add_achievement(ach)

# 4. EXTENSIVE RESEARCH (HMs PERMUTATIONS)
ach = Achievement(id=631817, title="Extensive Research", description="Defeat a Gym Leader while using only one Pokémon that knows at least 3 HM moves", points=10)

ach.add_core([
    (mem_battle_flag == 1),
    (mem_game_state == 0x2000010),
    trigger(mem_battle_out == 1),
    (mem_battle_out.delta() == 0),
    or_next(mem_trainer_id == 0x19e), or_next(mem_trainer_id == 0x19f), or_next(mem_trainer_id == 0x1a0),
    or_next(mem_trainer_id == 0x1a1), or_next(mem_trainer_id == 0x1a2), or_next(mem_trainer_id == 0x1a3),
    or_next(mem_trainer_id == 0x1a4), (mem_trainer_id == 0x15e),
])

def hm_slot(addr, is_last=False):
    hms = [15, 19, 57, 70, 127, 148]
    conds = [or_next(addr == hm) for hm in hms]
    conds.append(addr == 249 if is_last else and_next(addr == 249))
    return conds

moves = [word(0x02bbf0), word(0x02bbf2), word(0x02bbf4), word(0x02bbf6)]
for combo in combinations(moves, 3):
    ach.add_alt(hm_slot(combo[0]) + hm_slot(combo[1]) + hm_slot(combo[2], is_last=True))

my_set.add_achievement(ach)

# 5. MEDICAL HISTORY (SOMA DE BITS OTIMIZADA)
ach = Achievement(id=631806, title="Medical History", description="Gather all of Head Nurse Joy's medical records in the Fame Checker", points=5)

ach.add_core([
    add_address(ptr_save1), add_source(bit2(0x00ba90)),
    add_address(ptr_save1), add_source(bit3(0x00ba90)),
    add_address(ptr_save1), add_source(bit4(0x00ba90)),
    add_address(ptr_save1), add_source(bit5(0x00ba90)),
    add_address(ptr_save1), add_source(bit7(0x00ba90)),
    add_address(ptr_save1), measured(value(0) == 5),
    
    add_address(ptr_save1), measured_if(mem_map_id != 0),

    # Delta
    add_address(ptr_save1), add_source(bit2(0x00ba90).delta()),
    add_address(ptr_save1), add_source(bit3(0x00ba90).delta()),
    add_address(ptr_save1), add_source(bit4(0x00ba90).delta()),
    add_address(ptr_save1), add_source(bit5(0x00ba90).delta()),
    add_address(ptr_save1), add_source(bit7(0x00ba90).delta()),
    add_address(ptr_save1), (value(0).delta() == 4),
])
my_set.add_achievement(ach)

my_set.save()