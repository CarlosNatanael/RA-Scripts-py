from pycheevos.core.helpers import byte, word
from pycheevos.models.rich_presence import RichPresence
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=36353, title="Batman Vengeance")

# ==========================================
# 1. ALIAS DE MEMÓRIA
# ==========================================
mem_state    = byte(0x3d96)
mem_lang_a   = byte(0x3d9c) 
mem_lang_sel = byte(0x3d90) 
mem_leu      = word(0x4240) 
mem_mode     = byte(0x3db8) 
mem_level    = byte(0x3da8) 

# ==========================================
# 2. INICIANDO O RICH PRESENCE BUILDER
# ==========================================
rp = RichPresence()
rp.add_format("Value", "VALUE")

# Usando o SEU método add_lookup (Note o default="" embutido na sua função!)
rp.add_lookup("Mode", {0: "Story", 1: "Advanced"}, default="")
rp.add_lookup("GameState", {0: "Intro", 5: "Selecting Language", 7: "Main Menu", 20: "In Advanced Passwords"}, default="")
rp.add_lookup("SelectionLEUA", {0: "🇺🇸", 1: "🇫🇷", 2: "🇪🇸"}, default="")
rp.add_lookup("SelectionLEU", {0: "🇺🇸", 1: "🇫🇷", 2: "🇮🇹", 3: "🇳🇱", 4: "🇩🇪", 5: "🇪🇸"}, default="")

# Níveis
rp.add_lookup("Level", {
    0: "Level 1 | Batman", 1: "Level 2 | Batman", 2: "Level 3 | Batmobile", 3: "Level 4 | Batman vs. The Joker",
    4: "Level 5 | Batplane", 5: "Level 6 | Robin", 6: "Level 7 | Robin", 7: "Level 8 | Batmobile",
    8: "Level 9 | Batman", 9: "Level 10 | Batman vs. Mr. Freeze", 10: "Level 11 | Batmobile",
    11: "Level 12 | Batman", 12: "Level 13 | Batplane", 13: "Level 14 | Robin", 14: "Level 15 | Batman",
    15: "Level 16 | Batman vs. Poison Ivy", 16: "Level 17 | Batman", 17: "Level 18 | Batman",
    18: "Level 19 | Batman vs. Harley Quinn", 19: "Level 20 | Batman vs. The Joker: The Final Battle",
    20: "Level 21 | Batplane vs. The Joker's Dirigible",
    21: "Level 1 | Batman", 22: "Level 2 | Batmobile", 23: "Level 3 | Robin", 24: "Level 4 | Batplane",
    25: "Level 5 | Batmobile", 26: "Level 6 | Robin", 27: "Level 7 | Batplane", 28: "Level 8 | Batman",
    29: "Level 9 | Batman", 30: "Level 10 | Batplane", 31: "Level 11 | Robin", 32: "Level 12 | Batmobile",
    33: "Level 13 | Batman", 34: "Level 14 | Batmobile", 35: "Level 15 | Batman", 36: "Level 16 | Robin"
}, default="")

rp.add_lookup("CollectDisk", {0: "Empty", 1: "💿", 2: "💿💿", 3: "💿💿💿"}, default="")

# Lookups dinâmicos (Matemática do Python)
items_dict = {i: str(i) for i in range(1, 10)}
items_dict[0] = "Empty"
rp.add_lookup("Items", items_dict, default="")

hull_dict = {0: "Destroyed", 1: "Critical Level", 2: "Danger - Near Destruction"}
for i in range(3, 13): hull_dict[i] = f"{(i - 2) * 10}%"
rp.add_lookup("BarBatplane", hull_dict, default="")


# ==========================================
# 3. DISPLAYS (Usando os métodos estáticos nativos)
# ==========================================
# Helper local para não repetir muito código
L = RichPresence.lookup
V = RichPresence.value

# Menus Iniciais
rp.add_display([mem_state == 0], f"{L('GameState', mem_state)}")
rp.add_display([mem_state == 5, mem_lang_a == 14], f"{L('GameState', mem_state)}: {L('SelectionLEUA', mem_lang_sel)}")
rp.add_display([mem_state == 7, mem_lang_a == 28], f"{L('SelectionLEU', mem_leu)}: {L('GameState', mem_state)} | Selecting Mode: {L('Mode', mem_lang_sel)}")
rp.add_display([mem_state == 7, mem_lang_a == 19], f"{L('SelectionLEU', mem_leu)}: {L('GameState', mem_state)} | Selecting New Game")

# --- Agrupamento STORY MODE ---
story_formats = {
    (0, 1, 8, 11, 14, 16, 17): f" | Belt: 🦇{L('Items', byte(0x21))} 💨{L('Items', byte(0x22))} 💊{L('Items', byte(0x24))}",
    (5, 6, 13):                f" | Belt: 🦇{L('Items', byte(0xe1))} 💳{L('Items', byte(0xe3))} 💊{L('Items', byte(0xe4))}",
    (2, 7, 10):                f" | Timer: {V(byte(0x4312))}:{V(byte(0x4311))}{V(byte(0x4310))}",
    (4, 12, 20):               f" | Hull: {L('BarBatplane', byte(0x426e))}",
    (3, 9, 15, 18, 19):        ""
}

for levels, suffix in story_formats.items():
    for lvl in levels:
        condition = [mem_state == 7, mem_mode == 0, mem_level == lvl]
        string = f"{L('SelectionLEU', mem_leu)}: Story Mode: {L('Level', mem_level)}{suffix}"
        rp.add_display(condition, string)

# --- Agrupamento ADVANCED MODE ---
advanced_formats = {
    (21, 28, 29, 33, 35): f" Timer: {V(byte(0x2c))}:{V(byte(0x2b))}{V(byte(0x2a))} | Disk: {L('CollectDisk', byte(0x26))}",
    (22, 25, 32, 34):     f" Timer: {V(byte(0x4312))}:{V(byte(0x4311))}{V(byte(0x4310))} | Disk: {L('CollectDisk', byte(0x430e))}",
    (23, 26, 31, 36):     f" Timer: {V(byte(0xec))}:{V(byte(0xeb))}{V(byte(0xea))} | Disk: {L('CollectDisk', byte(0xe6))}",
    (24, 27, 30):         f" Timer: {V(byte(0x4272))}:{V(byte(0x4271))}{V(byte(0x4270))} | Disk: {L('CollectDisk', byte(0x425e))}"
}

for levels, suffix in advanced_formats.items():
    for lvl in levels:
        condition = [mem_state == 7, mem_mode == 1, mem_level == lvl]
        string = f"{L('SelectionLEU', mem_leu)}: Advanced Mode: {L('Level', mem_level)}{suffix}"
        rp.add_display(condition, string)

# Display Padrão (Fallback)
rp.add_display(None, "Playing Batman: Vengeance")

# ==========================================
# 4. SALVAR
# ==========================================
my_set.add_rich_presence(rp)
my_set.save()