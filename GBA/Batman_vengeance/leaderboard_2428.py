from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=2428, title="Imported Leaderboards")

leaderboard_data = [
    (28,  "08",  "Level 8",    0),
    (29,  "09",  "Level 9",    1),
    (33,  "13",  "Level 13",   2),
    (35,  "15",  "Level 15",   3),
]

for level_val, country, adjective, lb_id in leaderboard_data:
    
    next_level = level_val + 1

    # Retornamos o value() para garantir que a PyCheevos gere os objetos corretamente
    lb_start = [
        (byte(0x003db8) == value(1)),
        (byte(0x003da8) == value(level_val)),
        (byte(0x003da8).delta() != value(level_val)),
    ]
    
    lb_cancel = [
        (byte(0x003da8) != value(level_val)),
        (byte(0x003da8) != value(next_level)),
        (byte(0x003da8).delta() == value(level_val)),
    ]
    
    lb_submit = [
        (byte(0x003db8) == value(1)),
        (byte(0x003da8) == value(next_level)),
        (byte(0x003da8).delta() == value(level_val)),
    ]
    
    lb_value = [
        add_source(byte(0x00002c) * 60),
        add_source(byte(0x00002b) * 10),
        measured(byte(0x00002a) * 1), 
    ]
    
    # Criamos a Leaderboard passando o ID do loop
    lb = Leaderboard(
        id=lb_id,
        title=f"Advanced Trial {country}: Batman",
        description=f"Complete Advanced Mode {adjective}. Ranked by the highest time remaining on the clock",
        format=LeaderboardFormat.VALUE,
        lower_is_better=False
    )
    
    lb.set_start(lb_start)
    lb.set_cancel(lb_cancel)
    lb.set_submit(lb_submit)
    lb.set_value(lb_value)
    
    my_set.add_leaderboard(lb)

my_set.save()