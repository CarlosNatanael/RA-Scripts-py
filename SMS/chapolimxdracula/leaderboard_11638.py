from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=11638, title="Imported Leaderboards")

# --- LB: High Score ---
lb_start = [
    (byte(0x0191) == 0x10),
    (byte(0x01bb).delta() == 0x00),
    (byte(0x01bb) == 0x05),
]
lb_cancel = [
    (byte(0x01bb) == 0x00),
]
lb_submit = [
    (value(0) == value(0)),
]
lb_submit_alt1 = [
    (byte(0x01df).delta() != 0x07),
    (byte(0x01df) == 0x07),
]
lb_submit_alt2 = [
    (byte(0x01e0).delta() != 0xff),
    (byte(0x01e0) == 0xff),
]
lb_value = [
    measured(tbyte(0x01e8).bcd() * 10),
]
lb = Leaderboard(
    title="""High Score""",
    description="""Highest score achieved upon completing the game or receiving a Game Over""",
    id=162403,
    format=LeaderboardFormat.SCORE,
    lower_is_better=False
)
lb.set_start(lb_start)
lb.set_cancel(lb_cancel)
lb.set_submit(lb_submit, lb_submit_alt1, lb_submit_alt2)
lb.set_value(lb_value)
my_set.add_leaderboard(lb)
my_set.save()