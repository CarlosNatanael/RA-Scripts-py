from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=309, title="Super Street Fighter II")

# 1. ALIASES DE MEMÓRIA
mem_diff       = byte(0x001d23)
mem_char       = byte(0x00081a)
mem_stage      = byte(0x0018bc)
mem_bonus_id   = byte(0x0018e8)
mem_continues  = byte(0x0018d2)

# 2. ZERANDO COM OS PERSONAGENS (Diff 4+ e Diff 8)
# (Char_ID, Name, Title_Diff4, ID_Diff4, Badge_Diff4, Title_Diff8, ID_Diff8, Badge_Diff8)
char_data = [
    (0x00, "Ryu", "The Fight Is Everything", 24463, "721563", "Master of the Hadouken", 34534, "721564"),
    (0x01, "E. Honda", "Ultimate Yokozuna", 24464, "721565", "Master of the Flying Sumo Press", 34535, "721566"),
    (0x02, "Blanka", "Green Mother Lover", 24465, "721567", "Master of the Electric Thunder", 34536, "721568"),
    (0x03, "Guile", "It's All About Family", 24466, "721572", "Master of the Flash Kick", 34537, "721573"),
    (0x04, "Ken", "Just Married!", 24467, "721574", "Master of the Shoryuken", 34538, "721575"),
    (0x05, "Chun-Li", "The Strongest Woman in the World", 24468, "721576", "Master of the Kikouken", 34539, "721577"),
    (0x06, "Zangief", "Comrades in Dance", 24469, "721579", "Master of the Double Lariat", 34540, "721580"),
    (0x07, "Dhalsim", "Good Karma", 24470, "721582", "Master of the Yoga Teleport", 34541, "721584"),
    (0x08, "Dictator", "Birth of the New Overlord", 24478, "721604", "Master of the Psycho Crusher", 34549, "721605"),
    (0x09, "Sagat", "A Score to Eternally Settle", 24477, "721602", "Master of the Tiger Uppercut", 34548, "721603"),
    (0x0a, "Boxer", "Cash Rolls Everything Around Me", 24475, "721598", "Master of the Buffalo Headbutt", 34546, "721599"),
    (0x0b, "Claw", "Handsome Fighters Never Lose Battles", 24476, "721600", "Master of the Rainbow Suplex", 34547, "721601"),
    (0x0c, "Cammy", "Dark Secrets of Shadaloo", 24474, "721596", "Master of the Cannon Drill", 34545, "721597"),
    (0x0d, "T. Hawk", "Both Feet on Sacred Soil", 24471, "721585", "Master of the Condor Dive", 34543, "721586"),
    (0x0e, "Fei-Long", "The Dragon Lives Again", 24472, "721587", "Master of the Shienkyaku", 34542, "721591"),
    (0x0f, "Dee Jay", "Now That's What I Call Music!", 24473, "721593", "Master of the Knee Shot", 34544, "721594"),
]

for c_id, c_name, title4, id4, badge4, title8, id8, badge8 in char_data:
    # Difficulty 4 (Level 4 or higher)
    ach4 = Achievement(id=id4, title=title4, description=f"Beat the game as {c_name} on difficulty level 4 or higher", points=10, badge=badge4, type=AchievementType.WIN_CONDITION)
    ach4.add_core([
        (mem_char == c_id),
        (mem_diff >= 0x03),
        trigger(mem_stage == 0x0c),
        (mem_stage.delta() == 0x0b)
    ])
    my_set.add_achievement(ach4)

    # Difficulty 8 
    ach8 = Achievement(id=id8, title=title8, description=f"Beat the game as {c_name} on difficulty level 8", points=10, badge=badge8)
    ach8.add_core([
        (mem_char == c_id),
        (mem_diff >= 0x07),
        trigger(mem_stage == 0x0c),
        trigger(mem_stage.delta() == 0x0b) 
    ])
    my_set.add_achievement(ach8)

# 3. BONUS STAGES (Perfects)
bonus_data = [
    (24573, "Straight to the Junkyard", "Get a Perfect on the first bonus stage", 3, "721560", 0x03, 0x00, byte(0x00185c), 0x0e, 0x0d),
    (24574, "Like a Ton of Bricks", "Get a Perfect on the second bonus stage", 2, "721561", 0x06, 0x01, byte(0x001957), 0x0a, 0x09),
    (24575, "No More Barrel Rolls", "Get a Perfect on the third bonus stage", 5, "721562", 0x09, 0x02, tbyte(0x00068d), 0x200, 0x200, True), # Flag extra pro tbyte
]

for b_id, b_title, b_desc, b_pts, b_badge, b_stage, b_type, mem_check, val_curr, val_prev, *opt in bonus_data:
    is_less_than = bool(opt and opt[0]) # Verifica a flag pro tbyte
    ach = Achievement(id=b_id, title=b_title, description=b_desc, points=b_pts, badge=b_badge)
    logic = [
        (mem_stage == b_stage),
        (mem_bonus_id == b_type),
        (mem_check >= val_curr) if is_less_than else (mem_check == val_curr),
        (mem_check.delta() < val_prev) if is_less_than else (mem_check.delta() == val_prev),
    ]
    ach.add_core(logic)
    my_set.add_achievement(ach)

# 4. DESAFIOS GERAIS DE ENDGAME
ach = Achievement(id=44026, title="New Challengers, New Champion", description="Beat the game on difficulty level 8 without using any continues", points=50, badge="721606")
ach.add_core([
    (mem_diff >= 0x07),
    (mem_continues == 0x00),
    trigger(mem_stage == 0x0c),
    trigger(mem_stage.delta() == 0x0b)
])
my_set.add_achievement(ach)

ach = Achievement(id=44027, title="Super Street Fighter", description="Beat the game without using continues (Highest Difficulty)", points=35, badge="35642")
ach.add_core([
    (byte(0x0018bb) == 0x08),
    (byte(0x0018ca) == 0x01),
    (byte(0x0018cb) == 0x01),
    (byte(0x0018ed) == 0x13),
    (mem_diff == 0x07)
])
ach.add_alt([
    (byte(0x000702) == 0x00),
    (byte(0x0005da) == byte(0x000811)),
    (byte(0x000811) == 0x08)
])
ach.add_alt([
    (byte(0x000942) == 0x00),
    (byte(0x00081a) == byte(0x0005d1)),
    (byte(0x0005d1) == 0x08)
])
my_set.add_achievement(ach)

my_set.save()