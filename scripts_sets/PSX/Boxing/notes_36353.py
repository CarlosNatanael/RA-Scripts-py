# Code Notes for Game ID 36353
# Source: RA Server

from pycheevos.core.helpers import *

# 0x08ee1e: [8-bit] [JP] Input Controller P1
input_controller_p1 = byte(0x08ee1e)
#Bit0 = Select
#Bit3 = Start
#Bit4 = Up
#Bit5 = Right
#Bit6 = Down
#Bit7 = Left

# 0x08ee1f: [8-bit] [JP] Input Controller P1
input_controller_p1_2 = byte(0x08ee1f)
#Bit0 = L2
#Bit1 = R2
#Bit2 = L1
#Bit3 = R1
#Bit4 = Triangle
#Bit5 = Circle
#Bit6 = Cross/X
#Bit7 = Square

# 0x08ee40: [8-bit] [JP] Input Controller P2
input_controller_p2 = byte(0x08ee40)
#Bit0 = Select
#Bit3 = Start
#Bit4 = Up
#Bit5 = Right
#Bit6 = Down
#Bit7 = Left

# 0x08ee41: [8-bit] [JP] Input Controller P2
input_controller_p2_2 = byte(0x08ee41)
#Bit0 = L2
#Bit1 = R2
#Bit2 = L1
#Bit3 = R1
#Bit4 = Triangle
#Bit5 = Circle
#Bit6 = Cross/X
#Bit7 = Square

# 0x0902fe: [8-bit] [EU] Input Controller P1
input_controller_p1_3 = byte(0x0902fe)
#Bit0 = Select
#Bit3 = Start
#Bit4 = Up
#Bit5 = Right
#Bit6 = Down
#Bit7 = Left

# 0x0902ff: [8-bit] [EU] Input Controller P1
input_controller_p1_4 = byte(0x0902ff)
#Bit0 = L2
#Bit1 = R2
#Bit2 = L1
#Bit3 = R1
#Bit4 = Triangle
#Bit5 = Circle
#Bit6 = Cross/X
#Bit7 = Square

# 0x090320: [8-bit] [EU] Input Controller P2
input_controller_p2_3 = byte(0x090320)
#Bit0 = Select
#Bit3 = Start
#Bit4 = Up
#Bit5 = Right
#Bit6 = Down
#Bit7 = Left

# 0x090321: [8-bit] [EU] Input Controller P2
input_controller_p2_4 = byte(0x090321)
#Bit0 = L2
#Bit1 = R2
#Bit2 = L1
#Bit3 = R1
#Bit4 = Triangle
#Bit5 = Circle
#Bit6 = Cross/X
#Bit7 = Square

# 0x090876: [8-bit] [USA] Input Controller P1
input_controller_p1_5 = byte(0x090876)
#Bit0 = Select
#Bit3 = Start
#Bit4 = Up
#Bit5 = Right
#Bit6 = Down
#Bit7 = Left

# 0x090877: [8-bit] [USA] Input Controller P1
input_controller_p1_6 = byte(0x090877)
#Bit0 = L2
#Bit1 = R2
#Bit2 = L1
#Bit3 = R1
#Bit4 = Triangle
#Bit5 = Circle
#Bit6 = Cross/X
#Bit7 = Square

# 0x090898: [8-bit] [USA] Input Controller P2
input_controller_p2_5 = byte(0x090898)
#Bit0 = Select
#Bit3 = Start
#Bit4 = Up
#Bit5 = Right
#Bit6 = Down
#Bit7 = Left

# 0x090899: [8-bit] [USA] Input Controller P2
input_controller_p2_6 = byte(0x090899)
#Bit0 = L2
#Bit1 = R2
#Bit2 = L1
#Bit3 = R1
#Bit4 = Triangle
#Bit5 = Circle
#Bit6 = Cross/X
#Bit7 = Square

# 0x098780: [8-bit] [JP] Total timer
total_timer = byte(0x098780)
#- Centiseconds

# 0x098781: [8-bit] [JP] Total timer
total_timer_2 = byte(0x098781)
#- Seconds

# 0x098782: [8-bit] [JP] Total timer
total_timer_3 = byte(0x098782)
#- Minutes

# 0x098783: [8-bit] [JP] Total timer
total_timer_4 = byte(0x098783)
#- Hours

# 0x09dfe0: [8-bit] [EU] Total timer
total_timer_5 = byte(0x09dfe0)
#- Centiseconds

# 0x09dfe1: [8-bit] [EU] Total timer
total_timer_6 = byte(0x09dfe1)
#- Seconds

# 0x09dfe2: [8-bit] [EU] Total timer
total_timer_7 = byte(0x09dfe2)
#- Minutes

# 0x09dfe3: [8-bit] [EU] Total timer
total_timer_8 = byte(0x09dfe3)
#- Hours

# 0x09e538: [8-bit] [USA] Total timer
total_timer_9 = byte(0x09e538)
#- Centiseconds

# 0x09e539: [8-bit] [USA] Total timer
total_timer_10 = byte(0x09e539)
#- Seconds

# 0x09e53a: [8-bit] [USA] Total timer
total_timer_11 = byte(0x09e53a)
#- Minutes

# 0x09e53b: [8-bit] [USA] Total timer
total_timer_12 = byte(0x09e53b)
#- Hours

# 0x0a7781: [8-bit] ROM Region Anchor [JP]
rom_region_anchor = byte(0x0a7781)

# 0x0ad01b: [8-bit] ROM Region Anchor [EU]
rom_region_anchor_2 = byte(0x0ad01b)

# 0x0ad539: [8-bit] ROM Region Anchor [USA]
rom_region_anchor_3 = byte(0x0ad539)

# 0x1db67a: [8-bit] [USA] New Game Bit-Flag
new_game_bit_flag = byte(0x1db67a)

# 0x1db990: [8-bit] [USA] Character Select ID
character_select_id = byte(0x1db990)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1db9c0: [8-bit] [JP] Character Select ID
character_select_id_2 = byte(0x1db9c0)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1dc062: [8-bit] [USA] Character Select ID
character_select_id_3 = byte(0x1dc062)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1dc06c: [8-bit] [JP] Character Select ID
character_select_id_4 = byte(0x1dc06c)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1fe480: [32-bit] [ALL] Master Base Pointer: Active Match Struct
master_base_pointer__active_match_struct = dword(0x1fe480)
#Points to the dynamically allocated root of the current fight.
#Known Offsets:
match_state = master_base_pointer__active_match_struct >> byte(0x18)
#+0x18 | Match State [8-bit]
#0x01 = Intro
#0x04 = Fight
#0x06 = Decision
#0x08 = Knockdown
#0x0a = K.O.
#0x0f = Win
#0x0e = Replay
#0x10 = Lose
#0x11 = Draw
#0x13 = Champion

round_timer = master_base_pointer__active_match_struct >> word(0x28)
#+0x28 | Round Timer [16-bit]
#0x0704 = 30 sec, counts down to 0x0000

current_round = master_base_pointer__active_match_struct >> dword(0x2c)
#+0x2c | Current Round [32-bit]

total_rounds_configured = master_base_pointer__active_match_struct >> byte(0x30)
#+0x30 | Total Rounds Configured [8-bit]

p1_score_array = master_base_pointer__active_match_struct >> dword(0x34)
#+0x34 | P1 Score Array [32-bit]
#Next round is +0x08

p2_score_array = master_base_pointer__active_match_struct >> dword(0x38)
#+0x38 | P2 Score Array [32-bit]
#Next round is +0x08

pause_game = master_base_pointer__active_match_struct >> dword(0xd4)
#+0xd4 | Pause Game [Bit0]
#0 = Fighting
#1 = Paused

p1_knockdown_counter = master_base_pointer__active_match_struct >> byte(0xac)
#+0xac | P1 Knockdown Counter [8-bit]
#(Times P1 fell to the mat)

p2_knockdown_counter = master_base_pointer__active_match_struct >> byte(0xb0)
#+0xb0 | P2 Knockdown Counter [8-bit]
#(Times P2 fell to the mat)

p1_ground_state = master_base_pointer__active_match_struct >> byte(0xbC)
#+0xbC | P1 Ground State [8-bit]
#0x00 = Standing
#0x01 = On the Ground

p2_ground_state = master_base_pointer__active_match_struct >> byte(0xc0)
#+0xc0 | P2 Ground State [8-bit]
#0x00 = Standing
#0x01 = On the Ground

p1_match_winner_flag = master_base_pointer__active_match_struct >> dword(0xc8)
#+0xc8 | P1 Match Winner Flag [Bit0]
#1 = P1 Won the Match

p2_match_winner_flag = master_base_pointer__active_match_struct >> dword(0xd8)
#+0xd8 | P2 Match Winner Flag [Bit0]
#1 = P2 Won the Match

referee_count_display = master_base_pointer__active_match_struct >> dword(0xf4)
#+0xf4 | Referee Count Display [Bit0]
#1 = Knockdown 1-10 counter is on screen


# 0x1fe564: [16-bit] [ALL] Difficulty Game Mode VS
difficulty_game_mode_vs = word(0x1fe564)
#0x0064 = Very Hard
#0x004b = Hard
#0x0032 = Normal
#0x0019 = Easy

# 0x1fe6d0: [8-bit] [ALL] Tanaka - Scout Status
tanaka___scout_status = byte(0x1fe6d0)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d1: [8-bit] [ALL] Ryoko - Scout Status
ryoko___scout_status = byte(0x1fe6d1)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d2: [8-bit] [ALL] Red - Scout Status
red___scout_status = byte(0x1fe6d2)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d3: [8-bit] [ALL] B.T. - Scout Status
bt___scout_status = byte(0x1fe6d3)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d4: [8-bit] [ALL] Puma - Scout Status
puma___scout_status = byte(0x1fe6d4)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d5: [8-bit] [ALL] Prince - Scout Status
prince___scout_status = byte(0x1fe6d5)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d6: [8-bit] [ALL] Misha - Scout Status
misha___scout_status = byte(0x1fe6d6)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d7: [8-bit] [ALL] Silver Man - Scout Status
silver_man___scout_status = byte(0x1fe6d7)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d8: [8-bit] [ALL] Gio - Scout Status
gio___scout_status = byte(0x1fe6d8)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6d9: [8-bit] [ALL] Kojiromaru - Scout Status
kojiromaru___scout_status = byte(0x1fe6d9)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6da: [8-bit] [ALL] Spice - Scout Status
spice___scout_status = byte(0x1fe6da)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6db: [8-bit] [ALL] Asteka - Scout Status
asteka___scout_status = byte(0x1fe6db)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6dc: [8-bit] [ALL] Mr.Crown - Scout Status
mrcrown___scout_status = byte(0x1fe6dc)
#0x00 = Locked
#0x01 = Unlocked
#0x02 = Rematch (Extra Notes Unlocked)

# 0x1fe6dd: [8-bit] [ALL] Tanaka - Bio/Sign 1
tanaka___bio_sign_1 = byte(0x1fe6dd)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6de: [8-bit] [ALL] Tanaka - Bio/Sign 2
tanaka___bio_sign_2 = byte(0x1fe6de)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6df: [8-bit] [ALL] Tanaka - Bio/Sign 3
tanaka___bio_sign_3 = byte(0x1fe6df)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6e3: [8-bit] [ALL] Ryoko - Bio/Sign 1
ryoko___bio_sign_1 = byte(0x1fe6e3)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6e4: [8-bit] [ALL] Ryoko - Bio/Sign 2
ryoko___bio_sign_2 = byte(0x1fe6e4)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6e5: [8-bit] [ALL] Ryoko - Bio/Sign 3
ryoko___bio_sign_3 = byte(0x1fe6e5)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6e9: [8-bit] [ALL] Red - Bio/Sign 1
red___bio_sign_1 = byte(0x1fe6e9)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6ea: [8-bit] [ALL] Red - Bio/Sign 2
red___bio_sign_2 = byte(0x1fe6ea)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6ef: [8-bit] [ALL] B.T. - Bio/Sign 1
bt___bio_sign_1 = byte(0x1fe6ef)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6f0: [8-bit] [ALL] B.T. - Bio/Sign 2
bt___bio_sign_2 = byte(0x1fe6f0)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6f1: [8-bit] [ALL] B.T. - Bio/Sign 3
bt___bio_sign_3 = byte(0x1fe6f1)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6f2: [8-bit] [ALL] B.T. - Bio/Sign 4
bt___bio_sign_4 = byte(0x1fe6f2)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6f5: [8-bit] [ALL] Puma - Bio/Sign 1
puma___bio_sign_1 = byte(0x1fe6f5)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6fb: [8-bit] [ALL] Prince - Bio/Sign 1
prince___bio_sign_1 = byte(0x1fe6fb)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6fc: [8-bit] [ALL] Prince - Bio/Sign 2
prince___bio_sign_2 = byte(0x1fe6fc)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe6fd: [8-bit] [ALL] Prince - Bio/Sign 3
prince___bio_sign_3 = byte(0x1fe6fd)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe701: [8-bit] [ALL] Misha - Bio/Sign 1
misha___bio_sign_1 = byte(0x1fe701)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe702: [8-bit] [ALL] Misha - Bio/Sign 2
misha___bio_sign_2 = byte(0x1fe702)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe707: [8-bit] [ALL] Silver Man - Bio/Sign 1
silver_man___bio_sign_1 = byte(0x1fe707)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe70d: [8-bit] [ALL] Gio - Bio/Sign 1
gio___bio_sign_1 = byte(0x1fe70d)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe70e: [8-bit] [ALL] Gio - Bio/Sign 2
gio___bio_sign_2 = byte(0x1fe70e)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe70f: [8-bit] [ALL] Gio - Bio/Sign 3
gio___bio_sign_3 = byte(0x1fe70f)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe713: [8-bit] [ALL] Kojiromaru - Bio/Sign 1
kojiromaru___bio_sign_1 = byte(0x1fe713)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe714: [8-bit] [ALL] Kojiromaru - Bio/Sign 2
kojiromaru___bio_sign_2 = byte(0x1fe714)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe719: [8-bit] [ALL] Spice - Bio/Sign 1
spice___bio_sign_1 = byte(0x1fe719)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe71a: [8-bit] [ALL] Spice - Bio/Sign 2
spice___bio_sign_2 = byte(0x1fe71a)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe71b: [8-bit] [ALL] Spice - Bio/Sign 3
spice___bio_sign_3 = byte(0x1fe71b)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe71f: [8-bit] [ALL] Asteka - Bio/Sign 1
asteka___bio_sign_1 = byte(0x1fe71f)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe725: [8-bit] [ALL] Mr.Crown - Bio/Sign 1
mrcrown___bio_sign_1 = byte(0x1fe725)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe726: [8-bit] [ALL] Mr.Crown - Bio/Sign 2
mrcrown___bio_sign_2 = byte(0x1fe726)
#0x00 = Locked
#0x01 = Unlocked

# 0x1fe72c: [8-bit] [ALL] Tanaka - Selected for Championship Flag
tanaka___selected_for_championship_flag = byte(0x1fe72c)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe72d: [8-bit] [ALL] Tanaka - Active Championship Flag
tanaka___active_championship_flag = byte(0x1fe72d)
#0x00 = No
#0x01 = Yes

# 0x1fe72e: [8-bit] [ALL] Tanaka - Current Weight Class Participation
tanaka___current_weight_class_participation = byte(0x1fe72e)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe72f: [8-bit] [ALL] Tanaka - Current Tournament Participation
tanaka___current_tournament_participation = byte(0x1fe72f)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe730: [8-bit] [ALL] Tanaka - Championship Unlock Level
tanaka___championship_unlock_level = byte(0x1fe730)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe731: [8-bit] [ALL] Tanaka - Tournament Bracket Position / Opponent Rank
tanaka___tournament_bracket_position___opponent_rank = byte(0x1fe731)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe733: [8-bit] [ALL] Tanaka - Fighter Rank Category
tanaka___fighter_rank_category = byte(0x1fe733)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe734: [16-bit] [ALL] Tanaka - Total Matches (Session)
tanaka___total_matches = word(0x1fe734)
#Note: Resets if championship is abandoned or lost.

# 0x1fe736: [16-bit] [ALL] Tanaka - Total Wins (Session)
tanaka___total_wins = word(0x1fe736)
#Note: Resets if championship is abandoned or lost.

# 0x1fe738: [16-bit] [ALL] Tanaka - Total Losses (Session)
tanaka___total_losses = word(0x1fe738)
#Note: Resets if championship is abandoned or lost.

# 0x1fe73a: [16-bit] [ALL] Tanaka - Total K.Os (Session)
tanaka___total_k = word(0x1fe73a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe73c: [32-bit] [ALL] Tanaka - Character Points (Session)
tanaka___character_points = dword(0x1fe73c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe740: [16-bit] [ALL] Tanaka - Light Local Belt Counter (Session)
tanaka___light_local_belt_counter = word(0x1fe740)
#Note: Resets if championship is abandoned or lost.

# 0x1fe742: [16-bit] [ALL] Tanaka - Light National Belt Counter (Session)
tanaka___light_national_belt_counter = word(0x1fe742)
#Note: Resets if championship is abandoned or lost.

# 0x1fe744: [16-bit] [ALL] Tanaka - Light World Belt Counter (Session)
tanaka___light_world_belt_counter = word(0x1fe744)
#Note: Resets if championship is abandoned or lost.

# 0x1fe746: [16-bit] [ALL] Tanaka - Light Secret Belt Counter (Session)
tanaka___light_secret_belt_counter = word(0x1fe746)
#Note: Resets if championship is abandoned or lost.

# 0x1fe748: [16-bit] [ALL] Tanaka - Middle Local Belt Counter (Session)
tanaka___middle_local_belt_counter = word(0x1fe748)
#Note: Resets if championship is abandoned or lost.

# 0x1fe74a: [16-bit] [ALL] Tanaka - Middle National Belt Counter (Session)
tanaka___middle_national_belt_counter = word(0x1fe74a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe74c: [16-bit] [ALL] Tanaka - Middle World Belt Counter (Session)
tanaka___middle_world_belt_counter = word(0x1fe74c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe74e: [16-bit] [ALL] Tanaka - Middle Secret Belt Counter (Session)
tanaka___middle_secret_belt_counter = word(0x1fe74e)
#Note: Resets if championship is abandoned or lost.

# 0x1fe750: [16-bit] [ALL] Tanaka - Heavy Local Belt Counter (Session)
tanaka___heavy_local_belt_counter = word(0x1fe750)
#Note: Resets if championship is abandoned or lost.

# 0x1fe752: [16-bit] [ALL] Tanaka - Heavy National Belt Counter (Session)
tanaka___heavy_national_belt_counter = word(0x1fe752)
#Note: Resets if championship is abandoned or lost.

# 0x1fe754: [16-bit] [ALL] Tanaka - Heavy World Belt Counter (Session)
tanaka___heavy_world_belt_counter = word(0x1fe754)
#Note: Resets if championship is abandoned or lost.

# 0x1fe756: [16-bit] [ALL] Tanaka - Heavy Secret Belt Counter (Session)
tanaka___heavy_secret_belt_counter = word(0x1fe756)
#Note: Resets if championship is abandoned or lost.

# 0x1fe758: [16-bit] [ALL] Tanaka - Hall of Fame: Total Matches (Persistent)
tanaka___hall_of_fame__total_matches = word(0x1fe758)
#Note: Career cumulative total. Never resets.

# 0x1fe75a: [16-bit] [ALL] Tanaka - Hall of Fame: Total Wins (Persistent)
tanaka___hall_of_fame__total_wins = word(0x1fe75a)
#Note: Career cumulative total. Never resets.

# 0x1fe75c: [16-bit] [ALL] Tanaka - Hall of Fame: Total Losses (Persistent)
tanaka___hall_of_fame__total_losses = word(0x1fe75c)
#Note: Career cumulative total. Never resets.

# 0x1fe75e: [16-bit] [ALL] Tanaka - Hall of Fame: Total K.Os (Persistent)
tanaka___hall_of_fame__total_k = word(0x1fe75e)
#Note: Career cumulative total. Never resets.

# 0x1fe760: [32-bit] [ALL] Tanaka - Total Character Points (Persistent)
tanaka___total_character_points = dword(0x1fe760)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe764: [16-bit] [ALL] Tanaka - Hall of Fame: Light Local Belt Counter (Persistent)
tanaka___hall_of_fame__light_local_belt_counter = word(0x1fe764)

# 0x1fe766: [16-bit] [ALL] Tanaka - Hall of Fame: Light National Belt Counter (Persistent)
tanaka___hall_of_fame__light_national_belt_counter = word(0x1fe766)

# 0x1fe768: [16-bit] [ALL] Tanaka - Hall of Fame: Light World Belt Counter (Persistent)
tanaka___hall_of_fame__light_world_belt_counter = word(0x1fe768)

# 0x1fe76a: [16-bit] [ALL] Tanaka - Hall of Fame: Light Secret Belt Counter (Persistent)
tanaka___hall_of_fame__light_secret_belt_counter = word(0x1fe76a)

# 0x1fe76c: [16-bit] [ALL] Tanaka - Hall of Fame: Middle Local Belt Counter (Persistent)
tanaka___hall_of_fame__middle_local_belt_counter = word(0x1fe76c)

# 0x1fe76e: [16-bit] [ALL] Tanaka - Hall of Fame: Middle National Belt Counter (Persistent)
tanaka___hall_of_fame__middle_national_belt_counter = word(0x1fe76e)

# 0x1fe770: [16-bit] [ALL] Tanaka - Hall of Fame: Middle World Belt Counter (Persistent)
tanaka___hall_of_fame__middle_world_belt_counter = word(0x1fe770)

# 0x1fe772: [16-bit] [ALL] Tanaka - Hall of Fame: Middle Secret Belt Counter (Persistent)
tanaka___hall_of_fame__middle_secret_belt_counter = word(0x1fe772)

# 0x1fe774: [16-bit] [ALL] Tanaka - Hall of Fame: Heavy Local Belt Counter (Persistent)
tanaka___hall_of_fame__heavy_local_belt_counter = word(0x1fe774)

# 0x1fe776: [16-bit] [ALL] Tanaka - Hall of Fame: Heavy National Belt Counter (Persistent)
tanaka___hall_of_fame__heavy_national_belt_counter = word(0x1fe776)

# 0x1fe778: [16-bit] [ALL] Tanaka - Hall of Fame: Heavy World Belt Counter (Persistent)
tanaka___hall_of_fame__heavy_world_belt_counter = word(0x1fe778)

# 0x1fe77a: [16-bit] [ALL] Tanaka - Hall of Fame: Heavy Secret Belt Counter (Persistent)
tanaka___hall_of_fame__heavy_secret_belt_counter = word(0x1fe77a)

# 0x1fe77c: [8-bit] [ALL] Ryoko - Selected for Championship Flag
ryoko___selected_for_championship_flag = byte(0x1fe77c)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe77d: [8-bit] [ALL] Ryoko - Active Championship Flag
ryoko___active_championship_flag = byte(0x1fe77d)
#0x00 = No
#0x01 = Yes

# 0x1fe77e: [8-bit] [ALL] Ryoko - Current Weight Class Participation
ryoko___current_weight_class_participation = byte(0x1fe77e)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe77f: [8-bit] [ALL] Ryoko - Current Tournament Participation
ryoko___current_tournament_participation = byte(0x1fe77f)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe780: [8-bit] [ALL] Ryoko - Championship Unlock Level
ryoko___championship_unlock_level = byte(0x1fe780)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe781: [8-bit] [ALL] Ryoko - Tournament Bracket Position / Opponent Rank
ryoko___tournament_bracket_position___opponent_rank = byte(0x1fe781)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe783: [8-bit] [ALL] Ryoko - Fighter Rank Category
ryoko___fighter_rank_category = byte(0x1fe783)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe784: [16-bit] [ALL] Ryoko - Total Matches (Session)
ryoko___total_matches = word(0x1fe784)
#Note: Resets if championship is abandoned or lost.

# 0x1fe786: [16-bit] [ALL] Ryoko - Total Wins (Session)
ryoko___total_wins = word(0x1fe786)
#Note: Resets if championship is abandoned or lost.

# 0x1fe788: [16-bit] [ALL] Ryoko - Total Losses (Session)
ryoko___total_losses = word(0x1fe788)
#Note: Resets if championship is abandoned or lost.

# 0x1fe78a: [16-bit] [ALL] Ryoko - Total K.Os (Session)
ryoko___total_k = word(0x1fe78a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe78c: [32-bit] [ALL] Ryoko - Character Points (Session)
ryoko___character_points = dword(0x1fe78c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe790: [16-bit] [ALL] Ryoko - Light Local Belt Counter (Session)
ryoko___light_local_belt_counter = word(0x1fe790)
#Note: Resets if championship is abandoned or lost.

# 0x1fe792: [16-bit] [ALL] Ryoko - Light National Belt Counter (Session)
ryoko___light_national_belt_counter = word(0x1fe792)
#Note: Resets if championship is abandoned or lost.

# 0x1fe794: [16-bit] [ALL] Ryoko - Light World Belt Counter (Session)
ryoko___light_world_belt_counter = word(0x1fe794)
#Note: Resets if championship is abandoned or lost.

# 0x1fe796: [16-bit] [ALL] Ryoko - Light Secret Belt Counter (Session)
ryoko___light_secret_belt_counter = word(0x1fe796)
#Note: Resets if championship is abandoned or lost.

# 0x1fe798: [16-bit] [ALL] Ryoko - Middle Local Belt Counter (Session)
ryoko___middle_local_belt_counter = word(0x1fe798)
#Note: Resets if championship is abandoned or lost.

# 0x1fe79a: [16-bit] [ALL] Ryoko - Middle National Belt Counter (Session)
ryoko___middle_national_belt_counter = word(0x1fe79a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe79c: [16-bit] [ALL] Ryoko - Middle World Belt Counter (Session)
ryoko___middle_world_belt_counter = word(0x1fe79c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe79e: [16-bit] [ALL] Ryoko - Middle Secret Belt Counter (Session)
ryoko___middle_secret_belt_counter = word(0x1fe79e)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7a0: [16-bit] [ALL] Ryoko - Heavy Local Belt Counter (Session)
ryoko___heavy_local_belt_counter = word(0x1fe7a0)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7a2: [16-bit] [ALL] Ryoko - Heavy National Belt Counter (Session)
ryoko___heavy_national_belt_counter = word(0x1fe7a2)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7a4: [16-bit] [ALL] Ryoko - Heavy World Belt Counter (Session)
ryoko___heavy_world_belt_counter = word(0x1fe7a4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7a6: [16-bit] [ALL] Ryoko - Heavy Secret Belt Counter (Session)
ryoko___heavy_secret_belt_counter = word(0x1fe7a6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7a8: [16-bit] [ALL] Ryoko - Hall of Fame: Total Matches (Persistent)
ryoko___hall_of_fame__total_matches = word(0x1fe7a8)
#Note: Career cumulative total. Never resets.

# 0x1fe7aa: [16-bit] [ALL] Ryoko - Hall of Fame: Total Wins (Persistent)
ryoko___hall_of_fame__total_wins = word(0x1fe7aa)
#Note: Career cumulative total. Never resets.

# 0x1fe7ac: [16-bit] [ALL] Ryoko - Hall of Fame: Total Losses (Persistent)
ryoko___hall_of_fame__total_losses = word(0x1fe7ac)
#Note: Career cumulative total. Never resets.

# 0x1fe7ae: [16-bit] [ALL] Ryoko - Hall of Fame: Total K.Os (Persistent)
ryoko___hall_of_fame__total_k = word(0x1fe7ae)
#Note: Career cumulative total. Never resets.

# 0x1fe7b0: [32-bit] [ALL] Ryoko - Total Character Points (Persistent)
ryoko___total_character_points = dword(0x1fe7b0)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe7b4: [16-bit] [ALL] Ryoko - Hall of Fame: Light Local Belt Counter (Persistent)
ryoko___hall_of_fame__light_local_belt_counter = word(0x1fe7b4)

# 0x1fe7b6: [16-bit] [ALL] Ryoko - Hall of Fame: Light National Belt Counter (Persistent)
ryoko___hall_of_fame__light_national_belt_counter = word(0x1fe7b6)

# 0x1fe7b8: [16-bit] [ALL] Ryoko - Hall of Fame: Light World Belt Counter (Persistent)
ryoko___hall_of_fame__light_world_belt_counter = word(0x1fe7b8)

# 0x1fe7ba: [16-bit] [ALL] Ryoko - Hall of Fame: Light Secret Belt Counter (Persistent)
ryoko___hall_of_fame__light_secret_belt_counter = word(0x1fe7ba)

# 0x1fe7bc: [16-bit] [ALL] Ryoko - Hall of Fame: Middle Local Belt Counter (Persistent)
ryoko___hall_of_fame__middle_local_belt_counter = word(0x1fe7bc)

# 0x1fe7be: [16-bit] [ALL] Ryoko - Hall of Fame: Middle National Belt Counter (Persistent)
ryoko___hall_of_fame__middle_national_belt_counter = word(0x1fe7be)

# 0x1fe7c0: [16-bit] [ALL] Ryoko - Hall of Fame: Middle World Belt Counter (Persistent)
ryoko___hall_of_fame__middle_world_belt_counter = word(0x1fe7c0)

# 0x1fe7c2: [16-bit] [ALL] Ryoko - Hall of Fame: Middle Secret Belt Counter (Persistent)
ryoko___hall_of_fame__middle_secret_belt_counter = word(0x1fe7c2)

# 0x1fe7c4: [16-bit] [ALL] Ryoko - Hall of Fame: Heavy Local Belt Counter (Persistent)
ryoko___hall_of_fame__heavy_local_belt_counter = word(0x1fe7c4)

# 0x1fe7c6: [16-bit] [ALL] Ryoko - Hall of Fame: Heavy National Belt Counter (Persistent)
ryoko___hall_of_fame__heavy_national_belt_counter = word(0x1fe7c6)

# 0x1fe7c8: [16-bit] [ALL] Ryoko - Hall of Fame: Heavy World Belt Counter (Persistent)
ryoko___hall_of_fame__heavy_world_belt_counter = word(0x1fe7c8)

# 0x1fe7ca: [16-bit] [ALL] Ryoko - Hall of Fame: Heavy Secret Belt Counter (Persistent)
ryoko___hall_of_fame__heavy_secret_belt_counter = word(0x1fe7ca)

# 0x1fe7cc: [8-bit] [ALL] Red - Selected for Championship Flag
red___selected_for_championship_flag = byte(0x1fe7cc)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe7cd: [8-bit] [ALL] Red - Active Championship Flag
red___active_championship_flag = byte(0x1fe7cd)
#0x00 = No
#0x01 = Yes

# 0x1fe7ce: [8-bit] [ALL] Red - Current Weight Class Participation
red___current_weight_class_participation = byte(0x1fe7ce)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe7cf: [8-bit] [ALL] Red - Current Tournament Participation
red___current_tournament_participation = byte(0x1fe7cf)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe7d0: [8-bit] [ALL] Red - Championship Unlock Level
red___championship_unlock_level = byte(0x1fe7d0)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe7d1: [8-bit] [ALL] Red - Tournament Bracket Position / Opponent Rank
red___tournament_bracket_position___opponent_rank = byte(0x1fe7d1)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe7d3: [8-bit] [ALL] Red - Fighter Rank Category
red___fighter_rank_category = byte(0x1fe7d3)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe7d4: [16-bit] [ALL] Red - Total Matches (Session)
red___total_matches = word(0x1fe7d4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7d6: [16-bit] [ALL] Red - Total Wins (Session)
red___total_wins = word(0x1fe7d6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7d8: [16-bit] [ALL] Red - Total Losses (Session)
red___total_losses = word(0x1fe7d8)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7da: [16-bit] [ALL] Red - Total K.Os (Session)
red___total_k = word(0x1fe7da)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7dc: [32-bit] [ALL] Red - Character Points (Session)
red___character_points = dword(0x1fe7dc)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7e0: [16-bit] [ALL] Red - Light Local Belt Counter (Session)
red___light_local_belt_counter = word(0x1fe7e0)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7e2: [16-bit] [ALL] Red - Light National Belt Counter (Session)
red___light_national_belt_counter = word(0x1fe7e2)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7e4: [16-bit] [ALL] Red - Light World Belt Counter (Session)
red___light_world_belt_counter = word(0x1fe7e4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7e6: [16-bit] [ALL] Red - Light Secret Belt Counter (Session)
red___light_secret_belt_counter = word(0x1fe7e6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7e8: [16-bit] [ALL] Red - Middle Local Belt Counter (Session)
red___middle_local_belt_counter = word(0x1fe7e8)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7ea: [16-bit] [ALL] Red - Middle National Belt Counter (Session)
red___middle_national_belt_counter = word(0x1fe7ea)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7ec: [16-bit] [ALL] Red - Middle World Belt Counter (Session)
red___middle_world_belt_counter = word(0x1fe7ec)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7ee: [16-bit] [ALL] Red - Middle Secret Belt Counter (Session)
red___middle_secret_belt_counter = word(0x1fe7ee)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7f0: [16-bit] [ALL] Red - Heavy Local Belt Counter (Session)
red___heavy_local_belt_counter = word(0x1fe7f0)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7f2: [16-bit] [ALL] Red - Heavy National Belt Counter (Session)
red___heavy_national_belt_counter = word(0x1fe7f2)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7f4: [16-bit] [ALL] Red - Heavy World Belt Counter (Session)
red___heavy_world_belt_counter = word(0x1fe7f4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7f6: [16-bit] [ALL] Red - Heavy Secret Belt Counter (Session)
red___heavy_secret_belt_counter = word(0x1fe7f6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe7f8: [16-bit] [ALL] Red - Hall of Fame: Total Matches (Persistent)
red___hall_of_fame__total_matches = word(0x1fe7f8)
#Note: Career cumulative total. Never resets.

# 0x1fe7fa: [16-bit] [ALL] Red - Hall of Fame: Total Wins (Persistent)
red___hall_of_fame__total_wins = word(0x1fe7fa)
#Note: Career cumulative total. Never resets.

# 0x1fe7fc: [16-bit] [ALL] Red - Hall of Fame: Total Losses (Persistent)
red___hall_of_fame__total_losses = word(0x1fe7fc)
#Note: Career cumulative total. Never resets.

# 0x1fe7fe: [16-bit] [ALL] Red - Hall of Fame: Total K.Os (Persistent)
red___hall_of_fame__total_k = word(0x1fe7fe)
#Note: Career cumulative total. Never resets.

# 0x1fe800: [32-bit] [ALL] Red - Total Character Points (Persistent)
red___total_character_points = dword(0x1fe800)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe804: [16-bit] [ALL] Red - Hall of Fame: Light Local Belt Counter (Persistent)
red___hall_of_fame__light_local_belt_counter = word(0x1fe804)

# 0x1fe806: [16-bit] [ALL] Red - Hall of Fame: Light National Belt Counter (Persistent)
red___hall_of_fame__light_national_belt_counter = word(0x1fe806)

# 0x1fe808: [16-bit] [ALL] Red - Hall of Fame: Light World Belt Counter (Persistent)
red___hall_of_fame__light_world_belt_counter = word(0x1fe808)

# 0x1fe80a: [16-bit] [ALL] Red - Hall of Fame: Light Secret Belt Counter (Persistent)
red___hall_of_fame__light_secret_belt_counter = word(0x1fe80a)

# 0x1fe80c: [16-bit] [ALL] Red - Hall of Fame: Middle Local Belt Counter (Persistent)
red___hall_of_fame__middle_local_belt_counter = word(0x1fe80c)

# 0x1fe80e: [16-bit] [ALL] Red - Hall of Fame: Middle National Belt Counter (Persistent)
red___hall_of_fame__middle_national_belt_counter = word(0x1fe80e)

# 0x1fe810: [16-bit] [ALL] Red - Hall of Fame: Middle World Belt Counter (Persistent)
red___hall_of_fame__middle_world_belt_counter = word(0x1fe810)

# 0x1fe812: [16-bit] [ALL] Red - Hall of Fame: Middle Secret Belt Counter (Persistent)
red___hall_of_fame__middle_secret_belt_counter = word(0x1fe812)

# 0x1fe814: [16-bit] [ALL] Red - Hall of Fame: Heavy Local Belt Counter (Persistent)
red___hall_of_fame__heavy_local_belt_counter = word(0x1fe814)

# 0x1fe816: [16-bit] [ALL] Red - Hall of Fame: Heavy National Belt Counter (Persistent)
red___hall_of_fame__heavy_national_belt_counter = word(0x1fe816)

# 0x1fe818: [16-bit] [ALL] Red - Hall of Fame: Heavy World Belt Counter (Persistent)
red___hall_of_fame__heavy_world_belt_counter = word(0x1fe818)

# 0x1fe81a: [16-bit] [ALL] Red - Hall of Fame: Heavy Secret Belt Counter (Persistent)
red___hall_of_fame__heavy_secret_belt_counter = word(0x1fe81a)

# 0x1fe81c: [8-bit] [ALL] B. T. - Selected for Championship Flag
b_6 = byte(0x1fe81c)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe81d: [8-bit] [ALL] B. T. - Active Championship Flag
b_7 = byte(0x1fe81d)
#0x00 = No
#0x01 = Yes

# 0x1fe81e: [8-bit] [ALL] B. T. - Current Weight Class Participation
b_8 = byte(0x1fe81e)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe81f: [8-bit] [ALL] B. T. - Current Tournament Participation
b_9 = byte(0x1fe81f)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe820: [8-bit] [ALL] B. T. - Championship Unlock Level
b_10 = byte(0x1fe820)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe821: [8-bit] [ALL] B. T. - Tournament Bracket Position / Opponent Rank
b_11 = byte(0x1fe821)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe823: [8-bit] [ALL] B. T. - Fighter Rank Category
b_12 = byte(0x1fe823)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe824: [16-bit] [ALL] B. T. - Total Matches (Session)
b_13 = word(0x1fe824)
#Note: Resets if championship is abandoned or lost.

# 0x1fe826: [16-bit] [ALL] B. T. - Total Wins (Session)
b_14 = word(0x1fe826)
#Note: Resets if championship is abandoned or lost.

# 0x1fe828: [16-bit] [ALL] B. T. - Total Losses (Session)
b_15 = word(0x1fe828)
#Note: Resets if championship is abandoned or lost.

# 0x1fe82a: [16-bit] [ALL] B. T. - Total K.Os (Session)
b_16 = word(0x1fe82a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe82c: [32-bit] [ALL] B. T. - Character Points (Session)
b_17 = dword(0x1fe82c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe830: [16-bit] [ALL] B. T. - Light Local Belt Counter (Session)
b_18 = word(0x1fe830)
#Note: Resets if championship is abandoned or lost.

# 0x1fe832: [16-bit] [ALL] B. T. - Light National Belt Counter (Session)
b_19 = word(0x1fe832)
#Note: Resets if championship is abandoned or lost.

# 0x1fe834: [16-bit] [ALL] B. T. - Light World Belt Counter (Session)
b_20 = word(0x1fe834)
#Note: Resets if championship is abandoned or lost.

# 0x1fe836: [16-bit] [ALL] B. T. - Light Secret Belt Counter (Session)
b_21 = word(0x1fe836)
#Note: Resets if championship is abandoned or lost.

# 0x1fe838: [16-bit] [ALL] B. T. - Middle Local Belt Counter (Session)
b_22 = word(0x1fe838)
#Note: Resets if championship is abandoned or lost.

# 0x1fe83a: [16-bit] [ALL] B. T. - Middle National Belt Counter (Session)
b_23 = word(0x1fe83a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe83c: [16-bit] [ALL] B. T. - Middle World Belt Counter (Session)
b_24 = word(0x1fe83c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe83e: [16-bit] [ALL] B. T. - Middle Secret Belt Counter (Session)
b_25 = word(0x1fe83e)
#Note: Resets if championship is abandoned or lost.

# 0x1fe840: [16-bit] [ALL] B. T. - Heavy Local Belt Counter (Session)
b_26 = word(0x1fe840)
#Note: Resets if championship is abandoned or lost.

# 0x1fe842: [16-bit] [ALL] B. T. - Heavy National Belt Counter (Session)
b_27 = word(0x1fe842)
#Note: Resets if championship is abandoned or lost.

# 0x1fe844: [16-bit] [ALL] B. T. - Heavy World Belt Counter (Session)
b_28 = word(0x1fe844)
#Note: Resets if championship is abandoned or lost.

# 0x1fe846: [16-bit] [ALL] B. T. - Heavy Secret Belt Counter (Session)
b_29 = word(0x1fe846)
#Note: Resets if championship is abandoned or lost.

# 0x1fe848: [16-bit] [ALL] B. T. - Hall of Fame: Total Matches (Persistent)
b_30 = word(0x1fe848)
#Note: Career cumulative total. Never resets.

# 0x1fe84a: [16-bit] [ALL] B. T. - Hall of Fame: Total Wins (Persistent)
b_31 = word(0x1fe84a)
#Note: Career cumulative total. Never resets.

# 0x1fe84c: [16-bit] [ALL] B. T. - Hall of Fame: Total Losses (Persistent)
b_32 = word(0x1fe84c)
#Note: Career cumulative total. Never resets.

# 0x1fe84e: [16-bit] [ALL] B. T. - Hall of Fame: Total K.Os (Persistent)
b_33 = word(0x1fe84e)
#Note: Career cumulative total. Never resets.

# 0x1fe850: [32-bit] [ALL] B. T. - Total Character Points (Persistent)
b_34 = dword(0x1fe850)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe854: [16-bit] [ALL] B. T. - Hall of Fame: Light Local Belt Counter (Persistent)
b_35 = word(0x1fe854)

# 0x1fe856: [16-bit] [ALL] B. T. - Hall of Fame: Light National Belt Counter (Persistent)
b_36 = word(0x1fe856)

# 0x1fe858: [16-bit] [ALL] B. T. - Hall of Fame: Light World Belt Counter (Persistent)
b_37 = word(0x1fe858)

# 0x1fe85a: [16-bit] [ALL] B. T. - Hall of Fame: Light Secret Belt Counter (Persistent)
b_38 = word(0x1fe85a)

# 0x1fe85c: [16-bit] [ALL] B. T. - Hall of Fame: Middle Local Belt Counter (Persistent)
b_39 = word(0x1fe85c)

# 0x1fe85e: [16-bit] [ALL] B. T. - Hall of Fame: Middle National Belt Counter (Persistent)
b_40 = word(0x1fe85e)

# 0x1fe860: [16-bit] [ALL] B. T. - Hall of Fame: Middle World Belt Counter (Persistent)
b_41 = word(0x1fe860)

# 0x1fe862: [16-bit] [ALL] B. T. - Hall of Fame: Middle Secret Belt Counter (Persistent)
b_42 = word(0x1fe862)

# 0x1fe864: [16-bit] [ALL] B. T. - Hall of Fame: Heavy Local Belt Counter (Persistent)
b_43 = word(0x1fe864)

# 0x1fe866: [16-bit] [ALL] B. T. - Hall of Fame: Heavy National Belt Counter (Persistent)
b_44 = word(0x1fe866)

# 0x1fe868: [16-bit] [ALL] B. T. - Hall of Fame: Heavy World Belt Counter (Persistent)
b_45 = word(0x1fe868)

# 0x1fe86a: [16-bit] [ALL] B. T. - Hall of Fame: Heavy Secret Belt Counter (Persistent)
b_46 = word(0x1fe86a)

# 0x1fe86c: [8-bit] [ALL] Puma - Selected for Championship Flag
puma___selected_for_championship_flag = byte(0x1fe86c)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe86d: [8-bit] [ALL] Puma - Active Championship Flag
puma___active_championship_flag = byte(0x1fe86d)
#0x00 = No
#0x01 = Yes

# 0x1fe86e: [8-bit] [ALL] Puma - Current Weight Class Participation
puma___current_weight_class_participation = byte(0x1fe86e)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe86f: [8-bit] [ALL] Puma - Current Tournament Participation
puma___current_tournament_participation = byte(0x1fe86f)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe870: [8-bit] [ALL] Puma - Championship Unlock Level
puma___championship_unlock_level = byte(0x1fe870)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe871: [8-bit] [ALL] Puma - Tournament Bracket Position / Opponent Rank
puma___tournament_bracket_position___opponent_rank = byte(0x1fe871)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe873: [8-bit] [ALL] Puma - Fighter Rank Category
puma___fighter_rank_category = byte(0x1fe873)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe874: [16-bit] [ALL] Puma - Total Matches (Session)
puma___total_matches = word(0x1fe874)
#Note: Resets if championship is abandoned or lost.

# 0x1fe876: [16-bit] [ALL] Puma - Total Wins (Session)
puma___total_wins = word(0x1fe876)
#Note: Resets if championship is abandoned or lost.

# 0x1fe878: [16-bit] [ALL] Puma - Total Losses (Session)
puma___total_losses = word(0x1fe878)
#Note: Resets if championship is abandoned or lost.

# 0x1fe87a: [16-bit] [ALL] Puma - Total K.Os (Session)
puma___total_k = word(0x1fe87a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe87c: [32-bit] [ALL] Puma - Character Points (Session)
puma___character_points = dword(0x1fe87c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe880: [16-bit] [ALL] Puma - Light Local Belt Counter (Session)
puma___light_local_belt_counter = word(0x1fe880)
#Note: Resets if championship is abandoned or lost.

# 0x1fe882: [16-bit] [ALL] Puma - Light National Belt Counter (Session)
puma___light_national_belt_counter = word(0x1fe882)
#Note: Resets if championship is abandoned or lost.

# 0x1fe884: [16-bit] [ALL] Puma - Light World Belt Counter (Session)
puma___light_world_belt_counter = word(0x1fe884)
#Note: Resets if championship is abandoned or lost.

# 0x1fe886: [16-bit] [ALL] Puma - Light Secret Belt Counter (Session)
puma___light_secret_belt_counter = word(0x1fe886)
#Note: Resets if championship is abandoned or lost.

# 0x1fe888: [16-bit] [ALL] Puma - Middle Local Belt Counter (Session)
puma___middle_local_belt_counter = word(0x1fe888)
#Note: Resets if championship is abandoned or lost.

# 0x1fe88a: [16-bit] [ALL] Puma - Middle National Belt Counter (Session)
puma___middle_national_belt_counter = word(0x1fe88a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe88c: [16-bit] [ALL] Puma - Middle World Belt Counter (Session)
puma___middle_world_belt_counter = word(0x1fe88c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe88e: [16-bit] [ALL] Puma - Middle Secret Belt Counter (Session)
puma___middle_secret_belt_counter = word(0x1fe88e)
#Note: Resets if championship is abandoned or lost.

# 0x1fe890: [16-bit] [ALL] Puma - Heavy Local Belt Counter (Session)
puma___heavy_local_belt_counter = word(0x1fe890)
#Note: Resets if championship is abandoned or lost.

# 0x1fe892: [16-bit] [ALL] Puma - Heavy National Belt Counter (Session)
puma___heavy_national_belt_counter = word(0x1fe892)
#Note: Resets if championship is abandoned or lost.

# 0x1fe894: [16-bit] [ALL] Puma - Heavy World Belt Counter (Session)
puma___heavy_world_belt_counter = word(0x1fe894)
#Note: Resets if championship is abandoned or lost.

# 0x1fe896: [16-bit] [ALL] Puma - Heavy Secret Belt Counter (Session)
puma___heavy_secret_belt_counter = word(0x1fe896)
#Note: Resets if championship is abandoned or lost.

# 0x1fe898: [16-bit] [ALL] Puma - Hall of Fame: Total Matches (Persistent)
puma___hall_of_fame__total_matches = word(0x1fe898)
#Note: Career cumulative total. Never resets.

# 0x1fe89a: [16-bit] [ALL] Puma - Hall of Fame: Total Wins (Persistent)
puma___hall_of_fame__total_wins = word(0x1fe89a)
#Note: Career cumulative total. Never resets.

# 0x1fe89c: [16-bit] [ALL] Puma - Hall of Fame: Total Losses (Persistent)
puma___hall_of_fame__total_losses = word(0x1fe89c)
#Note: Career cumulative total. Never resets.

# 0x1fe89e: [16-bit] [ALL] Puma - Hall of Fame: Total K.Os (Persistent)
puma___hall_of_fame__total_k = word(0x1fe89e)
#Note: Career cumulative total. Never resets.

# 0x1fe8a0: [32-bit] [ALL] Puma - Total Character Points (Persistent)
puma___total_character_points = dword(0x1fe8a0)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe8a4: [16-bit] [ALL] Puma - Hall of Fame: Light Local Belt Counter (Persistent)
puma___hall_of_fame__light_local_belt_counter = word(0x1fe8a4)

# 0x1fe8a6: [16-bit] [ALL] Puma - Hall of Fame: Light National Belt Counter (Persistent)
puma___hall_of_fame__light_national_belt_counter = word(0x1fe8a6)

# 0x1fe8a8: [16-bit] [ALL] Puma - Hall of Fame: Light World Belt Counter (Persistent)
puma___hall_of_fame__light_world_belt_counter = word(0x1fe8a8)

# 0x1fe8aa: [16-bit] [ALL] Puma - Hall of Fame: Light Secret Belt Counter (Persistent)
puma___hall_of_fame__light_secret_belt_counter = word(0x1fe8aa)

# 0x1fe8ac: [16-bit] [ALL] Puma - Hall of Fame: Middle Local Belt Counter (Persistent)
puma___hall_of_fame__middle_local_belt_counter = word(0x1fe8ac)

# 0x1fe8ae: [16-bit] [ALL] Puma - Hall of Fame: Middle National Belt Counter (Persistent)
puma___hall_of_fame__middle_national_belt_counter = word(0x1fe8ae)

# 0x1fe8b0: [16-bit] [ALL] Puma - Hall of Fame: Middle World Belt Counter (Persistent)
puma___hall_of_fame__middle_world_belt_counter = word(0x1fe8b0)

# 0x1fe8b2: [16-bit] [ALL] Puma - Hall of Fame: Middle Secret Belt Counter (Persistent)
puma___hall_of_fame__middle_secret_belt_counter = word(0x1fe8b2)

# 0x1fe8b4: [16-bit] [ALL] Puma - Hall of Fame: Heavy Local Belt Counter (Persistent)
puma___hall_of_fame__heavy_local_belt_counter = word(0x1fe8b4)

# 0x1fe8b6: [16-bit] [ALL] Puma - Hall of Fame: Heavy National Belt Counter (Persistent)
puma___hall_of_fame__heavy_national_belt_counter = word(0x1fe8b6)

# 0x1fe8b8: [16-bit] [ALL] Puma - Hall of Fame: Heavy World Belt Counter (Persistent)
puma___hall_of_fame__heavy_world_belt_counter = word(0x1fe8b8)

# 0x1fe8ba: [16-bit] [ALL] Puma - Hall of Fame: Heavy Secret Belt Counter (Persistent)
puma___hall_of_fame__heavy_secret_belt_counter = word(0x1fe8ba)

# 0x1fe8bc: [8-bit] [ALL] Prince - Selected for Championship Flag
prince___selected_for_championship_flag = byte(0x1fe8bc)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe8bd: [8-bit] [ALL] Prince - Active Championship Flag
prince___active_championship_flag = byte(0x1fe8bd)
#0x00 = No
#0x01 = Yes

# 0x1fe8be: [8-bit] [ALL] Prince - Current Weight Class Participation
prince___current_weight_class_participation = byte(0x1fe8be)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe8bf: [8-bit] [ALL] Prince - Current Tournament Participation
prince___current_tournament_participation = byte(0x1fe8bf)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe8c0: [8-bit] [ALL] Prince - Championship Unlock Level
prince___championship_unlock_level = byte(0x1fe8c0)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe8c1: [8-bit] [ALL] Prince - Tournament Bracket Position / Opponent Rank
prince___tournament_bracket_position___opponent_rank = byte(0x1fe8c1)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe8c3: [8-bit] [ALL] Prince - Fighter Rank Category
prince___fighter_rank_category = byte(0x1fe8c3)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe8c4: [16-bit] [ALL] Prince - Total Matches (Session)
prince___total_matches = word(0x1fe8c4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8c6: [16-bit] [ALL] Prince - Total Wins (Session)
prince___total_wins = word(0x1fe8c6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8c8: [16-bit] [ALL] Prince - Total Losses (Session)
prince___total_losses = word(0x1fe8c8)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8ca: [16-bit] [ALL] Prince - Total K.Os (Session)
prince___total_k = word(0x1fe8ca)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8cc: [32-bit] [ALL] Prince - Character Points (Session)
prince___character_points = dword(0x1fe8cc)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8d0: [16-bit] [ALL] Prince - Light Local Belt Counter (Session)
prince___light_local_belt_counter = word(0x1fe8d0)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8d2: [16-bit] [ALL] Prince - Light National Belt Counter (Session)
prince___light_national_belt_counter = word(0x1fe8d2)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8d4: [16-bit] [ALL] Prince - Light World Belt Counter (Session)
prince___light_world_belt_counter = word(0x1fe8d4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8d6: [16-bit] [ALL] Prince - Light Secret Belt Counter (Session)
prince___light_secret_belt_counter = word(0x1fe8d6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8d8: [16-bit] [ALL] Prince - Middle Local Belt Counter (Session)
prince___middle_local_belt_counter = word(0x1fe8d8)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8da: [16-bit] [ALL] Prince - Middle National Belt Counter (Session)
prince___middle_national_belt_counter = word(0x1fe8da)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8dc: [16-bit] [ALL] Prince - Middle World Belt Counter (Session)
prince___middle_world_belt_counter = word(0x1fe8dc)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8de: [16-bit] [ALL] Prince - Middle Secret Belt Counter (Session)
prince___middle_secret_belt_counter = word(0x1fe8de)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8e0: [16-bit] [ALL] Prince - Heavy Local Belt Counter (Session)
prince___heavy_local_belt_counter = word(0x1fe8e0)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8e2: [16-bit] [ALL] Prince - Heavy National Belt Counter (Session)
prince___heavy_national_belt_counter = word(0x1fe8e2)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8e4: [16-bit] [ALL] Prince - Heavy World Belt Counter (Session)
prince___heavy_world_belt_counter = word(0x1fe8e4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8e6: [16-bit] [ALL] Prince - Heavy Secret Belt Counter (Session)
prince___heavy_secret_belt_counter = word(0x1fe8e6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe8e8: [16-bit] [ALL] Prince - Hall of Fame: Total Matches (Persistent)
prince___hall_of_fame__total_matches = word(0x1fe8e8)
#Note: Career cumulative total. Never resets.

# 0x1fe8ea: [16-bit] [ALL] Prince - Hall of Fame: Total Wins (Persistent)
prince___hall_of_fame__total_wins = word(0x1fe8ea)
#Note: Career cumulative total. Never resets.

# 0x1fe8ec: [16-bit] [ALL] Prince - Hall of Fame: Total Losses (Persistent)
prince___hall_of_fame__total_losses = word(0x1fe8ec)
#Note: Career cumulative total. Never resets.

# 0x1fe8ee: [16-bit] [ALL] Prince - Hall of Fame: Total K.Os (Persistent)
prince___hall_of_fame__total_k = word(0x1fe8ee)
#Note: Career cumulative total. Never resets.

# 0x1fe8f0: [32-bit] [ALL] Prince - Total Character Points (Persistent)
prince___total_character_points = dword(0x1fe8f0)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe8f4: [16-bit] [ALL] Prince - Hall of Fame: Light Local Belt Counter (Persistent)
prince___hall_of_fame__light_local_belt_counter = word(0x1fe8f4)

# 0x1fe8f6: [16-bit] [ALL] Prince - Hall of Fame: Light National Belt Counter (Persistent)
prince___hall_of_fame__light_national_belt_counter = word(0x1fe8f6)

# 0x1fe8f8: [16-bit] [ALL] Prince - Hall of Fame: Light World Belt Counter (Persistent)
prince___hall_of_fame__light_world_belt_counter = word(0x1fe8f8)

# 0x1fe8fa: [16-bit] [ALL] Prince - Hall of Fame: Light Secret Belt Counter (Persistent)
prince___hall_of_fame__light_secret_belt_counter = word(0x1fe8fa)

# 0x1fe8fc: [16-bit] [ALL] Prince - Hall of Fame: Middle Local Belt Counter (Persistent)
prince___hall_of_fame__middle_local_belt_counter = word(0x1fe8fc)

# 0x1fe8fe: [16-bit] [ALL] Prince - Hall of Fame: Middle National Belt Counter (Persistent)
prince___hall_of_fame__middle_national_belt_counter = word(0x1fe8fe)

# 0x1fe900: [16-bit] [ALL] Prince - Hall of Fame: Middle World Belt Counter (Persistent)
prince___hall_of_fame__middle_world_belt_counter = word(0x1fe900)

# 0x1fe902: [16-bit] [ALL] Prince - Hall of Fame: Middle Secret Belt Counter (Persistent)
prince___hall_of_fame__middle_secret_belt_counter = word(0x1fe902)

# 0x1fe904: [16-bit] [ALL] Prince - Hall of Fame: Heavy Local Belt Counter (Persistent)
prince___hall_of_fame__heavy_local_belt_counter = word(0x1fe904)

# 0x1fe906: [16-bit] [ALL] Prince - Hall of Fame: Heavy National Belt Counter (Persistent)
prince___hall_of_fame__heavy_national_belt_counter = word(0x1fe906)

# 0x1fe908: [16-bit] [ALL] Prince - Hall of Fame: Heavy World Belt Counter (Persistent)
prince___hall_of_fame__heavy_world_belt_counter = word(0x1fe908)

# 0x1fe90a: [16-bit] [ALL] Prince - Hall of Fame: Heavy Secret Belt Counter (Persistent)
prince___hall_of_fame__heavy_secret_belt_counter = word(0x1fe90a)

# 0x1fe90c: [8-bit] [ALL] Misha - Selected for Championship Flag
misha___selected_for_championship_flag = byte(0x1fe90c)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe90d: [8-bit] [ALL] Misha - Active Championship Flag
misha___active_championship_flag = byte(0x1fe90d)
#0x00 = No
#0x01 = Yes

# 0x1fe90e: [8-bit] [ALL] Misha - Current Weight Class Participation
misha___current_weight_class_participation = byte(0x1fe90e)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe90f: [8-bit] [ALL] Misha - Current Tournament Participation
misha___current_tournament_participation = byte(0x1fe90f)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe910: [8-bit] [ALL] Misha - Championship Unlock Level
misha___championship_unlock_level = byte(0x1fe910)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe911: [8-bit] [ALL] Misha - Tournament Bracket Position / Opponent Rank
misha___tournament_bracket_position___opponent_rank = byte(0x1fe911)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe913: [8-bit] [ALL] Misha - Fighter Rank Category
misha___fighter_rank_category = byte(0x1fe913)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe914: [16-bit] [ALL] Misha - Total Matches (Session)
misha___total_matches = word(0x1fe914)
#Note: Resets if championship is abandoned or lost.

# 0x1fe916: [16-bit] [ALL] Misha - Total Wins (Session)
misha___total_wins = word(0x1fe916)
#Note: Resets if championship is abandoned or lost.

# 0x1fe918: [16-bit] [ALL] Misha - Total Losses (Session)
misha___total_losses = word(0x1fe918)
#Note: Resets if championship is abandoned or lost.

# 0x1fe91a: [16-bit] [ALL] Misha - Total K.Os (Session)
misha___total_k = word(0x1fe91a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe91c: [32-bit] [ALL] Misha - Character Points (Session)
misha___character_points = dword(0x1fe91c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe920: [16-bit] [ALL] Misha - Light Local Belt Counter (Session)
misha___light_local_belt_counter = word(0x1fe920)
#Note: Resets if championship is abandoned or lost.

# 0x1fe922: [16-bit] [ALL] Misha - Light National Belt Counter (Session)
misha___light_national_belt_counter = word(0x1fe922)
#Note: Resets if championship is abandoned or lost.

# 0x1fe924: [16-bit] [ALL] Misha - Light World Belt Counter (Session)
misha___light_world_belt_counter = word(0x1fe924)
#Note: Resets if championship is abandoned or lost.

# 0x1fe926: [16-bit] [ALL] Misha - Light Secret Belt Counter (Session)
misha___light_secret_belt_counter = word(0x1fe926)
#Note: Resets if championship is abandoned or lost.

# 0x1fe928: [16-bit] [ALL] Misha - Middle Local Belt Counter (Session)
misha___middle_local_belt_counter = word(0x1fe928)
#Note: Resets if championship is abandoned or lost.

# 0x1fe92a: [16-bit] [ALL] Misha - Middle National Belt Counter (Session)
misha___middle_national_belt_counter = word(0x1fe92a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe92c: [16-bit] [ALL] Misha - Middle World Belt Counter (Session)
misha___middle_world_belt_counter = word(0x1fe92c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe92e: [16-bit] [ALL] Misha - Middle Secret Belt Counter (Session)
misha___middle_secret_belt_counter = word(0x1fe92e)
#Note: Resets if championship is abandoned or lost.

# 0x1fe930: [16-bit] [ALL] Misha - Heavy Local Belt Counter (Session)
misha___heavy_local_belt_counter = word(0x1fe930)
#Note: Resets if championship is abandoned or lost.

# 0x1fe932: [16-bit] [ALL] Misha - Heavy National Belt Counter (Session)
misha___heavy_national_belt_counter = word(0x1fe932)
#Note: Resets if championship is abandoned or lost.

# 0x1fe934: [16-bit] [ALL] Misha - Heavy World Belt Counter (Session)
misha___heavy_world_belt_counter = word(0x1fe934)
#Note: Resets if championship is abandoned or lost.

# 0x1fe936: [16-bit] [ALL] Misha - Heavy Secret Belt Counter (Session)
misha___heavy_secret_belt_counter = word(0x1fe936)
#Note: Resets if championship is abandoned or lost.

# 0x1fe938: [16-bit] [ALL] Misha - Hall of Fame: Total Matches (Persistent)
misha___hall_of_fame__total_matches = word(0x1fe938)
#Note: Career cumulative total. Never resets.

# 0x1fe93a: [16-bit] [ALL] Misha - Hall of Fame: Total Wins (Persistent)
misha___hall_of_fame__total_wins = word(0x1fe93a)
#Note: Career cumulative total. Never resets.

# 0x1fe93c: [16-bit] [ALL] Misha - Hall of Fame: Total Losses (Persistent)
misha___hall_of_fame__total_losses = word(0x1fe93c)
#Note: Career cumulative total. Never resets.

# 0x1fe93e: [16-bit] [ALL] Misha - Hall of Fame: Total K.Os (Persistent)
misha___hall_of_fame__total_k = word(0x1fe93e)
#Note: Career cumulative total. Never resets.

# 0x1fe940: [32-bit] [ALL] Misha - Total Character Points (Persistent)
misha___total_character_points = dword(0x1fe940)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe944: [16-bit] [ALL] Misha - Hall of Fame: Light Local Belt Counter (Persistent)
misha___hall_of_fame__light_local_belt_counter = word(0x1fe944)

# 0x1fe946: [16-bit] [ALL] Misha - Hall of Fame: Light National Belt Counter (Persistent)
misha___hall_of_fame__light_national_belt_counter = word(0x1fe946)

# 0x1fe948: [16-bit] [ALL] Misha - Hall of Fame: Light World Belt Counter (Persistent)
misha___hall_of_fame__light_world_belt_counter = word(0x1fe948)

# 0x1fe94a: [16-bit] [ALL] Misha - Hall of Fame: Light Secret Belt Counter (Persistent)
misha___hall_of_fame__light_secret_belt_counter = word(0x1fe94a)

# 0x1fe94c: [16-bit] [ALL] Misha - Hall of Fame: Middle Local Belt Counter (Persistent)
misha___hall_of_fame__middle_local_belt_counter = word(0x1fe94c)

# 0x1fe94e: [16-bit] [ALL] Misha - Hall of Fame: Middle National Belt Counter (Persistent)
misha___hall_of_fame__middle_national_belt_counter = word(0x1fe94e)

# 0x1fe950: [16-bit] [ALL] Misha - Hall of Fame: Middle World Belt Counter (Persistent)
misha___hall_of_fame__middle_world_belt_counter = word(0x1fe950)

# 0x1fe952: [16-bit] [ALL] Misha - Hall of Fame: Middle Secret Belt Counter (Persistent)
misha___hall_of_fame__middle_secret_belt_counter = word(0x1fe952)

# 0x1fe954: [16-bit] [ALL] Misha - Hall of Fame: Heavy Local Belt Counter (Persistent)
misha___hall_of_fame__heavy_local_belt_counter = word(0x1fe954)

# 0x1fe956: [16-bit] [ALL] Misha - Hall of Fame: Heavy National Belt Counter (Persistent)
misha___hall_of_fame__heavy_national_belt_counter = word(0x1fe956)

# 0x1fe958: [16-bit] [ALL] Misha - Hall of Fame: Heavy World Belt Counter (Persistent)
misha___hall_of_fame__heavy_world_belt_counter = word(0x1fe958)

# 0x1fe95a: [16-bit] [ALL] Misha - Hall of Fame: Heavy Secret Belt Counter (Persistent)
misha___hall_of_fame__heavy_secret_belt_counter = word(0x1fe95a)

# 0x1fe95c: [8-bit] [ALL] Silver Man - Selected for Championship Flag
silver_man___selected_for_championship_flag = byte(0x1fe95c)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe95d: [8-bit] [ALL] Silver Man - Active Championship Flag
silver_man___active_championship_flag = byte(0x1fe95d)
#0x00 = No
#0x01 = Yes

# 0x1fe95e: [8-bit] [ALL] Silver Man - Current Weight Class Participation
silver_man___current_weight_class_participation = byte(0x1fe95e)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe95f: [8-bit] [ALL] Silver Man - Current Tournament Participation
silver_man___current_tournament_participation = byte(0x1fe95f)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe960: [8-bit] [ALL] Silver Man - Championship Unlock Level
silver_man___championship_unlock_level = byte(0x1fe960)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe961: [8-bit] [ALL] Silver Man - Tournament Bracket Position / Opponent Rank
silver_man___tournament_bracket_position___opponent_rank = byte(0x1fe961)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe963: [8-bit] [ALL] Silver Man - Fighter Rank Category
silver_man___fighter_rank_category = byte(0x1fe963)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe964: [16-bit] [ALL] Silver Man - Total Matches (Session)
silver_man___total_matches = word(0x1fe964)
#Note: Resets if championship is abandoned or lost.

# 0x1fe966: [16-bit] [ALL] Silver Man - Total Wins (Session)
silver_man___total_wins = word(0x1fe966)
#Note: Resets if championship is abandoned or lost.

# 0x1fe968: [16-bit] [ALL] Silver Man - Total Losses (Session)
silver_man___total_losses = word(0x1fe968)
#Note: Resets if championship is abandoned or lost.

# 0x1fe96a: [16-bit] [ALL] Silver Man - Total K.Os (Session)
silver_man___total_k = word(0x1fe96a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe96c: [32-bit] [ALL] Silver Man - Character Points (Session)
silver_man___character_points = dword(0x1fe96c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe970: [16-bit] [ALL] Silver Man - Light Local Belt Counter (Session)
silver_man___light_local_belt_counter = word(0x1fe970)
#Note: Resets if championship is abandoned or lost.

# 0x1fe972: [16-bit] [ALL] Silver Man - Light National Belt Counter (Session)
silver_man___light_national_belt_counter = word(0x1fe972)
#Note: Resets if championship is abandoned or lost.

# 0x1fe974: [16-bit] [ALL] Silver Man - Light World Belt Counter (Session)
silver_man___light_world_belt_counter = word(0x1fe974)
#Note: Resets if championship is abandoned or lost.

# 0x1fe976: [16-bit] [ALL] Silver Man - Light Secret Belt Counter (Session)
silver_man___light_secret_belt_counter = word(0x1fe976)
#Note: Resets if championship is abandoned or lost.

# 0x1fe978: [16-bit] [ALL] Silver Man - Middle Local Belt Counter (Session)
silver_man___middle_local_belt_counter = word(0x1fe978)
#Note: Resets if championship is abandoned or lost.

# 0x1fe97a: [16-bit] [ALL] Silver Man - Middle National Belt Counter (Session)
silver_man___middle_national_belt_counter = word(0x1fe97a)
#Note: Resets if championship is abandoned or lost.

# 0x1fe97c: [16-bit] [ALL] Silver Man - Middle World Belt Counter (Session)
silver_man___middle_world_belt_counter = word(0x1fe97c)
#Note: Resets if championship is abandoned or lost.

# 0x1fe97e: [16-bit] [ALL] Silver Man - Middle Secret Belt Counter (Session)
silver_man___middle_secret_belt_counter = word(0x1fe97e)
#Note: Resets if championship is abandoned or lost.

# 0x1fe980: [16-bit] [ALL] Silver Man - Heavy Local Belt Counter (Session)
silver_man___heavy_local_belt_counter = word(0x1fe980)
#Note: Resets if championship is abandoned or lost.

# 0x1fe982: [16-bit] [ALL] Silver Man - Heavy National Belt Counter (Session)
silver_man___heavy_national_belt_counter = word(0x1fe982)
#Note: Resets if championship is abandoned or lost.

# 0x1fe984: [16-bit] [ALL] Silver Man - Heavy World Belt Counter (Session)
silver_man___heavy_world_belt_counter = word(0x1fe984)
#Note: Resets if championship is abandoned or lost.

# 0x1fe986: [16-bit] [ALL] Silver Man - Heavy Secret Belt Counter (Session)
silver_man___heavy_secret_belt_counter = word(0x1fe986)
#Note: Resets if championship is abandoned or lost.

# 0x1fe988: [16-bit] [ALL] Silver Man - Hall of Fame: Total Matches (Persistent)
silver_man___hall_of_fame__total_matches = word(0x1fe988)
#Note: Career cumulative total. Never resets.

# 0x1fe98a: [16-bit] [ALL] Silver Man - Hall of Fame: Total Wins (Persistent)
silver_man___hall_of_fame__total_wins = word(0x1fe98a)
#Note: Career cumulative total. Never resets.

# 0x1fe98c: [16-bit] [ALL] Silver Man - Hall of Fame: Total Losses (Persistent)
silver_man___hall_of_fame__total_losses = word(0x1fe98c)
#Note: Career cumulative total. Never resets.

# 0x1fe98e: [16-bit] [ALL] Silver Man - Hall of Fame: Total K.Os (Persistent)
silver_man___hall_of_fame__total_k = word(0x1fe98e)
#Note: Career cumulative total. Never resets.

# 0x1fe990: [32-bit] [ALL] Silver Man - Total Character Points (Persistent)
silver_man___total_character_points = dword(0x1fe990)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe994: [16-bit] [ALL] Silver Man - Hall of Fame: Light Local Belt Counter (Persistent)
silver_man___hall_of_fame__light_local_belt_counter = word(0x1fe994)

# 0x1fe996: [16-bit] [ALL] Silver Man - Hall of Fame: Light National Belt Counter (Persistent)
silver_man___hall_of_fame__light_national_belt_counter = word(0x1fe996)

# 0x1fe998: [16-bit] [ALL] Silver Man - Hall of Fame: Light World Belt Counter (Persistent)
silver_man___hall_of_fame__light_world_belt_counter = word(0x1fe998)

# 0x1fe99a: [16-bit] [ALL] Silver Man - Hall of Fame: Light Secret Belt Counter (Persistent)
silver_man___hall_of_fame__light_secret_belt_counter = word(0x1fe99a)

# 0x1fe99c: [16-bit] [ALL] Silver Man - Hall of Fame: Middle Local Belt Counter (Persistent)
silver_man___hall_of_fame__middle_local_belt_counter = word(0x1fe99c)

# 0x1fe99e: [16-bit] [ALL] Silver Man - Hall of Fame: Middle National Belt Counter (Persistent)
silver_man___hall_of_fame__middle_national_belt_counter = word(0x1fe99e)

# 0x1fe9a0: [16-bit] [ALL] Silver Man - Hall of Fame: Middle World Belt Counter (Persistent)
silver_man___hall_of_fame__middle_world_belt_counter = word(0x1fe9a0)

# 0x1fe9a2: [16-bit] [ALL] Silver Man - Hall of Fame: Middle Secret Belt Counter (Persistent)
silver_man___hall_of_fame__middle_secret_belt_counter = word(0x1fe9a2)

# 0x1fe9a4: [16-bit] [ALL] Silver Man - Hall of Fame: Heavy Local Belt Counter (Persistent)
silver_man___hall_of_fame__heavy_local_belt_counter = word(0x1fe9a4)

# 0x1fe9a6: [16-bit] [ALL] Silver Man - Hall of Fame: Heavy National Belt Counter (Persistent)
silver_man___hall_of_fame__heavy_national_belt_counter = word(0x1fe9a6)

# 0x1fe9a8: [16-bit] [ALL] Silver Man - Hall of Fame: Heavy World Belt Counter (Persistent)
silver_man___hall_of_fame__heavy_world_belt_counter = word(0x1fe9a8)

# 0x1fe9aa: [16-bit] [ALL] Silver Man - Hall of Fame: Heavy Secret Belt Counter (Persistent)
silver_man___hall_of_fame__heavy_secret_belt_counter = word(0x1fe9aa)

# 0x1fe9ac: [8-bit] [ALL] Gio - Selected for Championship Flag
gio___selected_for_championship_flag = byte(0x1fe9ac)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe9ad: [8-bit] [ALL] Gio - Active Championship Flag
gio___active_championship_flag = byte(0x1fe9ad)
#0x00 = No
#0x01 = Yes

# 0x1fe9ae: [8-bit] [ALL] Gio - Current Weight Class Participation
gio___current_weight_class_participation = byte(0x1fe9ae)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe9af: [8-bit] [ALL] Gio - Current Tournament Participation
gio___current_tournament_participation = byte(0x1fe9af)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fe9b0: [8-bit] [ALL] Gio - Championship Unlock Level
gio___championship_unlock_level = byte(0x1fe9b0)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fe9b1: [8-bit] [ALL] Gio - Tournament Bracket Position / Opponent Rank
gio___tournament_bracket_position___opponent_rank = byte(0x1fe9b1)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fe9b3: [8-bit] [ALL] Gio - Fighter Rank Category
gio___fighter_rank_category = byte(0x1fe9b3)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fe9b4: [16-bit] [ALL] Gio - Total Matches (Session)
gio___total_matches = word(0x1fe9b4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9b6: [16-bit] [ALL] Gio - Total Wins (Session)
gio___total_wins = word(0x1fe9b6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9b8: [16-bit] [ALL] Gio - Total Losses (Session)
gio___total_losses = word(0x1fe9b8)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9ba: [16-bit] [ALL] Gio - Total K.Os (Session)
gio___total_k = word(0x1fe9ba)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9bc: [32-bit] [ALL] Gio - Character Points (Session)
gio___character_points = dword(0x1fe9bc)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9c0: [16-bit] [ALL] Gio - Light Local Belt Counter (Session)
gio___light_local_belt_counter = word(0x1fe9c0)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9c2: [16-bit] [ALL] Gio - Light National Belt Counter (Session)
gio___light_national_belt_counter = word(0x1fe9c2)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9c4: [16-bit] [ALL] Gio - Light World Belt Counter (Session)
gio___light_world_belt_counter = word(0x1fe9c4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9c6: [16-bit] [ALL] Gio - Light Secret Belt Counter (Session)
gio___light_secret_belt_counter = word(0x1fe9c6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9c8: [16-bit] [ALL] Gio - Middle Local Belt Counter (Session)
gio___middle_local_belt_counter = word(0x1fe9c8)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9ca: [16-bit] [ALL] Gio - Middle National Belt Counter (Session)
gio___middle_national_belt_counter = word(0x1fe9ca)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9cc: [16-bit] [ALL] Gio - Middle World Belt Counter (Session)
gio___middle_world_belt_counter = word(0x1fe9cc)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9ce: [16-bit] [ALL] Gio - Middle Secret Belt Counter (Session)
gio___middle_secret_belt_counter = word(0x1fe9ce)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9d0: [16-bit] [ALL] Gio - Heavy Local Belt Counter (Session)
gio___heavy_local_belt_counter = word(0x1fe9d0)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9d2: [16-bit] [ALL] Gio - Heavy National Belt Counter (Session)
gio___heavy_national_belt_counter = word(0x1fe9d2)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9d4: [16-bit] [ALL] Gio - Heavy World Belt Counter (Session)
gio___heavy_world_belt_counter = word(0x1fe9d4)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9d6: [16-bit] [ALL] Gio - Heavy Secret Belt Counter (Session)
gio___heavy_secret_belt_counter = word(0x1fe9d6)
#Note: Resets if championship is abandoned or lost.

# 0x1fe9d8: [16-bit] [ALL] Gio - Hall of Fame: Total Matches (Persistent)
gio___hall_of_fame__total_matches = word(0x1fe9d8)
#Note: Career cumulative total. Never resets.

# 0x1fe9da: [16-bit] [ALL] Gio - Hall of Fame: Total Wins (Persistent)
gio___hall_of_fame__total_wins = word(0x1fe9da)
#Note: Career cumulative total. Never resets.

# 0x1fe9dc: [16-bit] [ALL] Gio - Hall of Fame: Total Losses (Persistent)
gio___hall_of_fame__total_losses = word(0x1fe9dc)
#Note: Career cumulative total. Never resets.

# 0x1fe9de: [16-bit] [ALL] Gio - Hall of Fame: Total K.Os (Persistent)
gio___hall_of_fame__total_k = word(0x1fe9de)
#Note: Career cumulative total. Never resets.

# 0x1fe9e0: [32-bit] [ALL] Gio - Total Character Points (Persistent)
gio___total_character_points = dword(0x1fe9e0)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fe9e4: [16-bit] [ALL] Gio - Hall of Fame: Light Local Belt Counter (Persistent)
gio___hall_of_fame__light_local_belt_counter = word(0x1fe9e4)

# 0x1fe9e6: [16-bit] [ALL] Gio - Hall of Fame: Light National Belt Counter (Persistent)
gio___hall_of_fame__light_national_belt_counter = word(0x1fe9e6)

# 0x1fe9e8: [16-bit] [ALL] Gio - Hall of Fame: Light World Belt Counter (Persistent)
gio___hall_of_fame__light_world_belt_counter = word(0x1fe9e8)

# 0x1fe9ea: [16-bit] [ALL] Gio - Hall of Fame: Light Secret Belt Counter (Persistent)
gio___hall_of_fame__light_secret_belt_counter = word(0x1fe9ea)

# 0x1fe9ec: [16-bit] [ALL] Gio - Hall of Fame: Middle Local Belt Counter (Persistent)
gio___hall_of_fame__middle_local_belt_counter = word(0x1fe9ec)

# 0x1fe9ee: [16-bit] [ALL] Gio - Hall of Fame: Middle National Belt Counter (Persistent)
gio___hall_of_fame__middle_national_belt_counter = word(0x1fe9ee)

# 0x1fe9f0: [16-bit] [ALL] Gio - Hall of Fame: Middle World Belt Counter (Persistent)
gio___hall_of_fame__middle_world_belt_counter = word(0x1fe9f0)

# 0x1fe9f2: [16-bit] [ALL] Gio - Hall of Fame: Middle Secret Belt Counter (Persistent)
gio___hall_of_fame__middle_secret_belt_counter = word(0x1fe9f2)

# 0x1fe9f4: [16-bit] [ALL] Gio - Hall of Fame: Heavy Local Belt Counter (Persistent)
gio___hall_of_fame__heavy_local_belt_counter = word(0x1fe9f4)

# 0x1fe9f6: [16-bit] [ALL] Gio - Hall of Fame: Heavy National Belt Counter (Persistent)
gio___hall_of_fame__heavy_national_belt_counter = word(0x1fe9f6)

# 0x1fe9f8: [16-bit] [ALL] Gio - Hall of Fame: Heavy World Belt Counter (Persistent)
gio___hall_of_fame__heavy_world_belt_counter = word(0x1fe9f8)

# 0x1fe9fa: [16-bit] [ALL] Gio - Hall of Fame: Heavy Secret Belt Counter (Persistent)
gio___hall_of_fame__heavy_secret_belt_counter = word(0x1fe9fa)

# 0x1fe9fc: [8-bit] [ALL] Kojiromaru - Selected for Championship Flag
kojiromaru___selected_for_championship_flag = byte(0x1fe9fc)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fe9fd: [8-bit] [ALL] Kojiromaru - Active Championship Flag
kojiromaru___active_championship_flag = byte(0x1fe9fd)
#0x00 = No
#0x01 = Yes

# 0x1fe9fe: [8-bit] [ALL] Kojiromaru - Current Weight Class Participation
kojiromaru___current_weight_class_participation = byte(0x1fe9fe)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fe9ff: [8-bit] [ALL] Kojiromaru - Current Tournament Participation
kojiromaru___current_tournament_participation = byte(0x1fe9ff)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fea00: [8-bit] [ALL] Kojiromaru - Championship Unlock Level
kojiromaru___championship_unlock_level = byte(0x1fea00)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fea01: [8-bit] [ALL] Kojiromaru - Tournament Bracket Position / Opponent Rank
kojiromaru___tournament_bracket_position___opponent_rank = byte(0x1fea01)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fea03: [8-bit] [ALL] Kojiromaru - Fighter Rank Category
kojiromaru___fighter_rank_category = byte(0x1fea03)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fea04: [16-bit] [ALL] Kojiromaru - Total Matches (Session)
kojiromaru___total_matches = word(0x1fea04)
#Note: Resets if championship is abandoned or lost.

# 0x1fea06: [16-bit] [ALL] Kojiromaru - Total Wins (Session)
kojiromaru___total_wins = word(0x1fea06)
#Note: Resets if championship is abandoned or lost.

# 0x1fea08: [16-bit] [ALL] Kojiromaru - Total Losses (Session)
kojiromaru___total_losses = word(0x1fea08)
#Note: Resets if championship is abandoned or lost.

# 0x1fea0a: [16-bit] [ALL] Kojiromaru - Total K.Os (Session)
kojiromaru___total_k = word(0x1fea0a)
#Note: Resets if championship is abandoned or lost.

# 0x1fea0c: [32-bit] [ALL] Kojiromaru - Character Points (Session)
kojiromaru___character_points = dword(0x1fea0c)
#Note: Resets if championship is abandoned or lost.

# 0x1fea10: [16-bit] [ALL] Kojiromaru - Light Local Belt Counter (Session)
kojiromaru___light_local_belt_counter = word(0x1fea10)
#Note: Resets if championship is abandoned or lost.

# 0x1fea12: [16-bit] [ALL] Kojiromaru - Light National Belt Counter (Session)
kojiromaru___light_national_belt_counter = word(0x1fea12)
#Note: Resets if championship is abandoned or lost.

# 0x1fea14: [16-bit] [ALL] Kojiromaru - Light World Belt Counter (Session)
kojiromaru___light_world_belt_counter = word(0x1fea14)
#Note: Resets if championship is abandoned or lost.

# 0x1fea16: [16-bit] [ALL] Kojiromaru - Light Secret Belt Counter (Session)
kojiromaru___light_secret_belt_counter = word(0x1fea16)
#Note: Resets if championship is abandoned or lost.

# 0x1fea18: [16-bit] [ALL] Kojiromaru - Middle Local Belt Counter (Session)
kojiromaru___middle_local_belt_counter = word(0x1fea18)
#Note: Resets if championship is abandoned or lost.

# 0x1fea1a: [16-bit] [ALL] Kojiromaru - Middle National Belt Counter (Session)
kojiromaru___middle_national_belt_counter = word(0x1fea1a)
#Note: Resets if championship is abandoned or lost.

# 0x1fea1c: [16-bit] [ALL] Kojiromaru - Middle World Belt Counter (Session)
kojiromaru___middle_world_belt_counter = word(0x1fea1c)
#Note: Resets if championship is abandoned or lost.

# 0x1fea1e: [16-bit] [ALL] Kojiromaru - Middle Secret Belt Counter (Session)
kojiromaru___middle_secret_belt_counter = word(0x1fea1e)
#Note: Resets if championship is abandoned or lost.

# 0x1fea20: [16-bit] [ALL] Kojiromaru - Heavy Local Belt Counter (Session)
kojiromaru___heavy_local_belt_counter = word(0x1fea20)
#Note: Resets if championship is abandoned or lost.

# 0x1fea22: [16-bit] [ALL] Kojiromaru - Heavy National Belt Counter (Session)
kojiromaru___heavy_national_belt_counter = word(0x1fea22)
#Note: Resets if championship is abandoned or lost.

# 0x1fea24: [16-bit] [ALL] Kojiromaru - Heavy World Belt Counter (Session)
kojiromaru___heavy_world_belt_counter = word(0x1fea24)
#Note: Resets if championship is abandoned or lost.

# 0x1fea26: [16-bit] [ALL] Kojiromaru - Heavy Secret Belt Counter (Session)
kojiromaru___heavy_secret_belt_counter = word(0x1fea26)
#Note: Resets if championship is abandoned or lost.

# 0x1fea28: [16-bit] [ALL] Kojiromaru - Hall of Fame: Total Matches (Persistent)
kojiromaru___hall_of_fame__total_matches = word(0x1fea28)
#Note: Career cumulative total. Never resets.

# 0x1fea2a: [16-bit] [ALL] Kojiromaru - Hall of Fame: Total Wins (Persistent)
kojiromaru___hall_of_fame__total_wins = word(0x1fea2a)
#Note: Career cumulative total. Never resets.

# 0x1fea2c: [16-bit] [ALL] Kojiromaru - Hall of Fame: Total Losses (Persistent)
kojiromaru___hall_of_fame__total_losses = word(0x1fea2c)
#Note: Career cumulative total. Never resets.

# 0x1fea2e: [16-bit] [ALL] Kojiromaru - Hall of Fame: Total K.Os (Persistent)
kojiromaru___hall_of_fame__total_k = word(0x1fea2e)
#Note: Career cumulative total. Never resets.

# 0x1fea30: [32-bit] [ALL] Kojiromaru - Total Character Points (Persistent)
kojiromaru___total_character_points = dword(0x1fea30)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fea34: [16-bit] [ALL] Kojiromaru - Hall of Fame: Light Local Belt Counter (Persistent)
kojiromaru___hall_of_fame__light_local_belt_counter = word(0x1fea34)

# 0x1fea36: [16-bit] [ALL] Kojiromaru - Hall of Fame: Light National Belt Counter (Persistent)
kojiromaru___hall_of_fame__light_national_belt_counter = word(0x1fea36)

# 0x1fea38: [16-bit] [ALL] Kojiromaru - Hall of Fame: Light World Belt Counter (Persistent)
kojiromaru___hall_of_fame__light_world_belt_counter = word(0x1fea38)

# 0x1fea3a: [16-bit] [ALL] Kojiromaru - Hall of Fame: Light Secret Belt Counter (Persistent)
kojiromaru___hall_of_fame__light_secret_belt_counter = word(0x1fea3a)

# 0x1fea3c: [16-bit] [ALL] Kojiromaru - Hall of Fame: Middle Local Belt Counter (Persistent)
kojiromaru___hall_of_fame__middle_local_belt_counter = word(0x1fea3c)

# 0x1fea3e: [16-bit] [ALL] Kojiromaru - Hall of Fame: Middle National Belt Counter (Persistent)
kojiromaru___hall_of_fame__middle_national_belt_counter = word(0x1fea3e)

# 0x1fea40: [16-bit] [ALL] Kojiromaru - Hall of Fame: Middle World Belt Counter (Persistent)
kojiromaru___hall_of_fame__middle_world_belt_counter = word(0x1fea40)

# 0x1fea42: [16-bit] [ALL] Kojiromaru - Hall of Fame: Middle Secret Belt Counter (Persistent)
kojiromaru___hall_of_fame__middle_secret_belt_counter = word(0x1fea42)

# 0x1fea44: [16-bit] [ALL] Kojiromaru - Hall of Fame: Heavy Local Belt Counter (Persistent)
kojiromaru___hall_of_fame__heavy_local_belt_counter = word(0x1fea44)

# 0x1fea46: [16-bit] [ALL] Kojiromaru - Hall of Fame: Heavy National Belt Counter (Persistent)
kojiromaru___hall_of_fame__heavy_national_belt_counter = word(0x1fea46)

# 0x1fea48: [16-bit] [ALL] Kojiromaru - Hall of Fame: Heavy World Belt Counter (Persistent)
kojiromaru___hall_of_fame__heavy_world_belt_counter = word(0x1fea48)

# 0x1fea4a: [16-bit] [ALL] Kojiromaru - Hall of Fame: Heavy Secret Belt Counter (Persistent)
kojiromaru___hall_of_fame__heavy_secret_belt_counter = word(0x1fea4a)

# 0x1fea4c: [8-bit] [ALL] Spice - Selected for Championship Flag
spice___selected_for_championship_flag = byte(0x1fea4c)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fea4d: [8-bit] [ALL] Spice - Active Championship Flag
spice___active_championship_flag = byte(0x1fea4d)
#0x00 = No
#0x01 = Yes

# 0x1fea4e: [8-bit] [ALL] Spice - Current Weight Class Participation
spice___current_weight_class_participation = byte(0x1fea4e)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fea4f: [8-bit] [ALL] Spice - Current Tournament Participation
spice___current_tournament_participation = byte(0x1fea4f)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1fea50: [8-bit] [ALL] Spice - Championship Unlock Level
spice___championship_unlock_level = byte(0x1fea50)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1fea51: [8-bit] [ALL] Spice - Tournament Bracket Position / Opponent Rank
spice___tournament_bracket_position___opponent_rank = byte(0x1fea51)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1fea53: [8-bit] [ALL] Spice - Fighter Rank Category
spice___fighter_rank_category = byte(0x1fea53)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1fea54: [16-bit] [ALL] Spice - Total Matches (Session)
spice___total_matches = word(0x1fea54)
#Note: Resets if championship is abandoned or lost.

# 0x1fea56: [16-bit] [ALL] Spice - Total Wins (Session)
spice___total_wins = word(0x1fea56)
#Note: Resets if championship is abandoned or lost.

# 0x1fea58: [16-bit] [ALL] Spice - Total Losses (Session)
spice___total_losses = word(0x1fea58)
#Note: Resets if championship is abandoned or lost.

# 0x1fea5a: [16-bit] [ALL] Spice - Total K.Os (Session)
spice___total_k = word(0x1fea5a)
#Note: Resets if championship is abandoned or lost.

# 0x1fea5c: [32-bit] [ALL] Spice - Character Points (Session)
spice___character_points = dword(0x1fea5c)
#Note: Resets if championship is abandoned or lost.

# 0x1fea60: [16-bit] [ALL] Spice - Light Local Belt Counter (Session)
spice___light_local_belt_counter = word(0x1fea60)
#Note: Resets if championship is abandoned or lost.

# 0x1fea62: [16-bit] [ALL] Spice - Light National Belt Counter (Session)
spice___light_national_belt_counter = word(0x1fea62)
#Note: Resets if championship is abandoned or lost.

# 0x1fea64: [16-bit] [ALL] Spice - Light World Belt Counter (Session)
spice___light_world_belt_counter = word(0x1fea64)
#Note: Resets if championship is abandoned or lost.

# 0x1fea66: [16-bit] [ALL] Spice - Light Secret Belt Counter (Session)
spice___light_secret_belt_counter = word(0x1fea66)
#Note: Resets if championship is abandoned or lost.

# 0x1fea68: [16-bit] [ALL] Spice - Middle Local Belt Counter (Session)
spice___middle_local_belt_counter = word(0x1fea68)
#Note: Resets if championship is abandoned or lost.

# 0x1fea6a: [16-bit] [ALL] Spice - Middle National Belt Counter (Session)
spice___middle_national_belt_counter = word(0x1fea6a)
#Note: Resets if championship is abandoned or lost.

# 0x1fea6c: [16-bit] [ALL] Spice - Middle World Belt Counter (Session)
spice___middle_world_belt_counter = word(0x1fea6c)
#Note: Resets if championship is abandoned or lost.

# 0x1fea6e: [16-bit] [ALL] Spice - Middle Secret Belt Counter (Session)
spice___middle_secret_belt_counter = word(0x1fea6e)
#Note: Resets if championship is abandoned or lost.

# 0x1fea70: [16-bit] [ALL] Spice - Heavy Local Belt Counter (Session)
spice___heavy_local_belt_counter = word(0x1fea70)
#Note: Resets if championship is abandoned or lost.

# 0x1fea72: [16-bit] [ALL] Spice - Heavy National Belt Counter (Session)
spice___heavy_national_belt_counter = word(0x1fea72)
#Note: Resets if championship is abandoned or lost.

# 0x1fea74: [16-bit] [ALL] Spice - Heavy World Belt Counter (Session)
spice___heavy_world_belt_counter = word(0x1fea74)
#Note: Resets if championship is abandoned or lost.

# 0x1fea76: [16-bit] [ALL] Spice - Heavy Secret Belt Counter (Session)
spice___heavy_secret_belt_counter = word(0x1fea76)
#Note: Resets if championship is abandoned or lost.

# 0x1fea78: [16-bit] [ALL] Spice - Hall of Fame: Total Matches (Persistent)
spice___hall_of_fame__total_matches = word(0x1fea78)
#Note: Career cumulative total. Never resets.

# 0x1fea7a: [16-bit] [ALL] Spice - Hall of Fame: Total Wins (Persistent)
spice___hall_of_fame__total_wins = word(0x1fea7a)
#Note: Career cumulative total. Never resets.

# 0x1fea7c: [16-bit] [ALL] Spice - Hall of Fame: Total Losses (Persistent)
spice___hall_of_fame__total_losses = word(0x1fea7c)
#Note: Career cumulative total. Never resets.

# 0x1fea7e: [16-bit] [ALL] Spice - Hall of Fame: Total K.Os (Persistent)
spice___hall_of_fame__total_k = word(0x1fea7e)
#Note: Career cumulative total. Never resets.

# 0x1fea80: [32-bit] [ALL] Spice - Total Character Points (Persistent)
spice___total_character_points = dword(0x1fea80)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fea84: [16-bit] [ALL] Spice - Hall of Fame: Light Local Belt Counter (Persistent)
spice___hall_of_fame__light_local_belt_counter = word(0x1fea84)

# 0x1fea86: [16-bit] [ALL] Spice - Hall of Fame: Light National Belt Counter (Persistent)
spice___hall_of_fame__light_national_belt_counter = word(0x1fea86)

# 0x1fea88: [16-bit] [ALL] Spice - Hall of Fame: Light World Belt Counter (Persistent)
spice___hall_of_fame__light_world_belt_counter = word(0x1fea88)

# 0x1fea8a: [16-bit] [ALL] Spice - Hall of Fame: Light Secret Belt Counter (Persistent)
spice___hall_of_fame__light_secret_belt_counter = word(0x1fea8a)

# 0x1fea8c: [16-bit] [ALL] Spice - Hall of Fame: Middle Local Belt Counter (Persistent)
spice___hall_of_fame__middle_local_belt_counter = word(0x1fea8c)

# 0x1fea8e: [16-bit] [ALL] Spice - Hall of Fame: Middle National Belt Counter (Persistent)
spice___hall_of_fame__middle_national_belt_counter = word(0x1fea8e)

# 0x1fea90: [16-bit] [ALL] Spice - Hall of Fame: Middle World Belt Counter (Persistent)
spice___hall_of_fame__middle_world_belt_counter = word(0x1fea90)

# 0x1fea92: [16-bit] [ALL] Spice - Hall of Fame: Middle Secret Belt Counter (Persistent)
spice___hall_of_fame__middle_secret_belt_counter = word(0x1fea92)

# 0x1fea94: [16-bit] [ALL] Spice - Hall of Fame: Heavy Local Belt Counter (Persistent)
spice___hall_of_fame__heavy_local_belt_counter = word(0x1fea94)

# 0x1fea96: [16-bit] [ALL] Spice - Hall of Fame: Heavy National Belt Counter (Persistent)
spice___hall_of_fame__heavy_national_belt_counter = word(0x1fea96)

# 0x1fea98: [16-bit] [ALL] Spice - Hall of Fame: Heavy World Belt Counter (Persistent)
spice___hall_of_fame__heavy_world_belt_counter = word(0x1fea98)

# 0x1fea9a: [16-bit] [ALL] Spice - Hall of Fame: Heavy Secret Belt Counter (Persistent)
spice___hall_of_fame__heavy_secret_belt_counter = word(0x1fea9a)

# 0x1fea9c: [8-bit] [ALL] Asteka - Selected for Championship Flag
asteka___selected_for_championship_flag = byte(0x1fea9c)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1fea9d: [8-bit] [ALL] Asteka - Active Championship Flag
asteka___active_championship_flag = byte(0x1fea9d)
#0x00 = No
#0x01 = Yes

# 0x1fea9e: [8-bit] [ALL] Asteka - Current Weight Class Participation
asteka___current_weight_class_participation = byte(0x1fea9e)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fea9f: [8-bit] [ALL] Asteka - Current Tournament Participation
asteka___current_tournament_participation = byte(0x1fea9f)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1feaa0: [8-bit] [ALL] Asteka - Championship Unlock Level
asteka___championship_unlock_level = byte(0x1feaa0)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1feaa1: [8-bit] [ALL] Asteka - Tournament Bracket Position / Opponent Rank
asteka___tournament_bracket_position___opponent_rank = byte(0x1feaa1)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1feaa3: [8-bit] [ALL] Asteka - Fighter Rank Category
asteka___fighter_rank_category = byte(0x1feaa3)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1feaa4: [16-bit] [ALL] Asteka - Total Matches (Session)
asteka___total_matches = word(0x1feaa4)
#Note: Resets if championship is abandoned or lost.

# 0x1feaa6: [16-bit] [ALL] Asteka - Total Wins (Session)
asteka___total_wins = word(0x1feaa6)
#Note: Resets if championship is abandoned or lost.

# 0x1feaa8: [16-bit] [ALL] Asteka - Total Losses (Session)
asteka___total_losses = word(0x1feaa8)
#Note: Resets if championship is abandoned or lost.

# 0x1feaaa: [16-bit] [ALL] Asteka - Total K.Os (Session)
asteka___total_k = word(0x1feaaa)
#Note: Resets if championship is abandoned or lost.

# 0x1feaac: [32-bit] [ALL] Asteka - Character Points (Session)
asteka___character_points = dword(0x1feaac)
#Note: Resets if championship is abandoned or lost.

# 0x1feab0: [16-bit] [ALL] Asteka - Light Local Belt Counter (Session)
asteka___light_local_belt_counter = word(0x1feab0)
#Note: Resets if championship is abandoned or lost.

# 0x1feab2: [16-bit] [ALL] Asteka - Light National Belt Counter (Session)
asteka___light_national_belt_counter = word(0x1feab2)
#Note: Resets if championship is abandoned or lost.

# 0x1feab4: [16-bit] [ALL] Asteka - Light World Belt Counter (Session)
asteka___light_world_belt_counter = word(0x1feab4)
#Note: Resets if championship is abandoned or lost.

# 0x1feab6: [16-bit] [ALL] Asteka - Light Secret Belt Counter (Session)
asteka___light_secret_belt_counter = word(0x1feab6)
#Note: Resets if championship is abandoned or lost.

# 0x1feab8: [16-bit] [ALL] Asteka - Middle Local Belt Counter (Session)
asteka___middle_local_belt_counter = word(0x1feab8)
#Note: Resets if championship is abandoned or lost.

# 0x1feaba: [16-bit] [ALL] Asteka - Middle National Belt Counter (Session)
asteka___middle_national_belt_counter = word(0x1feaba)
#Note: Resets if championship is abandoned or lost.

# 0x1feabc: [16-bit] [ALL] Asteka - Middle World Belt Counter (Session)
asteka___middle_world_belt_counter = word(0x1feabc)
#Note: Resets if championship is abandoned or lost.

# 0x1feabe: [16-bit] [ALL] Asteka - Middle Secret Belt Counter (Session)
asteka___middle_secret_belt_counter = word(0x1feabe)
#Note: Resets if championship is abandoned or lost.

# 0x1feac0: [16-bit] [ALL] Asteka - Heavy Local Belt Counter (Session)
asteka___heavy_local_belt_counter = word(0x1feac0)
#Note: Resets if championship is abandoned or lost.

# 0x1feac2: [16-bit] [ALL] Asteka - Heavy National Belt Counter (Session)
asteka___heavy_national_belt_counter = word(0x1feac2)
#Note: Resets if championship is abandoned or lost.

# 0x1feac4: [16-bit] [ALL] Asteka - Heavy World Belt Counter (Session)
asteka___heavy_world_belt_counter = word(0x1feac4)
#Note: Resets if championship is abandoned or lost.

# 0x1feac6: [16-bit] [ALL] Asteka - Heavy Secret Belt Counter (Session)
asteka___heavy_secret_belt_counter = word(0x1feac6)
#Note: Resets if championship is abandoned or lost.

# 0x1feac8: [16-bit] [ALL] Asteka - Hall of Fame: Total Matches (Persistent)
asteka___hall_of_fame__total_matches = word(0x1feac8)
#Note: Career cumulative total. Never resets.

# 0x1feaca: [16-bit] [ALL] Asteka - Hall of Fame: Total Wins (Persistent)
asteka___hall_of_fame__total_wins = word(0x1feaca)
#Note: Career cumulative total. Never resets.

# 0x1feacc: [16-bit] [ALL] Asteka - Hall of Fame: Total Losses (Persistent)
asteka___hall_of_fame__total_losses = word(0x1feacc)
#Note: Career cumulative total. Never resets.

# 0x1feace: [16-bit] [ALL] Asteka - Hall of Fame: Total K.Os (Persistent)
asteka___hall_of_fame__total_k = word(0x1feace)
#Note: Career cumulative total. Never resets.

# 0x1fead0: [32-bit] [ALL] Asteka - Total Character Points (Persistent)
asteka___total_character_points = dword(0x1fead0)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1fead4: [16-bit] [ALL] Asteka - Hall of Fame: Light Local Belt Counter (Persistent)
asteka___hall_of_fame__light_local_belt_counter = word(0x1fead4)

# 0x1fead6: [16-bit] [ALL] Asteka - Hall of Fame: Light National Belt Counter (Persistent)
asteka___hall_of_fame__light_national_belt_counter = word(0x1fead6)

# 0x1fead8: [16-bit] [ALL] Asteka - Hall of Fame: Light World Belt Counter (Persistent)
asteka___hall_of_fame__light_world_belt_counter = word(0x1fead8)

# 0x1feada: [16-bit] [ALL] Asteka - Hall of Fame: Light Secret Belt Counter (Persistent)
asteka___hall_of_fame__light_secret_belt_counter = word(0x1feada)

# 0x1feadc: [16-bit] [ALL] Asteka - Hall of Fame: Middle Local Belt Counter (Persistent)
asteka___hall_of_fame__middle_local_belt_counter = word(0x1feadc)

# 0x1feade: [16-bit] [ALL] Asteka - Hall of Fame: Middle National Belt Counter (Persistent)
asteka___hall_of_fame__middle_national_belt_counter = word(0x1feade)

# 0x1feae0: [16-bit] [ALL] Asteka - Hall of Fame: Middle World Belt Counter (Persistent)
asteka___hall_of_fame__middle_world_belt_counter = word(0x1feae0)

# 0x1feae2: [16-bit] [ALL] Asteka - Hall of Fame: Middle Secret Belt Counter (Persistent)
asteka___hall_of_fame__middle_secret_belt_counter = word(0x1feae2)

# 0x1feae4: [16-bit] [ALL] Asteka - Hall of Fame: Heavy Local Belt Counter (Persistent)
asteka___hall_of_fame__heavy_local_belt_counter = word(0x1feae4)

# 0x1feae6: [16-bit] [ALL] Asteka - Hall of Fame: Heavy National Belt Counter (Persistent)
asteka___hall_of_fame__heavy_national_belt_counter = word(0x1feae6)

# 0x1feae8: [16-bit] [ALL] Asteka - Hall of Fame: Heavy World Belt Counter (Persistent)
asteka___hall_of_fame__heavy_world_belt_counter = word(0x1feae8)

# 0x1feaea: [16-bit] [ALL] Asteka - Hall of Fame: Heavy Secret Belt Counter (Persistent)
asteka___hall_of_fame__heavy_secret_belt_counter = word(0x1feaea)

# 0x1feaec: [8-bit] [ALL] Mr.Crown - Selected for Championship Flag
mr_4 = byte(0x1feaec)
#0x00 = No
#0x01 = Yes
#Note: Indicates if this character has an ongoing championship session

# 0x1feaed: [8-bit] [ALL] Mr. Crown - Active Championship Flag
mr_5 = byte(0x1feaed)
#0x00 = No
#0x01 = Yes

# 0x1feaee: [8-bit] [ALL] Mr. Crown - Current Weight Class Participation
mr_6 = byte(0x1feaee)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1feaef: [8-bit] [ALL] Mr. Crown - Current Tournament Participation
mr_7 = byte(0x1feaef)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret

# 0x1feaf0: [8-bit] [ALL] Mr. Crown - Championship Unlock Level
mr_8 = byte(0x1feaf0)
#0x00 = Local
#0x01 = National
#0x02 = World
#0x03 = Secret 1
#0x04 = Secret Final

# 0x1feaf1: [8-bit] [ALL] Mr.Crown - Tournament Bracket Position / Opponent Rank
mr_9 = byte(0x1feaf1)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title

# 0x1feaf3: [8-bit] [ALL] Mr. Crown - Fighter Rank Category
mr_10 = byte(0x1feaf3)
#0x00 = None
#0x01-0x31 = Rookie
#0x32-0x64 = Pro
#0x65 = Veteran

# 0x1feaf4: [16-bit] [ALL] Mr. Crown - Total Matches (Session)
mr_11 = word(0x1feaf4)
#Note: Resets if championship is abandoned or lost.

# 0x1feaf6: [16-bit] [ALL] Mr. Crown - Total Wins (Session)
mr_12 = word(0x1feaf6)
#Note: Resets if championship is abandoned or lost.

# 0x1feaf8: [16-bit] [ALL] Mr. Crown - Total Losses (Session)
mr_13 = word(0x1feaf8)
#Note: Resets if championship is abandoned or lost.

# 0x1feafa: [16-bit] [ALL] Mr. Crown - Total K.Os (Session)
mr_14 = word(0x1feafa)
#Note: Resets if championship is abandoned or lost.

# 0x1feafc: [32-bit] [ALL] Mr. Crown - Character Points (Session)
mr_15 = dword(0x1feafc)
#Note: Resets if championship is abandoned or lost.

# 0x1feb00: [16-bit] [ALL] Mr. Crown - Light Local Belt Counter (Session)
mr_16 = word(0x1feb00)
#Note: Resets if championship is abandoned or lost.

# 0x1feb02: [16-bit] [ALL] Mr. Crown - Light National Belt Counter (Session)
mr_17 = word(0x1feb02)
#Note: Resets if championship is abandoned or lost.

# 0x1feb04: [16-bit] [ALL] Mr. Crown - Light World Belt Counter (Session)
mr_18 = word(0x1feb04)
#Note: Resets if championship is abandoned or lost.

# 0x1feb06: [16-bit] [ALL] Mr. Crown - Light Secret Belt Counter (Session)
mr_19 = word(0x1feb06)
#Note: Resets if championship is abandoned or lost.

# 0x1feb08: [16-bit] [ALL] Mr. Crown - Middle Local Belt Counter (Session)
mr_20 = word(0x1feb08)
#Note: Resets if championship is abandoned or lost.

# 0x1feb0a: [16-bit] [ALL] Mr. Crown - Middle National Belt Counter (Session)
mr_21 = word(0x1feb0a)
#Note: Resets if championship is abandoned or lost.

# 0x1feb0c: [16-bit] [ALL] Mr. Crown - Middle World Belt Counter (Session)
mr_22 = word(0x1feb0c)
#Note: Resets if championship is abandoned or lost.

# 0x1feb0e: [16-bit] [ALL] Mr. Crown - Middle Secret Belt Counter (Session)
mr_23 = word(0x1feb0e)
#Note: Resets if championship is abandoned or lost.

# 0x1feb10: [16-bit] [ALL] Mr. Crown - Heavy Local Belt Counter (Session)
mr_24 = word(0x1feb10)
#Note: Resets if championship is abandoned or lost.

# 0x1feb12: [16-bit] [ALL] Mr. Crown - Heavy National Belt Counter (Session)
mr_25 = word(0x1feb12)
#Note: Resets if championship is abandoned or lost.

# 0x1feb14: [16-bit] [ALL] Mr. Crown - Heavy World Belt Counter (Session)
mr_26 = word(0x1feb14)
#Note: Resets if championship is abandoned or lost.

# 0x1feb16: [16-bit] [ALL] Mr. Crown - Heavy Secret Belt Counter (Session)
mr_27 = word(0x1feb16)
#Note: Resets if championship is abandoned or lost.

# 0x1feb18: [16-bit] [ALL] Mr. Crown - Hall of Fame: Total Matches (Persistent)
mr_28 = word(0x1feb18)
#Note: Career cumulative total. Never resets.

# 0x1feb1a: [16-bit] [ALL] Mr. Crown - Hall of Fame: Total Wins (Persistent)
mr_29 = word(0x1feb1a)
#Note: Career cumulative total. Never resets.

# 0x1feb1c: [16-bit] [ALL] Mr. Crown - Hall of Fame: Total Losses (Persistent)
mr_30 = word(0x1feb1c)
#Note: Career cumulative total. Never resets.

# 0x1feb1e: [16-bit] [ALL] Mr. Crown - Hall of Fame: Total K.Os (Persistent)
mr_31 = word(0x1feb1e)
#Note: Career cumulative total. Never resets.

# 0x1feb20: [32-bit] [ALL] Mr. Crown - Total Character Points (Persistent)
mr_32 = dword(0x1feb20)
#Note: Total score shown in Hall of Fame. Never resets.

# 0x1feb24: [16-bit] [ALL] Mr. Crown - Hall of Fame: Light Local Belt Counter (Persistent)
mr_33 = word(0x1feb24)

# 0x1feb26: [16-bit] [ALL] Mr. Crown - Hall of Fame: Light National Belt Counter (Persistent)
mr_34 = word(0x1feb26)

# 0x1feb28: [16-bit] [ALL] Mr. Crown - Hall of Fame: Light World Belt Counter (Persistent)
mr_35 = word(0x1feb28)

# 0x1feb2a: [16-bit] [ALL] Mr. Crown - Hall of Fame: Light Secret Belt Counter (Persistent)
mr_36 = word(0x1feb2a)

# 0x1feb2c: [16-bit] [ALL] Mr. Crown - Hall of Fame: Middle Local Belt Counter (Persistent)
mr_37 = word(0x1feb2c)

# 0x1feb2e: [16-bit] [ALL] Mr. Crown - Hall of Fame: Middle National Belt Counter (Persistent)
mr_38 = word(0x1feb2e)

# 0x1feb30: [16-bit] [ALL] Mr. Crown - Hall of Fame: Middle World Belt Counter (Persistent)
mr_39 = word(0x1feb30)

# 0x1feb32: [16-bit] [ALL] Mr. Crown - Hall of Fame: Middle Secret Belt Counter (Persistent)
mr_40 = word(0x1feb32)

# 0x1feb34: [16-bit] [ALL] Mr. Crown - Hall of Fame: Heavy Local Belt Counter (Persistent)
mr_41 = word(0x1feb34)

# 0x1feb36: [16-bit] [ALL] Mr. Crown - Hall of Fame: Heavy National Belt Counter (Persistent)
mr_42 = word(0x1feb36)

# 0x1feb38: [16-bit] [ALL] Mr. Crown - Hall of Fame: Heavy World Belt Counter (Persistent)
mr_43 = word(0x1feb38)

# 0x1feb3a: [16-bit] [ALL] Mr. Crown - Hall of Fame: Heavy Secret Belt Counter (Persistent)
mr_44 = word(0x1feb3a)

# 0x1feb3c: [16-bit] [ALL] Hall of Fame 1st - Total Matches
hall_of_fame_1st___total_matches = word(0x1feb3c)
#[Struct] Hall of Fame Leaderboard (13 slots x 40 bytes)
#CRITERIA: Sorted dynamically by Total Points.
#BEHAVIOR: Fighters move between slots (0x1feb3c to 0x1fed40) based on their score rank.
#ANCHOR: To find a specific fighter, check the 'Character ID' at the end of each 40-byte block.

# 0x1feb3e: [16-bit] [ALL] Hall of Fame 1st - Total Wins
hall_of_fame_1st___total_wins = word(0x1feb3e)

# 0x1feb40: [16-bit] [ALL] Hall of Fame 1st - Total Draws
hall_of_fame_1st___total_draws = word(0x1feb40)

# 0x1feb42: [16-bit] [ALL] Hall of Fame 1st - Total K.Os
hall_of_fame_1st___total_k = word(0x1feb42)

# 0x1feb44: [32-bit] [ALL] Hall of Fame 1st - Total Points
hall_of_fame_1st___total_points = dword(0x1feb44)

# 0x1feb48: [16-bit] [ALL] Hall of Fame 1st - Light Local Belt
hall_of_fame_1st___light_local_belt = word(0x1feb48)

# 0x1feb4a: [16-bit] [ALL] Hall of Fame 1st - Light National Belt
hall_of_fame_1st___light_national_belt = word(0x1feb4a)

# 0x1feb4c: [16-bit] [ALL] Hall of Fame 1st - Light World Belt
hall_of_fame_1st___light_world_belt = word(0x1feb4c)

# 0x1feb4e: [16-bit] [ALL] Hall of Fame 1st - Light Secret Belt
hall_of_fame_1st___light_secret_belt = word(0x1feb4e)

# 0x1feb50: [16-bit] [ALL] Hall of Fame 1st - Middle Local Belt
hall_of_fame_1st___middle_local_belt = word(0x1feb50)

# 0x1feb52: [16-bit] [ALL] Hall of Fame 1st - Middle National Belt
hall_of_fame_1st___middle_national_belt = word(0x1feb52)

# 0x1feb54: [16-bit] [ALL] Hall of Fame 1st - Middle World Belt
hall_of_fame_1st___middle_world_belt = word(0x1feb54)

# 0x1feb56: [16-bit] [ALL] Hall of Fame 1st - Middle Secret Belt
hall_of_fame_1st___middle_secret_belt = word(0x1feb56)

# 0x1feb58: [16-bit] [ALL] Hall of Fame 1st - Heavy Local Belt
hall_of_fame_1st___heavy_local_belt = word(0x1feb58)

# 0x1feb5a: [16-bit] [ALL] Hall of Fame 1st - Heavy National Belt
hall_of_fame_1st___heavy_national_belt = word(0x1feb5a)

# 0x1feb5c: [16-bit] [ALL] Hall of Fame 1st - Heavy World Belt
hall_of_fame_1st___heavy_world_belt = word(0x1feb5c)

# 0x1feb5e: [16-bit] [ALL] Hall of Fame 1st - Heavy Secret Belt
hall_of_fame_1st___heavy_secret_belt = word(0x1feb5e)

# 0x1feb60: [16-bit] [ALL] Hall of Fame 1st - Character ID
hall_of_fame_1st___character_id = word(0x1feb60)

# 0x1feb64: [16-bit] [ALL] Hall of Fame 2nd - Total Matches
hall_of_fame_2nd___total_matches = word(0x1feb64)

# 0x1feb66: [16-bit] [ALL] Hall of Fame 2nd - Total Wins
hall_of_fame_2nd___total_wins = word(0x1feb66)

# 0x1feb68: [16-bit] [ALL] Hall of Fame 2nd - Total Draws
hall_of_fame_2nd___total_draws = word(0x1feb68)

# 0x1feb6a: [16-bit] [ALL] Hall of Fame 2nd - Total K.Os
hall_of_fame_2nd___total_k = word(0x1feb6a)

# 0x1feb6c: [32-bit] [ALL] Hall of Fame 2nd - Total Points
hall_of_fame_2nd___total_points = dword(0x1feb6c)

# 0x1feb70: [16-bit] [ALL] Hall of Fame 2nd - Light Local Belt
hall_of_fame_2nd___light_local_belt = word(0x1feb70)

# 0x1feb72: [16-bit] [ALL] Hall of Fame 2nd - Light National Belt
hall_of_fame_2nd___light_national_belt = word(0x1feb72)

# 0x1feb74: [16-bit] [ALL] Hall of Fame 2nd - Light World Belt
hall_of_fame_2nd___light_world_belt = word(0x1feb74)

# 0x1feb76: [16-bit] [ALL] Hall of Fame 2nd - Light Secret Belt
hall_of_fame_2nd___light_secret_belt = word(0x1feb76)

# 0x1feb78: [16-bit] [ALL] Hall of Fame 2nd - Middle Local Belt
hall_of_fame_2nd___middle_local_belt = word(0x1feb78)

# 0x1feb7a: [16-bit] [ALL] Hall of Fame 2nd - Middle National Belt
hall_of_fame_2nd___middle_national_belt = word(0x1feb7a)

# 0x1feb7c: [16-bit] [ALL] Hall of Fame 2nd - Middle World Belt
hall_of_fame_2nd___middle_world_belt = word(0x1feb7c)

# 0x1feb7e: [16-bit] [ALL] Hall of Fame 2nd - Middle Secret Belt
hall_of_fame_2nd___middle_secret_belt = word(0x1feb7e)

# 0x1feb80: [16-bit] [ALL] Hall of Fame 2nd - Heavy Local Belt
hall_of_fame_2nd___heavy_local_belt = word(0x1feb80)

# 0x1feb82: [16-bit] [ALL] Hall of Fame 2nd - Heavy National Belt
hall_of_fame_2nd___heavy_national_belt = word(0x1feb82)

# 0x1feb84: [16-bit] [ALL] Hall of Fame 2nd - Heavy World Belt
hall_of_fame_2nd___heavy_world_belt = word(0x1feb84)

# 0x1feb86: [16-bit] [ALL] Hall of Fame 2nd - Heavy Secret Belt
hall_of_fame_2nd___heavy_secret_belt = word(0x1feb86)

# 0x1feb88: [16-bit] [ALL] Hall of Fame 2nd - Character ID
hall_of_fame_2nd___character_id = word(0x1feb88)

# 0x1feb8c: [16-bit] [ALL] Hall of Fame 3rd - Total Matches
hall_of_fame_3rd___total_matches = word(0x1feb8c)

# 0x1feb8e: [16-bit] [ALL] Hall of Fame 3rd - Total Wins
hall_of_fame_3rd___total_wins = word(0x1feb8e)

# 0x1feb90: [16-bit] [ALL] Hall of Fame 3rd - Total Draws
hall_of_fame_3rd___total_draws = word(0x1feb90)

# 0x1feb92: [16-bit] [ALL] Hall of Fame 3rd - Total K.Os
hall_of_fame_3rd___total_k = word(0x1feb92)

# 0x1feb94: [32-bit] [ALL] Hall of Fame 3rd - Total Points
hall_of_fame_3rd___total_points = dword(0x1feb94)

# 0x1feb98: [16-bit] [ALL] Hall of Fame 3rd - Light Local Belt
hall_of_fame_3rd___light_local_belt = word(0x1feb98)

# 0x1feb9a: [16-bit] [ALL] Hall of Fame 3rd - Light National Belt
hall_of_fame_3rd___light_national_belt = word(0x1feb9a)

# 0x1feb9c: [16-bit] [ALL] Hall of Fame 3rd - Light World Belt
hall_of_fame_3rd___light_world_belt = word(0x1feb9c)

# 0x1feb9e: [16-bit] [ALL] Hall of Fame 3rd - Light Secret Belt
hall_of_fame_3rd___light_secret_belt = word(0x1feb9e)

# 0x1feba0: [16-bit] [ALL] Hall of Fame 3rd - Middle Local Belt
hall_of_fame_3rd___middle_local_belt = word(0x1feba0)

# 0x1feba2: [16-bit] [ALL] Hall of Fame 3rd - Middle National Belt
hall_of_fame_3rd___middle_national_belt = word(0x1feba2)

# 0x1feba4: [16-bit] [ALL] Hall of Fame 3rd - Middle World Belt
hall_of_fame_3rd___middle_world_belt = word(0x1feba4)

# 0x1feba6: [16-bit] [ALL] Hall of Fame 3rd - Middle Secret Belt
hall_of_fame_3rd___middle_secret_belt = word(0x1feba6)

# 0x1feba8: [16-bit] [ALL] Hall of Fame 3rd - Heavy Local Belt
hall_of_fame_3rd___heavy_local_belt = word(0x1feba8)

# 0x1febaa: [16-bit] [ALL] Hall of Fame 3rd - Heavy National Belt
hall_of_fame_3rd___heavy_national_belt = word(0x1febaa)

# 0x1febac: [16-bit] [ALL] Hall of Fame 3rd - Heavy World Belt
hall_of_fame_3rd___heavy_world_belt = word(0x1febac)

# 0x1febae: [16-bit] [ALL] Hall of Fame 3rd - Heavy Secret Belt
hall_of_fame_3rd___heavy_secret_belt = word(0x1febae)

# 0x1febb0: [16-bit] [ALL] Hall of Fame 3rd - Character ID
hall_of_fame_3rd___character_id = word(0x1febb0)

# 0x1febb4: [16-bit] [ALL] Hall of Fame 4th - Total Matches
hall_of_fame_4th___total_matches = word(0x1febb4)

# 0x1febb6: [16-bit] [ALL] Hall of Fame 4th - Total Wins
hall_of_fame_4th___total_wins = word(0x1febb6)

# 0x1febb8: [16-bit] [ALL] Hall of Fame 4th - Total Draws
hall_of_fame_4th___total_draws = word(0x1febb8)

# 0x1febba: [16-bit] [ALL] Hall of Fame 4th - Total K.Os
hall_of_fame_4th___total_k = word(0x1febba)

# 0x1febbc: [32-bit] [ALL] Hall of Fame 4th - Total Points
hall_of_fame_4th___total_points = dword(0x1febbc)

# 0x1febc0: [16-bit] [ALL] Hall of Fame 4th - Light Local Belt
hall_of_fame_4th___light_local_belt = word(0x1febc0)

# 0x1febc2: [16-bit] [ALL] Hall of Fame 4th - Light National Belt
hall_of_fame_4th___light_national_belt = word(0x1febc2)

# 0x1febc4: [16-bit] [ALL] Hall of Fame 4th - Light World Belt
hall_of_fame_4th___light_world_belt = word(0x1febc4)

# 0x1febc6: [16-bit] [ALL] Hall of Fame 4th - Light Secret Belt
hall_of_fame_4th___light_secret_belt = word(0x1febc6)

# 0x1febc8: [16-bit] [ALL] Hall of Fame 4th - Middle Local Belt
hall_of_fame_4th___middle_local_belt = word(0x1febc8)

# 0x1febca: [16-bit] [ALL] Hall of Fame 4th - Middle National Belt
hall_of_fame_4th___middle_national_belt = word(0x1febca)

# 0x1febcc: [16-bit] [ALL] Hall of Fame 4th - Middle World Belt
hall_of_fame_4th___middle_world_belt = word(0x1febcc)

# 0x1febce: [16-bit] [ALL] Hall of Fame 4th - Middle Secret Belt
hall_of_fame_4th___middle_secret_belt = word(0x1febce)

# 0x1febd0: [16-bit] [ALL] Hall of Fame 4th - Heavy Local Belt
hall_of_fame_4th___heavy_local_belt = word(0x1febd0)

# 0x1febd2: [16-bit] [ALL] Hall of Fame 4th - Heavy National Belt
hall_of_fame_4th___heavy_national_belt = word(0x1febd2)

# 0x1febd4: [16-bit] [ALL] Hall of Fame 4th - Heavy World Belt
hall_of_fame_4th___heavy_world_belt = word(0x1febd4)

# 0x1febd6: [16-bit] [ALL] Hall of Fame 4th - Heavy Secret Belt
hall_of_fame_4th___heavy_secret_belt = word(0x1febd6)

# 0x1febd8: [16-bit] [ALL] Hall of Fame 4th - Character ID
hall_of_fame_4th___character_id = word(0x1febd8)

# 0x1febdc: [16-bit] [ALL] Hall of Fame 5th - Total Matches
hall_of_fame_5th___total_matches = word(0x1febdc)

# 0x1febde: [16-bit] [ALL] Hall of Fame 5th - Total Wins
hall_of_fame_5th___total_wins = word(0x1febde)

# 0x1febe0: [16-bit] [ALL] Hall of Fame 5th - Total Draws
hall_of_fame_5th___total_draws = word(0x1febe0)

# 0x1febe2: [16-bit] [ALL] Hall of Fame 5th - Total K.Os
hall_of_fame_5th___total_k = word(0x1febe2)

# 0x1febe4: [32-bit] [ALL] Hall of Fame 5th - Total Points
hall_of_fame_5th___total_points = dword(0x1febe4)

# 0x1febe8: [16-bit] [ALL] Hall of Fame 5th - Light Local Belt
hall_of_fame_5th___light_local_belt = word(0x1febe8)

# 0x1febea: [16-bit] [ALL] Hall of Fame 5th - Light National Belt
hall_of_fame_5th___light_national_belt = word(0x1febea)

# 0x1febec: [16-bit] [ALL] Hall of Fame 5th - Light World Belt
hall_of_fame_5th___light_world_belt = word(0x1febec)

# 0x1febee: [16-bit] [ALL] Hall of Fame 5th - Light Secret Belt
hall_of_fame_5th___light_secret_belt = word(0x1febee)

# 0x1febf0: [16-bit] [ALL] Hall of Fame 5th - Middle Local Belt
hall_of_fame_5th___middle_local_belt = word(0x1febf0)

# 0x1febf2: [16-bit] [ALL] Hall of Fame 5th - Middle National Belt
hall_of_fame_5th___middle_national_belt = word(0x1febf2)

# 0x1febf4: [16-bit] [ALL] Hall of Fame 5th - Middle World Belt
hall_of_fame_5th___middle_world_belt = word(0x1febf4)

# 0x1febf6: [16-bit] [ALL] Hall of Fame 5th - Middle Secret Belt
hall_of_fame_5th___middle_secret_belt = word(0x1febf6)

# 0x1febf8: [16-bit] [ALL] Hall of Fame 5th - Heavy Local Belt
hall_of_fame_5th___heavy_local_belt = word(0x1febf8)

# 0x1febfa: [16-bit] [ALL] Hall of Fame 5th - Heavy National Belt
hall_of_fame_5th___heavy_national_belt = word(0x1febfa)

# 0x1febfc: [16-bit] [ALL] Hall of Fame 5th - Heavy World Belt
hall_of_fame_5th___heavy_world_belt = word(0x1febfc)

# 0x1febfe: [16-bit] [ALL] Hall of Fame 5th - Heavy Secret Belt
hall_of_fame_5th___heavy_secret_belt = word(0x1febfe)

# 0x1fec00: [16-bit] [ALL] Hall of Fame 5th - Character ID
hall_of_fame_5th___character_id = word(0x1fec00)

# 0x1fec04: [16-bit] [ALL] Hall of Fame 6th - Total Matches
hall_of_fame_6th___total_matches = word(0x1fec04)

# 0x1fec06: [16-bit] [ALL] Hall of Fame 6th - Total Wins
hall_of_fame_6th___total_wins = word(0x1fec06)

# 0x1fec08: [16-bit] [ALL] Hall of Fame 6th - Total Draws
hall_of_fame_6th___total_draws = word(0x1fec08)

# 0x1fec0a: [16-bit] [ALL] Hall of Fame 6th - Total K.Os
hall_of_fame_6th___total_k = word(0x1fec0a)

# 0x1fec0c: [32-bit] [ALL] Hall of Fame 6th - Total Points
hall_of_fame_6th___total_points = dword(0x1fec0c)

# 0x1fec10: [16-bit] [ALL] Hall of Fame 6th - Light Local Belt
hall_of_fame_6th___light_local_belt = word(0x1fec10)

# 0x1fec12: [16-bit] [ALL] Hall of Fame 6th - Light National Belt
hall_of_fame_6th___light_national_belt = word(0x1fec12)

# 0x1fec14: [16-bit] [ALL] Hall of Fame 6th - Light World Belt
hall_of_fame_6th___light_world_belt = word(0x1fec14)

# 0x1fec16: [16-bit] [ALL] Hall of Fame 6th - Light Secret Belt
hall_of_fame_6th___light_secret_belt = word(0x1fec16)

# 0x1fec18: [16-bit] [ALL] Hall of Fame 6th - Middle Local Belt
hall_of_fame_6th___middle_local_belt = word(0x1fec18)

# 0x1fec1a: [16-bit] [ALL] Hall of Fame 6th - Middle National Belt
hall_of_fame_6th___middle_national_belt = word(0x1fec1a)

# 0x1fec1c: [16-bit] [ALL] Hall of Fame 6th - Middle World Belt
hall_of_fame_6th___middle_world_belt = word(0x1fec1c)

# 0x1fec1e: [16-bit] [ALL] Hall of Fame 6th - Middle Secret Belt
hall_of_fame_6th___middle_secret_belt = word(0x1fec1e)

# 0x1fec20: [16-bit] [ALL] Hall of Fame 6th - Heavy Local Belt
hall_of_fame_6th___heavy_local_belt = word(0x1fec20)

# 0x1fec22: [16-bit] [ALL] Hall of Fame 6th - Heavy National Belt
hall_of_fame_6th___heavy_national_belt = word(0x1fec22)

# 0x1fec24: [16-bit] [ALL] Hall of Fame 6th - Heavy World Belt
hall_of_fame_6th___heavy_world_belt = word(0x1fec24)

# 0x1fec26: [16-bit] [ALL] Hall of Fame 6th - Heavy Secret Belt
hall_of_fame_6th___heavy_secret_belt = word(0x1fec26)

# 0x1fec28: [16-bit] [ALL] Hall of Fame 6th - Character ID
hall_of_fame_6th___character_id = word(0x1fec28)

# 0x1fec2c: [16-bit] [ALL] Hall of Fame 7th - Total Matches
hall_of_fame_7th___total_matches = word(0x1fec2c)

# 0x1fec2e: [16-bit] [ALL] Hall of Fame 7th - Total Wins
hall_of_fame_7th___total_wins = word(0x1fec2e)

# 0x1fec30: [16-bit] [ALL] Hall of Fame 7th - Total Draws
hall_of_fame_7th___total_draws = word(0x1fec30)

# 0x1fec32: [16-bit] [ALL] Hall of Fame 7th - Total K.Os
hall_of_fame_7th___total_k = word(0x1fec32)

# 0x1fec34: [32-bit] [ALL] Hall of Fame 7th - Total Points
hall_of_fame_7th___total_points = dword(0x1fec34)

# 0x1fec38: [16-bit] [ALL] Hall of Fame 7th - Light Local Belt
hall_of_fame_7th___light_local_belt = word(0x1fec38)

# 0x1fec3a: [16-bit] [ALL] Hall of Fame 7th - Light National Belt
hall_of_fame_7th___light_national_belt = word(0x1fec3a)

# 0x1fec3c: [16-bit] [ALL] Hall of Fame 7th - Light World Belt
hall_of_fame_7th___light_world_belt = word(0x1fec3c)

# 0x1fec3e: [16-bit] [ALL] Hall of Fame 7th - Light Secret Belt
hall_of_fame_7th___light_secret_belt = word(0x1fec3e)

# 0x1fec40: [16-bit] [ALL] Hall of Fame 7th - Middle Local Belt
hall_of_fame_7th___middle_local_belt = word(0x1fec40)

# 0x1fec42: [16-bit] [ALL] Hall of Fame 7th - Middle National Belt
hall_of_fame_7th___middle_national_belt = word(0x1fec42)

# 0x1fec44: [16-bit] [ALL] Hall of Fame 7th - Middle World Belt
hall_of_fame_7th___middle_world_belt = word(0x1fec44)

# 0x1fec46: [16-bit] [ALL] Hall of Fame 7th - Middle Secret Belt
hall_of_fame_7th___middle_secret_belt = word(0x1fec46)

# 0x1fec48: [16-bit] [ALL] Hall of Fame 7th - Heavy Local Belt
hall_of_fame_7th___heavy_local_belt = word(0x1fec48)

# 0x1fec4a: [16-bit] [ALL] Hall of Fame 7th - Heavy National Belt
hall_of_fame_7th___heavy_national_belt = word(0x1fec4a)

# 0x1fec4c: [16-bit] [ALL] Hall of Fame 7th - Heavy World Belt
hall_of_fame_7th___heavy_world_belt = word(0x1fec4c)

# 0x1fec4e: [16-bit] [ALL] Hall of Fame 7th - Heavy Secret Belt
hall_of_fame_7th___heavy_secret_belt = word(0x1fec4e)

# 0x1fec50: [16-bit] [ALL] Hall of Fame 7th - Character ID
hall_of_fame_7th___character_id = word(0x1fec50)

# 0x1fec54: [16-bit] [ALL] Hall of Fame 8th - Total Matches
hall_of_fame_8th___total_matches = word(0x1fec54)

# 0x1fec56: [16-bit] [ALL] Hall of Fame 8th - Total Wins
hall_of_fame_8th___total_wins = word(0x1fec56)

# 0x1fec58: [16-bit] [ALL] Hall of Fame 8th - Total Draws
hall_of_fame_8th___total_draws = word(0x1fec58)

# 0x1fec5a: [16-bit] [ALL] Hall of Fame 8th - Total K.Os
hall_of_fame_8th___total_k = word(0x1fec5a)

# 0x1fec5c: [32-bit] [ALL] Hall of Fame 8th - Total Points
hall_of_fame_8th___total_points = dword(0x1fec5c)

# 0x1fec60: [16-bit] [ALL] Hall of Fame 8th - Light Local Belt
hall_of_fame_8th___light_local_belt = word(0x1fec60)

# 0x1fec62: [16-bit] [ALL] Hall of Fame 8th - Light National Belt
hall_of_fame_8th___light_national_belt = word(0x1fec62)

# 0x1fec64: [16-bit] [ALL] Hall of Fame 8th - Light World Belt
hall_of_fame_8th___light_world_belt = word(0x1fec64)

# 0x1fec66: [16-bit] [ALL] Hall of Fame 8th - Light Secret Belt
hall_of_fame_8th___light_secret_belt = word(0x1fec66)

# 0x1fec68: [16-bit] [ALL] Hall of Fame 8th - Middle Local Belt
hall_of_fame_8th___middle_local_belt = word(0x1fec68)

# 0x1fec6a: [16-bit] [ALL] Hall of Fame 8th - Middle National Belt
hall_of_fame_8th___middle_national_belt = word(0x1fec6a)

# 0x1fec6c: [16-bit] [ALL] Hall of Fame 8th - Middle World Belt
hall_of_fame_8th___middle_world_belt = word(0x1fec6c)

# 0x1fec6e: [16-bit] [ALL] Hall of Fame 8th - Middle Secret Belt
hall_of_fame_8th___middle_secret_belt = word(0x1fec6e)

# 0x1fec70: [16-bit] [ALL] Hall of Fame 8th - Heavy Local Belt
hall_of_fame_8th___heavy_local_belt = word(0x1fec70)

# 0x1fec72: [16-bit] [ALL] Hall of Fame 8th - Heavy National Belt
hall_of_fame_8th___heavy_national_belt = word(0x1fec72)

# 0x1fec74: [16-bit] [ALL] Hall of Fame 8th - Heavy World Belt
hall_of_fame_8th___heavy_world_belt = word(0x1fec74)

# 0x1fec76: [16-bit] [ALL] Hall of Fame 8th - Heavy Secret Belt
hall_of_fame_8th___heavy_secret_belt = word(0x1fec76)

# 0x1fec78: [16-bit] [ALL] Hall of Fame 8th - Character ID
hall_of_fame_8th___character_id = word(0x1fec78)

# 0x1fec7c: [16-bit] [ALL] Hall of Fame 9th - Total Matches
hall_of_fame_9th___total_matches = word(0x1fec7c)

# 0x1fec7e: [16-bit] [ALL] Hall of Fame 9th - Total Wins
hall_of_fame_9th___total_wins = word(0x1fec7e)

# 0x1fec80: [16-bit] [ALL] Hall of Fame 9th - Total Draws
hall_of_fame_9th___total_draws = word(0x1fec80)

# 0x1fec82: [16-bit] [ALL] Hall of Fame 9th - Total K.Os
hall_of_fame_9th___total_k = word(0x1fec82)

# 0x1fec84: [32-bit] [ALL] Hall of Fame 9th - Total Points
hall_of_fame_9th___total_points = dword(0x1fec84)

# 0x1fec88: [16-bit] [ALL] Hall of Fame 9th - Light Local Belt
hall_of_fame_9th___light_local_belt = word(0x1fec88)

# 0x1fec8a: [16-bit] [ALL] Hall of Fame 9th - Light National Belt
hall_of_fame_9th___light_national_belt = word(0x1fec8a)

# 0x1fec8c: [16-bit] [ALL] Hall of Fame 9th - Light World Belt
hall_of_fame_9th___light_world_belt = word(0x1fec8c)

# 0x1fec8e: [16-bit] [ALL] Hall of Fame 9th - Light Secret Belt
hall_of_fame_9th___light_secret_belt = word(0x1fec8e)

# 0x1fec90: [16-bit] [ALL] Hall of Fame 9th - Middle Local Belt
hall_of_fame_9th___middle_local_belt = word(0x1fec90)

# 0x1fec92: [16-bit] [ALL] Hall of Fame 9th - Middle National Belt
hall_of_fame_9th___middle_national_belt = word(0x1fec92)

# 0x1fec94: [16-bit] [ALL] Hall of Fame 9th - Middle World Belt
hall_of_fame_9th___middle_world_belt = word(0x1fec94)

# 0x1fec96: [16-bit] [ALL] Hall of Fame 9th - Middle Secret Belt
hall_of_fame_9th___middle_secret_belt = word(0x1fec96)

# 0x1fec98: [16-bit] [ALL] Hall of Fame 9th - Heavy Local Belt
hall_of_fame_9th___heavy_local_belt = word(0x1fec98)

# 0x1fec9a: [16-bit] [ALL] Hall of Fame 9th - Heavy National Belt
hall_of_fame_9th___heavy_national_belt = word(0x1fec9a)

# 0x1fec9c: [16-bit] [ALL] Hall of Fame 9th - Heavy World Belt
hall_of_fame_9th___heavy_world_belt = word(0x1fec9c)

# 0x1fec9e: [16-bit] [ALL] Hall of Fame 9th - Heavy Secret Belt
hall_of_fame_9th___heavy_secret_belt = word(0x1fec9e)

# 0x1feca0: [16-bit] [ALL] Hall of Fame 9th - Character ID
hall_of_fame_9th___character_id = word(0x1feca0)

# 0x1feca4: [16-bit] [ALL] Hall of Fame 10th - Total Matches
hall_of_fame_10th___total_matches = word(0x1feca4)

# 0x1feca6: [16-bit] [ALL] Hall of Fame 10th - Total Wins
hall_of_fame_10th___total_wins = word(0x1feca6)

# 0x1feca8: [16-bit] [ALL] Hall of Fame 10th - Total Draws
hall_of_fame_10th___total_draws = word(0x1feca8)

# 0x1fecaa: [16-bit] [ALL] Hall of Fame 10th - Total K.Os
hall_of_fame_10th___total_k = word(0x1fecaa)

# 0x1fecac: [32-bit] [ALL] Hall of Fame 10th - Total Points
hall_of_fame_10th___total_points = dword(0x1fecac)

# 0x1fecb0: [16-bit] [ALL] Hall of Fame 10th - Light Local Belt
hall_of_fame_10th___light_local_belt = word(0x1fecb0)

# 0x1fecb2: [16-bit] [ALL] Hall of Fame 10th - Light National Belt
hall_of_fame_10th___light_national_belt = word(0x1fecb2)

# 0x1fecb4: [16-bit] [ALL] Hall of Fame 10th - Light World Belt
hall_of_fame_10th___light_world_belt = word(0x1fecb4)

# 0x1fecb6: [16-bit] [ALL] Hall of Fame 10th - Light Secret Belt
hall_of_fame_10th___light_secret_belt = word(0x1fecb6)

# 0x1fecb8: [16-bit] [ALL] Hall of Fame 10th - Middle Local Belt
hall_of_fame_10th___middle_local_belt = word(0x1fecb8)

# 0x1fecba: [16-bit] [ALL] Hall of Fame 10th - Middle National Belt
hall_of_fame_10th___middle_national_belt = word(0x1fecba)

# 0x1fecbc: [16-bit] [ALL] Hall of Fame 10th - Middle World Belt
hall_of_fame_10th___middle_world_belt = word(0x1fecbc)

# 0x1fecbe: [16-bit] [ALL] Hall of Fame 10th - Middle Secret Belt
hall_of_fame_10th___middle_secret_belt = word(0x1fecbe)

# 0x1fecc0: [16-bit] [ALL] Hall of Fame 10th - Heavy Local Belt
hall_of_fame_10th___heavy_local_belt = word(0x1fecc0)

# 0x1fecc2: [16-bit] [ALL] Hall of Fame 10th - Heavy National Belt
hall_of_fame_10th___heavy_national_belt = word(0x1fecc2)

# 0x1fecc4: [16-bit] [ALL] Hall of Fame 10th - Heavy World Belt
hall_of_fame_10th___heavy_world_belt = word(0x1fecc4)

# 0x1fecc6: [16-bit] [ALL] Hall of Fame 10th - Heavy Secret Belt
hall_of_fame_10th___heavy_secret_belt = word(0x1fecc6)

# 0x1fecc8: [16-bit] [ALL] Hall of Fame 10th - Character ID
hall_of_fame_10th___character_id = word(0x1fecc8)

# 0x1feccc: [16-bit] [ALL] Hall of Fame 11th - Total Matches
hall_of_fame_11th___total_matches = word(0x1feccc)

# 0x1fecce: [16-bit] [ALL] Hall of Fame 11th - Total Wins
hall_of_fame_11th___total_wins = word(0x1fecce)

# 0x1fecd0: [16-bit] [ALL] Hall of Fame 11th - Total Draws
hall_of_fame_11th___total_draws = word(0x1fecd0)

# 0x1fecd2: [16-bit] [ALL] Hall of Fame 11th - Total K.Os
hall_of_fame_11th___total_k = word(0x1fecd2)

# 0x1fecd4: [32-bit] [ALL] Hall of Fame 11th - Total Points
hall_of_fame_11th___total_points = dword(0x1fecd4)

# 0x1fecd8: [16-bit] [ALL] Hall of Fame 11th - Light Local Belt
hall_of_fame_11th___light_local_belt = word(0x1fecd8)

# 0x1fecda: [16-bit] [ALL] Hall of Fame 11th - Light National Belt
hall_of_fame_11th___light_national_belt = word(0x1fecda)

# 0x1fecdc: [16-bit] [ALL] Hall of Fame 11th - Light World Belt
hall_of_fame_11th___light_world_belt = word(0x1fecdc)

# 0x1fecde: [16-bit] [ALL] Hall of Fame 11th - Light Secret Belt
hall_of_fame_11th___light_secret_belt = word(0x1fecde)

# 0x1fece0: [16-bit] [ALL] Hall of Fame 11th - Middle Local Belt
hall_of_fame_11th___middle_local_belt = word(0x1fece0)

# 0x1fece2: [16-bit] [ALL] Hall of Fame 11th - Middle National Belt
hall_of_fame_11th___middle_national_belt = word(0x1fece2)

# 0x1fece4: [16-bit] [ALL] Hall of Fame 11th - Middle World Belt
hall_of_fame_11th___middle_world_belt = word(0x1fece4)

# 0x1fece6: [16-bit] [ALL] Hall of Fame 11th - Middle Secret Belt
hall_of_fame_11th___middle_secret_belt = word(0x1fece6)

# 0x1fece8: [16-bit] [ALL] Hall of Fame 11th - Heavy Local Belt
hall_of_fame_11th___heavy_local_belt = word(0x1fece8)

# 0x1fecea: [16-bit] [ALL] Hall of Fame 11th - Heavy National Belt
hall_of_fame_11th___heavy_national_belt = word(0x1fecea)

# 0x1fecec: [16-bit] [ALL] Hall of Fame 11th - Heavy World Belt
hall_of_fame_11th___heavy_world_belt = word(0x1fecec)

# 0x1fecee: [16-bit] [ALL] Hall of Fame 11th - Heavy Secret Belt
hall_of_fame_11th___heavy_secret_belt = word(0x1fecee)

# 0x1fecf0: [16-bit] [ALL] Hall of Fame 11th - Character ID
hall_of_fame_11th___character_id = word(0x1fecf0)

# 0x1fecf4: [16-bit] [ALL] Hall of Fame 12th - Total Matches
hall_of_fame_12th___total_matches = word(0x1fecf4)

# 0x1fecf6: [16-bit] [ALL] Hall of Fame 12th - Total Wins
hall_of_fame_12th___total_wins = word(0x1fecf6)

# 0x1fecf8: [16-bit] [ALL] Hall of Fame 12th - Total Draws
hall_of_fame_12th___total_draws = word(0x1fecf8)

# 0x1fecfa: [16-bit] [ALL] Hall of Fame 12th - Total K.Os
hall_of_fame_12th___total_k = word(0x1fecfa)

# 0x1fecfc: [32-bit] [ALL] Hall of Fame 12th - Total Points
hall_of_fame_12th___total_points = dword(0x1fecfc)

# 0x1fed00: [16-bit] [ALL] Hall of Fame 12th - Light Local Belt
hall_of_fame_12th___light_local_belt = word(0x1fed00)

# 0x1fed02: [16-bit] [ALL] Hall of Fame 12th - Light National Belt
hall_of_fame_12th___light_national_belt = word(0x1fed02)

# 0x1fed04: [16-bit] [ALL] Hall of Fame 12th - Light World Belt
hall_of_fame_12th___light_world_belt = word(0x1fed04)

# 0x1fed06: [16-bit] [ALL] Hall of Fame 12th - Light Secret Belt
hall_of_fame_12th___light_secret_belt = word(0x1fed06)

# 0x1fed08: [16-bit] [ALL] Hall of Fame 12th - Middle Local Belt
hall_of_fame_12th___middle_local_belt = word(0x1fed08)

# 0x1fed0a: [16-bit] [ALL] Hall of Fame 12th - Middle National Belt
hall_of_fame_12th___middle_national_belt = word(0x1fed0a)

# 0x1fed0c: [16-bit] [ALL] Hall of Fame 12th - Middle World Belt
hall_of_fame_12th___middle_world_belt = word(0x1fed0c)

# 0x1fed0e: [16-bit] [ALL] Hall of Fame 12th - Middle Secret Belt
hall_of_fame_12th___middle_secret_belt = word(0x1fed0e)

# 0x1fed10: [16-bit] [ALL] Hall of Fame 12th - Heavy Local Belt
hall_of_fame_12th___heavy_local_belt = word(0x1fed10)

# 0x1fed12: [16-bit] [ALL] Hall of Fame 12th - Heavy National Belt
hall_of_fame_12th___heavy_national_belt = word(0x1fed12)

# 0x1fed14: [16-bit] [ALL] Hall of Fame 12th - Heavy World Belt
hall_of_fame_12th___heavy_world_belt = word(0x1fed14)

# 0x1fed16: [16-bit] [ALL] Hall of Fame 12th - Heavy Secret Belt
hall_of_fame_12th___heavy_secret_belt = word(0x1fed16)

# 0x1fed18: [16-bit] [ALL] Hall of Fame 12th - Character ID
hall_of_fame_12th___character_id = word(0x1fed18)

# 0x1fed1c: [16-bit] [ALL] Hall of Fame 13th - Total Matches
hall_of_fame_13th___total_matches = word(0x1fed1c)

# 0x1fed1e: [16-bit] [ALL] Hall of Fame 13th - Total Wins
hall_of_fame_13th___total_wins = word(0x1fed1e)

# 0x1fed20: [16-bit] [ALL] Hall of Fame 13th - Total Draws
hall_of_fame_13th___total_draws = word(0x1fed20)

# 0x1fed22: [16-bit] [ALL] Hall of Fame 13th - Total K.Os
hall_of_fame_13th___total_k = word(0x1fed22)

# 0x1fed24: [32-bit] [ALL] Hall of Fame 13th - Total Points
hall_of_fame_13th___total_points = dword(0x1fed24)

# 0x1fed28: [16-bit] [ALL] Hall of Fame 13th - Light Local Belt
hall_of_fame_13th___light_local_belt = word(0x1fed28)

# 0x1fed2a: [16-bit] [ALL] Hall of Fame 13th - Light National Belt
hall_of_fame_13th___light_national_belt = word(0x1fed2a)

# 0x1fed2c: [16-bit] [ALL] Hall of Fame 13th - Light World Belt
hall_of_fame_13th___light_world_belt = word(0x1fed2c)

# 0x1fed2e: [16-bit] [ALL] Hall of Fame 13th - Light Secret Belt
hall_of_fame_13th___light_secret_belt = word(0x1fed2e)

# 0x1fed30: [16-bit] [ALL] Hall of Fame 13th - Middle Local Belt
hall_of_fame_13th___middle_local_belt = word(0x1fed30)

# 0x1fed32: [16-bit] [ALL] Hall of Fame 13th - Middle National Belt
hall_of_fame_13th___middle_national_belt = word(0x1fed32)

# 0x1fed34: [16-bit] [ALL] Hall of Fame 13th - Middle World Belt
hall_of_fame_13th___middle_world_belt = word(0x1fed34)

# 0x1fed36: [16-bit] [ALL] Hall of Fame 13th - Middle Secret Belt
hall_of_fame_13th___middle_secret_belt = word(0x1fed36)

# 0x1fed38: [16-bit] [ALL] Hall of Fame 13th - Heavy Local Belt
hall_of_fame_13th___heavy_local_belt = word(0x1fed38)

# 0x1fed3a: [16-bit] [ALL] Hall of Fame 13th - Heavy National Belt
hall_of_fame_13th___heavy_national_belt = word(0x1fed3a)

# 0x1fed3c: [16-bit] [ALL] Hall of Fame 13th - Heavy World Belt
hall_of_fame_13th___heavy_world_belt = word(0x1fed3c)

# 0x1fed3e: [16-bit] [ALL] Hall of Fame 13th - Heavy Secret Belt
hall_of_fame_13th___heavy_secret_belt = word(0x1fed3e)

# 0x1fed40: [16-bit] [ALL] Hall of Fame 13th - Character ID
hall_of_fame_13th___character_id = word(0x1fed40)

# 0x1fed60: [16-bit] [ALL] Match Points Received (Championship mode)
match_points_received = word(0x1fed60)

# 0x1fed62: [16-bit] [ALL] Bonus Points Received (Championship mode)
bonus_points_received = word(0x1fed62)

# 0x1fed64: [16-bit] [ALL] Total Points Received (Championship mode)
total_points_received = word(0x1fed64)

# 0x1fedac: [8-bit] [ALL] Versus Mode - Total Rounds Count
versus_mode___total_rounds_count = byte(0x1fedac)
#0x04 = 4 Rounds
#0x06 = 6 Rounds
#0x08 = 8 Rounds
#0x0a = 10 Rounds
#0x0c = 12 Rounds
#Note: This setting is specific to Versus/Exhibition mode

# 0x1fedb0: [8-bit] [ALL] P1 Character ID
p1_character_id = byte(0x1fedb0)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1fedb4: [8-bit] [ALL] P1 Weight Class
p1_weight_class = byte(0x1fedb4)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fedc0: [16-bit] [ALL] P1 Attack Power
p1_attack_power = word(0x1fedc0)

# 0x1fedc8: [16-bit] [ALL] P1 Defense Power
p1_defense_power = word(0x1fedc8)

# 0x1fedd0: [16-bit] [ALL] P1 Rush Gauge
p1_rush_gauge = word(0x1fedd0)

# 0x1fedd8: [16-bit] [ALL] P1 Max HP
p1_max_hp = word(0x1fedd8)

# 0x1feddc: [16-bit] [ALL] P1 Current HP
p1_current_hp = word(0x1feddc)

# 0x1fede0: [32-bit] [ALL] P1 Energy/Stamina
p1_energy_stamina = dword(0x1fede0)

# 0x1fede8: [8-bit] [ALL] P2 Character ID
p2_character_id = byte(0x1fede8)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1fedec: [8-bit] [ALL] P2 Weight Class
p2_weight_class = byte(0x1fedec)
#0x00 = Light
#0x01 = Middle
#0x02 = Heavy

# 0x1fedf8: [16-bit] [ALL] P2 Attack Power
p2_attack_power = word(0x1fedf8)

# 0x1fee00: [16-bit] [ALL] P2 Defense Power
p2_defense_power = word(0x1fee00)

# 0x1fee08: [16-bit] [ALL] P2 Rush Gauge
p2_rush_gauge = word(0x1fee08)

# 0x1fee10: [16-bit] [ALL] P2 Max HP
p2_max_hp = word(0x1fee10)

# 0x1fee14: [16-bit] [ALL] P2 Current HP
p2_current_hp = word(0x1fee14)

# 0x1fee18: [32-bit] [ALL] P2 Energy/Stamina
p2_energy_stamina = dword(0x1fee18)

# 0x1fee20: [8-bit] [ALL] P1 Punch Chain
p1_punch_chain = byte(0x1fee20)
#Note: This address tracks the current state of a punch combo. The value cycles back to 0x00 after the sequence is completed at 0x02
#0x00 = None
#0x01 = 1 Punch
#0x02 = 2 Punches

# 0x1fee24: [8-bit] [ALL] P2 Punch Chain
p2_punch_chain = byte(0x1fee24)
#Note: This address tracks the current state of a punch combo. The value cycles back to 0x00 after the sequence is completed at 0x02
#0x00 = None
#0x01 = 1 Punch
#0x02 = 2 Punches

# 0x1fee54: [16-bit] [ALL] P1 Damage Array (Index 0)
p1_damage_array = word(0x1fee54)
#Stores the raw impact force of the last punch landed
#This value is used to calculate the KG displayed on the impact panel
#Ratio: ~5:1 (Memory Value / 5 = Displayed KG)

# 0x1fee58: [16-bit] [ALL] P1 Damage Array (Index 1)
p1_damage_array_2 = word(0x1fee58)
#Stores the raw impact force of the last punch landed
#This value is used to calculate the KG displayed on the impact panel
#Ratio: ~5:1 (Memory Value / 5 = Displayed KG)

# 0x1fee5c: [16-bit] [ALL] P1 Damage Array (Index 2)
p1_damage_array_3 = word(0x1fee5c)
#Stores the raw impact force of the last punch landed
#This value is used to calculate the KG displayed on the impact panel
#Ratio: ~5:1 (Memory Value / 5 = Displayed KG)

# 0x1fee60: [16-bit] [ALL] P2 Damage Array (Index 0)
p2_damage_array = word(0x1fee60)
#Stores the raw impact force of the last punch landed
#This value is used to calculate the KG displayed on the impact panel
#Ratio: ~5:1 (Memory Value / 5 = Displayed KG)

# 0x1fee64: [16-bit] [ALL] P2 Damage Array (Index 1)
p2_damage_array_2 = word(0x1fee64)
#Stores the raw impact force of the last punch landed
#This value is used to calculate the KG displayed on the impact panel
#Ratio: ~5:1 (Memory Value / 5 = Displayed KG)

# 0x1fee68: [16-bit] [ALL] P2 Damage Array (Index 2)
p2_damage_array_3 = word(0x1fee68)
#Stores the raw impact force of the last punch landed
#This value is used to calculate the KG displayed on the impact panel
#Ratio: ~5:1 (Memory Value / 5 = Displayed KG)

# 0x1fef66: [8-bit] [ALL] P1 Character ID (Championship/Ranking Mode)
p1_character_id_2 = byte(0x1fef66)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1fef68: [8-bit] [ALL] Tournament Bracket Position / Opponent Rank
tournament_bracket_position___opponent_rank = byte(0x1fef68)
#0x07 = 7th Place (Start)
#0x06 = 6th Place
#0x05 = 5th Place
#0x04 = 4th Place
#0x03 = 3rd Place
#0x02 = 2nd Place
#0x01 = #1 Contender (Championship Match)
#Note: Counts down the remaining opponents. When at 0x01, the next victory secures the title.

# 0x1fef6a: [8-bit] [ALL] Match Win Indicator (Championship Mode)
match_win_indicator = byte(0x1fef6a)
#Bit0 = 1 (0x01) when Player 1 wins the match
#0x00 = Match in progress
#Note: In VS Mode, this value is sticky and remains 0x01 until the player returns to the main menu

# 0x1fef70: [8-bit] [ALL] Current Championship/Category Indicator
current_championship_category_indicator = byte(0x1fef70)
#0x00 = Heavy Local
#0x01 = Middle Local
#0x02 = Light Local
#0x03 = Heavy Nacional
#0x04 = Middle Nacional
#0x05 = Light Nacional
#0x06 = Heavy World
#0x07 = Middle World
#0x08 = Light World
#0x09 = Heavy Secret
#0x0a = Middle Secret
#0x0b = Light Secret

# 0x1fef74: [8-bit] [ALL] Menu Location ID
menu_location_id = byte(0x1fef74)
#0x00 = Ranking
#0x01 = Scout
#0x02 = VS
#0x03 = Record
#0x04 = Note
#0x05 = Memory Card

# 0x1fef7a: [8-bit] [ALL] Character Biography Viewer ID
character_biography_viewer_id = byte(0x1fef7a)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1fef7c: [8-bit] [ALL] P1 Character ID (VS Mode only)
p1_character_id_3 = byte(0x1fef7c)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1fef7e: [8-bit] [ALL] P2 Character ID (VS Mode only)
p2_character_id_2 = byte(0x1fef7e)
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1fef84: [8-bit] [ALL] Player 1 Control Flag
player_1_control_flag = byte(0x1fef84)
#0x00 = Inactive
#0x01 = Controlled by Player 1

# 0x1fef88: [8-bit] [ALL] Player 2 Control Flag
player_2_control_flag = byte(0x1fef88)
#0x00 = CPU / Inactive
#0x01 = Controlled by Player 2 (VS Mode)

# 0x1fef94: [8-bit] [ALL] Player 1 Match Score (VS Mode)
player_1_match_score = byte(0x1fef94)
#* Only active during 2-Player VS Mode.

# 0x1fef98: [8-bit] [ALL] Player 2 Match Score (VS Mode)
player_2_match_score = byte(0x1fef98)
#* Only active during 2-Player VS Mode.

# 0x1feff0: [8-bit] [ALL] Screen ID / Game State
screen_id___game_state = byte(0x1feff0)
#== USA / EU==
#0x06 = Boot Screen / Initial Warning
#0x07 = Nekogum Logo
#0x08 = A1 Games Logo
#0x09 = Title Screen
#0x0a = Main Menu
#0x0e = In Fight / Match Active
#0x0f = Story Mode View / Cutscene
#0x13 = Load/Save Screen (Memory Card)
#== JP ==
#0x0d = in Fight
#0x09 = in Menu
