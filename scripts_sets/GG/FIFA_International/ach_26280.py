from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet
from pycheevos.core.constants import *
from pycheevos.core.helpers import *

# Pode ajustar o título do Set conforme o nome real do jogo
my_set = AchievementSet(game_id=26280, title="Imported Set")

# ALIASES DE MEMÓRIA GERAIS
mem_comp_mode   = byte(0x0c9a)
mem_player_team = byte(0x0b0f)

# CONQUISTA: Absolute Dominance
ach_dominance = Achievement(
    id=111111,
    title="Absolute Dominance",
    description="Win all 3 matches during the Group Stage of a Tournament",
    points=10,
    badge="00000"
)

# --- CORE LOGIC ---
ach_dominance.add_core([
    (mem_comp_mode.delta() == 3),
    (mem_comp_mode == 4),
])

for i in range(24):
    # Endereço base (Points) de cada slot
    base_addr = 0x0c9b + (i * 8)
    mem_team_id = byte(base_addr + 1) # Slot Team ID
    mem_wins    = byte(base_addr + 3) # Slot Wins

    alt_logic = [
        (mem_player_team == mem_team_id),
        trigger(mem_wins == 3)
    ]

    ach_dominance.add_alt(alt_logic)

my_set.add_achievement(ach_dominance)
my_set.save()