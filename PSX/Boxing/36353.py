from pycheevos.core.condition import *
from pycheevos.core.value import *
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import *
from pycheevos.models.set import *
from pycheevos.models.achievement import *
from notes_36353 import *

meu_set = AchievementSet(game_id=36353, title="Boxing")

ach_block = Achievement(id=1, title="Enciclopédia do Ringue", points=10, badge="0", description="Desbloqueie todas as notas e segredos biográficos de todos os lutadores")
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
])
meu_set.add_achievement(ach_block)
meu_set.save()