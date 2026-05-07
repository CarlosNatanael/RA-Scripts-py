from pycheevos.core.helpers import byte, word, dword, tbyte, bit0, value, measured
from pycheevos.core.constants import LeaderboardFormat
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=36353, title="Boxing Leaderboards")

# ALIAS DE MEMÓRIA GLOBAIS
mem_screen  = byte(0x1feff0)
mem_menu    = byte(0x1fef74)
mem_char    = byte(0x1fef66)
mem_diff    = word(0x1fe564)
mem_p1_ctrl = byte(0x1fef84)
mem_p2_ctrl = byte(0x1fef88)
mem_champ   = byte(0x1fef70)
mem_rank    = byte(0x1fef68)
mem_win     = bit0(0x1fef6a)

# Construção dos Ponteiros
ptr_base    = tbyte(0x1fe480)
match_state = ptr_base >> byte(0x000018)
match_end   = ptr_base >> byte(0x0000c8)

# 1. LEADERBOARDS: FASTEST T.K.O.
tko_data = [
    (158011, "Very Hard", 100),
    (158012, "Hard",       75),
    (158013, "Normal",     50),
    (158014, "Easy",       25),
]

for lb_id, diff_name, diff_val in tko_data:
    lb = Leaderboard(
        id=lb_id,
        title=f"Fastest T.K.O. [{diff_name}]",
        description=f"T.K.O. the CPU opponent as fast as possible on {diff_name} difficulty",
        format=LeaderboardFormat.FRAMES,
        lower_is_better=True
    )
    lb.set_start([
        mem_p2_ctrl == 0,
        mem_diff == diff_val,
        mem_menu == 2,
        match_state.delta() != 4,
        match_state == 4
    ])
    lb.set_cancel([
        (mem_screen == 10) | (mem_screen == 9)
    ])
    lb.set_submit([
        match_end.delta() == 0,
        match_end == 1
    ])
    lb.set_value([
        measured(value(1) == 1)
    ])
    my_set.add_leaderboard(lb)


# 2. LEADERBOARDS: HALL OF FAME
CHAR_NAMES = [
    "Tanaka", "Ryoko", "Red", "B.T.", "Puma", "Prince",
    "Misha", "Silver Man", "Gio", "Kojiromaru", "Spice", "Asteka", "Mr. Crown"
]

BASE_SCORE = 0x1fe73c  
BASE_START = 0x1fe734
OFFSET_CHAR = 0x50     

base_lb_id = 158780

for char_id, name in enumerate(CHAR_NAMES):
    char_score = dword(BASE_SCORE + (char_id * OFFSET_CHAR))
    char_start_check = word(BASE_START + (char_id * OFFSET_CHAR))
    
    lb = Leaderboard(
        id=base_lb_id + char_id,
        title=f"Hall of Fame: {name}",
        description="Start a new Ranking career from the Local class and submit your highest score. Submits upon winning the World Heavyweight Championship or getting a Game Over",
        format=LeaderboardFormat.SCORE,
        lower_is_better=False
    )
    
    lb.set_start([
        mem_char == char_id,
        char_start_check == 0,
        mem_menu == 0,
        mem_champ <= 2,
        mem_p1_ctrl.delta() == 0,
        mem_p1_ctrl == 1
    ])
    
    lb.set_cancel(
        [value(1) == 1],
        [mem_menu.delta() == 0, mem_menu != 0],
        [mem_char.delta() == char_id, mem_char != char_id]
    )
    
    lb.set_submit(
        [mem_menu == 0], 
        [mem_champ == 6, mem_rank == 1, mem_win.delta() == 0, mem_win == 1],  
        [match_state.delta() != 16, match_state == 16] 
    )
    
    lb.set_value([
        measured(char_score)
    ])
    
    my_set.add_leaderboard(lb)
my_set.save()