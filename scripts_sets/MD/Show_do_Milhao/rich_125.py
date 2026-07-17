from pycheevos.core.helpers import *
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS
rp.add_lookup("Question", {
    0x00: "1",  0x01: "2",  0x02: "3",  0x03: "4",
    0x04: "5",  0x05: "6",  0x06: "7",  0x07: "8",
    0x08: "9",  0x09: "10", 0x0a: "11", 0x0b: "12",
    0x0c: "13", 0x0d: "14", 0x0e: "15", 0x0f: "16"
}, default="")

rp.add_lookup("PrizeV", {
    0xff: "Ainda Não ganhou",
    0x00: "500 reais!",
    0x01: "Mil reais!",
    0x02: "1.500 reais!",
    0x03: "2.000 reais!",
    0x06: "4.000 reais!",
    0x07: "5.000 reais!",
    0x08: "10 Mil reais!",
    0x09: "15 Mil reais!",
    0x0a: "20 Mil reais!",
    0x0b: "25 Mil reais!",
    0x0c: "30 Mil reais!",
    0x0d: "40 Mil reais!",
    0x0e: "50 Mil reais!",
    0x0f: "100 Mil reais!",
    0x10: "150 Mil reais!",
    0x11: "200 Mil reais!",
    0x13: "300 Mil reais!",
    0x14: "400 Mil reais!",
    0x15: "500 Mil reais!",
    0x16: "1 Million"
}, default="")

rp.add_lookup("Prize", {
    0x00: "Mil reais!",
    0x01: "2 Mil reais!",
    0x02: "3 Mil reais!",
    0x03: "4 Mil reais!",
    0x04: "5 Mil reais!",
    0x05: "10 Mil reais!",
    0x06: "20 Mil reais!",
    0x07: "30 Mil reais!",
    0x08: "40 Mil reais!",
    0x09: "50 Mil reais!",
    0x0a: "100 Mil reais!",
    0x0b: "200 Mil reais!",
    0x0c: "300 Mil reais!",
    0x0d: "400 Mil reais!",
    0x0e: "500 Mil reais!",
    0x0f: "1 Milhao de reais!"
}, default="")

# 2. ALIASES DE MEMÓRIA
mem_demo       = byte(0x0010)
mem_state      = byte(0x0907)
mem_in_game    = byte(0x0860)
mem_win_1m     = byte(0x5c60)

mem_prize_v    = byte(0x001c)
mem_question   = byte(0x0854)

mem_timer      = byte(0x085e).bcd()

# 3. DISPLAYS
rp.add_display(
    [mem_demo == 1],
    "Assistindo a Demo"
)

rp.add_display(
    [mem_state == 0],
    "No Menu Inicial"
)

rp.add_display(
    [mem_win_1m == 22, mem_state == 67, mem_in_game == 0],
    "GANHOU 1 MILHAO DE REAIS!!!"
)

rp.add_display(
    [mem_state == 97],
    "Registrando o participante"
)

rp.add_display(
    [mem_state == 99],
    f"Verificando o Placar de Hoje: {RichPresence.lookup('PrizeV', mem_prize_v)}"
)

rp.add_display(
    [mem_state == 67, mem_in_game == 1],
    f"Pergunta {RichPresence.lookup('Question', mem_question)} | "
    f"Valendo {RichPresence.lookup('Prize', mem_question)} | "
    f"⏱️ {RichPresence.value(mem_timer)}s"
)

rp.add_display(
    [mem_state == 67, mem_in_game == 0],
    f"Preparando a próxima rodada | Valendo {RichPresence.lookup('Prize', mem_question)}"
)

# Fallback
rp.add_display(None, "Playing Show do Milhão")

print(rp)