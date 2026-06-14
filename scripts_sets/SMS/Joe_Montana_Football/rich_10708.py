from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS
rp.add_lookup("Team_ID", {
    0: "San Francisco", 1: "Atlanta", 2: "LA Rams", 3: "New Orleans", 
    4: "Chicago", 5: "Detroit", 6: "Green Bay", 7: "Minnesota", 
    8: "Tampa Bay", 9: "Dallas", 10: "NY Giants", 11: "Philadelphia", 
    12: "Phoenix", 13: "Washington", 14: "Cincinnati", 15: "Cleveland", 
    16: "Houston", 17: "Pittsburgh", 18: "Denver", 19: "Kansas City", 
    20: "LA Raiders", 21: "San Diego", 22: "Seattle", 23: "Buffalo", 
    24: "Indianapolis", 25: "Miami", 26: "New England", 27: "NY Jets", 
    255: "Select team"
}, default="")

rp.add_lookup("Difficulty", {
    0: "Beginner", 1: "Normal", 2: "Professional"
}, default="")

rp.add_lookup("Quarter", {
    1: "1st Quarter", 2: "2nd Quarter", 3: "3rd Quarter", 4: "4th Quarter"
}, default="")

rp.add_lookup("Coin", {
    0: "Heads", 255: "Tails"
}, default="")

rp.add_lookup("CoinResult", {
    0: "Kicks Off", 1: "Receives"
}, default="")

rp.add_lookup("Strategy1", {
    0: "Rooter Right", 1: "Double Cross", 2: "Seam Splitter", 5: "Clear out",
    6: "Curl the flash", 7: "Burn Neon", 8: "Lotsa Curls", 9: "Zucchini Bit",
    10: "Hot Crossed Buns", 11: "Rhino's Charge", 12: "U.F.O", 13: "R.I.P",
    15: "Off tackle", 16: "Orville's Right", 17: "Hilbur's Left", 18: "Keeper",
    19: "Big End Around"
}, default="")

rp.add_lookup("Strategy2", {
    0: "Goal Line", 1: "Goal Shift", 2: "Sub-Dural Hematoma", 
    3: "Odd Jam", 4: "Odd Zone", 5: "Prevent"
}, default="")

rp.add_lookup("Action", {
    16: "Offense", 254: "Defense"
}, default="")

# 2. FORMATS
rp.add_format("Clock", "SECS")

# 3. ALIASES DE MEMÓRIA
mem_state    = byte(0x0891)
mem_action   = byte(0x03db)

mem_p1_team  = byte(0x08be)
mem_p2_team  = byte(0x08bf)

# Nota: O jogo salva o placar e certas infos em formato BCD (Hexadecimal lido como decimal)
mem_p1_score = byte(0x0866).bcd()
mem_p2_score = byte(0x0868).bcd()

mem_quarter  = byte(0x0872)
mem_diff     = byte(0x08d5)

mem_down     = byte(0x083b).bcd()
mem_ball_on  = byte(0x083e).bcd()

mem_play_off = byte(0x088b)
mem_play_def = byte(0x088c)

mem_coin     = byte(0x08d6)
mem_coin_res = byte(0x1f3a)

# Cálculo do Relógio
mem_clock_m  = byte(0x0886).bcd()
mem_clock_s  = byte(0x0885).bcd()
val_clock    = group(add_source(mem_clock_m * 60), measured(mem_clock_s))

# 4. DISPLAYS
rp.add_display(
    [mem_state == 1],
    f"🏈 {RichPresence.lookup('Team_ID', mem_p1_team)} {RichPresence.value(mem_p1_score)} - {RichPresence.value(mem_p2_score)} {RichPresence.lookup('Team_ID', mem_p2_team)} | "
    f"⏱️ {RichPresence.lookup('Quarter', mem_quarter)} ({RichPresence.value(val_clock, 'Clock')}) | "
    f"📊 {RichPresence.lookup('Difficulty', mem_diff)}"
)

rp.add_display(
    [mem_action == 16, mem_state == 2],
    f"🏈 {RichPresence.lookup('Team_ID', mem_p1_team)} {RichPresence.value(mem_p1_score)} - {RichPresence.value(mem_p2_score)} {RichPresence.lookup('Team_ID', mem_p2_team)} | "
    f"Down: {RichPresence.value(mem_down)} | Ball on: {RichPresence.value(mem_ball_on)} | "
    f"📋 {RichPresence.lookup('Action', mem_action)} Play: {RichPresence.lookup('Strategy1', mem_play_off)} | "
    f"⏱️ {RichPresence.lookup('Quarter', mem_quarter)}"
)

rp.add_display(
    [mem_action == 254, mem_state == 2],
    f"🏈 {RichPresence.lookup('Team_ID', mem_p1_team)} {RichPresence.value(mem_p1_score)} - {RichPresence.value(mem_p2_score)} {RichPresence.lookup('Team_ID', mem_p2_team)} | "
    f"Down: {RichPresence.value(mem_down)} | Ball on: {RichPresence.value(mem_ball_on)} | "
    f"🛡️ {RichPresence.lookup('Action', mem_action)} Play: {RichPresence.lookup('Strategy2', mem_play_def)} | "
    f"⏱️ {RichPresence.lookup('Quarter', mem_quarter)}"
)

rp.add_display(
    [mem_state == 4],
    f"📋 Team Selection: {RichPresence.lookup('Team_ID', mem_p1_team)} vs {RichPresence.lookup('Team_ID', mem_p2_team)} | "
    f"📊 {RichPresence.lookup('Difficulty', mem_diff)}"
)

rp.add_display(
    [mem_state == 8],
    "📺 Title Screen"
)

rp.add_display(
    [mem_action == 16, mem_state == 16],
    f"🎉 TOUCHDOWN {RichPresence.lookup('Team_ID', mem_p1_team)}! 🏈 | "
    f"Score: {RichPresence.value(mem_p1_score)} - {RichPresence.value(mem_p2_score)} | "
    f"⏱️ {RichPresence.lookup('Quarter', mem_quarter)}"
)

rp.add_display(
    [mem_action == 254, mem_state == 16],
    f"🎉 TOUCHDOWN {RichPresence.lookup('Team_ID', mem_p2_team)}! 🏈 | "
    f"Score: {RichPresence.value(mem_p1_score)} - {RichPresence.value(mem_p2_score)} | "
    f"⏱️ {RichPresence.lookup('Quarter', mem_quarter)}"
)

rp.add_display(
    [mem_state == 64],
    f"🪙 Coin Toss: {RichPresence.lookup('Coin', mem_coin)} - {RichPresence.lookup('CoinResult', mem_coin_res)} | "
    f"📊 {RichPresence.lookup('Difficulty', mem_diff)}"
)

# Fallback
rp.add_display(None, "Playing Joe Montana Football")

print(rp)