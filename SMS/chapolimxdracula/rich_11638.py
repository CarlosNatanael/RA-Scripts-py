from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS (Dicionários)
rp.add_lookup("Stage_id", {
    1: "Round 1",
    2: "Round 2",
    3: "Round 3",
    4: "Round 4",
    5: "Round 5",
    6: "Round 6"
})

# Dicionário de pause
rp.add_lookup("pause", {
    0: "",
    255: "[Paused] "
})

# 2. ALIASES DE MEMÓRIA DO RICH PRESENCE
mem_stage = byte(0x01df)
mem_pause = byte(0x0215)
mem_hp    = byte(0x021b)
mem_lives = byte(0x01e0)
mem_dracs = byte(0x0259)

# A mágica do Score: b0xW01e8*10
mem_score = word(0x01e8).bcd() * 10 


# 3. DISPLAYS (Do mais restrito ao mais geral)

# Display 1: Jogo Finalizado (Stage = 7)
rp.add_display(
    [mem_stage == 7],
    "Game Cleared!"
)

rp.add_format("Value", "VALUE")
rp.add_format("Score", "SCORE")

# Display 2: Em Jogo (Stages 1 a 6)
rp.add_display(
    [mem_stage >= 1, mem_stage <= 6],
    f"{RichPresence.lookup('pause', mem_pause)}"
    f"{RichPresence.lookup('Stage_id', mem_stage)} | "
    f"HP: {RichPresence.value(mem_hp)}/192 | "
    f"Lives: {RichPresence.value(mem_lives)} | "
    f"Draculas: {RichPresence.value(mem_dracs)}/5 | "
    f"Score: {RichPresence.value(mem_score, 'SCORE')}" # 'SCORE' garante o preenchimento de zeros (00000)
)

rp.add_display(None, "Playing Chapolim x Dracula: Um Duelo Assustador")
print(rp)