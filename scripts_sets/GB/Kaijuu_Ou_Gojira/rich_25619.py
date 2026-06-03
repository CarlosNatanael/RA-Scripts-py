from pycheevos.core.helpers import byte, or_next
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS
rp.add_lookup("StageDe", {
    0: "Stage 0", 1: "Stage 1", 2: "Stage 2",
    3: "Stage 3", 4: "Stage 4", 5: "Stage 5"
}, default="Unknown Stage")

rp.add_lookup("Stage", {
    0: "Stage 1", 1: "Stage 2", 2: "Stage 3",
    3: "Stage 4", 4: "Stage 5"
}, default="Unknown Stage")

rp.add_lookup("Pause", {
    0: "",
    1: "⏸️ [Paused]"
}, default="")

# 2. ALIASES DE MEMÓRIA
mem_pause     = byte(0xd886)
mem_stage     = byte(0xda2c)
mem_stage_de  = byte(0xdf02)
mem_debug     = byte(0xdf05)
mem_continues = byte(0xdb37)
mem_hp        = byte(0xffb9)

# 3. DISPLAYS
rp.add_display(
    [
        or_next(mem_pause == 0x00),
        (mem_pause == 0x01),
        (mem_debug == 0x00)
    ],
    f"{RichPresence.lookup('Pause', mem_pause)} {RichPresence.lookup('Stage', mem_stage)} | "
    f"Godzilla HP: {RichPresence.value(mem_hp)}/255 | Continues: {RichPresence.value(mem_continues)}/3"
)

rp.add_display(
    [
        (mem_pause == 0x01),
        (mem_debug == 0xff)
    ],
    f"Debugger Mode | Godzilla HP: {RichPresence.value(mem_debug)} | {RichPresence.lookup('StageDe', mem_stage_de)}"
)

rp.add_display(
    [
        or_next(mem_pause == 0x00),
        (mem_pause == 0x01),
        (mem_debug == 0xff)
    ],
    f"Debugger Mode:{RichPresence.lookup('Pause', mem_pause)} {RichPresence.lookup('Stage', mem_stage)} | "
    f"Godzilla HP: {RichPresence.value(mem_hp)}/255 | Continues: {RichPresence.value(mem_continues)}/3"
)

# Fallback
rp.add_display([], "Playing Kaijuu Ou Gojira")

print(rp)