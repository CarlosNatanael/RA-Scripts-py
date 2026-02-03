from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=23121, title="Imported Leaderboards")

# --- 1. Definição de Variáveis de Memória (Alias) ---
mem_gamestate = byte(0x0007dd)
mem_track     = byte(0x0013de)
mem_lap       = byte(0x0000a9)
mem_min       = byte(0x0000ad)
mem_sec       = byte(0x0000ae)
mem_mil       = byte(0x0000b0)

# --- 2. Tabela de Dados (Track ID, País, Adjetivo, Leaderboard ID) ---
leaderboard_data = [
    (0,  "Italy",         "Italian",       144627),
    (1,  "Great Britain", "Great Britain", 145005),
    (2,  "Germany",       "German",        145007),
    (3,  "Brazil",        "Brazilian",     145006),
    (4,  "San Marino",    "San Marino",    145008),
    (5,  "Spain",         "Spanish",       145009),
    (6,  "Portugal",      "Portuguese",    145010),
    (7,  "Mexico",        "Mexican",       145011),
    (8,  "Hungary",       "Hungarian",     145012),
    (9,  "Canada",        "Canadian",      145013),
    (10, "France",        "French",        145014),
    (11, "Belgium",       "Belgian",       145015),
    (12, "Australia",     "Australian",    145016),
    (13, "USA",           "USA",           145017),
    (14, "Monaco",        "Monaco",        145018),
    (15, "Japan",         "Japanese",      145019),
]

# --- 3. Loop Gerador ---
for track_val, country, adjective, lb_id in leaderboard_data:
    
    # Instancia o Leaderboard
    lb = Leaderboard(
        id=lb_id,
        title=f"Fastest Race - {country}",
        description=f"Best total race time on the {adjective} circuit.",
        format=LeaderboardFormat.MILLISECS,
        lower_is_better=True
    )

    # --- Lógica (Start) ---
    lb.set_start(
        mem_gamestate == 13,
        mem_track == track_val,
        mem_lap == 4,
        mem_lap.delta() == 3
    )

    # --- Lógica (Cancel) ---
    lb.set_cancel(value(0) == value(1))

    # --- Lógica (Submit) ---
    lb.set_submit(value(1) == value(1))

    # --- Lógica (Value) ---
    lb.set_value(
        add_source(mem_min.bcd()),
        add_source(mem_sec.bcd()),
        measured(mem_mil.bcd())
    )
    my_set.add_leaderboard(lb)
my_set.save()