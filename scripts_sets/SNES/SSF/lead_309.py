from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=309, title="Imported Leaderboards")

# 1. ALIASES DE MEMÓRIA (LEADERBOARDS)
mem_diff       = byte(0x001d23)
mem_char       = byte(0x00081a)
mem_continues  = byte(0x0018d2)
mem_game_mode  = byte(0x000039)
mem_p2_active  = byte(0x00080e)
mem_match_st   = byte(0x000810)
mem_stage      = byte(0x0018bc)

# 2. ESTRUTURA GERAL DOS LEADERBOARDS
# (Char_ID, Name, LB_ID)
char_data = [
    (0x00, "Ryu",      28047),
    (0x01, "E.Honda",  28049),
    (0x02, "Blanka",   28051),
    (0x03, "Guile",    28052),
    (0x04, "Ken",      28048),
    (0x05, "Chun-Li",  28050),
    (0x06, "Zangief",  28053),
    (0x07, "Dhalsim",  28054),
    (0x08, "M.Bison",  28062),
    (0x09, "Sagat",    28061),
    (0x0a, "Balrog",   28059),
    (0x0b, "Vega",     28060),
    (0x0c, "Cammy",    28058),
    (0x0d, "T.Hawk",   28055),
    (0x0e, "Feilong",  28056),
    (0x0f, "Dee Jay",  28057),
]

for c_id, c_name, lb_id in char_data:
    lb = Leaderboard(
        title=c_name,
        description=f"Make as many points as you can with {c_name} without use continue ( 8 Stars )",
        id=lb_id,
        format=LeaderboardFormat.VALUE,
        lower_is_better=False
    )
    
    # Condições de Início
    start_core = [
        (mem_diff == 0x07),
        (mem_char == c_id),
        (mem_game_mode == 0x00),
        (mem_continues == 0x00),
        (mem_p2_active == 0x00),
    ]
    start_alt1 = [(mem_match_st == 0x02), (mem_match_st.delta() == 0x01)]
    start_alt2 = [(mem_stage == 0x0c), (mem_stage.delta() == 0x0b)]
    lb.set_start(start_core, start_alt1, start_alt2)
    
    # Condições de Cancelamento e Submissão
    lb.set_cancel([(value(1) == value(0))])
    lb.set_submit([(value(1) == value(1))])
    
    # Cálculo do Valor (Score)
    val_logic = [
        add_source(byte(0x000702).bcd()),
        add_source(byte(0x000703).bcd()),
        add_source(byte(0x000704).bcd()),
        measured(byte(0x000705).bcd()),
    ]
    lb.set_value(val_logic)
    
    my_set.add_leaderboard(lb)

my_set.save()