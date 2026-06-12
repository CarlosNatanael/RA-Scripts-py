from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS
rp.add_lookup("Difficulty", {
    0: "Normal",
    1: "Easy",
    2: "Hard"
}, default="")

rp.add_lookup("Ballistic", {
    0: "None",
    1: "AVR-9 ",
    2: "IR-9000"
}, default="")

rp.add_lookup("Energy", {
    0: "None",
    1: "PPR-2 Plasma Pulse"
}, default="")

rp.add_lookup("Explosives", {
    1: "SBR-80 ",
    2: "Rockets Stone Dog"
}, default="")

rp.add_lookup("Stage", {
    9: "Main Menu",
    59: "Story Intro",
    106: "Level 1 - Area 1",
    107: "Level 1 - Area 2",
    94: "Level 2 - Area 1",
    82: "Level 2 - Area 2",
    83: "Level 3 - Area 1",
    86: "Level 3 - Area 2",
    101:"Level 3 - Area 3"
}, default="Area Unknown")

# 2. ALIASES DE MEMÓRIA E PONTEIROS
# Bases
ptr_base = tbyte(0x130f14)
ptr_hp   = tbyte(0x20a3d8)

# Dados Estáticos
mem_stage = dword(0x131ea8)
mem_diff  = byte(0x20a798)

# Variáveis Extraídas (Pointer + Measured)
mem_hp = group(add_address(ptr_hp), measured(float32(0x0000f0)))

wep_id_a   = group(add_address(ptr_base), measured(word(0x025c)))
wep_id_b   = group(add_address(ptr_base), measured(word(0x026c)))
wep_id_exp = group(add_address(ptr_base), measured(word(0x027c)))

wep_ammo_a   = group(add_address(ptr_base), measured(word(0x0280)))
wep_ammo_b   = group(add_address(ptr_base), measured(word(0x0284)))
wep_ammo_exp = group(add_address(ptr_base), measured(word(0x0288)))

# Condições de Troca de Slot (Weapon Set)
cond_set_0 = group(add_address(ptr_base), word(0x0258) == 0)
cond_set_1 = group(add_address(ptr_base), word(0x0258) == 1)

# 3. DISPLAYS
rp.add_display(
    cond_set_0,
    f"Stage: {RichPresence.lookup('Stage', mem_stage)} • HP {RichPresence.value(mem_hp)}/100 • "
    f"{RichPresence.lookup('Ballistic', wep_id_a)}: {RichPresence.value(wep_ammo_a)}/300 • "
    f"{RichPresence.lookup('Energy', wep_id_b)}: {RichPresence.value(wep_ammo_b)}/100 • "
    f"{RichPresence.lookup('Explosives', wep_id_exp)}: {RichPresence.value(wep_ammo_exp)}/50 | "
    f"{RichPresence.lookup('Difficulty', mem_diff)}"
)

rp.add_display(
    cond_set_1,
    f"Stage: {RichPresence.lookup('Stage', mem_stage)} • HP {RichPresence.value(mem_hp)}/100 • "
    f"{RichPresence.lookup('Ballistic', wep_id_b)}: {RichPresence.value(wep_ammo_a)}/300 • "
    f"{RichPresence.lookup('Energy', wep_id_a)}: {RichPresence.value(wep_ammo_b)}/100 • "
    f"{RichPresence.lookup('Explosives', wep_id_exp)}: {RichPresence.value(wep_ammo_exp)}/50 | "
    f"{RichPresence.lookup('Difficulty', mem_diff)}"
)

# Fallback
rp.add_display(None, "Playing Slave Zero")

print(rp)