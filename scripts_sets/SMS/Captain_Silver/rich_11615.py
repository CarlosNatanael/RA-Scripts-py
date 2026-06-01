from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

class MacroChain:
    def __init__(self, *conditions):
        self.conditions = conditions
    
    def render(self):
        return "_".join(cond.render() for cond in self.conditions)

rp = RichPresence()

# 1. LOOKUPS
rp.add_lookup("pause", {
    0: "", 
    255: "[Paused]"
}, default="")

rp.add_lookup("stage_id", {
    1: "Stage 1", 2: "Stage 2", 3: "Stage 3", 
    4: "Stage 4", 5: "Stage 5", 6: "Stage 6"
}, default="")

rp.add_lookup("powerlevel", {
    0: "Default", 1: "Level 1", 2: "Level 2", 3: "Level 3"
}, default="")

# 2. ALIASES DE MEMÓRIA
mem_pause = byte(0x0002)
mem_stage = byte(0x0025)
mem_gamestate = byte(0x03d5)
mem_lives = byte(0x0028)
mem_power = byte(0x0029)
mem_time_m = byte(0x002c)
mem_time_s = byte(0x002b).bcd()

calc_gold = MacroChain(
    add_source(byte(0x0024).bcd() * 100000),
    add_source(byte(0x0023).bcd() * 1000),
    measured(byte(0x0022).bcd() * 10)
)

letters_conds = [add_source(byte(addr).bcd()) for addr in range(0x00f3, 0x00ff)]
letters_conds.append(measured(byte(0x00ff).bcd()))
calc_letters = MacroChain(*letters_conds)

# 3. DISPLAYS
rp.add_display([mem_lives == 0, mem_gamestate == 255], "Demo mode")

rp.add_display([mem_stage == 0], "At Title Screen")

rp.add_display(
    [mem_stage >= 1],
    f"{RichPresence.lookup('pause', mem_pause)} "
    f"{RichPresence.lookup('stage_id', mem_stage)} | ⚔️ Power: {RichPresence.lookup('powerlevel', mem_power)} | "
    f"❤️ Lives: {RichPresence.value(mem_lives)} | "
    f"💰 Gold: {RichPresence.value(calc_gold)} | "
    f"⏱️ Time: {RichPresence.value(mem_time_m)}:{RichPresence.value(mem_time_s)} "
    f"[Letters: {RichPresence.value(calc_letters)}/13]"
)

# Fallback
rp.add_display([], "Playing Captain Silver")

print(rp)