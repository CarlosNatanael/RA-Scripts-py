from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=36353, title="Imported Set")

# --- Bronze Feather ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=2_d0xH1fef70=2
ach_589152_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x02),
    (byte(0x1fef70).delta() == 0x02),
]
ach_589152 = Achievement(
    title="""Bronze Feather""",
    description="""Win the Local Championship in the Lightweight weight class""",
    points=2, type=AchievementType.PROGRESSION,
    id=589152, badge="670383"
)
ach_589152.add_core(ach_589152_logic)
my_set.add_achievement(ach_589152)

# --- Silver Feather ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=5_d0xH1fef70=5
ach_589153_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x05),
    (byte(0x1fef70).delta() == 0x05),
]
ach_589153 = Achievement(
    title="""Silver Feather""",
    description="""Win the National Championship in the Lightweight weight class""",
    points=2, type=AchievementType.PROGRESSION,
    id=589153, badge="670384"
)
ach_589153.add_core(ach_589153_logic)
my_set.add_achievement(ach_589153)

# --- Gold Feather ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=8_d0xH1fef70=8
ach_589154_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x08),
    (byte(0x1fef70).delta() == 0x08),
]
ach_589154 = Achievement(
    title="""Gold Feather""",
    description="""Win the World Championship in the Lightweight weight class""",
    points=5, type=AchievementType.PROGRESSION,
    id=589154, badge="670385"
)
ach_589154.add_core(ach_589154_logic)
my_set.add_achievement(ach_589154)

# --- Local Impact ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=1_d0xH1fef70=1
ach_589156_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x01),
    (byte(0x1fef70).delta() == 0x01),
]
ach_589156 = Achievement(
    title="""Local Impact""",
    description="""Win the Local Championship in the Middleweight weight class""",
    points=2, type=AchievementType.PROGRESSION,
    id=589156, badge="670386"
)
ach_589156.add_core(ach_589156_logic)
my_set.add_achievement(ach_589156)

# --- National Pride ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=4_d0xH1fef70=4
ach_589157_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x04),
    (byte(0x1fef70).delta() == 0x04),
]
ach_589157 = Achievement(
    title="""National Pride""",
    description="""Win the National Championship in the Middleweight weight class""",
    points=5, type=AchievementType.PROGRESSION,
    id=589157, badge="669866"
)
ach_589157.add_core(ach_589157_logic)
my_set.add_achievement(ach_589157)

# --- Global Domination ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=7_d0xH1fef70=7
ach_589158_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x07),
    (byte(0x1fef70).delta() == 0x07),
]
ach_589158 = Achievement(
    title="""Global Domination""",
    description="""Win the World Championship in the Middleweight weight class""",
    points=10, type=AchievementType.PROGRESSION,
    id=589158, badge="670387"
)
ach_589158.add_core(ach_589158_logic)
my_set.add_achievement(ach_589158)

# --- Heavyweight Impact ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=0_d0xH1fef70=0
ach_589160_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x00),
    (byte(0x1fef70).delta() == 0x00),
]
ach_589160 = Achievement(
    title="""Heavyweight Impact""",
    description="""Win the Local Championship in the Heavyweight weight class""",
    points=10, type=AchievementType.PROGRESSION,
    id=589160, badge="670388"
)
ach_589160.add_core(ach_589160_logic)
my_set.add_achievement(ach_589160)

# --- Titan of the Nation ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=3_d0xH1fef70=3
ach_589161_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x03),
    (byte(0x1fef70).delta() == 0x03),
]
ach_589161 = Achievement(
    title="""Titan of the Nation""",
    description="""Win the National Championship in the Heavyweight weight class""",
    points=10, type=AchievementType.PROGRESSION,
    id=589161, badge="670389"
)
ach_589161.add_core(ach_589161_logic)
my_set.add_achievement(ach_589161)

# --- Heavyweight Legend ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=6_d0xH1fef70=6
ach_589162_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x06),
    (byte(0x1fef70).delta() == 0x06),
]
ach_589162 = Achievement(
    title="""Heavyweight Legend""",
    description="""Win the World Championship in the Heavyweight weight class""",
    points=10, type=AchievementType.PROGRESSION,
    id=589162, badge="670390"
)
ach_589162.add_core(ach_589162_logic)
my_set.add_achievement(ach_589162)

# --- True Veteran ---
# Logic: 0xH1feff0!=19S0xH1fef66=0_d0xH1fe733<99_0xH1fe733>=100S0xH1fef66=1_d0xH1fe783<99_0xH1fe783>=100S0xH1fef66=2_d0xH1fe7d3<99_0xH1fe7d3>=100S0xH1fef66=3_d0xH1fe823<99_0xH1fe823>=100S0xH1fef66=4_d0xH1fe873<99_0xH1fe873>=100S0xH1fef66=5_d0xH1fe8c3<99_0xH1fe8c3>=100S0xH1fef66=6_d0xH1fe913<99_0xH1fe913>=100S0xH1fef66=7_d0xH1fe963<99_0xH1fe963>=100S0xH1fef66=8_d0xH1fe9b3<99_0xH1fe9b3>=100S0xH1fef66=9_d0xH1fea03<99_0xH1fea03>=100S0xH1fef66=10_d0xH1fea53<99_0xH1fea53>=100S0xH1fef66=11_d0xH1feaa3<99_0xH1feaa3>=100S0xH1fef66=12_d0xH1feaf3<99_0xH1feaf3>=100
ach_589821_logic = [
    (byte(0x1feff0) != 0x13),
]
ach_589821_alt1 = [
    (byte(0x1fef66) == 0x00),
    (byte(0x1fe733).delta() < 0x63),
    (byte(0x1fe733) >= 0x64),
]
ach_589821_alt2 = [
    (byte(0x1fef66) == 0x01),
    (byte(0x1fe783).delta() < 0x63),
    (byte(0x1fe783) >= 0x64),
]
ach_589821_alt3 = [
    (byte(0x1fef66) == 0x02),
    (byte(0x1fe7d3).delta() < 0x63),
    (byte(0x1fe7d3) >= 0x64),
]
ach_589821_alt4 = [
    (byte(0x1fef66) == 0x03),
    (byte(0x1fe823).delta() < 0x63),
    (byte(0x1fe823) >= 0x64),
]
ach_589821_alt5 = [
    (byte(0x1fef66) == 0x04),
    (byte(0x1fe873).delta() < 0x63),
    (byte(0x1fe873) >= 0x64),
]
ach_589821_alt6 = [
    (byte(0x1fef66) == 0x05),
    (byte(0x1fe8c3).delta() < 0x63),
    (byte(0x1fe8c3) >= 0x64),
]
ach_589821_alt7 = [
    (byte(0x1fef66) == 0x06),
    (byte(0x1fe913).delta() < 0x63),
    (byte(0x1fe913) >= 0x64),
]
ach_589821_alt8 = [
    (byte(0x1fef66) == 0x07),
    (byte(0x1fe963).delta() < 0x63),
    (byte(0x1fe963) >= 0x64),
]
ach_589821_alt9 = [
    (byte(0x1fef66) == 0x08),
    (byte(0x1fe9b3).delta() < 0x63),
    (byte(0x1fe9b3) >= 0x64),
]
ach_589821_alt10 = [
    (byte(0x1fef66) == 0x09),
    (byte(0x1fea03).delta() < 0x63),
    (byte(0x1fea03) >= 0x64),
]
ach_589821_alt11 = [
    (byte(0x1fef66) == 0x0a),
    (byte(0x1fea53).delta() < 0x63),
    (byte(0x1fea53) >= 0x64),
]
ach_589821_alt12 = [
    (byte(0x1fef66) == 0x0b),
    (byte(0x1feaa3).delta() < 0x63),
    (byte(0x1feaa3) >= 0x64),
]
ach_589821_alt13 = [
    (byte(0x1fef66) == 0x0c),
    (byte(0x1feaf3).delta() < 0x63),
    (byte(0x1feaf3) >= 0x64),
]
ach_589821 = Achievement(
    title="""True Veteran""",
    description="""Reach Veteran level with any character""",
    points=10, type=AchievementType.PROGRESSION,
    id=589821, badge="669877"
)
ach_589821.add_core(ach_589821_logic)
ach_589821.add_alt(ach_589821_alt1)
ach_589821.add_alt(ach_589821_alt2)
ach_589821.add_alt(ach_589821_alt3)
ach_589821.add_alt(ach_589821_alt4)
ach_589821.add_alt(ach_589821_alt5)
ach_589821.add_alt(ach_589821_alt6)
ach_589821.add_alt(ach_589821_alt7)
ach_589821.add_alt(ach_589821_alt8)
ach_589821.add_alt(ach_589821_alt9)
ach_589821.add_alt(ach_589821_alt10)
ach_589821.add_alt(ach_589821_alt11)
ach_589821.add_alt(ach_589821_alt12)
ach_589821.add_alt(ach_589821_alt13)
my_set.add_achievement(ach_589821)

# --- Platinum Feather ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=11_d0xH1fef70=11
ach_589155_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x0b),
    (byte(0x1fef70).delta() == 0x0b),
]
ach_589155 = Achievement(
    title="""Platinum Feather""",
    description="""Win the Secret Championship in the Lightweight weight class""",
    points=10, type=AchievementType.PROGRESSION,
    id=589155, badge="670391"
)
ach_589155.add_core(ach_589155_logic)
my_set.add_achievement(ach_589155)

# --- Middleweight Enigma ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=10_d0xH1fef70=10
ach_589159_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x0a),
    (byte(0x1fef70).delta() == 0x0a),
]
ach_589159 = Achievement(
    title="""Middleweight Enigma""",
    description="""Win the Secret Championship in the Middleweight weight class""",
    points=10, type=AchievementType.PROGRESSION,
    id=589159, badge="669868"
)
ach_589159.add_core(ach_589159_logic)
my_set.add_achievement(ach_589159)

# --- The Final Challenge ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xM0000c8=1_I:0xW1fe480_0xH000018=19_0xH1fef70=9_d0xH1fef70=9
ach_589163_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
    (byte(0x1fef70) == 0x09),
    (byte(0x1fef70).delta() == 0x09),
]
ach_589163 = Achievement(
    title="""The Final Challenge""",
    description="""Win the Secret Championship in the Heavyweight weight class""",
    points=25, type=AchievementType.WIN_CONDITION,
    id=589163, badge="670392"
)
ach_589163.add_core(ach_589163_logic)
my_set.add_achievement(ach_589163)

# --- Son of a Legend ---
# Logic: 0xH1fef74=1_d0xH1fe6d3=0_0xH1fe6d3=1
ach_589149_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6d3).delta() == 0x00),
    (byte(0x1fe6d3) == 0x01),
]
ach_589149 = Achievement(
    title="""Son of a Legend""",
    description="""Unlock the fighter B.T.""",
    points=2,
    id=589149, badge="669846"
)
ach_589149.add_core(ach_589149_logic)
my_set.add_achievement(ach_589149)

# --- Lightning Counter ---
# Logic: 0xH1fef74=1_d0xH1fe6d4=0_0xH1fe6d4=1
ach_589140_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6d4).delta() == 0x00),
    (byte(0x1fe6d4) == 0x01),
]
ach_589140 = Achievement(
    title="""Lightning Counter""",
    description="""Unlock the fighter Puma""",
    points=2,
    id=589140, badge="669847"
)
ach_589140.add_core(ach_589140_logic)
my_set.add_achievement(ach_589140)

# --- The Prince's Ambition ---
# Logic: 0xH1fef74=1_d0xH1fe6d5=0_0xH1fe6d5=1
ach_589141_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6d5).delta() == 0x00),
    (byte(0x1fe6d5) == 0x01),
]
ach_589141 = Achievement(
    title="""The Prince's Ambition""",
    description="""Unlock the fighter Prince""",
    points=2,
    id=589141, badge="669848"
)
ach_589141.add_core(ach_589141_logic)
my_set.add_achievement(ach_589141)

# --- Precise Intuition ---
# Logic: 0xH1fef74=1_d0xH1fe6d6=0_0xH1fe6d6=1
ach_589142_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6d6).delta() == 0x00),
    (byte(0x1fe6d6) == 0x01),
]
ach_589142 = Achievement(
    title="""Precise Intuition""",
    description="""Unlock the fighter Misha""",
    points=5,
    id=589142, badge="669849"
)
ach_589142.add_core(ach_589142_logic)
my_set.add_achievement(ach_589142)

# --- The Living Legend ---
# Logic: 0xH1fef74=1_d0xH1fe6d7=0_0xH1fe6d7=1
ach_589143_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6d7).delta() == 0x00),
    (byte(0x1fe6d7) == 0x01),
]
ach_589143 = Achievement(
    title="""The Living Legend""",
    description="""Unlock the fighter Silver Man""",
    points=5,
    id=589143, badge="669850"
)
ach_589143.add_core(ach_589143_logic)
my_set.add_achievement(ach_589143)

# --- Devastating Reach ---
# Logic: 0xH1fef74=1_d0xH1fe6d8=0_0xH1fe6d8=1
ach_589144_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6d8).delta() == 0x00),
    (byte(0x1fe6d8) == 0x01),
]
ach_589144 = Achievement(
    title="""Devastating Reach""",
    description="""Unlock the fighter Gio""",
    points=5,
    id=589144, badge="669851"
)
ach_589144.add_core(ach_589144_logic)
my_set.add_achievement(ach_589144)

# --- From Dohyo to the Ring ---
# Logic: 0xH1fef74=1_d0xH1fe6d9=0_0xH1fe6d9=1
ach_589145_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6d9).delta() == 0x00),
    (byte(0x1fe6d9) == 0x01),
]
ach_589145 = Achievement(
    title="""From Dohyo to the Ring""",
    description="""Unlock the fighter Kojiromaru""",
    points=5,
    id=589145, badge="669852"
)
ach_589145.add_core(ach_589145_logic)
my_set.add_achievement(ach_589145)

# --- The Ring Spy ---
# Logic: 0xH1fef74=1_d0xH1fe6da=0_0xH1fe6da=1
ach_589146_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6da).delta() == 0x00),
    (byte(0x1fe6da) == 0x01),
]
ach_589146 = Achievement(
    title="""The Ring Spy""",
    description="""Unlock the fighter Spice""",
    points=5,
    id=589146, badge="669853"
)
ach_589146.add_core(ach_589146_logic)
my_set.add_achievement(ach_589146)

# --- Warrior of the Sun ---
# Logic: 0xH1fef74=1_d0xH1fe6db=0_0xH1fe6db=1
ach_589147_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6db).delta() == 0x00),
    (byte(0x1fe6db) == 0x01),
]
ach_589147 = Achievement(
    title="""Warrior of the Sun""",
    description="""Unlock the fighter Asteka""",
    points=10,
    id=589147, badge="669854"
)
ach_589147.add_core(ach_589147_logic)
my_set.add_achievement(ach_589147)

# --- The Disguised Champion ---
# Logic: 0xH1fef74=1_d0xH1fe6dc=0_0xH1fe6dc=1
ach_589148_logic = [
    (byte(0x1fef74) == 0x01),
    (byte(0x1fe6dc).delta() == 0x00),
    (byte(0x1fe6dc) == 0x01),
]
ach_589148 = Achievement(
    title="""The Disguised Champion""",
    description="""Unlock the fighter Mr. Crown""",
    points=10,
    id=589148, badge="669855"
)
ach_589148.add_core(ach_589148_logic)
my_set.add_achievement(ach_589148)

# --- Ring Encyclopedia ---
# Logic: Q:0xH1fef74=1_C:0xH1fe6d0=2.1._C:0xH1fe6d1=2.1._C:0xH1fe6d2=2.1._C:0xH1fe6d3=2.1._C:0xH1fe6d4=2.1._C:0xH1fe6d5=2.1._C:0xH1fe6d6=2.1._C:0xH1fe6d7=2.1._C:0xH1fe6d8=2.1._C:0xH1fe6d9=2.1._C:0xH1fe6da=2.1._C:0xH1fe6db=2.1._C:0xH1fe6dc=2.1._M:0=1.13._N:d0xH1fe6d0=1_C:0xH1fe6d0=2_N:d0xH1fe6d1=1_C:0xH1fe6d1=2_N:d0xH1fe6d2=1_C:0xH1fe6d2=2_N:d0xH1fe6d3=1_C:0xH1fe6d3=2_N:d0xH1fe6d4=1_C:0xH1fe6d4=2_N:d0xH1fe6d5=1_C:0xH1fe6d5=2_N:d0xH1fe6d6=1_C:0xH1fe6d6=2_N:d0xH1fe6d7=1_C:0xH1fe6d7=2_N:d0xH1fe6d8=1_C:0xH1fe6d8=2_N:d0xH1fe6d9=1_C:0xH1fe6d9=2_N:d0xH1fe6da=1_C:0xH1fe6da=2_N:d0xH1fe6db=1_C:0xH1fe6db=2_N:d0xH1fe6dc=1_C:0xH1fe6dc=2_0=1.1._R:0xH1fef74!=1
ach_589139_logic = [
    measured_if((byte(0x1fef74) == 0x01)),
    add_hits((byte(0x1fe6d0) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d1) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d2) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d3) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d4) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d5) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d6) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d7) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d8) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6d9) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6da) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6db) == 0x02).with_hits(1)),
    add_hits((byte(0x1fe6dc) == 0x02).with_hits(1)),
    measured((value(0x00) == 0x01).with_hits(13)),
    and_next((byte(0x1fe6d0).delta() == 0x01)),
    add_hits((byte(0x1fe6d0) == 0x02)),
    and_next((byte(0x1fe6d1).delta() == 0x01)),
    add_hits((byte(0x1fe6d1) == 0x02)),
    and_next((byte(0x1fe6d2).delta() == 0x01)),
    add_hits((byte(0x1fe6d2) == 0x02)),
    and_next((byte(0x1fe6d3).delta() == 0x01)),
    add_hits((byte(0x1fe6d3) == 0x02)),
    and_next((byte(0x1fe6d4).delta() == 0x01)),
    add_hits((byte(0x1fe6d4) == 0x02)),
    and_next((byte(0x1fe6d5).delta() == 0x01)),
    add_hits((byte(0x1fe6d5) == 0x02)),
    and_next((byte(0x1fe6d6).delta() == 0x01)),
    add_hits((byte(0x1fe6d6) == 0x02)),
    and_next((byte(0x1fe6d7).delta() == 0x01)),
    add_hits((byte(0x1fe6d7) == 0x02)),
    and_next((byte(0x1fe6d8).delta() == 0x01)),
    add_hits((byte(0x1fe6d8) == 0x02)),
    and_next((byte(0x1fe6d9).delta() == 0x01)),
    add_hits((byte(0x1fe6d9) == 0x02)),
    and_next((byte(0x1fe6da).delta() == 0x01)),
    add_hits((byte(0x1fe6da) == 0x02)),
    and_next((byte(0x1fe6db).delta() == 0x01)),
    add_hits((byte(0x1fe6db) == 0x02)),
    and_next((byte(0x1fe6dc).delta() == 0x01)),
    add_hits((byte(0x1fe6dc) == 0x02)),
    (value(0x00) == 0x01).with_hits(1),
    reset_if((byte(0x1fef74) != 0x01)),
]
ach_589139 = Achievement(
    title="""Ring Encyclopedia""",
    description="""Unlock every bio note and secret for every fighter""",
    points=25,
    id=589139, badge="670227"
)
ach_589139.add_core(ach_589139_logic)
my_set.add_achievement(ach_589139)

# --- Master of Techniques ---
# Logic: Q:0xH1fef74=4_A:d0xH1fe6dd_A:d0xH1fe6de_A:d0xH1fe6df_A:d0xH1fe6e3_A:d0xH1fe6e4_A:d0xH1fe6e5_A:d0xH1fe6e9_A:d0xH1fe6ea_A:d0xH1fe6ef_A:d0xH1fe6f0_A:d0xH1fe6f1_A:d0xH1fe6f2_A:d0xH1fe6f5_A:d0xH1fe6fb_A:d0xH1fe6fc_A:d0xH1fe6fd_A:d0xH1fe701_A:d0xH1fe702_A:d0xH1fe707_A:d0xH1fe70d_A:d0xH1fe70e_A:d0xH1fe70f_A:d0xH1fe713_A:d0xH1fe714_A:d0xH1fe719_A:d0xH1fe71a_A:d0xH1fe71b_A:d0xH1fe71f_A:d0xH1fe725_A:d0xH1fe726_0<30_A:0xH1fe6dd_A:0xH1fe6de_A:0xH1fe6df_A:0xH1fe6e3_A:0xH1fe6e4_A:0xH1fe6e5_A:0xH1fe6e9_A:0xH1fe6ea_A:0xH1fe6ef_A:0xH1fe6f0_A:0xH1fe6f1_A:0xH1fe6f2_A:0xH1fe6f5_A:0xH1fe6fb_A:0xH1fe6fc_A:0xH1fe6fd_A:0xH1fe701_A:0xH1fe702_A:0xH1fe707_A:0xH1fe70d_A:0xH1fe70e_A:0xH1fe70f_A:0xH1fe713_A:0xH1fe714_A:0xH1fe719_A:0xH1fe71a_A:0xH1fe71b_A:0xH1fe71f_A:0xH1fe725_A:0xH1fe726_M:0=30_R:0xH1fef74!=4_0xH1fef74=4.1.
ach_589151_logic = [
    measured_if((byte(0x1fef74) == 0x04)),
    add_source(byte(0x1fe6dd).delta()),
    add_source(byte(0x1fe6de).delta()),
    add_source(byte(0x1fe6df).delta()),
    add_source(byte(0x1fe6e3).delta()),
    add_source(byte(0x1fe6e4).delta()),
    add_source(byte(0x1fe6e5).delta()),
    add_source(byte(0x1fe6e9).delta()),
    add_source(byte(0x1fe6ea).delta()),
    add_source(byte(0x1fe6ef).delta()),
    add_source(byte(0x1fe6f0).delta()),
    add_source(byte(0x1fe6f1).delta()),
    add_source(byte(0x1fe6f2).delta()),
    add_source(byte(0x1fe6f5).delta()),
    add_source(byte(0x1fe6fb).delta()),
    add_source(byte(0x1fe6fc).delta()),
    add_source(byte(0x1fe6fd).delta()),
    add_source(byte(0x1fe701).delta()),
    add_source(byte(0x1fe702).delta()),
    add_source(byte(0x1fe707).delta()),
    add_source(byte(0x1fe70d).delta()),
    add_source(byte(0x1fe70e).delta()),
    add_source(byte(0x1fe70f).delta()),
    add_source(byte(0x1fe713).delta()),
    add_source(byte(0x1fe714).delta()),
    add_source(byte(0x1fe719).delta()),
    add_source(byte(0x1fe71a).delta()),
    add_source(byte(0x1fe71b).delta()),
    add_source(byte(0x1fe71f).delta()),
    add_source(byte(0x1fe725).delta()),
    add_source(byte(0x1fe726).delta()),
    (value(0x00) < 0x1e),
    add_source(byte(0x1fe6dd)),
    add_source(byte(0x1fe6de)),
    add_source(byte(0x1fe6df)),
    add_source(byte(0x1fe6e3)),
    add_source(byte(0x1fe6e4)),
    add_source(byte(0x1fe6e5)),
    add_source(byte(0x1fe6e9)),
    add_source(byte(0x1fe6ea)),
    add_source(byte(0x1fe6ef)),
    add_source(byte(0x1fe6f0)),
    add_source(byte(0x1fe6f1)),
    add_source(byte(0x1fe6f2)),
    add_source(byte(0x1fe6f5)),
    add_source(byte(0x1fe6fb)),
    add_source(byte(0x1fe6fc)),
    add_source(byte(0x1fe6fd)),
    add_source(byte(0x1fe701)),
    add_source(byte(0x1fe702)),
    add_source(byte(0x1fe707)),
    add_source(byte(0x1fe70d)),
    add_source(byte(0x1fe70e)),
    add_source(byte(0x1fe70f)),
    add_source(byte(0x1fe713)),
    add_source(byte(0x1fe714)),
    add_source(byte(0x1fe719)),
    add_source(byte(0x1fe71a)),
    add_source(byte(0x1fe71b)),
    add_source(byte(0x1fe71f)),
    add_source(byte(0x1fe725)),
    add_source(byte(0x1fe726)),
    measured((value(0x00) == 0x1e)),
    reset_if((byte(0x1fef74) != 0x04)),
    (byte(0x1fef74) == 0x04).with_hits(1),
]
ach_589151 = Achievement(
    title="""Master of Techniques""",
    description="""Successfully perform the special move of each of the 13 characters""",
    points=10,
    id=589151, badge="670229"
)
ach_589151.add_core(ach_589151_logic)
my_set.add_achievement(ach_589151)

# --- Champion's Retirement ---
# Logic: 0xH1feff0!=19_I:0xW1fe480_T:0xH000018=19S0xH1fef66=0_d0x 1fe768=0_0x 1fe768>0_0x 1fe770>0_0x 1fe778>0S0xH1fef66=0_0x 1fe768>0_d0x 1fe770=0_0x 1fe770>0_0x 1fe778>0S0xH1fef66=0_0x 1fe768>0_0x 1fe770>0_d0x 1fe778=0_0x 1fe778>0S0xH1fef66=1_d0x 1fe7b8=0_0x 1fe7b8>0_0x 1fe7c0>0_0x 1fe7c8>0S0xH1fef66=1_0x 1fe7b8>0_d0x 1fe7c0=0_0x 1fe7c0>0_0x 1fe7c8>0S0xH1fef66=1_0x 1fe7b8>0_0x 1fe7c0>0_d0x 1fe7c8=0_0x 1fe7c8>0S0xH1fef66=2_d0x 1fe808=0_0x 1fe808>0_0x 1fe810>0_0x 1fe818>0S0xH1fef66=2_0x 1fe808>0_d0x 1fe810=0_0x 1fe810>0_0x 1fe818>0S0xH1fef66=2_0x 1fe808>0_0x 1fe810>0_d0x 1fe818=0_0x 1fe818>0S0xH1fef66=3_d0x 1fe858=0_0x 1fe858>0_0x 1fe860>0_0x 1fe868>0S0xH1fef66=3_0x 1fe858>0_d0x 1fe860=0_0x 1fe860>0_0x 1fe868>0S0xH1fef66=3_0x 1fe858>0_0x 1fe860>0_d0x 1fe868=0_0x 1fe868>0S0xH1fef66=4_d0x 1fe8a8=0_0x 1fe8a8>0_0x 1fe8b0>0_0x 1fe8b8>0S0xH1fef66=4_0x 1fe8a8>0_d0x 1fe8b0=0_0x 1fe8b0>0_0x 1fe8b8>0S0xH1fef66=4_0x 1fe8a8>0_0x 1fe8b0>0_d0x 1fe8b8=0_0x 1fe8b8>0S0xH1fef66=5_d0x 1fe8f8=0_0x 1fe8f8>0_0x 1fe900>0_0x 1fe908>0S0xH1fef66=5_0x 1fe8f8>0_d0x 1fe900=0_0x 1fe900>0_0x 1fe908>0S0xH1fef66=5_0x 1fe8f8>0_0x 1fe900>0_d0x 1fe908=0_0x 1fe908>0S0xH1fef66=6_d0x 1fe948=0_0x 1fe948>0_0x 1fe950>0_0x 1fe958>0S0xH1fef66=6_0x 1fe948>0_d0x 1fe950=0_0x 1fe950>0_0x 1fe958>0S0xH1fef66=6_0x 1fe948>0_0x 1fe950>0_d0x 1fe958=0_0x 1fe958>0S0xH1fef66=7_d0x 1fe998=0_0x 1fe998>0_0x 1fe9a0>0_0x 1fe9a8>0S0xH1fef66=7_0x 1fe998>0_d0x 1fe9a0=0_0x 1fe9a0>0_0x 1fe9a8>0S0xH1fef66=7_0x 1fe998>0_0x 1fe9a0>0_d0x 1fe9a8=0_0x 1fe9a8>0S0xH1fef66=8_d0x 1fe9e8=0_0x 1fe9e8>0_0x 1fe9f0>0_0x 1fe9f8>0S0xH1fef66=8_0x 1fe9e8>0_d0x 1fe9f0=0_0x 1fe9f0>0_0x 1fe9f8>0S0xH1fef66=8_0x 1fe9e8>0_0x 1fe9f0>0_d0x 1fe9f8=0_0x 1fe9f8>0S0xH1fef66=9_d0x 1fea38=0_0x 1fea38>0_0x 1fea40>0_0x 1fea48>0S0xH1fef66=9_0x 1fea38>0_d0x 1fea40=0_0x 1fea40>0_0x 1fea48>0S0xH1fef66=9_0x 1fea38>0_0x 1fea40>0_d0x 1fea48=0_0x 1fea48>0S0xH1fef66=10_d0x 1fea88=0_0x 1fea88>0_0x 1fea90>0_0x 1fea98>0S0xH1fef66=10_0x 1fea88>0_d0x 1fea90=0_0x 1fea90>0_0x 1fea98>0S0xH1fef66=10_0x 1fea88>0_0x 1fea90>0_d0x 1fea98=0_0x 1fea98>0S0xH1fef66=11_d0x 1fead8=0_0x 1fead8>0_0x 1feae0>0_0x 1feae8>0S0xH1fef66=11_0x 1fead8>0_d0x 1feae0=0_0x 1feae0>0_0x 1feae8>0S0xH1fef66=11_0x 1fead8>0_0x 1feae0>0_d0x 1feae8=0_0x 1feae8>0S0xH1fef66=12_d0x 1feb28=0_0x 1feb28>0_0x 1feb30>0_0x 1feb38>0S0xH1fef66=12_0x 1feb28>0_d0x 1feb30=0_0x 1feb30>0_0x 1feb38>0S0xH1fef66=12_0x 1feb28>0_0x 1feb30>0_d0x 1feb38=0_0x 1feb38>0
ach_589309_logic = [
    (byte(0x1feff0) != 0x13),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x13)),
]
ach_589309_alt1 = [
    (byte(0x1fef66) == 0x00),
    (word(0x1fe768).delta() == 0x00),
    (word(0x1fe768) > 0x00),
    (word(0x1fe770) > 0x00),
    (word(0x1fe778) > 0x00),
]
ach_589309_alt2 = [
    (byte(0x1fef66) == 0x00),
    (word(0x1fe768) > 0x00),
    (word(0x1fe770).delta() == 0x00),
    (word(0x1fe770) > 0x00),
    (word(0x1fe778) > 0x00),
]
ach_589309_alt3 = [
    (byte(0x1fef66) == 0x00),
    (word(0x1fe768) > 0x00),
    (word(0x1fe770) > 0x00),
    (word(0x1fe778).delta() == 0x00),
    (word(0x1fe778) > 0x00),
]
ach_589309_alt4 = [
    (byte(0x1fef66) == 0x01),
    (word(0x1fe7b8).delta() == 0x00),
    (word(0x1fe7b8) > 0x00),
    (word(0x1fe7c0) > 0x00),
    (word(0x1fe7c8) > 0x00),
]
ach_589309_alt5 = [
    (byte(0x1fef66) == 0x01),
    (word(0x1fe7b8) > 0x00),
    (word(0x1fe7c0).delta() == 0x00),
    (word(0x1fe7c0) > 0x00),
    (word(0x1fe7c8) > 0x00),
]
ach_589309_alt6 = [
    (byte(0x1fef66) == 0x01),
    (word(0x1fe7b8) > 0x00),
    (word(0x1fe7c0) > 0x00),
    (word(0x1fe7c8).delta() == 0x00),
    (word(0x1fe7c8) > 0x00),
]
ach_589309_alt7 = [
    (byte(0x1fef66) == 0x02),
    (word(0x1fe808).delta() == 0x00),
    (word(0x1fe808) > 0x00),
    (word(0x1fe810) > 0x00),
    (word(0x1fe818) > 0x00),
]
ach_589309_alt8 = [
    (byte(0x1fef66) == 0x02),
    (word(0x1fe808) > 0x00),
    (word(0x1fe810).delta() == 0x00),
    (word(0x1fe810) > 0x00),
    (word(0x1fe818) > 0x00),
]
ach_589309_alt9 = [
    (byte(0x1fef66) == 0x02),
    (word(0x1fe808) > 0x00),
    (word(0x1fe810) > 0x00),
    (word(0x1fe818).delta() == 0x00),
    (word(0x1fe818) > 0x00),
]
ach_589309_alt10 = [
    (byte(0x1fef66) == 0x03),
    (word(0x1fe858).delta() == 0x00),
    (word(0x1fe858) > 0x00),
    (word(0x1fe860) > 0x00),
    (word(0x1fe868) > 0x00),
]
ach_589309_alt11 = [
    (byte(0x1fef66) == 0x03),
    (word(0x1fe858) > 0x00),
    (word(0x1fe860).delta() == 0x00),
    (word(0x1fe860) > 0x00),
    (word(0x1fe868) > 0x00),
]
ach_589309_alt12 = [
    (byte(0x1fef66) == 0x03),
    (word(0x1fe858) > 0x00),
    (word(0x1fe860) > 0x00),
    (word(0x1fe868).delta() == 0x00),
    (word(0x1fe868) > 0x00),
]
ach_589309_alt13 = [
    (byte(0x1fef66) == 0x04),
    (word(0x1fe8a8).delta() == 0x00),
    (word(0x1fe8a8) > 0x00),
    (word(0x1fe8b0) > 0x00),
    (word(0x1fe8b8) > 0x00),
]
ach_589309_alt14 = [
    (byte(0x1fef66) == 0x04),
    (word(0x1fe8a8) > 0x00),
    (word(0x1fe8b0).delta() == 0x00),
    (word(0x1fe8b0) > 0x00),
    (word(0x1fe8b8) > 0x00),
]
ach_589309_alt15 = [
    (byte(0x1fef66) == 0x04),
    (word(0x1fe8a8) > 0x00),
    (word(0x1fe8b0) > 0x00),
    (word(0x1fe8b8).delta() == 0x00),
    (word(0x1fe8b8) > 0x00),
]
ach_589309_alt16 = [
    (byte(0x1fef66) == 0x05),
    (word(0x1fe8f8).delta() == 0x00),
    (word(0x1fe8f8) > 0x00),
    (word(0x1fe900) > 0x00),
    (word(0x1fe908) > 0x00),
]
ach_589309_alt17 = [
    (byte(0x1fef66) == 0x05),
    (word(0x1fe8f8) > 0x00),
    (word(0x1fe900).delta() == 0x00),
    (word(0x1fe900) > 0x00),
    (word(0x1fe908) > 0x00),
]
ach_589309_alt18 = [
    (byte(0x1fef66) == 0x05),
    (word(0x1fe8f8) > 0x00),
    (word(0x1fe900) > 0x00),
    (word(0x1fe908).delta() == 0x00),
    (word(0x1fe908) > 0x00),
]
ach_589309_alt19 = [
    (byte(0x1fef66) == 0x06),
    (word(0x1fe948).delta() == 0x00),
    (word(0x1fe948) > 0x00),
    (word(0x1fe950) > 0x00),
    (word(0x1fe958) > 0x00),
]
ach_589309_alt20 = [
    (byte(0x1fef66) == 0x06),
    (word(0x1fe948) > 0x00),
    (word(0x1fe950).delta() == 0x00),
    (word(0x1fe950) > 0x00),
    (word(0x1fe958) > 0x00),
]
ach_589309_alt21 = [
    (byte(0x1fef66) == 0x06),
    (word(0x1fe948) > 0x00),
    (word(0x1fe950) > 0x00),
    (word(0x1fe958).delta() == 0x00),
    (word(0x1fe958) > 0x00),
]
ach_589309_alt22 = [
    (byte(0x1fef66) == 0x07),
    (word(0x1fe998).delta() == 0x00),
    (word(0x1fe998) > 0x00),
    (word(0x1fe9a0) > 0x00),
    (word(0x1fe9a8) > 0x00),
]
ach_589309_alt23 = [
    (byte(0x1fef66) == 0x07),
    (word(0x1fe998) > 0x00),
    (word(0x1fe9a0).delta() == 0x00),
    (word(0x1fe9a0) > 0x00),
    (word(0x1fe9a8) > 0x00),
]
ach_589309_alt24 = [
    (byte(0x1fef66) == 0x07),
    (word(0x1fe998) > 0x00),
    (word(0x1fe9a0) > 0x00),
    (word(0x1fe9a8).delta() == 0x00),
    (word(0x1fe9a8) > 0x00),
]
ach_589309_alt25 = [
    (byte(0x1fef66) == 0x08),
    (word(0x1fe9e8).delta() == 0x00),
    (word(0x1fe9e8) > 0x00),
    (word(0x1fe9f0) > 0x00),
    (word(0x1fe9f8) > 0x00),
]
ach_589309_alt26 = [
    (byte(0x1fef66) == 0x08),
    (word(0x1fe9e8) > 0x00),
    (word(0x1fe9f0).delta() == 0x00),
    (word(0x1fe9f0) > 0x00),
    (word(0x1fe9f8) > 0x00),
]
ach_589309_alt27 = [
    (byte(0x1fef66) == 0x08),
    (word(0x1fe9e8) > 0x00),
    (word(0x1fe9f0) > 0x00),
    (word(0x1fe9f8).delta() == 0x00),
    (word(0x1fe9f8) > 0x00),
]
ach_589309_alt28 = [
    (byte(0x1fef66) == 0x09),
    (word(0x1fea38).delta() == 0x00),
    (word(0x1fea38) > 0x00),
    (word(0x1fea40) > 0x00),
    (word(0x1fea48) > 0x00),
]
ach_589309_alt29 = [
    (byte(0x1fef66) == 0x09),
    (word(0x1fea38) > 0x00),
    (word(0x1fea40).delta() == 0x00),
    (word(0x1fea40) > 0x00),
    (word(0x1fea48) > 0x00),
]
ach_589309_alt30 = [
    (byte(0x1fef66) == 0x09),
    (word(0x1fea38) > 0x00),
    (word(0x1fea40) > 0x00),
    (word(0x1fea48).delta() == 0x00),
    (word(0x1fea48) > 0x00),
]
ach_589309_alt31 = [
    (byte(0x1fef66) == 0x0a),
    (word(0x1fea88).delta() == 0x00),
    (word(0x1fea88) > 0x00),
    (word(0x1fea90) > 0x00),
    (word(0x1fea98) > 0x00),
]
ach_589309_alt32 = [
    (byte(0x1fef66) == 0x0a),
    (word(0x1fea88) > 0x00),
    (word(0x1fea90).delta() == 0x00),
    (word(0x1fea90) > 0x00),
    (word(0x1fea98) > 0x00),
]
ach_589309_alt33 = [
    (byte(0x1fef66) == 0x0a),
    (word(0x1fea88) > 0x00),
    (word(0x1fea90) > 0x00),
    (word(0x1fea98).delta() == 0x00),
    (word(0x1fea98) > 0x00),
]
ach_589309_alt34 = [
    (byte(0x1fef66) == 0x0b),
    (word(0x1fead8).delta() == 0x00),
    (word(0x1fead8) > 0x00),
    (word(0x1feae0) > 0x00),
    (word(0x1feae8) > 0x00),
]
ach_589309_alt35 = [
    (byte(0x1fef66) == 0x0b),
    (word(0x1fead8) > 0x00),
    (word(0x1feae0).delta() == 0x00),
    (word(0x1feae0) > 0x00),
    (word(0x1feae8) > 0x00),
]
ach_589309_alt36 = [
    (byte(0x1fef66) == 0x0b),
    (word(0x1fead8) > 0x00),
    (word(0x1feae0) > 0x00),
    (word(0x1feae8).delta() == 0x00),
    (word(0x1feae8) > 0x00),
]
ach_589309_alt37 = [
    (byte(0x1fef66) == 0x0c),
    (word(0x1feb28).delta() == 0x00),
    (word(0x1feb28) > 0x00),
    (word(0x1feb30) > 0x00),
    (word(0x1feb38) > 0x00),
]
ach_589309_alt38 = [
    (byte(0x1fef66) == 0x0c),
    (word(0x1feb28) > 0x00),
    (word(0x1feb30).delta() == 0x00),
    (word(0x1feb30) > 0x00),
    (word(0x1feb38) > 0x00),
]
ach_589309_alt39 = [
    (byte(0x1fef66) == 0x0c),
    (word(0x1feb28) > 0x00),
    (word(0x1feb30) > 0x00),
    (word(0x1feb38).delta() == 0x00),
    (word(0x1feb38) > 0x00),
]
ach_589309 = Achievement(
    title="""Champion's Retirement""",
    description="""Win the World Championship in all three weight classes with the same fighter""",
    points=10,
    id=589309, badge="670230"
)
ach_589309.add_core(ach_589309_logic)
ach_589309.add_alt(ach_589309_alt1)
ach_589309.add_alt(ach_589309_alt2)
ach_589309.add_alt(ach_589309_alt3)
ach_589309.add_alt(ach_589309_alt4)
ach_589309.add_alt(ach_589309_alt5)
ach_589309.add_alt(ach_589309_alt6)
ach_589309.add_alt(ach_589309_alt7)
ach_589309.add_alt(ach_589309_alt8)
ach_589309.add_alt(ach_589309_alt9)
ach_589309.add_alt(ach_589309_alt10)
ach_589309.add_alt(ach_589309_alt11)
ach_589309.add_alt(ach_589309_alt12)
ach_589309.add_alt(ach_589309_alt13)
ach_589309.add_alt(ach_589309_alt14)
ach_589309.add_alt(ach_589309_alt15)
ach_589309.add_alt(ach_589309_alt16)
ach_589309.add_alt(ach_589309_alt17)
ach_589309.add_alt(ach_589309_alt18)
ach_589309.add_alt(ach_589309_alt19)
ach_589309.add_alt(ach_589309_alt20)
ach_589309.add_alt(ach_589309_alt21)
ach_589309.add_alt(ach_589309_alt22)
ach_589309.add_alt(ach_589309_alt23)
ach_589309.add_alt(ach_589309_alt24)
ach_589309.add_alt(ach_589309_alt25)
ach_589309.add_alt(ach_589309_alt26)
ach_589309.add_alt(ach_589309_alt27)
ach_589309.add_alt(ach_589309_alt28)
ach_589309.add_alt(ach_589309_alt29)
ach_589309.add_alt(ach_589309_alt30)
ach_589309.add_alt(ach_589309_alt31)
ach_589309.add_alt(ach_589309_alt32)
ach_589309.add_alt(ach_589309_alt33)
ach_589309.add_alt(ach_589309_alt34)
ach_589309.add_alt(ach_589309_alt35)
ach_589309.add_alt(ach_589309_alt36)
ach_589309.add_alt(ach_589309_alt37)
ach_589309.add_alt(ach_589309_alt38)
ach_589309.add_alt(ach_589309_alt39)
my_set.add_achievement(ach_589309)

# --- Neighborhood Hero ---
# Logic: 0xH1fef70<=1_0xH1fef68=1_d0xM1fef6a=0_0xM1fef6a=1_I:0xW1fe480_T:0xH000018=19_0xH1fef74=0S0xH1fef66=0_0x 1fe738=0S0xH1fef66=1_0x 1fe788=0S0xH1fef66=2_0x 1fe7d8=0S0xH1fef66=3_0x 1fe828=0S0xH1fef66=4_0x 1fe878=0S0xH1fef66=5_0x 1fe8c8=0S0xH1fef66=6_0x 1fe918=0S0xH1fef66=7_0x 1fe968=0S0xH1fef66=8_0x 1fe9b8=0S0xH1fef66=9_0x 1fea08=0S0xH1fef66=10_0x 1fea58=0S0xH1fef66=11_0x 1feaa8=0S0xH1fef66=12_0x 1feaf8=0
ach_589308_logic = [
    (byte(0x1fef70) <= 0x01),
    (byte(0x1fef68) == 0x01),
    (bit0(0x1fef6a).delta() == 0x00),
    (bit0(0x1fef6a) == 0x01),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x13)),
    (byte(0x1fef74) == 0x00),
]
ach_589308_alt1 = [
    (byte(0x1fef66) == 0x00),
    (word(0x1fe738) == 0x00),
]
ach_589308_alt2 = [
    (byte(0x1fef66) == 0x01),
    (word(0x1fe788) == 0x00),
]
ach_589308_alt3 = [
    (byte(0x1fef66) == 0x02),
    (word(0x1fe7d8) == 0x00),
]
ach_589308_alt4 = [
    (byte(0x1fef66) == 0x03),
    (word(0x1fe828) == 0x00),
]
ach_589308_alt5 = [
    (byte(0x1fef66) == 0x04),
    (word(0x1fe878) == 0x00),
]
ach_589308_alt6 = [
    (byte(0x1fef66) == 0x05),
    (word(0x1fe8c8) == 0x00),
]
ach_589308_alt7 = [
    (byte(0x1fef66) == 0x06),
    (word(0x1fe918) == 0x00),
]
ach_589308_alt8 = [
    (byte(0x1fef66) == 0x07),
    (word(0x1fe968) == 0x00),
]
ach_589308_alt9 = [
    (byte(0x1fef66) == 0x08),
    (word(0x1fe9b8) == 0x00),
]
ach_589308_alt10 = [
    (byte(0x1fef66) == 0x09),
    (word(0x1fea08) == 0x00),
]
ach_589308_alt11 = [
    (byte(0x1fef66) == 0x0a),
    (word(0x1fea58) == 0x00),
]
ach_589308_alt12 = [
    (byte(0x1fef66) == 0x0b),
    (word(0x1feaa8) == 0x00),
]
ach_589308_alt13 = [
    (byte(0x1fef66) == 0x0c),
    (word(0x1feaf8) == 0x00),
]
ach_589308 = Achievement(
    title="""Neighborhood Hero""",
    description="""Win the Local Championship in Middleweight weight class or higher without losing a match""",
    points=10, type=AchievementType.MISSABLE,
    id=589308, badge="670239"
)
ach_589308.add_core(ach_589308_logic)
ach_589308.add_alt(ach_589308_alt1)
ach_589308.add_alt(ach_589308_alt2)
ach_589308.add_alt(ach_589308_alt3)
ach_589308.add_alt(ach_589308_alt4)
ach_589308.add_alt(ach_589308_alt5)
ach_589308.add_alt(ach_589308_alt6)
ach_589308.add_alt(ach_589308_alt7)
ach_589308.add_alt(ach_589308_alt8)
ach_589308.add_alt(ach_589308_alt9)
ach_589308.add_alt(ach_589308_alt10)
ach_589308.add_alt(ach_589308_alt11)
ach_589308.add_alt(ach_589308_alt12)
ach_589308.add_alt(ach_589308_alt13)
my_set.add_achievement(ach_589308)

# --- National Idol ---
# Logic: O:0xH1fef70=3_0xH1fef70=4_0xH1fef68=1_d0xM1fef6a=0_0xM1fef6a=1_I:0xW1fe480_T:0xH000018=19_0xH1fef74=0S0xH1fef66=0_0x 1fe738=0S0xH1fef66=1_0x 1fe788=0S0xH1fef66=2_0x 1fe7d8=0S0xH1fef66=3_0x 1fe828=0S0xH1fef66=4_0x 1fe878=0S0xH1fef66=5_0x 1fe8c8=0S0xH1fef66=6_0x 1fe918=0S0xH1fef66=7_0x 1fe968=0S0xH1fef66=8_0x 1fe9b8=0S0xH1fef66=9_0x 1fea08=0S0xH1fef66=10_0x 1fea58=0S0xH1fef66=11_0x 1feaa8=0S0xH1fef66=12_0x 1feaf8=0
ach_589810_logic = [
    or_next((byte(0x1fef70) == 0x03)),
    (byte(0x1fef70) == 0x04),
    (byte(0x1fef68) == 0x01),
    (bit0(0x1fef6a).delta() == 0x00),
    (bit0(0x1fef6a) == 0x01),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x13)),
    (byte(0x1fef74) == 0x00),
]
ach_589810_alt1 = [
    (byte(0x1fef66) == 0x00),
    (word(0x1fe738) == 0x00),
]
ach_589810_alt2 = [
    (byte(0x1fef66) == 0x01),
    (word(0x1fe788) == 0x00),
]
ach_589810_alt3 = [
    (byte(0x1fef66) == 0x02),
    (word(0x1fe7d8) == 0x00),
]
ach_589810_alt4 = [
    (byte(0x1fef66) == 0x03),
    (word(0x1fe828) == 0x00),
]
ach_589810_alt5 = [
    (byte(0x1fef66) == 0x04),
    (word(0x1fe878) == 0x00),
]
ach_589810_alt6 = [
    (byte(0x1fef66) == 0x05),
    (word(0x1fe8c8) == 0x00),
]
ach_589810_alt7 = [
    (byte(0x1fef66) == 0x06),
    (word(0x1fe918) == 0x00),
]
ach_589810_alt8 = [
    (byte(0x1fef66) == 0x07),
    (word(0x1fe968) == 0x00),
]
ach_589810_alt9 = [
    (byte(0x1fef66) == 0x08),
    (word(0x1fe9b8) == 0x00),
]
ach_589810_alt10 = [
    (byte(0x1fef66) == 0x09),
    (word(0x1fea08) == 0x00),
]
ach_589810_alt11 = [
    (byte(0x1fef66) == 0x0a),
    (word(0x1fea58) == 0x00),
]
ach_589810_alt12 = [
    (byte(0x1fef66) == 0x0b),
    (word(0x1feaa8) == 0x00),
]
ach_589810_alt13 = [
    (byte(0x1fef66) == 0x0c),
    (word(0x1feaf8) == 0x00),
]
ach_589810 = Achievement(
    title="""National Idol""",
    description="""Win the National Championship in Middleweight weight class or higher without losing a match""",
    points=25, type=AchievementType.MISSABLE,
    id=589810, badge="670240"
)
ach_589810.add_core(ach_589810_logic)
ach_589810.add_alt(ach_589810_alt1)
ach_589810.add_alt(ach_589810_alt2)
ach_589810.add_alt(ach_589810_alt3)
ach_589810.add_alt(ach_589810_alt4)
ach_589810.add_alt(ach_589810_alt5)
ach_589810.add_alt(ach_589810_alt6)
ach_589810.add_alt(ach_589810_alt7)
ach_589810.add_alt(ach_589810_alt8)
ach_589810.add_alt(ach_589810_alt9)
ach_589810.add_alt(ach_589810_alt10)
ach_589810.add_alt(ach_589810_alt11)
ach_589810.add_alt(ach_589810_alt12)
ach_589810.add_alt(ach_589810_alt13)
my_set.add_achievement(ach_589810)

# --- Living Legend ---
# Logic: O:0xH1fef70=6_0xH1fef70=7_0xH1fef68=1_d0xM1fef6a=0_0xM1fef6a=1_I:0xW1fe480_T:0xH000018=19_0xH1fef74=0S0xH1fef66=0_0x 1fe738=0S0xH1fef66=1_0x 1fe788=0S0xH1fef66=2_0x 1fe7d8=0S0xH1fef66=3_0x 1fe828=0S0xH1fef66=4_0x 1fe878=0S0xH1fef66=5_0x 1fe8c8=0S0xH1fef66=6_0x 1fe918=0S0xH1fef66=7_0x 1fe968=0S0xH1fef66=8_0x 1fe9b8=0S0xH1fef66=9_0x 1fea08=0S0xH1fef66=10_0x 1fea58=0S0xH1fef66=11_0x 1feaa8=0S0xH1fef66=12_0x 1feaf8=0
ach_589812_logic = [
    or_next((byte(0x1fef70) == 0x06)),
    (byte(0x1fef70) == 0x07),
    (byte(0x1fef68) == 0x01),
    (bit0(0x1fef6a).delta() == 0x00),
    (bit0(0x1fef6a) == 0x01),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x13)),
    (byte(0x1fef74) == 0x00),
]
ach_589812_alt1 = [
    (byte(0x1fef66) == 0x00),
    (word(0x1fe738) == 0x00),
]
ach_589812_alt2 = [
    (byte(0x1fef66) == 0x01),
    (word(0x1fe788) == 0x00),
]
ach_589812_alt3 = [
    (byte(0x1fef66) == 0x02),
    (word(0x1fe7d8) == 0x00),
]
ach_589812_alt4 = [
    (byte(0x1fef66) == 0x03),
    (word(0x1fe828) == 0x00),
]
ach_589812_alt5 = [
    (byte(0x1fef66) == 0x04),
    (word(0x1fe878) == 0x00),
]
ach_589812_alt6 = [
    (byte(0x1fef66) == 0x05),
    (word(0x1fe8c8) == 0x00),
]
ach_589812_alt7 = [
    (byte(0x1fef66) == 0x06),
    (word(0x1fe918) == 0x00),
]
ach_589812_alt8 = [
    (byte(0x1fef66) == 0x07),
    (word(0x1fe968) == 0x00),
]
ach_589812_alt9 = [
    (byte(0x1fef66) == 0x08),
    (word(0x1fe9b8) == 0x00),
]
ach_589812_alt10 = [
    (byte(0x1fef66) == 0x09),
    (word(0x1fea08) == 0x00),
]
ach_589812_alt11 = [
    (byte(0x1fef66) == 0x0a),
    (word(0x1fea58) == 0x00),
]
ach_589812_alt12 = [
    (byte(0x1fef66) == 0x0b),
    (word(0x1feaa8) == 0x00),
]
ach_589812_alt13 = [
    (byte(0x1fef66) == 0x0c),
    (word(0x1feaf8) == 0x00),
]
ach_589812 = Achievement(
    title="""Living Legend""",
    description="""Win the World Championship in Middleweight weight class or higher without losing a match""",
    points=25, type=AchievementType.MISSABLE,
    id=589812, badge="670241"
)
ach_589812.add_core(ach_589812_logic)
ach_589812.add_alt(ach_589812_alt1)
ach_589812.add_alt(ach_589812_alt2)
ach_589812.add_alt(ach_589812_alt3)
ach_589812.add_alt(ach_589812_alt4)
ach_589812.add_alt(ach_589812_alt5)
ach_589812.add_alt(ach_589812_alt6)
ach_589812.add_alt(ach_589812_alt7)
ach_589812.add_alt(ach_589812_alt8)
ach_589812.add_alt(ach_589812_alt9)
ach_589812.add_alt(ach_589812_alt10)
ach_589812.add_alt(ach_589812_alt11)
ach_589812.add_alt(ach_589812_alt12)
ach_589812.add_alt(ach_589812_alt13)
my_set.add_achievement(ach_589812)

# --- Beyond the Limit ---
# Logic: O:0xH1fef70=9_0xH1fef70=10_0xH1fef68=1_d0xM1fef6a=0_0xM1fef6a=1_I:0xW1fe480_T:0xH000018=19_0xH1fef74=0S0xH1fef66=0_0x 1fe738=0S0xH1fef66=1_0x 1fe788=0S0xH1fef66=2_0x 1fe7d8=0S0xH1fef66=3_0x 1fe828=0S0xH1fef66=4_0x 1fe878=0S0xH1fef66=5_0x 1fe8c8=0S0xH1fef66=6_0x 1fe918=0S0xH1fef66=7_0x 1fe968=0S0xH1fef66=8_0x 1fe9b8=0S0xH1fef66=9_0x 1fea08=0S0xH1fef66=10_0x 1fea58=0S0xH1fef66=11_0x 1feaa8=0S0xH1fef66=12_0x 1feaf8=0
ach_589814_logic = [
    or_next((byte(0x1fef70) == 0x09)),
    (byte(0x1fef70) == 0x0a),
    (byte(0x1fef68) == 0x01),
    (bit0(0x1fef6a).delta() == 0x00),
    (bit0(0x1fef6a) == 0x01),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x13)),
    (byte(0x1fef74) == 0x00),
]
ach_589814_alt1 = [
    (byte(0x1fef66) == 0x00),
    (word(0x1fe738) == 0x00),
]
ach_589814_alt2 = [
    (byte(0x1fef66) == 0x01),
    (word(0x1fe788) == 0x00),
]
ach_589814_alt3 = [
    (byte(0x1fef66) == 0x02),
    (word(0x1fe7d8) == 0x00),
]
ach_589814_alt4 = [
    (byte(0x1fef66) == 0x03),
    (word(0x1fe828) == 0x00),
]
ach_589814_alt5 = [
    (byte(0x1fef66) == 0x04),
    (word(0x1fe878) == 0x00),
]
ach_589814_alt6 = [
    (byte(0x1fef66) == 0x05),
    (word(0x1fe8c8) == 0x00),
]
ach_589814_alt7 = [
    (byte(0x1fef66) == 0x06),
    (word(0x1fe918) == 0x00),
]
ach_589814_alt8 = [
    (byte(0x1fef66) == 0x07),
    (word(0x1fe968) == 0x00),
]
ach_589814_alt9 = [
    (byte(0x1fef66) == 0x08),
    (word(0x1fe9b8) == 0x00),
]
ach_589814_alt10 = [
    (byte(0x1fef66) == 0x09),
    (word(0x1fea08) == 0x00),
]
ach_589814_alt11 = [
    (byte(0x1fef66) == 0x0a),
    (word(0x1fea58) == 0x00),
]
ach_589814_alt12 = [
    (byte(0x1fef66) == 0x0b),
    (word(0x1feaa8) == 0x00),
]
ach_589814_alt13 = [
    (byte(0x1fef66) == 0x0c),
    (word(0x1feaf8) == 0x00),
]
ach_589814 = Achievement(
    title="""Beyond the Limit""",
    description="""Win the Secret Championship in Middleweight weight class or higher without losing a match""",
    points=25, type=AchievementType.MISSABLE,
    id=589814, badge="670242"
)
ach_589814.add_core(ach_589814_logic)
ach_589814.add_alt(ach_589814_alt1)
ach_589814.add_alt(ach_589814_alt2)
ach_589814.add_alt(ach_589814_alt3)
ach_589814.add_alt(ach_589814_alt4)
ach_589814.add_alt(ach_589814_alt5)
ach_589814.add_alt(ach_589814_alt6)
ach_589814.add_alt(ach_589814_alt7)
ach_589814.add_alt(ach_589814_alt8)
ach_589814.add_alt(ach_589814_alt9)
ach_589814.add_alt(ach_589814_alt10)
ach_589814.add_alt(ach_589814_alt11)
ach_589814.add_alt(ach_589814_alt12)
ach_589814.add_alt(ach_589814_alt13)
my_set.add_achievement(ach_589814)

# --- Unshakable Perfection ---
# Logic: 0xH1feff0!=19_0xH1fef68=1_d0xM1fef6a=0_0xM1fef6a=1S0xH1fef66=0_0x1fe75c=0_O:d0x1fe764=0_O:d0x1fe766=0_O:d0x1fe768=0_O:d0x1fe76a=0_O:d0x1fe76c=0_O:d0x1fe76e=0_O:d0x1fe770=0_O:d0x1fe772=0_O:d0x1fe774=0_O:d0x1fe776=0_O:d0x1fe778=0_d0x1fe77a=0_0x1fe764>0_0x1fe766>0_0x1fe768>0_0x1fe76a>0_0x1fe76c>0_0x1fe76e>0_0x1fe770>0_0x1fe772>0_0x1fe774>0_0x1fe776>0_0x1fe778>0_0x1fe77a>0S0xH1fef66=1_0x1fe7ac=0_O:d0x1fe7b4=0_O:d0x1fe7b6=0_O:d0x1fe7b8=0_O:d0x1fe7ba=0_O:d0x1fe7bc=0_O:d0x1fe7be=0_O:d0x1fe7c0=0_O:d0x1fe7c2=0_O:d0x1fe7c4=0_O:d0x1fe7c6=0_O:d0x1fe7c8=0_d0x1fe7ca=0_0x1fe7b4>0_0x1fe7b6>0_0x1fe7b8>0_0x1fe7ba>0_0x1fe7bc>0_0x1fe7be>0_0x1fe7c0>0_0x1fe7c2>0_0x1fe7c4>0_0x1fe7c6>0_0x1fe7c8>0_0x1fe7ca>0S0xH1fef66=2_0x1fe7fc=0_O:d0x1fe804=0_O:d0x1fe806=0_O:d0x1fe808=0_O:d0x1fe80a=0_O:d0x1fe80c=0_O:d0x1fe80e=0_O:d0x1fe810=0_O:d0x1fe812=0_O:d0x1fe814=0_O:d0x1fe816=0_O:d0x1fe818=0_d0x1fe81a=0_0x1fe804>0_0x1fe806>0_0x1fe808>0_0x1fe80a>0_0x1fe80c>0_0x1fe80e>0_0x1fe810>0_0x1fe812>0_0x1fe814>0_0x1fe816>0_0x1fe818>0_0x1fe81a>0S0xH1fef66=3_0x1fe84c=0_O:d0x1fe854=0_O:d0x1fe856=0_O:d0x1fe858=0_O:d0x1fe85a=0_O:d0x1fe85c=0_O:d0x1fe85e=0_O:d0x1fe860=0_O:d0x1fe862=0_O:d0x1fe864=0_O:d0x1fe866=0_O:d0x1fe868=0_d0x1fe86a=0_0x1fe854>0_0x1fe856>0_0x1fe858>0_0x1fe85a>0_0x1fe85c>0_0x1fe85e>0_0x1fe860>0_0x1fe862>0_0x1fe864>0_0x1fe866>0_0x1fe868>0_0x1fe86a>0S0xH1fef66=4_0x1fe89c=0_O:d0x1fe8a4=0_O:d0x1fe8a6=0_O:d0x1fe8a8=0_O:d0x1fe8aa=0_O:d0x1fe8ac=0_O:d0x1fe8ae=0_O:d0x1fe8b0=0_O:d0x1fe8b2=0_O:d0x1fe8b4=0_O:d0x1fe8b6=0_O:d0x1fe8b8=0_d0x1fe8ba=0_0x1fe8a4>0_0x1fe8a6>0_0x1fe8a8>0_0x1fe8aa>0_0x1fe8ac>0_0x1fe8ae>0_0x1fe8b0>0_0x1fe8b2>0_0x1fe8b4>0_0x1fe8b6>0_0x1fe8b8>0_0x1fe8ba>0S0xH1fef66=5_0x1fe8ec=0_O:d0x1fe8f4=0_O:d0x1fe8f6=0_O:d0x1fe8f8=0_O:d0x1fe8fa=0_O:d0x1fe8fc=0_O:d0x1fe8fe=0_O:d0x1fe900=0_O:d0x1fe902=0_O:d0x1fe904=0_O:d0x1fe906=0_O:d0x1fe908=0_d0x1fe90a=0_0x1fe8f4>0_0x1fe8f6>0_0x1fe8f8>0_0x1fe8fa>0_0x1fe8fc>0_0x1fe8fe>0_0x1fe900>0_0x1fe902>0_0x1fe904>0_0x1fe906>0_0x1fe908>0_0x1fe90a>0S0xH1fef66=6_0x1fe93c=0_O:d0x1fe944=0_O:d0x1fe946=0_O:d0x1fe948=0_O:d0x1fe94a=0_O:d0x1fe94c=0_O:d0x1fe94e=0_O:d0x1fe950=0_O:d0x1fe952=0_O:d0x1fe954=0_O:d0x1fe956=0_O:d0x1fe958=0_d0x1fe95a=0_0x1fe944>0_0x1fe946>0_0x1fe948>0_0x1fe94a>0_0x1fe94c>0_0x1fe94e>0_0x1fe950>0_0x1fe952>0_0x1fe954>0_0x1fe956>0_0x1fe958>0_0x1fe95a>0S0xH1fef66=7_0x1fe98c=0_O:d0x1fe994=0_O:d0x1fe996=0_O:d0x1fe998=0_O:d0x1fe99a=0_O:d0x1fe99c=0_O:d0x1fe99e=0_O:d0x1fe9a0=0_O:d0x1fe9a2=0_O:d0x1fe9a4=0_O:d0x1fe9a6=0_O:d0x1fe9a8=0_d0x1fe9aa=0_0x1fe994>0_0x1fe996>0_0x1fe998>0_0x1fe99a>0_0x1fe99c>0_0x1fe99e>0_0x1fe9a0>0_0x1fe9a2>0_0x1fe9a4>0_0x1fe9a6>0_0x1fe9a8>0_0x1fe9aa>0S0xH1fef66=8_0x1fe9dc=0_O:d0x1fe9e4=0_O:d0x1fe9e6=0_O:d0x1fe9e8=0_O:d0x1fe9ea=0_O:d0x1fe9ec=0_O:d0x1fe9ee=0_O:d0x1fe9f0=0_O:d0x1fe9f2=0_O:d0x1fe9f4=0_O:d0x1fe9f6=0_O:d0x1fe9f8=0_d0x1fe9fa=0_0x1fe9e4>0_0x1fe9e6>0_0x1fe9e8>0_0x1fe9ea>0_0x1fe9ec>0_0x1fe9ee>0_0x1fe9f0>0_0x1fe9f2>0_0x1fe9f4>0_0x1fe9f6>0_0x1fe9f8>0_0x1fe9fa>0S0xH1fef66=9_0x1fea2c=0_O:d0x1fea34=0_O:d0x1fea36=0_O:d0x1fea38=0_O:d0x1fea3a=0_O:d0x1fea3c=0_O:d0x1fea3e=0_O:d0x1fea40=0_O:d0x1fea42=0_O:d0x1fea44=0_O:d0x1fea46=0_O:d0x1fea48=0_d0x1fea4a=0_0x1fea34>0_0x1fea36>0_0x1fea38>0_0x1fea3a>0_0x1fea3c>0_0x1fea3e>0_0x1fea40>0_0x1fea42>0_0x1fea44>0_0x1fea46>0_0x1fea48>0_0x1fea4a>0S0xH1fef66=10_0x1fea7c=0_O:d0x1fea84=0_O:d0x1fea86=0_O:d0x1fea88=0_O:d0x1fea8a=0_O:d0x1fea8c=0_O:d0x1fea8e=0_O:d0x1fea90=0_O:d0x1fea92=0_O:d0x1fea94=0_O:d0x1fea96=0_O:d0x1fea98=0_d0x1fea9a=0_0x1fea84>0_0x1fea86>0_0x1fea88>0_0x1fea8a>0_0x1fea8c>0_0x1fea8e>0_0x1fea90>0_0x1fea92>0_0x1fea94>0_0x1fea96>0_0x1fea98>0_0x1fea9a>0S0xH1fef66=11_0x1feacc=0_O:d0x1fead4=0_O:d0x1fead6=0_O:d0x1fead8=0_O:d0x1feada=0_O:d0x1feadc=0_O:d0x1feade=0_O:d0x1feae0=0_O:d0x1feae2=0_O:d0x1feae4=0_O:d0x1feae6=0_O:d0x1feae8=0_d0x1feaea=0_0x1fead4>0_0x1fead6>0_0x1fead8>0_0x1feada>0_0x1feadc>0_0x1feade>0_0x1feae0>0_0x1feae2>0_0x1feae4>0_0x1feae6>0_0x1feae8>0_0x1feaea>0S0xH1fef66=12_0x1feb1c=0_O:d0x1feb24=0_O:d0x1feb26=0_O:d0x1feb28=0_O:d0x1feb2a=0_O:d0x1feb2c=0_O:d0x1feb2e=0_O:d0x1feb30=0_O:d0x1feb32=0_O:d0x1feb34=0_O:d0x1feb36=0_O:d0x1feb38=0_d0x1feb3a=0_0x1feb24>0_0x1feb26>0_0x1feb28>0_0x1feb2a>0_0x1feb2c>0_0x1feb2e>0_0x1feb30>0_0x1feb32>0_0x1feb34>0_0x1feb36>0_0x1feb38>0_0x1feb3a>0
ach_589818_logic = [
    (byte(0x1feff0) != 0x13),
    (byte(0x1fef68) == 0x01),
    (bit0(0x1fef6a).delta() == 0x00),
    (bit0(0x1fef6a) == 0x01),
]
ach_589818_alt1 = [
    (byte(0x1fef66) == 0x00),
    (word(0x1fe75c) == 0x00),
    or_next((word(0x1fe764).delta() == 0x00)),
    or_next((word(0x1fe766).delta() == 0x00)),
    or_next((word(0x1fe768).delta() == 0x00)),
    or_next((word(0x1fe76a).delta() == 0x00)),
    or_next((word(0x1fe76c).delta() == 0x00)),
    or_next((word(0x1fe76e).delta() == 0x00)),
    or_next((word(0x1fe770).delta() == 0x00)),
    or_next((word(0x1fe772).delta() == 0x00)),
    or_next((word(0x1fe774).delta() == 0x00)),
    or_next((word(0x1fe776).delta() == 0x00)),
    or_next((word(0x1fe778).delta() == 0x00)),
    (word(0x1fe77a).delta() == 0x00),
    (word(0x1fe764) > 0x00),
    (word(0x1fe766) > 0x00),
    (word(0x1fe768) > 0x00),
    (word(0x1fe76a) > 0x00),
    (word(0x1fe76c) > 0x00),
    (word(0x1fe76e) > 0x00),
    (word(0x1fe770) > 0x00),
    (word(0x1fe772) > 0x00),
    (word(0x1fe774) > 0x00),
    (word(0x1fe776) > 0x00),
    (word(0x1fe778) > 0x00),
    (word(0x1fe77a) > 0x00),
]
ach_589818_alt2 = [
    (byte(0x1fef66) == 0x01),
    (word(0x1fe7ac) == 0x00),
    or_next((word(0x1fe7b4).delta() == 0x00)),
    or_next((word(0x1fe7b6).delta() == 0x00)),
    or_next((word(0x1fe7b8).delta() == 0x00)),
    or_next((word(0x1fe7ba).delta() == 0x00)),
    or_next((word(0x1fe7bc).delta() == 0x00)),
    or_next((word(0x1fe7be).delta() == 0x00)),
    or_next((word(0x1fe7c0).delta() == 0x00)),
    or_next((word(0x1fe7c2).delta() == 0x00)),
    or_next((word(0x1fe7c4).delta() == 0x00)),
    or_next((word(0x1fe7c6).delta() == 0x00)),
    or_next((word(0x1fe7c8).delta() == 0x00)),
    (word(0x1fe7ca).delta() == 0x00),
    (word(0x1fe7b4) > 0x00),
    (word(0x1fe7b6) > 0x00),
    (word(0x1fe7b8) > 0x00),
    (word(0x1fe7ba) > 0x00),
    (word(0x1fe7bc) > 0x00),
    (word(0x1fe7be) > 0x00),
    (word(0x1fe7c0) > 0x00),
    (word(0x1fe7c2) > 0x00),
    (word(0x1fe7c4) > 0x00),
    (word(0x1fe7c6) > 0x00),
    (word(0x1fe7c8) > 0x00),
    (word(0x1fe7ca) > 0x00),
]
ach_589818_alt3 = [
    (byte(0x1fef66) == 0x02),
    (word(0x1fe7fc) == 0x00),
    or_next((word(0x1fe804).delta() == 0x00)),
    or_next((word(0x1fe806).delta() == 0x00)),
    or_next((word(0x1fe808).delta() == 0x00)),
    or_next((word(0x1fe80a).delta() == 0x00)),
    or_next((word(0x1fe80c).delta() == 0x00)),
    or_next((word(0x1fe80e).delta() == 0x00)),
    or_next((word(0x1fe810).delta() == 0x00)),
    or_next((word(0x1fe812).delta() == 0x00)),
    or_next((word(0x1fe814).delta() == 0x00)),
    or_next((word(0x1fe816).delta() == 0x00)),
    or_next((word(0x1fe818).delta() == 0x00)),
    (word(0x1fe81a).delta() == 0x00),
    (word(0x1fe804) > 0x00),
    (word(0x1fe806) > 0x00),
    (word(0x1fe808) > 0x00),
    (word(0x1fe80a) > 0x00),
    (word(0x1fe80c) > 0x00),
    (word(0x1fe80e) > 0x00),
    (word(0x1fe810) > 0x00),
    (word(0x1fe812) > 0x00),
    (word(0x1fe814) > 0x00),
    (word(0x1fe816) > 0x00),
    (word(0x1fe818) > 0x00),
    (word(0x1fe81a) > 0x00),
]
ach_589818_alt4 = [
    (byte(0x1fef66) == 0x03),
    (word(0x1fe84c) == 0x00),
    or_next((word(0x1fe854).delta() == 0x00)),
    or_next((word(0x1fe856).delta() == 0x00)),
    or_next((word(0x1fe858).delta() == 0x00)),
    or_next((word(0x1fe85a).delta() == 0x00)),
    or_next((word(0x1fe85c).delta() == 0x00)),
    or_next((word(0x1fe85e).delta() == 0x00)),
    or_next((word(0x1fe860).delta() == 0x00)),
    or_next((word(0x1fe862).delta() == 0x00)),
    or_next((word(0x1fe864).delta() == 0x00)),
    or_next((word(0x1fe866).delta() == 0x00)),
    or_next((word(0x1fe868).delta() == 0x00)),
    (word(0x1fe86a).delta() == 0x00),
    (word(0x1fe854) > 0x00),
    (word(0x1fe856) > 0x00),
    (word(0x1fe858) > 0x00),
    (word(0x1fe85a) > 0x00),
    (word(0x1fe85c) > 0x00),
    (word(0x1fe85e) > 0x00),
    (word(0x1fe860) > 0x00),
    (word(0x1fe862) > 0x00),
    (word(0x1fe864) > 0x00),
    (word(0x1fe866) > 0x00),
    (word(0x1fe868) > 0x00),
    (word(0x1fe86a) > 0x00),
]
ach_589818_alt5 = [
    (byte(0x1fef66) == 0x04),
    (word(0x1fe89c) == 0x00),
    or_next((word(0x1fe8a4).delta() == 0x00)),
    or_next((word(0x1fe8a6).delta() == 0x00)),
    or_next((word(0x1fe8a8).delta() == 0x00)),
    or_next((word(0x1fe8aa).delta() == 0x00)),
    or_next((word(0x1fe8ac).delta() == 0x00)),
    or_next((word(0x1fe8ae).delta() == 0x00)),
    or_next((word(0x1fe8b0).delta() == 0x00)),
    or_next((word(0x1fe8b2).delta() == 0x00)),
    or_next((word(0x1fe8b4).delta() == 0x00)),
    or_next((word(0x1fe8b6).delta() == 0x00)),
    or_next((word(0x1fe8b8).delta() == 0x00)),
    (word(0x1fe8ba).delta() == 0x00),
    (word(0x1fe8a4) > 0x00),
    (word(0x1fe8a6) > 0x00),
    (word(0x1fe8a8) > 0x00),
    (word(0x1fe8aa) > 0x00),
    (word(0x1fe8ac) > 0x00),
    (word(0x1fe8ae) > 0x00),
    (word(0x1fe8b0) > 0x00),
    (word(0x1fe8b2) > 0x00),
    (word(0x1fe8b4) > 0x00),
    (word(0x1fe8b6) > 0x00),
    (word(0x1fe8b8) > 0x00),
    (word(0x1fe8ba) > 0x00),
]
ach_589818_alt6 = [
    (byte(0x1fef66) == 0x05),
    (word(0x1fe8ec) == 0x00),
    or_next((word(0x1fe8f4).delta() == 0x00)),
    or_next((word(0x1fe8f6).delta() == 0x00)),
    or_next((word(0x1fe8f8).delta() == 0x00)),
    or_next((word(0x1fe8fa).delta() == 0x00)),
    or_next((word(0x1fe8fc).delta() == 0x00)),
    or_next((word(0x1fe8fe).delta() == 0x00)),
    or_next((word(0x1fe900).delta() == 0x00)),
    or_next((word(0x1fe902).delta() == 0x00)),
    or_next((word(0x1fe904).delta() == 0x00)),
    or_next((word(0x1fe906).delta() == 0x00)),
    or_next((word(0x1fe908).delta() == 0x00)),
    (word(0x1fe90a).delta() == 0x00),
    (word(0x1fe8f4) > 0x00),
    (word(0x1fe8f6) > 0x00),
    (word(0x1fe8f8) > 0x00),
    (word(0x1fe8fa) > 0x00),
    (word(0x1fe8fc) > 0x00),
    (word(0x1fe8fe) > 0x00),
    (word(0x1fe900) > 0x00),
    (word(0x1fe902) > 0x00),
    (word(0x1fe904) > 0x00),
    (word(0x1fe906) > 0x00),
    (word(0x1fe908) > 0x00),
    (word(0x1fe90a) > 0x00),
]
ach_589818_alt7 = [
    (byte(0x1fef66) == 0x06),
    (word(0x1fe93c) == 0x00),
    or_next((word(0x1fe944).delta() == 0x00)),
    or_next((word(0x1fe946).delta() == 0x00)),
    or_next((word(0x1fe948).delta() == 0x00)),
    or_next((word(0x1fe94a).delta() == 0x00)),
    or_next((word(0x1fe94c).delta() == 0x00)),
    or_next((word(0x1fe94e).delta() == 0x00)),
    or_next((word(0x1fe950).delta() == 0x00)),
    or_next((word(0x1fe952).delta() == 0x00)),
    or_next((word(0x1fe954).delta() == 0x00)),
    or_next((word(0x1fe956).delta() == 0x00)),
    or_next((word(0x1fe958).delta() == 0x00)),
    (word(0x1fe95a).delta() == 0x00),
    (word(0x1fe944) > 0x00),
    (word(0x1fe946) > 0x00),
    (word(0x1fe948) > 0x00),
    (word(0x1fe94a) > 0x00),
    (word(0x1fe94c) > 0x00),
    (word(0x1fe94e) > 0x00),
    (word(0x1fe950) > 0x00),
    (word(0x1fe952) > 0x00),
    (word(0x1fe954) > 0x00),
    (word(0x1fe956) > 0x00),
    (word(0x1fe958) > 0x00),
    (word(0x1fe95a) > 0x00),
]
ach_589818_alt8 = [
    (byte(0x1fef66) == 0x07),
    (word(0x1fe98c) == 0x00),
    or_next((word(0x1fe994).delta() == 0x00)),
    or_next((word(0x1fe996).delta() == 0x00)),
    or_next((word(0x1fe998).delta() == 0x00)),
    or_next((word(0x1fe99a).delta() == 0x00)),
    or_next((word(0x1fe99c).delta() == 0x00)),
    or_next((word(0x1fe99e).delta() == 0x00)),
    or_next((word(0x1fe9a0).delta() == 0x00)),
    or_next((word(0x1fe9a2).delta() == 0x00)),
    or_next((word(0x1fe9a4).delta() == 0x00)),
    or_next((word(0x1fe9a6).delta() == 0x00)),
    or_next((word(0x1fe9a8).delta() == 0x00)),
    (word(0x1fe9aa).delta() == 0x00),
    (word(0x1fe994) > 0x00),
    (word(0x1fe996) > 0x00),
    (word(0x1fe998) > 0x00),
    (word(0x1fe99a) > 0x00),
    (word(0x1fe99c) > 0x00),
    (word(0x1fe99e) > 0x00),
    (word(0x1fe9a0) > 0x00),
    (word(0x1fe9a2) > 0x00),
    (word(0x1fe9a4) > 0x00),
    (word(0x1fe9a6) > 0x00),
    (word(0x1fe9a8) > 0x00),
    (word(0x1fe9aa) > 0x00),
]
ach_589818_alt9 = [
    (byte(0x1fef66) == 0x08),
    (word(0x1fe9dc) == 0x00),
    or_next((word(0x1fe9e4).delta() == 0x00)),
    or_next((word(0x1fe9e6).delta() == 0x00)),
    or_next((word(0x1fe9e8).delta() == 0x00)),
    or_next((word(0x1fe9ea).delta() == 0x00)),
    or_next((word(0x1fe9ec).delta() == 0x00)),
    or_next((word(0x1fe9ee).delta() == 0x00)),
    or_next((word(0x1fe9f0).delta() == 0x00)),
    or_next((word(0x1fe9f2).delta() == 0x00)),
    or_next((word(0x1fe9f4).delta() == 0x00)),
    or_next((word(0x1fe9f6).delta() == 0x00)),
    or_next((word(0x1fe9f8).delta() == 0x00)),
    (word(0x1fe9fa).delta() == 0x00),
    (word(0x1fe9e4) > 0x00),
    (word(0x1fe9e6) > 0x00),
    (word(0x1fe9e8) > 0x00),
    (word(0x1fe9ea) > 0x00),
    (word(0x1fe9ec) > 0x00),
    (word(0x1fe9ee) > 0x00),
    (word(0x1fe9f0) > 0x00),
    (word(0x1fe9f2) > 0x00),
    (word(0x1fe9f4) > 0x00),
    (word(0x1fe9f6) > 0x00),
    (word(0x1fe9f8) > 0x00),
    (word(0x1fe9fa) > 0x00),
]
ach_589818_alt10 = [
    (byte(0x1fef66) == 0x09),
    (word(0x1fea2c) == 0x00),
    or_next((word(0x1fea34).delta() == 0x00)),
    or_next((word(0x1fea36).delta() == 0x00)),
    or_next((word(0x1fea38).delta() == 0x00)),
    or_next((word(0x1fea3a).delta() == 0x00)),
    or_next((word(0x1fea3c).delta() == 0x00)),
    or_next((word(0x1fea3e).delta() == 0x00)),
    or_next((word(0x1fea40).delta() == 0x00)),
    or_next((word(0x1fea42).delta() == 0x00)),
    or_next((word(0x1fea44).delta() == 0x00)),
    or_next((word(0x1fea46).delta() == 0x00)),
    or_next((word(0x1fea48).delta() == 0x00)),
    (word(0x1fea4a).delta() == 0x00),
    (word(0x1fea34) > 0x00),
    (word(0x1fea36) > 0x00),
    (word(0x1fea38) > 0x00),
    (word(0x1fea3a) > 0x00),
    (word(0x1fea3c) > 0x00),
    (word(0x1fea3e) > 0x00),
    (word(0x1fea40) > 0x00),
    (word(0x1fea42) > 0x00),
    (word(0x1fea44) > 0x00),
    (word(0x1fea46) > 0x00),
    (word(0x1fea48) > 0x00),
    (word(0x1fea4a) > 0x00),
]
ach_589818_alt11 = [
    (byte(0x1fef66) == 0x0a),
    (word(0x1fea7c) == 0x00),
    or_next((word(0x1fea84).delta() == 0x00)),
    or_next((word(0x1fea86).delta() == 0x00)),
    or_next((word(0x1fea88).delta() == 0x00)),
    or_next((word(0x1fea8a).delta() == 0x00)),
    or_next((word(0x1fea8c).delta() == 0x00)),
    or_next((word(0x1fea8e).delta() == 0x00)),
    or_next((word(0x1fea90).delta() == 0x00)),
    or_next((word(0x1fea92).delta() == 0x00)),
    or_next((word(0x1fea94).delta() == 0x00)),
    or_next((word(0x1fea96).delta() == 0x00)),
    or_next((word(0x1fea98).delta() == 0x00)),
    (word(0x1fea9a).delta() == 0x00),
    (word(0x1fea84) > 0x00),
    (word(0x1fea86) > 0x00),
    (word(0x1fea88) > 0x00),
    (word(0x1fea8a) > 0x00),
    (word(0x1fea8c) > 0x00),
    (word(0x1fea8e) > 0x00),
    (word(0x1fea90) > 0x00),
    (word(0x1fea92) > 0x00),
    (word(0x1fea94) > 0x00),
    (word(0x1fea96) > 0x00),
    (word(0x1fea98) > 0x00),
    (word(0x1fea9a) > 0x00),
]
ach_589818_alt12 = [
    (byte(0x1fef66) == 0x0b),
    (word(0x1feacc) == 0x00),
    or_next((word(0x1fead4).delta() == 0x00)),
    or_next((word(0x1fead6).delta() == 0x00)),
    or_next((word(0x1fead8).delta() == 0x00)),
    or_next((word(0x1feada).delta() == 0x00)),
    or_next((word(0x1feadc).delta() == 0x00)),
    or_next((word(0x1feade).delta() == 0x00)),
    or_next((word(0x1feae0).delta() == 0x00)),
    or_next((word(0x1feae2).delta() == 0x00)),
    or_next((word(0x1feae4).delta() == 0x00)),
    or_next((word(0x1feae6).delta() == 0x00)),
    or_next((word(0x1feae8).delta() == 0x00)),
    (word(0x1feaea).delta() == 0x00),
    (word(0x1fead4) > 0x00),
    (word(0x1fead6) > 0x00),
    (word(0x1fead8) > 0x00),
    (word(0x1feada) > 0x00),
    (word(0x1feadc) > 0x00),
    (word(0x1feade) > 0x00),
    (word(0x1feae0) > 0x00),
    (word(0x1feae2) > 0x00),
    (word(0x1feae4) > 0x00),
    (word(0x1feae6) > 0x00),
    (word(0x1feae8) > 0x00),
    (word(0x1feaea) > 0x00),
]
ach_589818_alt13 = [
    (byte(0x1fef66) == 0x0c),
    (word(0x1feb1c) == 0x00),
    or_next((word(0x1feb24).delta() == 0x00)),
    or_next((word(0x1feb26).delta() == 0x00)),
    or_next((word(0x1feb28).delta() == 0x00)),
    or_next((word(0x1feb2a).delta() == 0x00)),
    or_next((word(0x1feb2c).delta() == 0x00)),
    or_next((word(0x1feb2e).delta() == 0x00)),
    or_next((word(0x1feb30).delta() == 0x00)),
    or_next((word(0x1feb32).delta() == 0x00)),
    or_next((word(0x1feb34).delta() == 0x00)),
    or_next((word(0x1feb36).delta() == 0x00)),
    or_next((word(0x1feb38).delta() == 0x00)),
    (word(0x1feb3a).delta() == 0x00),
    (word(0x1feb24) > 0x00),
    (word(0x1feb26) > 0x00),
    (word(0x1feb28) > 0x00),
    (word(0x1feb2a) > 0x00),
    (word(0x1feb2c) > 0x00),
    (word(0x1feb2e) > 0x00),
    (word(0x1feb30) > 0x00),
    (word(0x1feb32) > 0x00),
    (word(0x1feb34) > 0x00),
    (word(0x1feb36) > 0x00),
    (word(0x1feb38) > 0x00),
    (word(0x1feb3a) > 0x00),
]
ach_589818 = Achievement(
    title="""Unshakable Perfection""",
    description="""Claim all 12 championship belts with one fighter without ever losing a match""",
    points=50, type=AchievementType.MISSABLE,
    id=589818, badge="670251"
)
ach_589818.add_core(ach_589818_logic)
ach_589818.add_alt(ach_589818_alt1)
ach_589818.add_alt(ach_589818_alt2)
ach_589818.add_alt(ach_589818_alt3)
ach_589818.add_alt(ach_589818_alt4)
ach_589818.add_alt(ach_589818_alt5)
ach_589818.add_alt(ach_589818_alt6)
ach_589818.add_alt(ach_589818_alt7)
ach_589818.add_alt(ach_589818_alt8)
ach_589818.add_alt(ach_589818_alt9)
ach_589818.add_alt(ach_589818_alt10)
ach_589818.add_alt(ach_589818_alt11)
ach_589818.add_alt(ach_589818_alt12)
ach_589818.add_alt(ach_589818_alt13)
my_set.add_achievement(ach_589818)

# --- Don't Blink! ---
# Logic: 0xH1feff0!=19_0xH1fef84=1_0xH1fef88=0_O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_0xX00002c=1_I:0xW1fe480_d0xM0000c8=0_I:0xW1fe480_0xM0000c8=1
ach_589836_logic = [
    (byte(0x1feff0) != 0x13),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fef88) == 0x00),
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    (dword(0x00002c) == 0x01),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8).delta() == 0x00),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
]
ach_589836 = Achievement(
    title="""Don't Blink!""",
    description="""Score a KO in the first round""",
    points=1,
    id=589836, badge="670253"
)
ach_589836.add_core(ach_589836_logic)
my_set.add_achievement(ach_589836)

# --- Clean Code ---
# Logic: 0xH1feff0!=19_0xH1fef84=1_0xH1fef88=0_O:0xH1feff0=14_0xH1feff0=13_I:0xW1fe480_P:0xH0000ac=1.1._I:0xW1fe480_d0xH000018!=15_I:0xW1fe480_T:0xH000018=15SR:0xH1feff0=10_0xH1feff0=14.1.
ach_589843_logic = [
    (byte(0x1feff0) != 0x13),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fef88) == 0x00),
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    add_address(tbyte(0x1fe480)),
    pause_if((byte(0x0000ac) == 0x01).with_hits(1)),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018).delta() != 0x0f),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_589843_alt1 = [
    reset_if((byte(0x1feff0) == 0x0a)),
    (byte(0x1feff0) == 0x0e).with_hits(1),
]
ach_589843 = Achievement(
    title="""Clean Code""",
    description="""Win a fight without being knocked down""",
    points=2,
    id=589843, badge="670761"
)
ach_589843.add_core(ach_589843_logic)
ach_589843.add_alt(ach_589843_alt1)
my_set.add_achievement(ach_589843)

# --- Human Dynamometer ---
# Logic: 0xH1feff0!=19_O:0xH1feff0=14_0xH1feff0=13_0xH1fef88=0_0xH1fef84=1_O:0x 1fee54>=500_O:0x 1fee58>=500_0x 1fee5c>=500_I:0xW1fe480_d0xH0000c0=0_I:0xW1fe480_0xH0000c0=1
ach_589908_logic = [
    (byte(0x1feff0) != 0x13),
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    or_next((word(0x1fee54) >= 0x1f4)),
    or_next((word(0x1fee58) >= 0x1f4)),
    (word(0x1fee5c) >= 0x1f4),
    add_address(tbyte(0x1fe480)),
    (byte(0x0000c0).delta() == 0x00),
    add_address(tbyte(0x1fe480)),
    (byte(0x0000c0) == 0x01),
]
ach_589908 = Achievement(
    title="""Human Dynamometer""",
    description="""Knock down your opponent with a strike that registers 100kg or more of force on the impact panel""",
    points=2,
    id=589908, badge="670762"
)
ach_589908.add_core(ach_589908_logic)
my_set.add_achievement(ach_589908)

# --- Optimized Defense ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef88=0_0xH1fef84=1_A:0x 1fedd8_B:0x 1feddc_0x 1fedd8>0_I:0xW1fe480_0xH0000b0>0_I:0xW1fe480_0xH0000c0=1_I:0xW1fe480_d0xH000018!=15_I:0xW1fe480_0xH000018=15
ach_589930_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    add_source(word(0x1fedd8)),
    sub_source(word(0x1feddc)),
    (word(0x1fedd8) > 0x00),
    add_address(tbyte(0x1fe480)),
    (byte(0x0000b0) > 0x00),
    add_address(tbyte(0x1fe480)),
    (byte(0x0000c0) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018).delta() != 0x0f),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x0f),
]
ach_589930 = Achievement(
    title="""Optimized Defense""",
    description="""Win a fight while maintaining over 50% HP""",
    points=2,
    id=589930, badge="670763"
)
ach_589930.add_core(ach_589930_logic)
my_set.add_achievement(ach_589930)

# --- [VOID]Reverse Logic ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef88=0_0xH1fef84=1_O:0x 1fee54>d0x 1fee54_O:0x 1fee58>d0x 1fee58_0x 1fee5c>d0x 1fee5c_O:0x 1fee54>=100_O:0x 1fee58>=100_0x 1fee5c>=100_I:0xW1fe480_d0xM0000c8=0_I:0xW1fe480_0xM0000c8=1
ach_589931_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    or_next((word(0x1fee54) > word(0x1fee54).delta())),
    or_next((word(0x1fee58) > word(0x1fee58).delta())),
    (word(0x1fee5c) > word(0x1fee5c).delta()),
    or_next((word(0x1fee54) >= 0x64)),
    or_next((word(0x1fee58) >= 0x64)),
    (word(0x1fee5c) >= 0x64),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8).delta() == 0x00),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
]
ach_589931 = Achievement(
    title="""[VOID]Reverse Logic""",
    description="""KO an opponent using a Counter""",
    points=5,
    id=589931, badge="670764"
)
ach_589931.add_core(ach_589931_logic)
my_set.add_achievement(ach_589931)

# --- Human Projectile ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef88=0_0xH1fef84=1_R:0x 1fedd8<d0x 1fedd8_I:0xW1fe480_P:0xM0000d4=1_R:0x 1fee10=d0x 1fee10.120._0x 1fee10<d0x 1fee10.5.
ach_589932_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    reset_if((word(0x1fedd8) < word(0x1fedd8).delta())),
    add_address(tbyte(0x1fe480)),
    pause_if((bit0(0x0000d4) == 0x01)),
    reset_if((word(0x1fee10) == value(0)).with_hits(120)),
    (word(0x1fee10) < value(0)).with_hits(5),
]
ach_589932 = Achievement(
    title="""Human Projectile""",
    description="""Land 5 consecutive hits without the opponent blocking""",
    points=2,
    id=589932, badge="670765"
)
ach_589932.add_core(ach_589932_logic)
my_set.add_achievement(ach_589932)

# --- Ring Dance ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef88=0_0xH1fef84=1.1._0x 1feddc>0_R:0x 1fedd8<0x 1feddcSI:0xW1fe480_0xH0000b0>0_I:0xW1fe480_0xH0000c0=1_I:0xW1fe480_d0xH000018!=15_I:0xW1fe480_T:0xH000018=15SI:0xW1fe480_N:d0xX00002c>0_I:0xW1fe480_T:d0xX00002c<0xX00002c
ach_589933_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01).with_hits(1),
    (word(0x1feddc) > 0x00),
    reset_if((word(0x1fedd8) < word(0x1feddc))),
]
ach_589933_alt1 = [
    add_address(tbyte(0x1fe480)),
    (byte(0x0000b0) > 0x00),
    add_address(tbyte(0x1fe480)),
    (byte(0x0000c0) == 0x01),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018).delta() != 0x0f),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_589933_alt2 = [
    add_address(tbyte(0x1fe480)),
    and_next((dword(0x00002c).delta() > 0x00)),
    add_address(tbyte(0x1fe480)),
    trigger((dword(0x00002c).delta() < dword(0x00002c))),
]
ach_589933 = Achievement(
    title="""Ring Dance""",
    description="""Survive an entire round without being hit""",
    points=5,
    id=589933, badge="670801"
)
ach_589933.add_core(ach_589933_logic)
ach_589933.add_alt(ach_589933_alt1)
ach_589933.add_alt(ach_589933_alt2)
my_set.add_achievement(ach_589933)

# --- The Amazing Chicken ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef88=0_0xH1fef84=1_O:0xH1feff0=10_Z:0xH1feff0=9_I:0xW1fe480_N:0xX00002c=1_P:0x 1fee10<d0x 1fee10.1._I:0xW1fe480_0xH00002c>1_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_589934_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    or_next((byte(0x1feff0) == 0x0a)),
    reset_next_if((byte(0x1feff0) == 0x09)),
    add_address(tbyte(0x1fe480)),
    and_next((dword(0x00002c) == 0x01)),
    pause_if((word(0x1fee10) < value(0)).with_hits(1)),
    add_address(tbyte(0x1fe480)),
    (byte(0x00002c) > 0x01),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_589934 = Achievement(
    title="""The Amazing Chicken""",
    description="""Run away for an entire round without attacking and win the fight afterward""",
    points=5,
    id=589934, badge="670802"
)
ach_589934.add_core(ach_589934_logic)
my_set.add_achievement(ach_589934)

# --- Feline Reflex ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef88=0_0xH1fef84=1_R:0x 1fedd8<d0x 1fedd8_N:0x 1fee60!=0_C:0x 1fee60!=d0x 1fee60_N:0x 1fee64!=0_C:0x 1fee64!=d0x 1fee64_N:0x 1fee68!=0_0x 1fee68!=d0x 1fee68.5.
ach_591285_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    reset_if((word(0x1fedd8) < word(0x1fedd8).delta())),
    and_next((word(0x1fee60) != 0x00)),
    add_hits((word(0x1fee60) != word(0x1fee60).delta())),
    and_next((word(0x1fee64) != 0x00)),
    add_hits((word(0x1fee64) != word(0x1fee64).delta())),
    and_next((word(0x1fee68) != 0x00)),
    (word(0x1fee68) != value(0)).with_hits(5),
]
ach_591285 = Achievement(
    title="""Feline Reflex""",
    description="""Block or evade 5 consecutive attacks""",
    points=5,
    id=591285, badge="670803"
)
ach_591285.add_core(ach_591285_logic)
my_set.add_achievement(ach_591285)

# --- Floor Sweeper ---
# Logic: 0xH1fef88=0_0xH1fef84=1_O:0xH1feff0=14_0xH1feff0=13_R:0xH1feff0=9_I:0xW1fe480_0xH0000b0>d0xH0000b0.1._I:0xW1fe480_N:0xW000148=2_I:0xW1fe480_R:0xH0000c0=0_I:0xW1fe480_d0xM0000c8=0_I:0xW1fe480_0xM0000c8=1
ach_591418_logic = [
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    reset_if((byte(0x1feff0) == 0x09)),
    add_address(tbyte(0x1fe480)),
    (byte(0x0000b0) > value(0)).with_hits(1),
    add_address(tbyte(0x1fe480)),
    and_next((tbyte(0x000148) == 0x02)),
    add_address(tbyte(0x1fe480)),
    reset_if((byte(0x0000c0) == 0x00)),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8).delta() == 0x00),
    add_address(tbyte(0x1fe480)),
    (bit0(0x0000c8) == 0x01),
]
ach_591418 = Achievement(
    title="""Floor Sweeper""",
    description="""K.O your opponent using a special move""",
    points=5,
    id=591418, badge="670804"
)
ach_591418.add_core(ach_591418_logic)
my_set.add_achievement(ach_591418)

# --- Noble Final Act ---
# Logic: 0xH1fef66=5_0xH1fe8bf=2_d0xH1fe8c1=1_0xH1fe8c1=0_I:0xW1fe480_d0xH000018!=19_I:0xW1fe480_0xH000018=19
ach_591419_logic = [
    (byte(0x1fef66) == 0x05),
    (byte(0x1fe8bf) == 0x02),
    (byte(0x1fe8c1).delta() == 0x01),
    (byte(0x1fe8c1) == 0x00),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018).delta() != 0x13),
    add_address(tbyte(0x1fe480)),
    (byte(0x000018) == 0x13),
]
ach_591419 = Achievement(
    title="""Noble Final Act""",
    description="""Win the World Championship as Prince in any weight class""",
    points=5,
    id=591419, badge="671053"
)
ach_591419.add_core(ach_591419_logic)
my_set.add_achievement(ach_591419)

# --- Sparring of a Lifetime ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef74=2_O:0x 1fe564=75_0x 1fe564=100_0xH1fef88=0_0xH1fef84=1_0xH1fedb0=0_0xH1fede8=7_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_591420_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef74) == 0x02),
    or_next((word(0x1fe564) == 0x4b)),
    (word(0x1fe564) == 0x64),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fedb0) == 0x00),
    (byte(0x1fede8) == 0x07),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_591420 = Achievement(
    title="""Sparring of a Lifetime""",
    description="""As Tanaka, defeat Silver Man on Hard difficulty or higher""",
    points=2,
    id=591420, badge="671069"
)
ach_591420.add_core(ach_591420_logic)
my_set.add_achievement(ach_591420)

# --- The Script Changed ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef74=2_O:0x 1fe564=75_0x 1fe564=100_0xH1fef88=0_0xH1fef84=1_0xH1fedb0=1_0xH1fede8=0_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_591421_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef74) == 0x02),
    or_next((word(0x1fe564) == 0x4b)),
    (word(0x1fe564) == 0x64),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fedb0) == 0x01),
    (byte(0x1fede8) == 0x00),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_591421 = Achievement(
    title="""The Script Changed""",
    description="""As Ryoko, defeat her father Tanaka on Hard difficulty or higher""",
    points=5,
    id=591421, badge="671070"
)
ach_591421.add_core(ach_591421_logic)
my_set.add_achievement(ach_591421)

# --- End of the Shadow ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef74=2_O:0x 1fe564=75_0x 1fe564=100_0xH1fef88=0_0xH1fef84=1_0xH1fedb0=2_0xH1fede8=1_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_591422_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef74) == 0x02),
    or_next((word(0x1fe564) == 0x4b)),
    (word(0x1fe564) == 0x64),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fedb0) == 0x02),
    (byte(0x1fede8) == 0x01),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_591422 = Achievement(
    title="""End of the Shadow""",
    description="""As Red, finally defeat his colleague Ryoko on Hard difficulty or higher""",
    points=5,
    id=591422, badge="671071"
)
ach_591422.add_core(ach_591422_logic)
my_set.add_achievement(ach_591422)

# --- Number One Fan ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef74=2_O:0x 1fe564=75_0x 1fe564=100_0xH1fef88=0_0xH1fef84=1_0xH1fedb0=6_0xH1fede8=11_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_591423_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef74) == 0x02),
    or_next((word(0x1fe564) == 0x4b)),
    (word(0x1fe564) == 0x64),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fedb0) == 0x06),
    (byte(0x1fede8) == 0x0b),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_591423 = Achievement(
    title="""Number One Fan""",
    description="""As Misha, defeat her hero Asteka on Hard difficulty or higher""",
    points=10,
    id=591423, badge="671086"
)
ach_591423.add_core(ach_591423_logic)
my_set.add_achievement(ach_591423)

# --- Childhood Pact ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef74=2_O:0x 1fe564=75_0x 1fe564=100_0xH1fef88=0_0xH1fef84=1_0xH1fedb0=5_0xH1fede8=8_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_591424_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef74) == 0x02),
    or_next((word(0x1fe564) == 0x4b)),
    (word(0x1fe564) == 0x64),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fedb0) == 0x05),
    (byte(0x1fede8) == 0x08),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_591424 = Achievement(
    title="""Childhood Pact""",
    description="""As Prince, defeat his friend Gio on Hard difficulty or higher""",
    points=3,
    id=591424, badge="671087"
)
ach_591424.add_core(ach_591424_logic)
my_set.add_achievement(ach_591424)

# --- Final Service ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef74=2_O:0x 1fe564=75_0x 1fe564=100_0xH1fef88=0_0xH1fef84=1_0xH1fedb0=10_0xH1fede8=12_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_591425_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef74) == 0x02),
    or_next((word(0x1fe564) == 0x4b)),
    (word(0x1fe564) == 0x64),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fedb0) == 0x0a),
    (byte(0x1fede8) == 0x0c),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_591425 = Achievement(
    title="""Final Service""",
    description="""As Spice, defeat Mr. Crown on Hard difficulty or higher""",
    points=10,
    id=591425, badge="671088"
)
ach_591425.add_core(ach_591425_logic)
my_set.add_achievement(ach_591425)

# --- Master of Evasion ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef74=2_0x 1fe564=100_0xH1fef84=1_0xH1fef88=0_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_591426_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef74) == 0x02),
    (word(0x1fe564) == 0x64),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fef88) == 0x00),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_591426 = Achievement(
    title="""Master of Evasion""",
    description="""Win a fight on Very Hard difficulty""",
    points=5,
    id=591426, badge="671090"
)
ach_591426.add_core(ach_591426_logic)
my_set.add_achievement(ach_591426)

# --- Shadow Boxing ---
# Logic: O:0xH1feff0=14_0xH1feff0=13_0xH1fef74=2_0x 1fe564=100_0xH1fef88=0_0xH1fef84=1_0xH1fedb0=0xH1fede8_I:0xW1fe480_N:0xH0000b0>0_I:0xW1fe480_N:0xH0000c0=1_I:0xW1fe480_N:d0xH000018!=15_I:0xW1fe480_T:0xH000018=15
ach_591427_logic = [
    or_next((byte(0x1feff0) == 0x0e)),
    (byte(0x1feff0) == 0x0d),
    (byte(0x1fef74) == 0x02),
    (word(0x1fe564) == 0x64),
    (byte(0x1fef88) == 0x00),
    (byte(0x1fef84) == 0x01),
    (byte(0x1fedb0) == byte(0x1fede8)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000b0) > 0x00)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x0000c0) == 0x01)),
    add_address(tbyte(0x1fe480)),
    and_next((byte(0x000018).delta() != 0x0f)),
    add_address(tbyte(0x1fe480)),
    trigger((byte(0x000018) == 0x0f)),
]
ach_591427 = Achievement(
    title="""Shadow Boxing""",
    description="""Win a fight in Exhibition mode against the same character you are using on Very Hard difficulty""",
    points=10,
    id=591427, badge="671091"
)
ach_591427.add_core(ach_591427_logic)
my_set.add_achievement(ach_591427)

my_set.save()