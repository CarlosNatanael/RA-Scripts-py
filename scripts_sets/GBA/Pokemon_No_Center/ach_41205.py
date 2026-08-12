from pycheevos.core.helpers import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=41205, title="Pokémon FireRed - Gym Leaders")

mem_trainer_id  = word(0x0406ae)
mem_game_state  = dword(0x02bfe8)
ptr_save_block1 = tbyte(0x005008)
ptr_pkmn_stor   = tbyte(0x005010)

alt_heal_reset = [
    add_address(ptr_save_block1),
    or_next(word(0x801c) == 0),
    add_address(ptr_save_block1),
    reset_if(word(0x801c) == 253)
]

gym_leaders = [
    (0x019e, bit0, "Brock", "Boulder Badge"),
    (0x019f, bit1, "Misty", "Cascade Badge"),
    (0x01a0, bit2, "Lt. Surge", "Thunder Badge"),
    (0x01a1, bit3, "Erika", "Rainbow Badge"),
    (0x01a2, bit4, "Koga", "Soul Badge"),
    (0x01a4, bit5, "Sabrina", "Marsh Badge"),
    (0x01a3, bit6, "Blaine", "Volcano Badge"),
    (0x015e, bit7, "Giovanni", "Earth Badge"),
]

for trainer_id, badge_bit_func, leader_name, badge_name in gym_leaders:
    ach = Achievement(
        id=1,
        title=f"Defeated {leader_name}",
        description=f"Defeat Gym Leader {leader_name} and earn the {badge_name}.",
        points=5
    )

    core_logic = [
        (mem_trainer_id == trainer_id),
        add_address(ptr_pkmn_stor),
        (badge_bit_func(0x51fc) == 1),
        add_address(ptr_pkmn_stor),
        (badge_bit_func(0x51fc).delta() == 0),
        and_next(mem_game_state == 0x02000010),
        add_address(ptr_save_block1),
        pause_if(word(0x801c) != 3).with_hits(1)
    ]

    ach.add_core(core_logic)
    ach.add_alt(alt_heal_reset)
    my_set.add_achievement(ach)

my_set.save()