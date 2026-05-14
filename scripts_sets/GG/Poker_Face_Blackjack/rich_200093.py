from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS (Dicionários)
rp.add_lookup("location", {
    0: "Las Vegas The Strip",
    1: "London",
    2: "Atlantic City",
    3: "Downtown Las Vegas"
}, default="Unknown")

rp.add_lookup("Dealer", {
    0: "a Dealer",
    255: "the Dealer"
}, default="a Dealer")

rp.add_lookup("Currency", {
    (0, 2, 3): "$",
    1: "£"
}, default="$")

# 2. ALIASES DE MEMÓRIA
mem_bankroll_cond = byte(0x1b68)
mem_dealer        = byte(0x1b71)
mem_loc           = byte(0x1b6c)
mem_bet           = byte(0x1a51).bcd()

math_bankroll     = "b0xX1b68-b0xH1a51" 

# 3. DISPLAYS
rp.add_display(
    [mem_bankroll_cond <= 1],
    f"💸 Lost everything to {RichPresence.lookup('Dealer', mem_dealer)} in {RichPresence.lookup('location', mem_loc)}!"
)
# 2. Tela de Jogo
rp.add_display(
    [mem_bankroll_cond >= 0],
    f"🃏 Playing a hand against {RichPresence.lookup('Dealer', mem_dealer)} in {RichPresence.lookup('location', mem_loc)} | "
    f"Bet: {RichPresence.lookup('Currency', mem_loc)}{RichPresence.value(mem_bet)} | "
    f"Bankroll: {RichPresence.lookup('Currency', mem_loc)}{RichPresence.value(math_bankroll)}"
)
# 3. Fallback / Default
rp.add_display(None, "Playing Poker Face Paul's Blackjack")
print(rp)