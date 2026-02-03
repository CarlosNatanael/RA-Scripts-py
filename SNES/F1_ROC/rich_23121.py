from pycheevos.models.rich_presence import RichPresence
from pycheevos.core.helpers import byte, word

# 1. Instanciar o Rich Presence
rp = RichPresence()

# 2. Mapeamento de Memória (Variables)
mem_state   = byte(0x0007dd)
mem_track   = byte(0x0013de)
mem_weather = byte(0x0013e0)
mem_season  = byte(0x0013e6)
mem_money   = word(0x0013e2)
mem_points  = byte(0x001468)
mem_lap     = byte(0x0000a9)
mem_pos     = byte(0x0007d9)

# 3. Definição dos Lookups (Dicionários)

# GameState
lookup_gamestate = {
    0x01: "Training results screen",
    0x10: "In the Menus",
    0x0c: "Viewing Next Track",
    0x06: "Reviewing Race Results",
    0x08: "Reviewing Race Results",
    0x04: "Reviewing Race Results",
    0x03: "Reviewing Race Results",
    0x0b: "Saving Progress",
    0x11: "Setting up the Car",
    0x0e: "In Qualifying",
    0x05: "Viewing Qualy Results",
    0x07: "Overall Classification Results Screen",
    0x0d: "Racing",
    0x0a: "Casino Minigame"
}
rp.add_lookup("GameState", lookup_gamestate, default="Loading...")

# Track
lookup_track = {
    0x00: "in Italy",
    0x01: "in Great Britain",
    0x02: "in Germany",
    0x03: "in Brazil",
    0x04: "in San Marino",
    0x05: "in Spain",
    0x06: "in Portugal",
    0x07: "in Mexico",
    0x08: "in Hungary",
    0x09: "in Canada",
    0x0a: "in France",
    0x0b: "in Belgium",
    0x0c: "in Australia",
    0x0d: "in the USA",
    0x0e: "in Monaco",
    0x0f: "in Japan"
}
rp.add_lookup("Track", lookup_track, default=" ")

# Weather
lookup_weather = {
    0x00: "☀️",
    0x01: "🌧️",
    0x02: "⛈️"
}
rp.add_lookup("Weather", lookup_weather, default=" ")

# Lap
lookup_lap = {
    0x01: "Lap 1/3",
    0x02: "Lap 2/3",
    0x03: "Lap 3/3",
    0x04: "Finished 🏁"
}
rp.add_lookup("Lap", lookup_lap, default="")

# Position
lookup_pos = {
    0x00: "(1st Place)",
    0x01: "(2nd Place)",
    0x02: "(3rd Place)",
    0x03: "(4th Place)",
    0x04: "(5th Place)",
    0x05: "(6th Place)",
    0x06: "(7th Place)",
    0x07: "(8th Place)"
}
rp.add_lookup("Position", lookup_pos, default="")

# 4. Definição dos Formatos (Value)
rp.add_format("Money", "VALUE")
rp.add_format("Points", "VALUE")
rp.add_format("Season", "VALUE")


# Training
rp.add_display(mem_state == 1, f"@GameState({mem_state})")

# Menus
rp.add_display(mem_state == 16, f"@GameState({mem_state})")

# Car Setup
rp.add_display(
    mem_state == 17, 
    f"@GameState({mem_state}) @Track({mem_track}) @Weather({mem_weather}) | Season @Season({mem_season}) | $@Money({mem_money}*10)"
)
# Casino
rp.add_display(
    mem_state == 10, 
    f"@GameState({mem_state}) @Track({mem_track}) @Weather({mem_weather}) | $@Money({mem_money}*10)"
)

# Next Track
rp.add_display(
    mem_state == 12, 
    f"@GameState({mem_state}): @Track({mem_track}) @Weather({mem_weather}) | Season @Season({mem_season}) | $@Money({mem_money}*10) | Pts:@Points({mem_points})"
)

results_condition = (
    (mem_state == 3) | (mem_state == 4) | (mem_state == 6) | 
    (mem_state == 7) | (mem_state == 8)
)
rp.add_display(
    results_condition, 
    f"@GameState({mem_state}) @Track({mem_track}) @Weather({mem_weather}) @Position({mem_pos}) | Pts:@Points({mem_points})"
)
# Qualifying
rp.add_display(
    mem_state == 14, 
    f"@GameState({mem_state}) @Track({mem_track}) @Weather({mem_weather}) | @Lap({mem_lap}) | Pts:@Points({mem_points})"
)
# Viewing Qualy Results
rp.add_display(
    mem_state == 5, 
    f"@GameState({mem_state}) @Track({mem_track}) @Weather({mem_weather}) | Pts:@Points({mem_points})"
)
# Save Screen
rp.add_display(
    mem_state == 11, 
    f"@GameState({mem_state}) | Season @Season({mem_season}) | $@Money({mem_money}*10) | Pts:@Points({mem_points})"
)
# Racing
rp.add_display(
    mem_state == 13, 
    f"@GameState({mem_state}) @Track({mem_track}) @Weather({mem_weather}) | @Lap({mem_lap}) | @Position({mem_pos})"
)
# Default String (Sem condição = Fallback)
rp.add_display(None, "Playing F1 ROC: Race of Champions")
print(rp)