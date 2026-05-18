from pycheevos.core.helpers import byte
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# ALIASES DE MEMÓRIA ESTÁTICOS
mem_menu_c6b = byte(0x0c6b)
mem_menu_c9a = byte(0x0c9a)
mem_menu_bb3 = byte(0x0bb3)
mem_player_team = byte(0x0b0f)

# LOOP DOS 24 SLOTS DA LIGA/TORNEIO
for i in range(24):

    base_addr = 0x0c9b + (i * 8)
    
    mem_pts     = byte(base_addr)
    mem_team_id = byte(base_addr + 1)
    mem_matches = byte(base_addr + 2)
    mem_wins    = byte(base_addr + 3)
    mem_draws   = byte(base_addr + 4)

    cond_gerenciar = [
        mem_menu_c6b <= 4,
        mem_menu_c9a == 1,
        mem_menu_bb3 == 0,
        mem_player_team == mem_team_id
    ]

    math_losses = f"{mem_matches.render()}-{mem_wins.render()}"
    
    display_str = (
        f"📋 League Menu | Managing {RichPresence.lookup('TeamsC', mem_player_team)} | "
        f"G:{RichPresence.value(mem_matches)} W:{RichPresence.value(mem_wins)}"
        f"L:{RichPresence.value(math_losses)}D:{RichPresence.value(mem_draws)}"
        f"Pts:{RichPresence.value(mem_pts)}"
    )
    
    rp.add_display(cond_gerenciar, display_str)

rp.add_display([], "...")
print(rp)