from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=20093, title="Poker Face Paul's Blackjack")

# 1. ALIASES DE MEMÓRIA
mem_state    = byte(0x0036)
mem_menu     = byte(0x008d)
mem_action   = byte(0x0142)
mem_loc      = byte(0x1b6c)
mem_bankroll = dword(0x1b68)
mem_result   = byte(0x1b9b)
mem_turn     = byte(0x1db3)

# 2. PROGRESSÃO DE BANKROLL POR LOCAL
loc_data = [
    (608989, "Neon Lights", "Las Vegas Strip", 0x00, "690804"),
    (608990, "The Crown's Fortune", "London", 0x01, "690805"),
    (608991, "Boardwalk Empire", "Atlantic City", 0x02, "690806"),
    (608992, "Downtown Hustler", "Downtown Las Vegas", 0x03, "690807"),
]

for a_id, title, loc_name, loc_val, badge in loc_data:
    ach = Achievement(id=a_id, title=title, description=f"Reach a bankroll of 500 playing under {loc_name} rules", points=5, badge=badge)
    ach.add_core([
        (mem_loc == loc_val),
        (mem_bankroll.delta() < 0x500),
        (mem_bankroll >= 0x500),
    ])
    my_set.add_achievement(ach)

# 3. BANKROLL TOTAL (CARREIRA)
bankroll_data = [
    (608993, "Making a Living", "1,000", 0x1000, 25, "690808"),
    (608994, "Breaking the Bank", "5,000", 0x5000, 50, "690809"),
]

for a_id, title, desc_val, target, pts, badge in bankroll_data:
    ach = Achievement(id=a_id, title=title, description=f"Reach a total bankroll of {desc_val}", points=pts, badge=badge)
    ach.add_core([
        (mem_state == 0x01),
        (mem_bankroll.delta() < target),
        (mem_bankroll >= target),
    ])
    my_set.add_achievement(ach)

# 4. AÇÕES ESPECÍFICAS & VITÓRIAS
# Natural Born Winner
ach = Achievement(id=608995, title="Natural Born Winner", description="Win a hand instantly with a Blackjack", points=10, badge="690810")
ach.add_core([
    reset_if(mem_menu == 0x08),
    (mem_state == 0x01),
    (mem_result.delta() == 0x05).with_hits(14),
    (mem_result == 0x02),
])
my_set.add_achievement(ach)

# Ações de Mesa (Split, Double Down, Insurance)
action_data = [
    (608996, "Divide and Conquer", "Choose to Split a pair and win your hands", 5, 0x05, "690811"),
    (608997, "Double or Nothing", "Choose to Double Down and win the hand", 10, 0x04, "690812"),
    (608998, "Safe Bet", "Successfully win an Insurance bet against the Dealer", 5, 0x0a, "690813"),
]

for a_id, title, desc, pts, act_val, badge in action_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        or_next((mem_turn == 0x01).with_hits(1)),
        reset_if(mem_menu == 0x08),
        or_next((mem_turn == 0x00).with_hits(1)),
        (mem_turn == 0xff).with_hits(1),
        and_next((mem_action == act_val).with_hits(1)),
        (mem_action == 0x03).with_hits(1),
        or_next(mem_result.delta() == 0x00),
        (mem_result.delta() == 0x05).with_hits(14),
        trigger(mem_result == 0x01),
    ])
    my_set.add_achievement(ach)

# 5. DESAFIOS (STREAK)
ach = Achievement(id=608999, title="Unbreakable Streak", description="Win 5 consecutive hands without tying or losing", points=10, badge="690814")
ach.add_core([
    or_next(mem_result == 0x03),
    or_next(mem_result == 0x04),
    reset_if(mem_bankroll == 0x00),
    or_next(mem_turn == 0x00),
    measured_if(mem_turn == 0xff),
    and_next(mem_result.delta() != 0x02),
    add_hits(mem_result == 0x02),
    and_next(mem_result.delta() != 0x01),
    add_hits(mem_result == 0x01),
    measured((value(0) == 1).with_hits(5)),
])
my_set.add_achievement(ach)

my_set.save()