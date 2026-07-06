from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

rp.add_lookup("Round", {
    1: "Round 1",
    2: "Round 2",
    3: "Round 3",
    4: "Round 4",
    5: "Round 5",
    6: "Round 6"
}, default="")

rp.add_lookup("State", {
    0: "",
    255: "⏸ Pause"
}, default="")

mem_state      = byte(0x0004)
mem_round      = byte(0x0080)
mem_hp         = word(0x0459)
mem_lives      = byte(0x0081).bcd()
mem_talisman   = byte(0x0082).bcd()
mem_sub_weapon = byte(0x0083)
rp.add_display(
    None, 
    f"{RichPresence.lookup('State', mem_state)} {RichPresence.lookup('Round', mem_round)} • "
    f"HP: {RichPresence.value(mem_hp)}/40 • "
    f"Lives: {RichPresence.value(mem_lives)} • "
    f"Talisman: {RichPresence.value(mem_talisman)} • "
    f"Sub Weapon: {RichPresence.value(mem_sub_weapon)}"
)

print(rp)