from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS (Dicionários)
rp.add_lookup("Villain", {
    2: "Living Laser", 5: "Whirlwind", 8: "Juggernaut", 11: "Grim Reaper",
    16: "Living Laser", 19: "Juggernaut", 22: "Ultron", 25: "Crossbones",
    28: "Red Skull"
})

rp.add_lookup("Hero", {
    0: "Captain America", 1: "Ironman", 2: "Vision", 3: "Hawkeye"
})

rp.add_lookup("Difficulty", {
    0: "Practice", 1: "Normal", 2: "Challenge Mode"
})

rp.add_lookup("Stage", {
    0: "Stage 1-1", 1: "Stage 1-2", 2: "Stage 1-3", 3: "Stage 1-4", 4: "Stage 1-5", 5: "Stage 1-6",
    6: "Stage 2-1", 7: "Stage 2-2", 8: "Stage 2-3", 9: "Stage 2-4", 10: "Stage 2-5", 11: "Stage 2-6",
    12: "Stage 3-1", 13: "Stage 3-2", 14: "Stage 3-3", 15: "Stage 3-4", 16: "Stage 3-6",
    17: "Stage 4-1", 18: "Stage 4-2", 19: "Stage 4-3", 20: "Stage 4-4", 21: "Stage 4-5", 22: "Stage 4-6",
    23: "Stage 5-1", 24: "Stage 5-2", 25: "Stage 5-3", 26: "Stage 5-4", 27: "Stage 5-5", 28: "Stage 5-6",
    29: "Victory Screen"
})

rp.add_lookup("Continues", {
    3: "3", 4: "4", 5: "5"
})

# 2. ALIASES DE MEMÓRIA
mem_prep   = byte(0x1d0c)
mem_state  = byte(0x1d22)
mem_diff   = byte(0x1d0f)
mem_cont   = byte(0x1d10)
mem_hero   = byte(0x031f)
mem_stage  = byte(0x1a93)
mem_boss_f = byte(0x1d15) # Boss Flag
mem_hp     = byte(0x0320)

# Montando a linguiça de Score de forma limpa em Python
score_string = (
    f"{RichPresence.value(byte(0x1d5b))}"
    f"{RichPresence.value(byte(0x1d5a))}"
    f"{RichPresence.value(byte(0x1d59))}"
    f"{RichPresence.value(byte(0x1d58))}"
    f"{RichPresence.value(byte(0x1d57))}"
    f"{RichPresence.value(byte(0x1d56))}"
    f"{RichPresence.value(byte(0x1d55))}"
    f"{RichPresence.value(byte(0x1d54))}"
)

# 3. DISPLAYS (Do mais específico para o Fallback)
# Preparing for Battle
rp.add_display(
    [mem_prep == 0x01],
    f"Preparing for Battle | {RichPresence.lookup('Difficulty', mem_diff)} Mode | "
    f"Continues: {RichPresence.lookup('Continues', mem_cont)}"
)

# Main Menu
rp.add_display(
    [mem_state == 0x01],
    "In the Main Menu"
)

# Selecting Hero
rp.add_display(
    [mem_state == 0x02],
    f"Avengers Assemble! Selecting the mightiest hero: {RichPresence.lookup('Hero', mem_hero)}"
)

# Debriefing (Stage = 8)
rp.add_display(
    [mem_state == 0x08],
    f"Debriefing at Headquarters | Score: {score_string}"
)

# Mission Accomplished (Stage = 7)
# Passamos a string bruta "0xH1a93-1" para o emulador resolver a matemática com segurança
rp.add_display(
    [mem_state == 0x07],
    f"Mission Accomplished! {RichPresence.lookup('Stage', '0xH1a93-1')} Cleared | Score: {score_string}"
)

# In Game (vs Villain)
rp.add_display(
    [mem_state == 0x03, mem_boss_f == 0x00],
    f"{RichPresence.lookup('Stage', mem_stage)} | {RichPresence.lookup('Hero', mem_hero)} "
    f"vs {RichPresence.lookup('Villain', mem_stage)} | Difficulty: {RichPresence.lookup('Difficulty', mem_diff)} | "
    f"Score: {score_string}"
)

# In Game (Health display)
rp.add_display(
    [mem_state == 0x03, mem_boss_f == 0x01],
    f"{RichPresence.lookup('Stage', mem_stage)} | {RichPresence.lookup('Hero', mem_hero)} "
    f"(Health: {RichPresence.value(mem_hp)}) | Difficulty: {RichPresence.lookup('Difficulty', mem_diff)} | "
    f"Score: {score_string}"
)

# 4. ACOPLAR AO SET
# Fallback
rp.add_display(None, "Playing F1 ROC: Race of Champions")
print(rp)