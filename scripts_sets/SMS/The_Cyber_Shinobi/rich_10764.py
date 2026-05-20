from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS
rp.add_lookup("State", {
    0: "", 
    2: "[Paused ⏸]"
}, default="")

rp.add_lookup("Stage", {
    0: "Stage 1", 1: "Stage 2", 2: "Stage 3",
    3: "Stage 4", 4: "Stage 5", 5: "Stage 6"
}, default="")

rp.add_lookup("SubStage", {
    0: "Area 1", 1: "Area 2", 2: "Boss Fight"
}, default="")

# Usando as novas Tuplas para agrupar os valores salteados!
rp.add_lookup("ShotQdt", {
    0: 0,
    (1, 9, 17): 1,
    (2, 10, 18): 2,
    (3, 11, 19): 3,
    (4, 12, 20): 4,
    (5, 13, 21): 5,
    (6, 14, 22): 6,
    (7, 15, 23): 7,
    (8, 16, 24): 8
}, default=0)
rp.add_lookup("Shot", {
    0: "None",
    range(1, 9): "Shuriken",
    range(9, 17): "Laser Vulcan",
    range(17, 25): "Supergrenade"
}, default="None")

rp.add_lookup("Ninjutsu", {
    0: "None",
    range(1, 4): "Fire",
    (4, 5): "Tornado",
    (6, 7): "Lightning",
    8: "Earth"
}, default="None")


# 2. ALIASES DE MEMÓRIA
mem_screen   = byte(0x02)
mem_pause    = byte(0x01)
mem_stage    = byte(0x0c)
mem_substage = byte(0x0d)
mem_enemies  = byte(0x25)
mem_hp       = byte(0x11c)
mem_lives    = byte(0x0e)
mem_power    = byte(0x10)
mem_ninjutsu = byte(0x11)
mem_shot     = byte(0x12)

# Tempo
mem_time_min = byte(0x16)
mem_time_s10 = byte(0x15) # Dezena de segundo
mem_time_s1  = byte(0x14) # Unidade de segundo

# String de macro para concatenar o Score em BCD
macro_score = (
    f"{RichPresence.value(byte(0x1e).bcd())}{RichPresence.value(byte(0x1d).bcd())}"
    f"{RichPresence.value(byte(0x1c).bcd())}{RichPresence.value(byte(0x1b).bcd())}"
    f"{RichPresence.value(byte(0x1a).bcd())}{RichPresence.value(byte(0x19).bcd())}"
    f"{RichPresence.value(byte(0x18).bcd())}"
)


# 3. DISPLAYS
rp.add_display([mem_screen == 1], "Title Screen")
rp.add_display([mem_screen == 14], "Cheat Menu")

# Intro
rp.add_display(
    [mem_screen == 18], 
    f"🎬 {RichPresence.lookup('Stage', mem_stage)} Intro | 🏆 Score: {macro_score}"
)

# Stage Cleared
rp.add_display(
    [mem_screen == 20], 
    f"✅ {RichPresence.lookup('Stage', mem_stage)} Cleared | 💀 Inimigos: {RichPresence.value(mem_enemies)} | 🏆 Score: {macro_score}"
)

# In-Game Normal
rp.add_display(
    [mem_screen == 5],
    f"{RichPresence.lookup('State', mem_pause)} {RichPresence.lookup('Stage', mem_stage)}: {RichPresence.lookup('SubStage', mem_substage)} | "
    f"HP: {RichPresence.value(mem_hp)} Lives: {RichPresence.value(mem_lives)} | "
    f"Power: {RichPresence.value(mem_power)}/8 | "
    f"Ninjutsu: {RichPresence.lookup('Ninjutsu', mem_ninjutsu)} ({RichPresence.value(mem_ninjutsu)}/8) | "
    f"Special: {RichPresence.lookup('Shot', mem_shot)} ({RichPresence.lookup('ShotQdt', mem_shot)}/8) | "
    f"Score: {macro_score} | Time: {RichPresence.value(mem_time_min)}:{RichPresence.value(mem_time_s10)}{RichPresence.value(mem_time_s1)}"
)

# Usando Ninjutsu
rp.add_display(
    [mem_screen == 9],
    f"✨ Using Ninjutsu: {RichPresence.lookup('Ninjutsu', mem_ninjutsu)} | "
    f"Score: {macro_score} | Time: {RichPresence.value(mem_time_min)}:{RichPresence.value(mem_time_s10)}{RichPresence.value(mem_time_s1)}"
)

# Fallback
rp.add_display([], "Playing The Cyber Shinobi")

print(rp)