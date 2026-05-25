from pycheevos.core.helpers import word
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS
rp.add_lookup("Mode", {
    0: "🆚 Vs Mode",
    1: "🏆 Tournament",
    3: "Demo Mode"
}, default="")

rp.add_lookup("Teams", {
    0: "Japan", 1: "USA", 2: "USSR", 3: "China", 
    5: "Italy", 6: "France", 7: "Germany", 8: "Great Britain", 
    9: "Spain", 10: "Sweden", 11: "Norway", 12: "Denmark", 
    13: "Brazil", 15: "Cuba"
}, default="Unknown Team")

# 2. ALIASES DE MEMÓRIA
mem_state       = word(0x000022)
mem_mode        = word(0x00002e)
mem_score_p1    = word(0x00168e)
mem_score_p2    = word(0x001690)
mem_team1       = word(0x0019c0)
mem_team2       = word(0x0019c2)
mem_score_match = word(0x0023d2)
mem_score_final = word(0x0023f2)

# 3. DISPLAYS
rp.add_display([mem_mode == 3], "Watching Demo")

rp.add_display([mem_state == 0], "Booting the game")

rp.add_display([mem_state == 3], "At the Title Screen / Insert Coin")

rp.add_display(
    [mem_state == 4],
    f"Selecting Team: {RichPresence.lookup('Teams', mem_team1)} | {RichPresence.lookup('Mode', mem_mode)}"
)

rp.add_display(
    [mem_state == 8],
    f"Arcade Cleared! | 🏐 {RichPresence.lookup('Teams', mem_team1)} | Final Score: {RichPresence.value(mem_score_final)}"
)

rp.add_display(
    [mem_state == 9],
    f"Game Over | 🏐 {RichPresence.lookup('Teams', mem_team1)} | Score: {RichPresence.value(mem_score_final)}"
)

rp.add_display(
    [mem_state == 5],
    f"{RichPresence.lookup('Mode', mem_mode)} | Matchup: {RichPresence.lookup('Teams', mem_team1)} vs {RichPresence.lookup('Teams', mem_team2)} | Score: {RichPresence.value(mem_score_match)}"
)

# Fallback / Gameplay Padrão
rp.add_display(
    [],
    f"{RichPresence.lookup('Mode', mem_mode)} | {RichPresence.lookup('Teams', mem_team1)} [{RichPresence.value(mem_score_p1)}] - [{RichPresence.value(mem_score_p2)}] {RichPresence.lookup('Teams', mem_team2)} | Score: {RichPresence.value(mem_score_match)}"
)

print(rp)