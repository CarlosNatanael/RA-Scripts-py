from pycheevos.core.condition import *
from pycheevos.core.value import *
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import *
from pycheevos.models.set import *
from pycheevos.models.achievement import *
from notes_36353 import *

meu_set = AchievementSet(game_id=36353, title="Boxing")

ach_block = Achievement(title="Enciclopédia do Ringue", points=10, badge="0", description="Desbloqueie todas as notas e segredos biográficos de todos os lutadores")
ach_block.add_core([
    tanaka___scout == 2,
    ryoko___scout == 2,
    red___scout == 2,
    b == 2,
    puma___scout == 2,
    prince___scout == 2,
    misha___scout == 2,
    silver_man___scout == 2,
    gio___scout == 2,
    kojiromaru___scout == 2,
    spice___scout == 2,
    asteka___scout == 2,
    mr == 2,
    delta(indicador_de_localio_ele_armazena_aonde_o_player_esta) == 1
])
meu_set.add_achievement(ach_block)

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
    char_mem = byte(addr)
    ach = Achievement(
        id=base_id + index,
        title=title,
        description=desc,
        points=5,
        badge="00000"
    )
    ach.add_core([
        char_mem == 1,
        delta(indicador_de_localio_ele_armazena_aonde_o_player_esta) == 1
    ])
    meu_set.add_achievement(ach)

ach_block = Achievement(title="Mestre das Técnicas", points=10, badge="0", description="Execute com sucesso o movimento especial de cada um dos 13 personagens")
ach_block.add_core([
    tanaka___sign1 == 1,
    tanaka___sign2 == 1,
    tanaka___sign3 == 1,
    ryoko___sign1 == 1,
    ryoko___sign2 == 1,
    ryoko___sign3 == 1,
    red___sign1 == 1,
    red___sign2 == 1,
    b_2 == 1,
    b_3 == 1,
    b_4 == 1,
    b_5 == 1,
    puma___sign1 == 1,
    prince___sign1 == 1,
    prince___sign2 == 1,
    prince___sign3 == 1,
    misha___sign1 == 1,
    misha___sign2 == 1,
    silver_man___sign1 == 1,
    gio___sign1 == 1,
    gio___sign2 == 1,
    gio___sign3 == 1,
    kojiromaru___sign1 == 1,
    kojiromaru___sign2 == 1,
    spice___sign1 == 1,
    spice___sign2 == 1,
    spice___sign3 == 1,
    asteka___sign1 == 1,
    mr_2 == 1,
    mr_3 == 1,
    delta(indicador_de_localio_ele_armazena_aonde_o_player_esta) == 4
])
meu_set.add_achievement(ach_block)

meu_set.save()