# Code Notes for Game ID 16444
# Source: 16444-User.txt

from pycheevos.core.helpers import * # type: ignore

# 0x000032: [8-bit] Screen ID 
# Values:
# 0x00 = Konami logo (on boot)
# 0x01 = Title screen
# 0x03 = In-game (Demo)
# 0x05 = Title screen to Mode Select transition
# 0x06 = Mode Select screen (and in-game during normal play)
# 0x09 = Intro (before title screen)
# Note: Seems to be 0x06 consistently during all normal game modes after the mode select screen. Seems consistent.
screen_id_rnvalues_rn0x00_konami_logo_rn0x01_title_screenrn0x03_i = byte(0x000032)

# 0x000052: [8-bit] CPU Active
# Values:
# 0x00 = Yes
# 0x01 = No
cpu_activernvalues_rn0x00 = byte(0x000052)

# 0x000058: [8-bit] Game State / Scenario
# Values:
# 0x01 = Game Over screen (Win or Lose)
# 0x03 = Penalty Shootout
game_state___scenariornvalues_rn0x01 = byte(0x000058)

# 0x0000a8: [8-bit] Match Period
# Values:
# 0x00 = First Half
# 0x01 = Second Half
# 0x02 = First Half (Extra Time)
# 0x03 = Second Half (Extra Time)
# Note: Value remains 0x03 if the match goes to a penalty shootout after extra time.
match_periodrnvalues_rn0x00_first_halfrn0x01_second_halfrn0x02_fi = byte(0x0000a8)

# 0x000da0: [8-bit] Team P1 ID
# # == Brazil Teams ==
# 0x00 = Cruzeiro
# 0x02 = Palmeiras
# 0x04 = Botafogo
# 0x06 = Parana
# 0x08 = Bragantino
# 0x0a = Guarani
# 0x0c = Gremio
# 0x0e = Juventude
# 0x10 = Flamengo
# 0x12 = Paysandu
# 0x14 = Corinthians
# 0x16 = Vitoria
# 0x18 = Fluminense
# 0x1a = Internacional
# 0x1c = Santos
# 0x1e = São Paulo
# 0x20 = Portuguesa
# 0x22 = Goias
# 0x24 = Criciuma
# 0x26 = Bahia
# 0x28 = Sport
# 0x2a = Vasco
# 0x2c = Atletico-MG
# 0x2e = União
# # == Europe Teams ==
# 0x30 = Ajax
# 0x32 = PSG
# 0x34 = Bayern
# 0x36 = Juventus
# 0x38 = Real Madrid
# 0x3a = Barcelona
# # == Libertadores Teams ==
# 0x3c = Boca Juniors
# 0x3e = River Plate
# 0x40 = Independiente
# 0x42 = Penarol
# 0x44 = Univ de Chile
# 0x46 = Colo Colo
# # == All-Star Teams ==
# 0x48 = Brasil
# 0x4a = Brasil 58
# 0x4c = Brasil 96
# 0x4e = Europa (Europe All-Stars)
# 0x50 = America A (America All-Stars A)
# 0x52 = America E (America All-Stars E)
team_p1_idrn = byte(0x000da0)

# 0x000da2: [8-bit] Player 1 Score
# Note: Holds the P1 score as a standard hex value
player_1_scorernnote__holds_the_p1_score_as_a_standard_hex_value = byte(0x000da2)

# 0x000da6: [8-bit] P1 Team Formation
# Values:
# 0x00 = 4-5-1
# 0x01 = 4-4-2
# 0x02 = 4-3-3
# 0x03 = 4-2-4
# 0x04 = 3-5-2
# 0x05 = 3-4-3
# 0x06 = 3-3-4
# 0x07 = 3-2-5
# 0x08 = 2-5-3
# 0x09 = 2-4-4
# 0x0a = 2-3-5
# 0x0b = 5-4-1
# 0x0c = 5-3-2
# 0x0d = 5-2-3
# 0x0e = 1-5-4
# 0x0f = 1-4-5
p1_team_formationrnvalues_rn0x00 = byte(0x000da6)

# 0x000daa: [8-bit] P1 Total Shots
# Note: Tracks the total number of shots taken by Player 1. Value is standard hex.
p1_total_shotsrnnote__tracks_the_total_number_of_shots_taken_by_p = byte(0x000daa)

# 0x000dab: [8-bit] P1 Total Free Kicks
# Note: Tracks the total number of free kicks taken by Player 1. Value is standard hex.
p1_total_free_kicksrnnote__tracks_the_total_number_of_free_kicks_ = byte(0x000dab)

# 0x000dac: [8-bit] P1 Total Corner Kicks
# Note: Tracks the total number of corner kicks taken by Player 1. Value is standard hex.
p1_total_corner_kicksrnnote__tracks_the_total_number_of_corner_ki = byte(0x000dac)

# 0x000dad: [8-bit] P1 Total Penalties
# Note: Tracks the total number of penalties taken by Player 1. Value is standard hex.
p1_total_penaltiesrnnote__tracks_the_total_number_of_penalties_ta = byte(0x000dad)

# 0x000dae: [8-bit] P1 Total Yellow Cards
# Note: Tracks the total number of yellow cards received by Player 1. Value is standard hex.
p1_total_yellow_cardsrnnote__tracks_the_total_number_of_yellow_ca = byte(0x000dae)

# 0x000daf: [8-bit] P1 Total Red Cards
# Note: Tracks the total number of red cards received by Player 1. Value is standard hex.
p1_total_red_cardsrnnote__tracks_the_total_number_of_red_cards_re = byte(0x000daf)

# 0x000db0: [8-bit] P1 Total Substitutions
# Note: Tracks the total number of substitutions made by Player 1. Value is standard hex.
p1_total_substitutionsrnnote__tracks_the_total_number_of_substitu = byte(0x000db0)

# 0x000de2: [8-bit] P1 Goalkeeper Skill Level
# Values:
# 0x00 = Very Weak
# 0x01 = Weak
# 0x02 = Normal
# 0x03 = Good
# 0x04 = Strong
p1_goalkeeper_skill_levelrnvalues_rn0x00 = byte(0x000de2)

# 0x000ea0: [8-bit] Team P2 ID
# # == Brazil Teams ==
# 0x00 = Cruzeiro
# 0x02 = Palmeiras
# 0x04 = Botafogo
# 0x06 = Parana
# 0x08 = Bragantino
# 0x0a = Guarani
# 0x0c = Gremio
# 0x0e = Juventude
# 0x10 = Flamengo
# 0x12 = Paysandu
# 0x14 = Corinthians
# 0x16 = Vitoria
# 0x18 = Fluminense
# 0x1a = Internacional
# 0x1c = Santos
# 0x1e = São Paulo
# 0x20 = Portuguesa
# 0x22 = Goias
# 0x24 = Criciuma
# 0x26 = Bahia
# 0x28 = Sport
# 0x2a = Vasco
# 0x2c = Atletico-MG
# 0x2e = União
# # == Europe Teams ==
# 0x30 = Ajax
# 0x32 = PSG
# 0x34 = Bayern
# 0x36 = Juventus
# 0x38 = Real Madrid
# 0x3a = Barcelona
# # == Libertadores Teams ==
# 0x3c = Boca Juniors
# 0x3e = River Plate
# 0x40 = Independiente
# 0x42 = Penarol
# 0x44 = Univ de Chile
# 0x46 = Colo Colo
# # == All-Star Teams ==
# 0x48 = Brasil
# 0x4a = Brasil 58
# 0x4c = Brasil 96
# 0x4e = Europa (Europe All-Stars)
# 0x50 = America A (America All-Stars A)
# 0x52 = America E (America All-Stars E)
team_p2_idrn = byte(0x000ea0)

# 0x000ea2: [8-bit] Player 2 Score
# Note: Holds the P2 score as a standard hex value
player_2_scorernnote__holds_the_p2_score_as_a_standard_hex_value = byte(0x000ea2)

# 0x000ea6: [8-bit] P2 Team Formation
# Values:
# 0x00 = 4-5-1
# 0x01 = 4-4-2
# 0x02 = 4-3-3
# 0x03 = 4-2-4
# 0x04 = 3-5-2
# 0x05 = 3-4-3
# 0x06 = 3-3-4
# 0x07 = 3-2-5
# 0x08 = 2-5-3
# 0x09 = 2-4-4
# 0x0a = 2-3-5
# 0x0b = 5-4-1
# 0x0c = 5-3-2
# 0x0d = 5-2-3
# 0x0e = 1-5-4
# 0x0f = 1-4-5
p2_team_formationrnvalues_rn0x00 = byte(0x000ea6)

# 0x000eaa: [8-bit] P2 Total Shots
# Note: Tracks the total number of shots taken by Player 2. Value is standard hex.
p2_total_shotsrnnote__tracks_the_total_number_of_shots_taken_by_p = byte(0x000eaa)

# 0x000eab: [8-bit] P2 Total Free Kicks
# Note: Tracks the total number of free kicks taken by Player 2. Value is standard hex.
p2_total_free_kicksrnnote__tracks_the_total_number_of_free_kicks_ = byte(0x000eab)

# 0x000eac: [8-bit] P2 Total Corner Kicks
# Note: Tracks the total number of corner kicks taken by Player 2. Value is standard hex.
p2_total_corner_kicksrnnote__tracks_the_total_number_of_corner_ki = byte(0x000eac)

# 0x000ead: [8-bit] P2 Total Penalties
# Note: Tracks the total number of penalties taken by Player 2. Value is standard hex.
p2_total_penaltiesrnnote__tracks_the_total_number_of_penalties_ta = byte(0x000ead)

# 0x000eae: [8-bit] P2 Total Yellow Cards
# Note: Tracks the total number of yellow cards received by Player 2. Value is standard hex.
p2_total_yellow_cardsrnnote__tracks_the_total_number_of_yellow_ca = byte(0x000eae)

# 0x000eaf: [8-bit] P2 Total Red Cards
# Note: Tracks the total number of red cards received by Player 2. Value is standard hex.
p2_total_red_cardsrnnote__tracks_the_total_number_of_red_cards_re = byte(0x000eaf)

# 0x000eb0: [8-bit] P2 Total Substitutions
# Note: Tracks the total number of substitutions made by Player 2. Value is standard hex.
p2_total_substitutionsrnnote__tracks_the_total_number_of_substitu = byte(0x000eb0)

# 0x000ee2: [8-bit] P2 Goalkeeper Skill Level
# Values:
# 0x00 = Very Weak
# 0x01 = Weak
# 0x02 = Normal
# 0x03 = Good
# 0x04 = Strong
p2_goalkeeper_skill_levelrnvalues_rn0x00 = byte(0x000ee2)

# 0x0014ee: [8-bit] Pause Menu
# Values:
# 0x00 = Resume
# 0x01 = Replay
pause_menurnvalues_rn0x00 = byte(0x0014ee)

# 0x00154e: [8-bit] Weather
# Values:
# 0x00 = Snow
# 0x01 = Good
# 0x02 = Rain
weatherrnvalues_rn0x00 = byte(0x00154e)

# 0x0016d2: [8-bit] Game Timer - Seconds
# Note: Stores the seconds portion of the game timer. The value is standard hexadecimal (Hex=Dec).
game_timer___secondsrnnote__stores_the_seconds_portion_of_the_gam = byte(0x0016d2)

# 0x0016d3: [8-bit] Game Timer - Minutes
# Note: Stores the minutes portion of the game timer. The value is standard hexadecimal.
game_timer___minutesrnnote__stores_the_minutes_portion_of_the_gam = byte(0x0016d3)

# 0x0016d4: [8-bit] Game Timer - Frames
# Note: Stores the frames (centiseconds) portion of the game timer.
game_timer___framesrnnote__stores_the_frames_portion_of_the_game_ = byte(0x0016d4)

# 0x0019ac: [8-bit] Coin Toss Call
# Note: Registers the players call before the toss.
# Values:
# 0x00 = Heads
# 0x01 = Tails
coin_toss_callrnnote__registers_the_players_call_before_the_toss = byte(0x0019ac)

# 0x0019b8: [8-bit] Coin Toss Result
# Note: The actual result of the referees coin toss.
# Values:
# 0x00 = Heads
# 0x01 = Tails
coin_toss_resultrnnote__the_actual_result_of_the_referees_coin_to = byte(0x0019b8)

# 0x0019c8: [8-bit] Kick-off/Side Selection
# Note: Active after the toss. If the player won, all 3 options are available.
# Values:
# 0x00 = Start with Ball
# 0x01 = Home Side (Left)
# 0x02 = Away Side (Right)
kick_off_side_selectionrnnote__active_after_the_toss = byte(0x0019c8)

# 0x001d08: [8-bit] Voice Line ID / Event Trigger
# Note: Indicates the sound/voice line currently being played.
# Values:
# 0x01 = Corner Kick
# 0x02 = Goal Kick
# 0x03 = Throw-in
# 0x04 = Free Kick
# 0x07 = Replay
# 0x08 = End of 1st Half
# 0x09 = Extra Time
# 0x0b = Player Down
# 0x0d = Long Pass
# 0x11 = Bicycle Kick
# 0x13 = You Lose!
# 0x14 = You Win!
# 0x27 = Kick-off / Start
# 0x28 = Foul
# 0x29 = Yellow Card
# 0x2c = Normal Shot
# 0x2d = Very Strong Shot
# 0x32 = Own Goal
# 0x34 = Strong Shot
# 0x38 = Goalkeeper Save
# 0x40 = Tackle
# 0x43 = Full Time / Game End
# 0x46 = Goal
# 0x48 = Barking (Dog Referee Active)
voice_line_id___event_triggerrnnote__indicates_the_sound_voice_li = byte(0x001d08)

# 0x001e5e: [8-bit] Main Menu Option
# Note: Stores the currently selected main game mode.
# Values:
# 0x00 = Quick Match
# 0x01 = Championship
# 0x02 = Brazil Cup
# 0x03 = Password
# 0x04 = Scenarios
# 0x05 = Penalties
# 0x06 = Training
# 0x07 = Options
main_menu_optionrnnote__stores_the_currently_selected_main_game_m = byte(0x001e5e)

# 0x001e68: [8-bit] P1 Number of Players
# Values:
# 0x06 = 7
# 0x07 = 8
# 0x08 = 9
# 0x09 = 10
# 0x0a = 11
p1_number_of_playersrnvalues_rn0x06 = byte(0x001e68)

# 0x001e6a: [8-bit] P2 Number of Players
# Values:
# 0x06 = 7
# 0x07 = 8
# 0x08 = 9
# 0x09 = 10
# 0x0a = 11
p2_number_of_playersrnvalues_rn0x06 = byte(0x001e6a)

# 0x001f88: [8-bit] Match Duration
# Values:
# 0x00 = 3 Minutes
# 0x01 = 5 Minutes
# 0x02 = 7 Minutes
match_durationrnvalues_rn0x00 = byte(0x001f88)

# 0x001f90: [8-bit] Sound Setting
# Values:
# 0x00 = Stereo
# 0x01 = Mono
sound_settingrnvalues_rn0x00 = byte(0x001f90)

# 0x001f92: [8-bit] Offside Enabled
# Values:
# 0x00 = Yes
# 0x01 = No
offside_enabledrnvalues_rn0x00 = byte(0x001f92)

# 0x001f98: [8-bit] Fouls Enabled
# Values:
# 0x00 = Yes
# 0x01 = No
fouls_enabledrnvalues_rn0x00 = byte(0x001f98)

# 0x001f9a: [8-bit] Bookings Enabled
# Values:
# 0x00 = Yes
# 0x01 = No
bookings_enabledrnvalues_rn0x00 = byte(0x001f9a)

# 0x001f9c: [8-bit] Game Difficulty
# Values:
# 0x00 = Level 1
# 0x01 = Level 2
# 0x02 = Level 3
# 0x03 = Level 4
# 0x04 = Level 5
game_difficultyrnvalues_rn0x00 = byte(0x001f9c)

# 0x001fa0: [8-bit] Referee Selection
# Values:
# 0x00 = Carlos
# 0x01 = Heinz
# 0x02 = Hasegaa
# 0x03 = Random
referee_selectionrnvalues_rn0x00 = byte(0x001fa0)

# 0x001fa2: [8-bit] Stadiums
# Values:
# 0x00 = Flamengo
# 0x01 = São Paulo
# 0x02 = Vasco
# 0x03 = Bahia
# 0x04 = Palmeiras
# 0x05 = Gremio
# 0x06 = Fluminense
# 0x07 = Botafogo
stadiumsrnvalues_rn0x00 = byte(0x001fa2)

# 0x001fe0: [8-bit] Extra Time Enabled
# Values:
# 0x00 = No
# 0x01 = Yes
extra_time_enabledrnvalues_rn0x00 = byte(0x001fe0)

# 0x00d442: [8-bit] Player 1 Penalty Score
# Note: Holds the P1 score during a penalty shootout. Value is standard hex.
player_1_penalty_scorernnote__holds_the_p1_score_during_a_penalty = byte(0x00d442)

# 0x00d443: [8-bit] Player 2 Penalty Score
# Note: Holds the P2 score during a penalty shootout. Value is standard hex.
player_2_penalty_scorernnote__holds_the_p2_score_during_a_penalty = byte(0x00d443)

# 0x00d474: [8-bit] P1 Player Condition
# Values:
# 0x00 = Terrible (Purple/Down)
# 0x01 = Bad (Blue/Down-Right)
# 0x02 = Average (Green/Right)
# 0x03 = Good (Orange/Up-Right)
# 0x04 = Excellent (Red/Up)
# 0x05 = Random
p1_player_conditionrnvalues_rn0x00 = byte(0x00d474)

# 0x00d476: [8-bit] P2 Player Condition
# Values:
# 0x00 = Terrible (Purple/Down)
# 0x01 = Bad (Blue/Down-Right)
# 0x02 = Average (Green/Right)
# 0x03 = Good (Orange/Up-Right)
# 0x04 = Excellent (Red/Up)
# 0x05 = Random
p2_player_conditionrnvalues_rn0x00 = byte(0x00d476)

# 0x00d706: [8-bit] Scenario Modes Won (9-12)
# Note: This is a bitfield. Each bit corresponds to a completed scenario.
# Values:
# Bit 3 = Scenario 9 Won (0x08)
# Bit 2 = Scenario 10 Won (0x04)
# Bit 1 = Scenario 11 Won (0x02)
# Bit 0 = Scenario 12 Won (0x01)
scenario_modes_won_rnnote__this_is_a_bitfield = byte(0x00d706)

# 0x00d88d: [8-bit] Scenario Modes Won (1-8)
# Note: This is a bitfield. Each bit corresponds to a completed scenario.
# Values:
# Bit 7 = Scenario 1 Won (0x80)
# Bit 6 = Scenario 2 Won (0x40)
# Bit 5 = Scenario 3 Won (0x20)
# Bit 4 = Scenario 4 Won (0x10)
# Bit 3 = Scenario 5 Won (0x08)
# Bit 2 = Scenario 6 Won (0x04)
# Bit 1 = Scenario 7 Won (0x02)
# Bit 0 = Scenario 8 Won (0x01)
scenario_modes_won_rnnote__this_is_a_bitfield_0x00d88d = byte(0x00d88d)

# 0x00d88e: [8-bit] Scenario 1 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 1. Starts at 0x00.
scenario_1_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d88e)

# 0x00d88f: [8-bit] Scenario 2 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 2.
scenario_2_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d88f)

# 0x00d890: [8-bit] Scenario 3 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 3.
scenario_3_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d890)

# 0x00d891: [8-bit] Scenario 4 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 4.
scenario_4_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d891)

# 0x00d892: [8-bit] Scenario 5 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 5.
scenario_5_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d892)

# 0x00d893: [8-bit] Scenario 6 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 6.
scenario_6_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d893)

# 0x00d894: [8-bit] Scenario 7 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 7.
scenario_7_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d894)

# 0x00d895: [8-bit] Scenario 8 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 8.
scenario_8_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d895)

# 0x00d896: [8-bit] Scenario 9 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 9.
scenario_9_attempt_countrnnote__tracks_the_number_of_times_the_pl = byte(0x00d896)

# 0x00d897: [8-bit] Scenario 10 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 10.
scenario_10_attempt_countrnnote__tracks_the_number_of_times_the_p = byte(0x00d897)

# 0x00d898: [8-bit] Scenario 11 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 11.
scenario_11_attempt_countrnnote__tracks_the_number_of_times_the_p = byte(0x00d898)

# 0x00d899: [8-bit] Scenario 12 Attempt Count
# Note: Tracks the number of times the player has attempted Scenario 12.
scenario_12_attempt_countrnnote__tracks_the_number_of_times_the_p = byte(0x00d899)

# 0x00e528: [8-bit] Challenge Mode Active
# Note: Flag that indicates if the specific Challenge Mode logic is running.
# Values:
# 0x00 = Inactive
# 0x01 = Active
challenge_mode_activernnote__flag_that_indicates_if_the_specific_ = byte(0x00e528)

# 0x00e52a: [8-bit] Selected Scenario
# Note: Stores the currently selected scenario (01-12).
# Values:
# 0x00 = Scenario 01
# 0x01 = Scenario 02
# 0x02 = Scenario 03
# 0x03 = Scenario 04
# 0x04 = Scenario 05
# 0x05 = Scenario 06
# 0x06 = Scenario 07
# 0x07 = Scenario 08
# 0x08 = Scenario 09
# 0x09 = Scenario 10
# 0x0a = Scenario 11
# 0x0b = Scenario 12
selected_scenariornnote__stores_the_currently_selected_scenario = byte(0x00e52a)

# 0x00e52c: [8-bit] Challenge Mode Type
# Note: Determines which mini-game is currently selected/active in Challenge Mode.
# Values:
# 0x00 = Dribble Challenge
# 0x01 = Pass Challenge
# 0x02 = Shoot Challenge
# 0x03 = Defense Challenge
# 0x04 = Corner Kick Challenge
# 0x05 = Free Kick Challenge
challenge_mode_typernnote__determines_which_mini_game_is_currentl = byte(0x00e52c)

# 0x00e52e: [8-bit] Challenge Mode Level
# Note: Selects the difficulty level for the chosen challenge.
# Values:
# 0x00 = Level 1
# 0x01 = Level 2
# 0x02 = Level 3
# 0x03 = Level 4
challenge_mode_levelrnnote__selects_the_difficulty_level_for_the_ = byte(0x00e52e)

# 0x00e534: [8-bit] Training Mode Active
# Note: Flag that indicates if the specific Training Mode logic is running.
# Values:
# 0x00 = Inactive
# 0x01 = Active
training_mode_activernnote__flag_that_indicates_if_the_specific_t = byte(0x00e534)
