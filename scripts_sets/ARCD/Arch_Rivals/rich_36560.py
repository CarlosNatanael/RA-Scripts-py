from pycheevos.core.helpers import byte
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()


# 1. LOOKUPS
rp.add_lookup("ID_pers", {
    0: "Tyrone", 1: "Vinnie", 2: "Hammer", 
    3: "Moose", 4: "Lewis", 5: "Blade", 
    6: "Mohawk", 7: "Reggie"
}, default="Unknown")

rp.add_lookup("Controller", {
    0: "[CPU]", 2: "[P2]"
}, default="[?]")

rp.add_lookup("Matchup", {
    0: "Los Angeles vs Chicago",
    1: "Brawl State vs Natural High",
    2: "Chicago vs Brawl State",
    3: "Natural High vs Los Angeles",
    4: "Natural High vs Chicago",
    5: "Brawl State vs Los Angeles"
})

rp.add_lookup("Period", {
    1: "1st Quarter", 2: "2nd Quarter", 
    3: "3rd Quarter", 4: "4th Quarter", 
    8: "Sudden Death 💀"
}, default="Unknown")


# 2. ALIASES DE MEMÓRIA
mem_period      = byte(0x01e2)
mem_matchup     = byte(0x0371)
mem_p1_char1    = byte(0x0377)
mem_p1_char2    = byte(0x0587)
mem_p1_score    = byte(0x0216)
mem_p2_ctrl     = byte(0x0795)
mem_p2_score    = byte(0x021a)
mem_p2_char1    = byte(0x0797)
mem_p2_char2    = byte(0x09a7)
mem_coins       = byte(0x1e16)


# 3. DISPLAYS

rp.add_display(
    [mem_period == 0],
    f"📋 Team Select: {RichPresence.lookup('Matchup', mem_matchup)} [P1: {RichPresence.lookup('ID_pers', mem_p1_char1)}] | "
    f"🪙 {RichPresence.value(mem_coins)} Coins"
)
rp.add_display(
    [mem_period >= 1],
    f"🏀 [P1] {RichPresence.lookup('ID_pers', mem_p1_char1)} & {RichPresence.lookup('ID_pers', mem_p1_char2)} "
    f"{RichPresence.value(mem_p1_score)} - {RichPresence.value(mem_p2_score)} "
    f"{RichPresence.lookup('Controller', mem_p2_ctrl)} {RichPresence.lookup('ID_pers', mem_p2_char1)} & {RichPresence.lookup('ID_pers', mem_p2_char2)} | "
    f"⏱️ {RichPresence.lookup('Period', mem_period)} | 🪙 {RichPresence.value(mem_coins)} Coins"
)

# Fallback
rp.add_display([], "Playing Arch Rivals")

print(rp)