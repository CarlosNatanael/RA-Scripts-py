from pycheevos.models.set import *
from pycheevos.models.achievement import *
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

# 1. CONFIGURAÇÃO DO SET
meu_set = AchievementSet(game_id=23121, title="F1 ROC: Champions of Race")

# 2. MAPEAMENTO DE MEMÓRIA (VARIABLES)

# Endereços extraídos das Code Notes
mem_state       = byte(0x0007dd)  # 13=Corrida, 7=Vitoria, 17=Shop, 16=Nome
mem_circuit     = byte(0x0013de)  # ID da Pista
mem_position    = byte(0x0007d9)  # 0 = 1º Lugar
mem_qualify     = byte(0x00009e)  # Luz Verde / Grid
mem_damage      = byte(0x000076)  # Dano
mem_rain        = byte(0x0013e0)  # Clima (>0 chuva)
mem_tires       = byte(0x0005a2)  # Pneus (1=Rain)
mem_mode        = byte(0x000032)  # Modo de jogo / Grid Pos
mem_start_pos   = byte(0x000039)  # Posição de largada 8th?
mem_money_hi    = word(0x0013e2)  # Dinheiro
mem_season_wins = byte(0x001468)  # Pontos/Vitórias
mem_champ_pts   = byte(0x0000a3)  # Cutscene ID ou Pontos? (Usado no ID 555915)

# Slots Minigame
mem_slots_state = byte(0x0006d0)
mem_slots_w1    = byte(0x001222) # Win digit

# 3. HELPERS (Lógica Reutilizável)
def win_condition():
    """
    Padrão de vitória encontrado nas conquistas:
    Posição = 0 (1º), Estado = 7 (Vitória), Veio do estado 13 (Corrida)
    """
    return (mem_position == 0) & (mem_state == 7) & (delta(mem_state) == 13)

# 4. CONQUISTAS DE PISTAS (LOOP)
TRACKS = {
    0:  {"id": 554324, "badge": "640397", "pts": 1, "title": "Tifosi's Hero",         "desc": "Italian"},
    1:  {"id": 554334, "badge": "640398", "pts": 1, "title": "Silverstone Conqueror", "desc": "Great Britain"},
    2:  {"id": 554325, "badge": "640399", "pts": 1, "title": "Autobahn Ace",          "desc": "German"},
    3:  {"id": 554333, "badge": "640400", "pts": 2, "title": "Samba Victory",         "desc": "Brazilian"},
    4:  {"id": 554329, "badge": "640401", "pts": 1, "title": "Imola Champion",        "desc": "San Marino"},
    5:  {"id": 554337, "badge": "640402", "pts": 2, "title": "The Matador",           "desc": "Spanish"},
    6:  {"id": 554327, "badge": "640403", "pts": 1, "title": "Estoril Excellence",    "desc": "Portuguese"},
    7:  {"id": 554328, "badge": "640404", "pts": 1, "title": "High-Altitude Hero",    "desc": "Mexican"},
    8:  {"id": 554331, "badge": "640405", "pts": 1, "title": "King of the Hungaroring","desc": "Hungarian"},
    9:  {"id": 554339, "badge": "640406", "pts": 2, "title": "Wall of Champions",     "desc": "Canadian"},
    10: {"id": 554338, "badge": "640407", "pts": 2, "title": "Vive La Victoire!",     "desc": "French"},
    11: {"id": 554332, "badge": "640408", "pts": 2, "title": "Master of Eau Rouge",   "desc": "Belgian"},
    12: {"id": 554326, "badge": "640409", "pts": 2, "title": "Down Under Dominator",  "desc": "Australian"},
    13: {"id": 554336, "badge": "640410", "pts": 1, "title": "The American Dream",    "desc": "USA"},
    14: {"id": 554330, "badge": "640411", "pts": 2, "title": "Jewel in the Crown",    "desc": "Monaco"},
    15: {"id": 554335, "badge": "640412", "pts": 2, "title": "Suzuka Samurai",        "desc": "Japanese"},
}

for track_id, data in TRACKS.items():
    ach = Achievement(
        id=data['id'], title=data['title'], points=data['pts'], badge=data['badge'],
        description=f"Win a race at the {data['desc']} circuit"
    )
    ach.add_core([
        mem_circuit == track_id,
        win_condition()
    ])
    meu_set.add_achievement(ach)

# 5. CONQUISTAS DE UPGRADES (LOOP)
UPGRADES = {
    'chassis':    {'mem': byte(0x00059b), 'max': 2, 'id': 555219, 'badge': '640414', 'pts': 5, 'name': 'Type 3 chassis'},
    'gearbox':    {'mem': byte(0x00059c), 'max': 3, 'id': 555218, 'badge': '640415', 'pts': 2, 'name': '7Speed transmission'},
    'brakes':     {'mem': byte(0x00059d), 'max': 2, 'id': 555217, 'badge': '640416', 'pts': 2, 'name': 'Antilock brake'},
    'suspension': {'mem': byte(0x00059e), 'max': 2, 'id': 555216, 'badge': '640417', 'pts': 1, 'name': 'Active suspension'},
    'diffuser':   {'mem': byte(0x00059f), 'max': 3, 'id': 555215, 'badge': '640418', 'pts': 2, 'name': 'Special Diffuser'},
    'rear_wing':  {'mem': byte(0x0005a1), 'max': 2, 'id': 555213, 'badge': '640419', 'pts': 5, 'name': 'HI D.F Rear Wing'},
    'front_wing': {'mem': byte(0x0005a0), 'max': 4, 'id': 555214, 'badge': '640420', 'pts': 2, 'name': 'SPECIAL.W Front Wing'},
    'tires':      {'mem': byte(0x0005a2), 'max': 4, 'id': 555212, 'badge': '640421', 'pts': 1, 'name': 'Special Tires'},
    'engine':     {'mem': byte(0x0005a3), 'max': 5, 'id': 555211, 'badge': '640422', 'pts': 5, 'name': 'Homda V12 engine'},
}

# 5.1 Conquistas Individuais "Chief Engineer"
for key, data in UPGRADES.items():
    ach = Achievement(
        id=data['id'], title=f"Chief Engineer: {key.replace('_',' ').title()}", 
        points=data['pts'], badge=data['badge'],
        description=f"Purchase the {data['name']} upgrade"
    )
    ach.add_core([
        mem_state == 17,
        data['mem'] == data['max'],
        delta(data['mem']) < data['max']
    ])
    meu_set.add_achievement(ach)

# 5.2 First Upgrade
ach_first = Achievement(id=555385, title="First Upgrade", points=1, badge="640396", description="Buy your first car improvement")
ach_first.add_core(mem_state == 17)
for key, data in UPGRADES.items():
    ach_first.add_alt([
        delta(data['mem']) == 0,
        data['mem'] > 0
    ])
meu_set.add_achievement(ach_first)

# 5.3 The Perfect Machine
ach_perfect = Achievement(id=555220, title="The Perfect Machine", points=25, badge="640428", description="Purchase all available upgrades for an F1 car")
# Core conditions
conds_perf = [
    mem_state == 17,
]
for key, data in UPGRADES.items():
    conds_perf.append(data['mem'] == data['max'])

# Trigger na transição da loja ou update
conds_perf.append(delta(mem_state) == 17) 
ach_perfect.add_core(conds_perf)
meu_set.add_achievement(ach_perfect)

# 6. CONQUISTAS ESPECÍFICAS

# Pole Position
ach_pole = Achievement(id=555894, title="Pole Position", points=1, badge="640254", type=AchievementType.PROGRESSION,
    description="Achieve your first Pole Position in any circuit")
ach_pole.add_core([
    mem_qualify == 1, 
    delta(mem_qualify) == 0, 
    mem_mode == 0, 
    mem_state == 13
])
meu_set.add_achievement(ach_pole)

# Pole to Win
ach_polewin = Achievement(id=555895, title="Pole to Win", points=2, badge="640435", type=AchievementType.PROGRESSION,
    description="Win a race after starting from Pole Position")
ach_polewin.add_core([
    mem_mode == 0,
    mem_position == 0,
    mem_state == 7,
    delta(mem_state) == 13
])
meu_set.add_achievement(ach_polewin)

# Back of the Pack
ach_back = Achievement(id=555909, title="Back of the Pack", points=10, badge="640423",
    description="Win a race after starting from 8th place")
ach_back.add_core([
    mem_start_pos == 0,
    win_condition()
])
meu_set.add_achievement(ach_back)

# Interlagos Rain Master
ach_rain_br = Achievement(id=556004, title="Interlagos Rain Master", points=10, badge="640424",
    description="Win a race in rainy conditions at the Brazilian circuit")
ach_rain_br.add_core([
    mem_circuit == 3,
    mem_rain > 0,
    mem_position == 0,
    trigger(mem_state == 7),
    mem_state != 14,
    delta(mem_state) == 13
])
meu_set.add_achievement(ach_rain_br)

# Dancing in the Rain
ach_dance = Achievement(id=555222, title="Dancing in the Rain", points=2, badge="640425",
    description="Win any race in wet conditions after equipping RAIN tires")
ach_dance.add_core([
    mem_position == 0,
    mem_tires == 1,
    mem_rain > 0,
    trigger(mem_state == 7),
    mem_state != 14, mem_state != 17,
    delta(mem_state) == 13
])
meu_set.add_achievement(ach_dance)

# Untouchable (Missable)
ach_untouch = Achievement(id=555221, title="Untouchable", points=25, badge="640426",
    description="Win a race at the Monaco circuit with zero damage to your car")
ach_untouch.add_core([
    (mem_qualify == 1).with_hits(1),
    mem_circuit == 14,
    mem_position == 0,
    trigger(mem_state == 7),
    delta(mem_state) == 13
])
ach_untouch.add_alt(reset_if(mem_damage > 0))
meu_set.add_achievement(ach_untouch)

# Capital Injection
ach_capital = Achievement(id=555198, title="Capital Injection", points=1, badge="640413", type=AchievementType.MISSABLE,
    description="Start the game with a $10,000 bonus")
ach_capital.add_core([
    mem_money_hi == 1000,
    delta(mem_money_hi) < 1000,
    mem_season_wins == 0,
    delta(mem_state) == 16
])
meu_set.add_achievement(ach_capital)

# Monaco Jackpot
ach_jackpot = Achievement(id=555203, title="Monaco Jackpot", points=1, badge="640427", type=AchievementType.MISSABLE,
    description="Discover and play the secret slot machine minigame in Monaco")
ach_jackpot.add_core([
    mem_state == 10,
    byte(0x0013e8) == 67, # C
    byte(0x0013e9) == 65, # A
    byte(0x0013ea) == 83, # S
    byte(0x0013eb) == 73, # I
    byte(0x0013ec) == 78, # N
    byte(0x0013ed) == 79, # O
    mem_slots_state == 5,
    delta(mem_state) == 10
])
meu_set.add_achievement(ach_jackpot)

# Big Luck 777
ach_777 = Achievement(id=563375, title="[VOID]Big Luck 777", points=10, badge="640431",
    description="Win the top prize Jackpot of 4000 on the slot machine in Monaco")
ach_777.add_core([
    mem_state == 10,
    mem_slots_w1 == 244, # Raw value from note
    byte(0x001223) == 240,
    byte(0x001224) == 240,
    byte(0x001225) == 240,
    delta(mem_slots_w1) != 244
])
meu_set.add_achievement(ach_777)

# The Dream Comes True (Win Championship)
ach_dream = Achievement(id=555915, title="The Dream Comes True", points=25, badge="640429", type=AchievementType.WIN_CONDITION,
    description="Win the F1 World Championship for the first time")
ach_dream.add_core([
    byte(0x0000a3) == 32, # Cutscene ID para vitória
    delta(byte(0x0000a3)) != 32,
    byte(0x0000a4) == 144,
    byte(0x0000a5) == 29,
    mem_circuit == 15,
    byte(0x001390) == 0
])
meu_set.add_achievement(ach_dream)

# Perfect Season
ach_perfect_season = Achievement(id=555384, title="Perfect Season", points=50, badge="640430",
    description="Win every single race in a full F1 season")
ach_perfect_season.add_core([
    mem_season_wins == 160,
    byte(0x0000a3) == 237,
    byte(0x0000a4) == 231,
    byte(0x0000a5) == 31,
    delta(byte(0x0000a3)) != 237
])
meu_set.add_achievement(ach_perfect_season)

# Legend (Back to Back)
ach_legend = Achievement(id=555916, title="[VOID] Legend of the Asphalt", points=0, badge="640432",
    description="Win back-to-back Formula 1 World Championships")
ach_legend.add_core(byte(0x0013e6) == 2) # Season 2
meu_set.add_achievement(ach_legend)

# 7. EXPORTAÇÃO
meu_set.save()