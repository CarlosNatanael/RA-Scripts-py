from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS (Dicionários)
rp.add_lookup("Stage", {
    0: "Stage 1", 1: "Stage 2", 2: "Stage 3", 3: "Stage 4",
    4: "Stage 5", 5: "Stage 5-1", 6: "Stage 5-2", 7: "Stage 5-3", 8: "Stage 5-4"
}, default="Unknown Stage")

rp.add_lookup("Boss", {
    0: "Marcus", 1: "Lyle & Erik", 2: "Mother Cell", 3: "Mk. I",
    (5, 6, 8): "Heavy Blast Man"
}, default="Unknown Boss")

rp.add_lookup("Difficulty", {
    0: "Easy", 1: "Normal", 2: "Hard", 3: "Very Hard"
}, default="Unknown")

rp.add_lookup("confir", {
    0: "❌", 1: "✅"
}, default="❓")

rp.add_lookup("soco", {
    1: "1st", 2: "2nd", 3: "3rd"
}, default=" ")

rp.add_lookup("hit_stage", {
    0: "1", 1: "2", 2: "3", 3: "4", 4: "5"
}, default="Unknown")

rp.add_lookup("player_stock", {
    0: "1 Life", 1: "3 Lives", 2: "5 Lives"
}, default="Unknown")


# 2. ALIASES DE MEMÓRIA DO RICH PRESENCE
mem_state        = byte(0x0062)
mem_stage        = byte(0x00aa)
mem_mode         = byte(0x1852)
mem_diff         = byte(0x185a)
mem_stock        = byte(0x185c)
mem_dpunch       = byte(0x0fa3)
mem_lives        = byte(0x0fa1)
mem_opt_flag     = byte(0x18a8)

# Menu de Hit Stage
mem_hit_id       = byte(0x18e8)
mem_hit_conf1    = byte(0x18ea)
mem_hit_conf2    = byte(0x18eb)
mem_hit_conf3    = byte(0x18ec)
mem_hit_conf4    = byte(0x18ed)
mem_hit_conf5    = byte(0x18ee)

# Variáveis do Hit Stage BCD
mem_hit_time_sec = byte(0x19a1)
mem_hit_time_ms  = byte(0x19a3).bcd()
mem_hit_strike   = byte(0x199f)
mem_hit_curr_h   = byte(0x1992).bcd()
mem_hit_curr_l   = byte(0x1991).bcd()
mem_hit_tot_h    = byte(0x19e8).bcd()
mem_hit_tot_l    = byte(0x19e7).bcd()

# Aproveitando nosso patch para strings brutas nas macros complexas de Score
macro_score = "A:b0xH1a0c*1000000_A:b0xH1a0b*10000_A:b0xH1a0a*100_M:b0xH1a09"

# 3. DISPLAYS
rp.add_display([mem_state == 149], "📺 Main Menu")
rp.add_display([mem_state == 147], "📺 Title Screen")
rp.add_display([mem_state == 253], "🎬 Intro Cutscene")
rp.add_display([mem_state == 255], "🎬 Intro Cutscene")

# Option Mode
rp.add_display(
    [mem_state == 214, mem_opt_flag == 0],
    f"⚙️ Option Mode | Difficulty: {RichPresence.lookup('Difficulty', mem_diff)} | Player Stock: {RichPresence.lookup('player_stock', mem_stock)}"
)

# In-Game Normal
rp.add_display(
    [mem_state == 199, mem_mode == 0],
    f"🏙️ {RichPresence.lookup('Stage', mem_stage)} | 👊 D-Punch: {RichPresence.value(mem_dpunch)} | "
    f"💖 Lives: {RichPresence.value(mem_lives)} | ⚙️ {RichPresence.lookup('Difficulty', mem_diff)} | "
    f"Score: {RichPresence.value(macro_score, 'SCORE')}"
)

# Boss Battle
rp.add_display(
    [mem_state == 219, mem_mode == 0],
    f"🚨 {RichPresence.lookup('Stage', mem_stage)} vs {RichPresence.lookup('Boss', mem_stage)} | "
    f"👊 D-Punch: {RichPresence.value(mem_dpunch)} | 💖 Lives: {RichPresence.value(mem_lives)} | "
    f"⚙️ {RichPresence.lookup('Difficulty', mem_diff)} | Score: {RichPresence.value(macro_score, 'SCORE')}"
)

# Stage Clear
rp.add_display(
    [mem_state == 182],
    f"✅ {RichPresence.lookup('Stage', mem_stage)} Clear! | Score: {RichPresence.value(macro_score, 'SCORE')}"
)

# Hit Stage Select Menu
display_hit_menu = (
    f"🥊 Hit Stage Select: {RichPresence.lookup('hit_stage', mem_hit_id)} | "
    f"[1:{RichPresence.lookup('confir', mem_hit_conf1)}] "
    f"[2:{RichPresence.lookup('confir', mem_hit_conf2)}] "
    f"[3:{RichPresence.lookup('confir', mem_hit_conf3)}] "
    f"[4:{RichPresence.lookup('confir', mem_hit_conf4)}] "
    f"[5:{RichPresence.lookup('confir', mem_hit_conf5)}]"
)
rp.add_display([mem_state == 211], display_hit_menu)
rp.add_display([mem_mode == 9], display_hit_menu)

# Playing a Hit Stage
rp.add_display(
    [mem_state == 208],
    f"Hit Stage {RichPresence.lookup('hit_stage', mem_hit_id)} | ⏱️ Time: {RichPresence.value(mem_hit_time_sec)}.{RichPresence.value(mem_hit_time_ms)} | "
    f"🥊 Strike ({RichPresence.lookup('soco', mem_hit_strike)}): {RichPresence.value(mem_hit_curr_h)}{RichPresence.value(mem_hit_curr_l)}t | "
    f"Total: {RichPresence.value(mem_hit_tot_h)}{RichPresence.value(mem_hit_tot_l)}t"
)

# Hit Stage Results / Total
rp.add_display(
    [mem_state == 214, mem_opt_flag == 1],
    f"Hit Stage {RichPresence.lookup('hit_stage', mem_hit_id)} | "
    f"Total: {RichPresence.value(mem_hit_tot_h)}{RichPresence.value(mem_hit_tot_l)}t | "
    f"Score: {RichPresence.value(macro_score, 'SCORE')}"
)

# Boss Rush Mode
rp.add_display(
    [mem_mode == 10, mem_state == 219],
    f"Boss Rush: Blast Man vs {RichPresence.lookup('Boss', mem_stage)} | "
    f"👊 D-Punch: {RichPresence.value(mem_dpunch)} | 💖 Lives: {RichPresence.value(mem_lives)} | ⚙️ {RichPresence.lookup('Difficulty', mem_diff)}"
)

# Fallback (Menu / Default)
rp.add_display([], "Playing Sonic Blast Man")
print(rp)