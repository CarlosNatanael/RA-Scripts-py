from pycheevos.core.helpers import *
from pycheevos.core.constants import LeaderboardFormat
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=41205, title="Pokémon FireRed - Leaderboards")

mem_trainer_id = word(0x0406ae)
mem_battle_out = byte(0x02be8a)
ptr_save2      = tbyte(0x00500c)

mem_hours   = word(0x00800e)
mem_minutes = byte(0x008010)
mem_seconds = byte(0x008011)
mem_frames  = byte(0x008012)

lb = Leaderboard(
    id=169800,
    title="Hall of Fame - Speedrun",
    description="Defeat the Pokémon League Champion and complete the game as fast as possible",
    format=LeaderboardFormat.FRAMES,
    lower_is_better=True
)

lb.start = [[
    or_next(mem_trainer_id == 438),
    or_next(mem_trainer_id == 439),
    (mem_trainer_id == 440),
    (mem_battle_out == 1),
    (mem_battle_out.delta() == 0),
]]

lb.cancel = [[always_false()]]

lb.submit = [[always_true()]]

lb.value = [[
    add_address(ptr_save2),
    add_source(mem_hours * 216000), 
    add_address(ptr_save2),
    add_source(mem_minutes * 3600),
    add_address(ptr_save2),
    add_source(mem_seconds * 60),
    add_address(ptr_save2),
    measured(mem_frames),
]]

my_set.add_leaderboard(lb)
my_set.save()