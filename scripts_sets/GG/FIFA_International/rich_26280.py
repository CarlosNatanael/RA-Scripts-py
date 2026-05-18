from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS (Dicionários)
rp.add_lookup("Period", {
    0: "1st Half", 1: "2nd Half", 2: "Extra Time"
}, default="")

rp.add_lookup("Cursor", {
    0: "Exhibition", 1: "Tournament", 2: "Playoffs", 3: "League", 4: "Restore", 5: "Options"
}, default="Unknown")

rp.add_lookup("Language", {
    0: "English", 1: "French", 2: "Spanish", 3: "German"
}, default="English")

rp.add_lookup("Competition", {
    0: "Exhibition Match", 1: "League Match", 2: "Playoffs Match", 3: "Tournament Match", 4: "Round of 16 Match"
}, default="Match")

# Lista de Times (Tournament / League - TeamsC)
rp.add_lookup("TeamsC", {
    0: "Algeria", 1: "Argentina", 2: "Australia", 3: "Austria", 4: "Belgium", 5: "Bolivia", 6: "Brazil", 7: "Bulgaria", 8: "Cameroon", 9: "Canada",
    10: "Chile", 11: "China", 12: "Colombia", 13: "Czech Republic", 14: "Denmark", 15: "England", 16: "France", 17: "Germany", 18: "Greece", 19: "Netherlands",
    20: "Hong Kong", 21: "Hungary", 22: "Iraq", 23: "Israel", 24: "Italy", 25: "Ivory Coast", 26: "Japan", 27: "Luxembourg", 28: "Mexico", 29: "Morocco",
    30: "New Zealand", 31: "Nigeria", 32: "Northern Ireland", 33: "Norway", 34: "Poland", 35: "Portugal", 36: "Qatar", 37: "Republic of Ireland", 38: "Romania", 39: "Russia",
    40: "Saudi Arabia", 41: "Scotland", 42: "South Korea", 43: "Spain", 44: "Sweden", 45: "Switzerland", 46: "Turkey", 47: "USA", 48: "Ukraine", 49: "Uruguay", 50: "Wales", 51: "EA All Stars"
}, default="Unknown Team")

# Lista de Times (Exhibition - Teams)
rp.add_lookup("Teams", {
    0: "Algeria", 1: "Argentina", 2: "Australia", 3: "Austria", 4: "Belgium", 5: "Bolivia", 6: "Brazil", 7: "Bulgaria", 8: "Cameroon", 9: "Canada",
    10: "Chile", 11: "China", 12: "Colombia", 13: "Czech Republic", 14: "Denmark", 15: "England", 16: "France", 17: "Germany", 18: "Greece", 19: "Hong Kong",
    20: "Hungary", 21: "Iraq", 22: "Israel", 23: "Italy", 24: "Ivory Coast", 25: "Japan", 26: "Luxembourg", 27: "Mexico", 28: "Morocco", 29: "Netherlands",
    30: "New Zealand", 31: "Nigeria", 32: "Northern Ireland", 33: "Norway", 34: "Poland", 35: "Portugal", 36: "Qatar", 37: "Republic of Ireland", 38: "Romania", 39: "Russia",
    40: "Saudi Arabia", 41: "Scotland", 42: "South Korea", 43: "Spain", 44: "Sweden", 45: "Switzerland", 46: "Turkey", 47: "USA", 48: "Ukraine", 49: "Uruguay", 50: "Wales", 51: "EA All Stars"
}, default="Unknown Team")


# 2. ALIASES DE MEMÓRIA
mem_comp_mode   = byte(0x0c9a)
mem_player_team = byte(0x0b0f)
mem_period      = byte(0x0af0)
mem_team_c_h    = byte(0x0b0d)
mem_team_c_a    = byte(0x0b0e)
mem_team_ex_h   = byte(0x0b11)
mem_team_ex_a   = byte(0x0b12)
mem_score_h     = byte(0x0d85)
mem_score_a     = byte(0x0d93)
mem_clock_min   = byte(0x0ad4)
mem_clock_sec   = byte(0x0ad5)
mem_scr_timer   = byte(0x0c6b)
mem_scr_trans   = byte(0x0c6a)
mem_game_active = byte(0x0bb3)
mem_cursor      = byte(0x0b30)
mem_lang        = byte(0x0b3b)

# 3. DISPLAYS
# Menus Básicos
rp.add_display([mem_comp_mode == 255], "🔑 Entering a Password")
rp.add_display(
    [mem_player_team == 255],
    f"📺 Watching a Demo | {RichPresence.lookup('Period', mem_period)} | "
    f"{RichPresence.lookup('TeamsC', mem_team_c_h)} {RichPresence.value(mem_score_h)}-{RichPresence.value(mem_score_a)} {RichPresence.lookup('TeamsC', mem_team_c_a)} | "
    f"⌚ Time: {RichPresence.value(mem_clock_min)}:{RichPresence.value(mem_clock_sec)}"
)
rp.add_display([mem_scr_timer == 0, mem_scr_trans == 1], "🎬 Watching the Intro")

# Loop do Menu da Liga
for i in range(24):
    base_addr = 0x0c9b + (i * 8)
    mem_pts     = byte(base_addr)
    mem_team_id = byte(base_addr + 1)
    mem_matches = byte(base_addr + 2)
    mem_wins    = byte(base_addr + 3)
    mem_draws   = byte(base_addr + 4)
    
    # Cálculo das Derrotas injetado como string bruta
    math_losses = f"{mem_matches.render()}-{mem_wins.render()}"
    
    rp.add_display(
        [mem_scr_timer <= 4, mem_comp_mode == 1, mem_game_active == 0, mem_player_team == mem_team_id],
        f"📋 League Menu | Managing {RichPresence.lookup('TeamsC', mem_player_team)} | "
        f"G:{RichPresence.value(mem_matches)} W:{RichPresence.value(mem_wins)} L:{RichPresence.value(math_losses)} "
        f"D:{RichPresence.value(mem_draws)} Pts:{RichPresence.value(mem_pts)}"
    )

# Menu dos Playoffs
rp.add_display(
    [mem_scr_timer <= 4, mem_comp_mode == 2, mem_game_active == 0],
    f"📋 Playoffs Menu | Managing {RichPresence.lookup('TeamsC', mem_player_team)}"
)

# Loop do Menu do Torneio
for i in range(24):
    base_addr = 0x0c9b + (i * 8)
    mem_pts     = byte(base_addr)
    mem_team_id = byte(base_addr + 1)
    mem_matches = byte(base_addr + 2)
    mem_wins    = byte(base_addr + 3)
    mem_draws   = byte(base_addr + 4)
    
    math_losses = f"{mem_matches.render()}-{mem_wins.render()}" 
    
    rp.add_display(
        [mem_scr_timer <= 4, mem_comp_mode == 3, mem_game_active == 0, mem_player_team == mem_team_id],
        f"📋 Tournament Menu | Managing {RichPresence.lookup('TeamsC', mem_player_team)} | "
        f"G:{RichPresence.value(mem_matches)} W:{RichPresence.value(mem_wins)} L:{RichPresence.value(math_losses)} "
        f"D:{RichPresence.value(mem_draws)} Pts:{RichPresence.value(mem_pts)}"
    )

# Menu Round of 16 e Setup de Jogo
rp.add_display(
    [mem_scr_timer <= 4, mem_comp_mode == 4, mem_game_active == 0],
    f"📋 Round of 16 Menu | Managing {RichPresence.lookup('TeamsC', mem_player_team)}"
)
rp.add_display(
    [mem_scr_timer <= 4, mem_game_active == 0],
    f"⚙️ Game Setup: Selecting {RichPresence.lookup('Cursor', mem_cursor)} | Language: {RichPresence.lookup('Language', mem_lang)}"
)

# Partidas (In-Game)
rp.add_display(
    [mem_comp_mode == 0, mem_game_active == 1],
    f"⚽ {RichPresence.lookup('Competition', mem_comp_mode)} | {RichPresence.lookup('Period', mem_period)} | "
    f"{RichPresence.lookup('Teams', mem_team_ex_h)} {RichPresence.value(mem_score_h)}-{RichPresence.value(mem_score_a)} {RichPresence.lookup('Teams', mem_team_ex_a)} | "
    f"⌚ Time: {RichPresence.value(mem_clock_min)}:{RichPresence.value(mem_clock_sec)}"
)

for mode_id in range(1, 5):
    rp.add_display(
        [mem_comp_mode == mode_id, mem_game_active == 1],
        f"⚽ {RichPresence.lookup('Competition', mem_comp_mode)} | {RichPresence.lookup('Period', mem_period)} | "
        f"{RichPresence.lookup('TeamsC', mem_team_c_h)} {RichPresence.value(mem_score_h)}-{RichPresence.value(mem_score_a)} {RichPresence.lookup('TeamsC', mem_team_c_a)} | "
        f"⌚ Time: {RichPresence.value(mem_clock_min)}:{RichPresence.value(mem_clock_sec)}"
    )

# Fallback (Menu / Default)
rp.add_display([], "Playing FIFA International Soccer")
print(rp)