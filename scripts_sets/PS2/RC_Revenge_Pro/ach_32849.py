from pycheevos.core.helpers import *
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=32849, title="RC Revenge Pro")

# 1. ALT 1 LOGIC (COMPARTILHADO)
# Lista de tuplas com (Offset, Valor esperado)
alt_data = [
    (0x00, 1985229328), (0x08, 0), (0x0c, 0), (0x04, 1),
    (0x18, 0), (0x1c, 24), (0x20, 24), (0x24, 24),
    (0x28, 24), (0x2c, 24), (0x30, 22), (0x34, 22),
    (0x38, 27), (0x3c, 26), (0x40, 23), (0x44, 23),
    (0x48, 24), (0x4c, 36), (0x50, 43), (0x54, 24),
    (0x58, 17), (0x5c, 39), (0x60, 23), (0x64, 3),
    (0x68, 9), (0x6c, 39), (0x80, 25), (0x84, 19),
    (0x88, 29), (0x8c, 6), (0x90, 2), (0x94, 25),
    (0x98, 46), (0x9c, 38), (0xa0, 22), (0xa4, 24),
    (0xa8, 23), (0xac, 24), (0xb0, 10), (0xb4, 34),
    (0xb8, 4), (0xbc, 23), (0xc0, 24), (0xc4, 39),
    (0xc8, 38), (0xcc, 23), (0xd0, 24), (0xd4, 43),
    (0xd8, 43), (0xdc, 44), (0xe0, 36), (0xe4, 24),
    (0xe8, 42), (0xec, 25), (0xf0, 24), (0xf4, 47),
    (0xf8, 25), (0xfc, 24), (0x100, 24), (0x104, 24),
]

alt1_logic = []
pointer_base = dword(0x001f093c) & 33554431

for offset, val in alt_data:
    alt1_logic.append(add_address(pointer_base))
    alt1_logic.append(dword(offset) == val)

# 2. ACHIEVEMENT: Curve Upon Curve
core_curve = [
    (dword(0x001edc4c) == 268435964),
    (byte(0x001edc4a) == 97),
    add_address(dword(0x001ee7e8)),
    (word(0x0000013c) == 0),
    (dword(0x001ed900).delta() != 32),
    trigger(dword(0x001ed900) == 32),
]

ach_curve = Achievement(
    id=1, 
    title="Curve Upon Curve",
    description="Finish in 1st place on the track that defies the laws of the straight line",
    points=5
)
ach_curve.add_core(core_curve)
ach_curve.add_alt(alt1_logic)
my_set.add_achievement(ach_curve)

# 3. ACHIEVEMENT: Blink and You Miss It
core_blink = [
    (dword(0x001edc4c) == 268435966),
    (byte(0x001edc4a) == 97),
    (byte(0x001edcdf) == 9),
    add_address(dword(0x001ee7e8)),
    (dword(0x00000140).delta() < 77000),
    add_address(dword(0x001ee7e8)),
    trigger(word(0x00000104) != 0),
    add_address(dword(0x001ee7e8)),
    sub_source(word(0x00000104).delta()),
    add_address(dword(0x001ee7e8)),
    trigger(word(0x00000104) == 1),
]

ach_blink = Achievement(
    id=2, 
    title="Blink and You Miss It",
    description="Complete a lap using F1 in under 1:17.00 in Time Trial mode",
    points=5
)
ach_blink.add_core(core_blink)
ach_blink.add_alt(alt1_logic)
my_set.add_achievement(ach_blink)

my_set.save()