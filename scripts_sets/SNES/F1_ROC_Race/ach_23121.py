from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=23121, title="Imported Set")

# --- ALIAS DE MEMÓRIA (Facilita a leitura e manutenção) ---
mem_state = byte(0x0007dd)
mem_track = byte(0x0013de)
mem_pos   = byte(0x0007d9)
mem_money = word(0x0013e2)


# Pole Position
ach_pole = Achievement(title="Pole Position", points=1, id=555894, badge="640254", description="Achieve your first Pole Position in any circuit", type=AchievementType.PROGRESSION)
ach_pole.add_core([byte(0x9e) == 1, byte(0x9e).delta() == 0, byte(0x32) == 0, mem_state == 0x0d])
my_set.add_achievement(ach_pole)

# Pole to Win
ach_ptw = Achievement(title="Pole to Win", points=2, id=555895, badge="640435", description="Win a race after starting from Pole Position", type=AchievementType.PROGRESSION)
ach_ptw.add_core([byte(0x32) == 0, mem_pos == 0, mem_state == 7, mem_state.delta() == 0x0d])
my_set.add_achievement(ach_ptw)

# Back of the Pack
ach_botp = Achievement(title="Back of the Pack", points=10, id=555909, badge="640423", description="Win a race after starting from 8th place")
ach_botp.add_core([byte(0x39) == 0, mem_pos == 0, mem_state == 7, mem_state.delta() == 0x0d])
my_set.add_achievement(ach_botp)

# Interlagos Rain Master
ach_rain_br = Achievement(title="Interlagos Rain Master", points=10, id=556004, badge="640424", description="Win a race in rainy conditions at the Brazilian circuit")
ach_rain_br.add_core([mem_track == 3, byte(0x13e0) > 0, mem_pos == 0, trigger(mem_state == 7), mem_state.delta() == 0x0d])
my_set.add_achievement(ach_rain_br)

# Dancing in the Rain
ach_dance = Achievement(title="Dancing in the Rain", points=2, id=555222, badge="640425", description="Win any race in wet conditions after equipping RAIN tires")
ach_dance.add_core([mem_pos == 0, byte(0x5a2) == 1, byte(0x13e0) > 0, trigger(mem_state == 7), mem_state.delta() == 0x0d])
my_set.add_achievement(ach_dance)

# Untouchable
ach_untouch = Achievement(title="Untouchable", points=25, id=555221, badge="640426", description="Win a race in 1st place without taking any damage to your car")
ach_untouch.add_core([
    and_next(mem_track == 0x0e), (byte(0x9e) == 1).with_hits(1), 
    mem_pos == 0, trigger(mem_state == 7), mem_state.delta() != 7, reset_if(byte(0x76) > 0)
])
my_set.add_achievement(ach_untouch)

# Monaco Jackpot
ach_jackpot = Achievement(title="Monaco Jackpot", points=1, id=555203, badge="640427", description="Find and try your luck at the secret slot machine minigame in Monaco", type=AchievementType.MISSABLE)
casino_str = [0x43, 0x41, 0x53, 0x49, 0x4e, 0x4f] # C A S I N O
ach_jackpot.add_core([mem_state == 0x0a] + [byte(0x13e8 + i) == char for i, char in enumerate(casino_str)] + [byte(0x6d0) == 5, byte(0x6d0).delta() != 5])
my_set.add_achievement(ach_jackpot)

# Capital Injection
ach_capital = Achievement(title="Capital Injection", points=1, id=555198, badge="640413", description="Start the game with a $10,000 bonus", type=AchievementType.MISSABLE)
ach_capital.add_core([mem_money == 1000, mem_money.delta() < 1000, mem_state.delta() == 0x10])
my_set.add_achievement(ach_capital)

# The Dream Comes True
ach_champ = Achievement(title="The Dream Comes True", points=25, id=555915, badge="640429", description="Win the F1 World Championship for the first time", type=AchievementType.WIN_CONDITION)
ach_champ.add_core([tbyte(0xa3) == 0x1d9020, tbyte(0xa3).delta() != 0x1d9020, mem_track == 0x0f, byte(0x1390) == 0])
my_set.add_achievement(ach_champ)

# Perfect Season
ach_perfect = Achievement(title="Perfect Season", points=50, id=555384, badge="640430", description="Win every single race in a full F1 season")
ach_perfect.add_core([byte(0x1468) == 0xa0, tbyte(0xa3) == 0x1d9020, tbyte(0xa3).delta() != 0x1d9020])
my_set.add_achievement(ach_perfect)

# First Upgrade
ach_first_up = Achievement(title="First Upgrade", points=1, id=555385, badge="640396", description="Buy your first car improvement")
ach_first_up.add_core(mem_state == 0x11)
# Groups: (Addr, Type: 0=(d=0, v>0), 1=(d=1, v!=1))
upg_checks = [
    (0x59b,0), (0x59c,0), (0x59d,0), (0x59e,0), (0x59f,1), (0x5a0,1), (0x5a1,1), (0x5a3,0)
]
for addr, logic_type in upg_checks:
    b = byte(addr)
    conds = [b.delta() == 0, b > 0] if logic_type == 0 else [b.delta() == 1, b != 1]
    ach_first_up.add_alt(conds)
my_set.add_achievement(ach_first_up)

# --- VENCER CORRIDAS (Circuitos) ---
# (TrackID, Title, Points, ID, Badge, Desc_Circuit_Name)
track_wins = [
    (0x00, "Tifosi's Hero",         2, 554324, "640397", "Italian"),
    (0x01, "Silverstone Conqueror", 2, 554334, "640398", "Great Britain"),
    (0x02, "Autobahn Ace",          2, 554325, "640399", "German"),
    (0x03, "Samba Victory",         5, 554333, "640400", "Brazilian"),
    (0x04, "Imola Champion",        2, 554329, "640401", "San Marino"),
    (0x05, "The Matador",           5, 554337, "640402", "Spanish"),
    (0x06, "Estoril Excellence",    2, 554327, "640403", "Portuguese"),
    (0x07, "High-Altitude Hero",    2, 554328, "640404", "Mexican"),
    (0x08, "King of the Hungaroring",2,554331, "640405", "Hungarian"),
    (0x09, "Wall of Champions",     5, 554339, "640406", "Canadian"),
    (0x0a, "Vive La Victoire!",     5, 554338, "640407", "French"),
    (0x0b, "Master of Eau Rouge",   5, 554332, "640408", "Belgian"),
    (0x0c, "Down Under Dominator",  5, 554326, "640409", "Australian"),
    (0x0d, "The American Dream",    5, 554336, "640410", "USA"),
    (0x0e, "Jewel in the Crown",    5, 554330, "640411", "Monaco"),
    (0x0f, "Suzuka Samurai",        5, 554335, "640412", "Japanese"),
]

for tid, title, pts, aid, badge, cname in track_wins:
    ach = Achievement(title=title, description=f"Win a race at the {cname} circuit", points=pts, id=aid, badge=badge)
    ach.add_core([mem_track == tid, mem_pos == 0, mem_state == 7, mem_state.delta() == 0x0d])
    my_set.add_achievement(ach)

# --- UPGRADES (Chief Engineer) ---
# (Addr, MaxVal, TitleSuffix, DescName, Points, ID, Badge)
upgrades = [
    (0x59b, 2, "Chassis",    "Type 3 chassis",          5, 555219, "640414"),
    (0x59c, 3, "Gearing",    "7Speed transmission",     2, 555218, "640415"),
    (0x59d, 2, "Brakes",     "Antilock brake",          2, 555217, "640416"),
    (0x59e, 2, "Suspension", "Active suspension",       1, 555216, "640417"),
    (0x59f, 3, "Diffuser",   "Special Diffuser",        2, 555215, "640418"),
    (0x5a1, 2, "Rear Wing",  "HI D.F Rear Wing",        5, 555213, "640419"),
    (0x5a0, 4, "Front Wing", "SPECIAL.W Front Wing",    2, 555214, "640420"),
    (0x5a2, 4, "Tires",      "Special Tires",           1, 555212, "640421"),
    (0x5a3, 5, "Engine",     "Homda V12 engine",        5, 555211, "640422"),
]

for addr, maxv, suffix, dname, pts, aid, badge in upgrades:
    ach = Achievement(title=f"Chief Engineer: {suffix}", description=f"Purchase the {dname} upgrade", points=pts, id=aid, badge=badge)
    b = byte(addr)
    ach.add_core([b == maxv, b.delta() < maxv, mem_state == 0x11])
    my_set.add_achievement(ach)

# The Perfect Machine
ach_perf = Achievement(title="The Perfect Machine", points=25, id=555220, badge="640428", description="Purchase all available upgrades for an F1 car")
conds_perf = []
for addr, maxv, _, _, _, _, _ in upgrades:
    conds_perf.append((byte(addr) == maxv).with_hits(1))
conds_perf.append(measured((value(0) == 1).with_hits(8)))
for addr, maxv, _, _, _, _, _ in upgrades:
    conds_perf.append((byte(addr).delta() == maxv).with_hits(1))
conds_perf.append((value(0) == 1).with_hits(7))
conds_perf.append(reset_if(mem_state != 0x11))

ach_perf.add_core(conds_perf)
my_set.add_achievement(ach_perf)

my_set.save()