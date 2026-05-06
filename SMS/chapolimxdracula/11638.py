from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=11638, title="Imported Set")

# 1. ALIASES DE MEMÓRIA (O Fim dos Números Mágicos)
mem_stage     = byte(0x01df)
mem_state     = byte(0x01e0)
mem_ingame    = byte(0x01bb)
mem_score     = tbyte(0x01e8)

# Tesouros
mem_treas_1   = bitcount(0x01ed)
mem_treas_2   = bitcount(0x01ee)
mem_last_tr   = bit4(0x01ed)

# Misc / Combate
mem_hammer    = bit0(0x041e)
mem_arrows    = byte(0x0253)
mem_drac_hp   = byte(0x0242)
mem_play_hp   = byte(0x021b)
mem_lamps     = byte(0x023d)


# 2. PROGRESSÃO (Stages 1 a 6)
progression_data = [
    (606286, "Sigam-me os Bons!", "Complete Stage 1", 2, "00000", 0x02, AchievementType.PROGRESSION),
    (606287, "Palma, Palma, Não Priemos Cânico!", "Complete Stage 2", 5, "00000", 0x03, AchievementType.PROGRESSION),
    (606288, "Silêncio, Silêncio!", "Complete Stage 3", 5, "00000", 0x04, AchievementType.PROGRESSION),
    (606289, "Suspeitei Desde o Princípio", "Complete Stage 4", 5, "00000", 0x05, AchievementType.PROGRESSION),
    (606290, "Se Aproveitam de Minha Nobreza", "Complete Stage 5", 10, "00000", 0x06, AchievementType.PROGRESSION),
    (606291, "Não Contavam Com Minha Astúcia!", "Complete Stage 6", 25, "00000", 0x07, AchievementType.WIN_CONDITION),
]

for a_id, title, desc, pts, badge, target_stage, a_type in progression_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=a_type)
    ach.add_core([
        reset_if(mem_state == 0xff),
        (mem_stage == target_stage),
        (mem_stage.delta() == (target_stage - 1)).with_hits(1),
    ])
    my_set.add_achievement(ach)


# 3. TESOUROS (Missables)
treasure_data = [
    (606292, "O Tesouro do Pirata Alma Negra", "Plunder all 12 treasures hidden across Stage 1", 5, "00000", 0x01),
    (606293, "O Tesouro do Racha Cuca", "Rustle up all 12 treasures hidden across Stage 2", 5, "00000", 0x02),
    (606294, "O Tesouro do Tripa Seca", "Secure all 12 treasures hidden across Stage 3", 10, "00000", 0x03),
    (606295, "O Tesouro do Quase Nada", "Pocket all 12 treasures hidden across Stage 4", 10, "00000", 0x04),
    (606296, "O Tesouro do Cientista Louco", "Recover all 12 experimental treasures hidden across Stage 5", 10, "00000", 0x05),
    (606297, "O Tesouro da Bruxa Baratuxa", "Gather all 12 cursed treasures hidden across Stage 6", 10, "00000", 0x06),
]

for a_id, title, desc, pts, badge, stage_val in treasure_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge, type=AchievementType.MISSABLE)
    ach.add_core([
        measured_if(mem_stage == stage_val),
        add_source(mem_treas_1),
        measured(mem_treas_2 == 0x0c), # 12 tesouros
        (mem_last_tr == 0x01),
        (mem_last_tr.delta() == 0x00),
    ])
    my_set.add_achievement(ach)


# 4. PONTUAÇÃO (Score Milestones)
score_data = [
    (606298, "Mais vale a mão que 5 voando", "Reach 10,000 points", 1, "00000", 0x1000),
    (606299, "Mais Rápido Que Uma Tartaruga!", "Reach 30,000 points", 2, "00000", 0x3000),
    (606300, "Mais Forte Que Um Rato!", "Reach 50,000 points and earn an extra life", 5, "00000", 0x5000),
    (606301, "O Chapolin Colorado!", "Reach 100,000 points", 10, "00000", 0x10000),
]

for a_id, title, desc, pts, badge, target_score in score_data:
    ach = Achievement(id=a_id, title=title, description=desc, points=pts, badge=badge)
    ach.add_core([
        (mem_ingame == 0x05),
        (mem_score.delta() < target_score),
        (mem_score >= target_score),
    ])
    my_set.add_achievement(ach)


# 5. CONQUISTAS ESPECÍFICAS (Misc & Bosses)
# Minha Marreta Biônica!
ach = Achievement(id=606302, title="Minha Marreta Biônica!", description="Jump over the Hammer to collect it and use it as a weapon", points=1, badge="00000")
ach.add_core([(mem_ingame == 0x05), (mem_hammer.delta() == 0x00), (mem_hammer == 0x01)])
my_set.add_achievement(ach)

# Anteninhas de Vinil
ach = Achievement(id=606303, title="Anteninhas de Vinil", description="Jump over 15 arrows to make enemies momentarily harmless", points=2, badge="00000")
ach.add_core([(mem_ingame == 0x05), measured(mem_arrows == 0x0f), (mem_arrows.delta() == 0x0e)])
my_set.add_achievement(ach)

# Função helper para montar as lógicas do Dracula
def boss_achievement(a_id, title, desc, points, pause_logic):
    ach = Achievement(id=a_id, title=title, description=desc, points=points, badge="00000")
    ach.add_core([
        and_next(mem_drac_hp != 0x00),
        pause_logic,
        (mem_drac_hp.delta() != 0x00),
        trigger(mem_drac_hp == 0x00),
    ])
    ach.add_alt([
        or_next(mem_play_hp == 0x00),
        reset_if(mem_state < mem_state.delta()),
    ])
    my_set.add_achievement(ach)

# Boss 1: Damageless
boss_achievement(
    606304, "Todos os Meus Movimentos São Friamente Calculados", 
    "Defeat any Dracula and collect the jewel without taking any damage during the battle", 25,
    pause_if((mem_play_hp < mem_play_hp.delta()).with_hits(1)) 
)

# Boss 2: No Lamps
boss_achievement(
    606305, "Quem muito corre nunca chega", 
    "Defeat any Dracula and collect the jewel without using the lamps to paralyze him", 25,
    pause_if((mem_lamps != 0x00).with_hits(1))
)

my_set.save()