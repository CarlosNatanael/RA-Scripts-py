from pycheevos.core.helpers import byte, word
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

rp.add_format("Value", "VALUE")

rp.add_lookup("RegionUS", {0x55: "🇺🇸"}, default="")
rp.add_lookup("RegionEU", {0x55: "🇪🇺"}, default="")
rp.add_lookup("RegionJP", {0x55: "🇯🇵"}, default="")

rp.add_lookup("Fighter", {
    0x00: "Tanaka", 0x01: "Ryoko", 0x02: "Red", 0x03: "B.T.",
    0x04: "Puma", 0x05: "Prince", 0x06: "Misha", 0x07: "Silver Man",
    0x08: "Gio", 0x09: "Kojiromaru", 0x0a: "Spice", 0x0b: "Asteka",
    0x0c: "Mr. Crown"
}, default="Fighter")

rp.add_lookup("WeightClass", {0x00: "Heavyweight", 0x01: "Middleweight", 0x02: "Lightweight"})

rp.add_lookup("Difficulty", {0x64: " Very Hard", 0x4b: " Hard", 0x32: " Normal", 0x19: " Easy"})

rp.add_lookup("Championship", {
    0x00: "Local Heavyweight", 0x01: "Local Middleweight", 0x02: "Local Lightweight",
    0x03: "National Heavyweight", 0x04: "National Middleweight", 0x05: "National Lightweight",
    0x06: "World Heavyweight", 0x07: "World Middleweight", 0x08: "World Lightweight",
    0x09: "Secret Heavyweight", 0x0a: "Secret Middleweight", 0x0b: "Secret Lightweight"
})

rp.add_lookup("RankingPos", {
    0x01: "Rank #1 (Contender)", 0x02: "Rank #2", 0x03: "Rank #3",
    0x04: "Rank #4", 0x05: "Rank #5", 0x06: "Rank #6", 0x07: "Rank #7"
})

rp.add_lookup("ScreenID", {
    0x06: "Booting up the game",
    0x07: "Watching the Nekogum logo",
    0x08: "Watching the A1 Games logo",
    0x09: "At the Title Screen"
}, default="Playing the game")

rp.add_lookup("Round", {0x04: "4s", 0x06: "6s", 0x08: "8s", 0x0a: "10s", 0x0c: "12s"})

rp.add_lookup("RoundNum", {
    0x01: "Round 1", 0x02: "Round 2", 0x03: "Round 3", 0x04: "Round 4",
    0x05: "Round 5", 0x06: "Round 6", 0x07: "Round 7", 0x08: "Round 8",
    0x09: "Round 9", 0x0a: "Round 10", 0x0b: "Round 11", 0x0c: "Round 12"
}, default="Round")

rp.add_lookup("Rematch", {0x00: "No", 0x01: "1", 0x02: "2"}, default="")

mem_screen = byte(0x1feff0)
mem_mode   = byte(0x1fef74)

# Macros de Bandeiras (Regiões)
reg_us = rp.lookup("RegionUS", byte(0x0ad539))
reg_eu = rp.lookup("RegionEU", byte(0x0ad01b))
reg_jp = rp.lookup("RegionJP", byte(0x0a7781))

flags_us_eu = f"{reg_us}{reg_eu}"
flags_all   = f"{reg_us}{reg_eu}{reg_jp}"

# Variáveis em Jogo
val_screen = rp.lookup("ScreenID", mem_screen)
p1_fighter = rp.lookup("Fighter", byte(0x1fedb0))
p2_fighter = rp.lookup("Fighter", byte(0x1fede8))
champ      = rp.lookup("Championship", byte(0x1fef70))
round_num = "@RoundNum(I:0xW1fe480_M:0xH002c)"
diff       = rp.lookup("Difficulty", word(0x1fe564))

# Setup e Rankings
p1_sel     = rp.lookup("Fighter", byte(0x1fef7c))
p2_sel     = rp.lookup("Fighter", byte(0x1dc062))
rank_char  = rp.lookup("Fighter", byte(0x1fef66))
rank_pos   = rp.lookup("RankingPos", byte(0x1fef68))
rank_champ = rp.lookup("Championship", byte(0x1fef70))
bio_char   = rp.lookup("Fighter", byte(0x1fef7a))
scout_opp  = rp.lookup("Fighter", byte(0x1db990))

# Record Viewer
rec_char    = rp.lookup("Fighter", word(0x1feb60))
val_matches = rp.value(word(0x1feb3c), "Value")
val_wins    = rp.value(word(0x1feb3e), "Value")
val_kos     = rp.value(word(0x1feb42), "Value")

val_trophies = "@Value(A:0x1feb4a_A:0x1feb4c_A:0x1feb4e_A:0x1feb52_A:0x1feb54_A:0x1feb56_A:0x1feb5a_A:0x1feb5c_M:0x1feb5e)"

# 1. Telas Iniciais (IDs 6 a 9)
for sid in [6, 7, 8, 9]:
    rp.add_display(mem_screen == sid, f"{flags_all}: {val_screen}")

# 2. Championship
rp.add_display([mem_screen == 14, mem_mode == 0], f"{flags_us_eu}: Championship: {p1_fighter} vs {p2_fighter} | {champ} | {round_num}")
rp.add_display([mem_screen == 13, mem_mode == 0], f"{reg_jp}: Championship: {p1_fighter} vs {p2_fighter} | {champ} | {round_num}")

# 3. VS Mode
rp.add_display([mem_screen == 14, mem_mode == 2], f"{flags_us_eu}: Brawling in the ring VS Mode: {p1_fighter} vs {p2_fighter} | {round_num} | {diff}")
rp.add_display([mem_screen == 13, mem_mode == 2], f"{reg_jp}: Brawling in the ring VS Mode: {p1_fighter} vs {p2_fighter} | {round_num} | {diff}")
rp.add_display([mem_screen == 10, mem_mode == 2], f"{flags_us_eu}: Setting up a VS Match: Selecting {p1_sel} vs {p2_sel}")
rp.add_display([mem_screen ==  9, mem_mode == 2], f"{reg_jp}: Setting up a VS Match: Selecting {p1_sel} vs {p2_sel}")

# 4. Rankings
rp.add_display([mem_screen == 10, mem_mode == 0], f"{flags_us_eu}: Checking the Rankings: {rank_char} is {rank_pos} in {rank_champ}")
rp.add_display([mem_screen ==  9, mem_mode == 0], f"{reg_jp}: Checking the Rankings: {rank_char} is {rank_pos} in {rank_champ}")

# 5. Bio Notes
rp.add_display(mem_mode == 4, f"{flags_all}: Reading the Bio Notes: {bio_char}")

# 6. O LOOP MÁGICO DO SCOUT MODE
mem_scout_opp = byte(0x1db990)
for opp_id in range(13):
    rematch_val = rp.lookup("Rematch", byte(0x1fe6d0 + opp_id))
    rp.add_display([mem_screen == 10, mem_mode == 1, mem_scout_opp == opp_id], 
                   f"{flags_us_eu}: Preparing for Scout Mode: Face {scout_opp} [Rematch: {rematch_val}]")
    rp.add_display([mem_screen ==  9, mem_mode == 1, mem_scout_opp == opp_id], 
                   f"{reg_jp}: Preparing for Scout Mode: Face {scout_opp} [Rematch: {rematch_val}]")

# 7. Scout Mode In-Game
rp.add_display([mem_screen == 14, mem_mode == 1], f"{flags_us_eu}: Brawling in the ring Scout Mode: {p1_fighter} vs {p2_fighter} | {round_num}")
rp.add_display([mem_screen == 13, mem_mode == 1], f"{reg_jp}: Brawling in the ring Scout Mode: {p1_fighter} vs {p2_fighter} | {round_num}")

# 8. Record Viewer & Save Data
rp.add_display(mem_mode == 3, f"{flags_all}: Viewing Records: {rec_char} | Matches: {val_matches} | Wins: {val_wins} | KOs: {val_kos} | 🏆: {val_trophies}")
rp.add_display(mem_mode == 5, f"{flags_all}: Managing Save Data")

# 9. Fallback Padrão
rp.add_display(None, "Playing Boxing")
print(rp)