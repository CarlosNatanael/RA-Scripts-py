from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet
from pycheevos.core.helpers import byte, delta
from notes_36353 import *

mem_loc = indicador_de_localio_ele_armazena_aonde_o_player_esta

meu_set = AchievementSet(game_id=36353, title="Boxing")

scout_vars = [
    tanaka___scout, ryoko___scout, red___scout, b, puma___scout,
    prince___scout, misha___scout, silver_man___scout, gio___scout,
    kojiromaru___scout, spice___scout, asteka___scout, mr
]

ach_enciclopedia = Achievement(
    title="Enciclopédia do Ringue", points=10, badge="0",
    description="Desbloqueie todas as notas e segredos biográficos de todos os lutadores"
)

ach_enciclopedia.add_core([s == 2 for s in scout_vars])
ach_enciclopedia.add_core(delta(mem_loc) == 1)

meu_set.add_achievement(ach_enciclopedia)

UNLOCK_DATA = [
    (0x1fe6d3, "O Despertar do Touro", "Desbloqueie o lutador B.T."),
    (0x1fe6d4, "Instinto Selvagem",    "Desbloqueie o lutador Puma"),
    (0x1fe6d5, "Nobreza no Ringue",    "Desbloqueie o lutador Prince"),
    (0x1fe6d6, "Urso de Prata",        "Desbloqueie o lutador Misha"),
    (0x1fe6d7, "Reflexo Metálico",     "Desbloqueie o lutador Silver Man"),
    (0x1fe6d8, "Herança Italiana",     "Desbloqueie o lutador Gio"),
    (0x1fe6d9, "Espírito Samurai",     "Desbloqueie o lutador Kojiromaru"),
    (0x1fe6da, "Tempero Picante",      "Desbloqueie o lutador Spice"),
    (0x1fe6db, "Guerreiro do Sol",     "Desbloqueie o lutador Asteka"),
    (0x1fe6dc, "A Coroa do Rei",       "Desbloqueie o lutador Mr. Crown"),
]

base_id = 111002

for index, (addr, title, desc) in enumerate(UNLOCK_DATA):
    ach = Achievement(
        id=base_id + index,
        title=title, description=desc, points=5, badge="00000"
    )
    ach.add_core([
        byte(addr) == 1,
        delta(mem_loc) == 1
    ])
    meu_set.add_achievement(ach)

sign_vars = [
    tanaka___sign1, tanaka___sign2, tanaka___sign3,
    ryoko___sign1, ryoko___sign2, ryoko___sign3,
    red___sign1, red___sign2,
    b_2, b_3, b_4, b_5,
    puma___sign1,
    prince___sign1, prince___sign2, prince___sign3,
    misha___sign1, misha___sign2,
    silver_man___sign1,
    gio___sign1, gio___sign2, gio___sign3,
    kojiromaru___sign1, kojiromaru___sign2,
    spice___sign1, spice___sign2, spice___sign3,
    asteka___sign1,
    mr_2, mr_3
]

ach_mestre = Achievement(
    title="Mestre das Técnicas", points=10, badge="0",
    description="Execute com sucesso o movimento especial de cada um dos 13 personagens"
)

ach_mestre.add_core([s == 1 for s in sign_vars])
ach_mestre.add_core(delta(mem_loc) == 4)
meu_set.add_achievement(ach_mestre)

meu_set.save()