from pycheevos.core.helpers import byte, word
from pycheevos.models.rich_presence import RichPresence

rp = RichPresence()

# 1. LOOKUPS
rp.add_lookup("Teams", {
    0: "Austria", 1: "Belgium", 2: "Bulgaria", 3: "Croatia", 4: "Czech Republic",
    5: "Denmark", 6: "England", 7: "Finland", 8: "France", 9: "Germany",
    10: "Greece", 11: "Hungary", 12: "Ireland", 13: "Israel", 14: "Italy",
    15: "Netherlands", 16: "Northern Ireland", 17: "Norway", 18: "Poland", 19: "Portugal",
    20: "Romania", 21: "Russia", 22: "Scotland", 23: "Serbia", 24: "Slovakia",
    25: "Slovenia", 26: "Spain", 27: "Sweden", 28: "Switzerland", 29: "Turkey",
    30: "Ukraine", 31: "Wales", 32: "Algeria", 33: "Cameroon", 34: "Cote d'Ivoire",
    35: "Egypt", 36: "Ghana", 37: "Nigeria", 38: "South Africa", 39: "Zambia",
    40: "Costa Rica", 41: "Honduras", 42: "Mexico", 43: "USA", 44: "Argentina",
    45: "Brazil", 46: "Chile", 47: "Colombia", 48: "Ecuador", 49: "Paraguay",
    50: "Peru", 51: "Uruguay", 52: "Australia", 53: "China", 54: "Japan",
    55: "North Korea", 56: "Saudi Arabia", 57: "South Korea", 58: "UAE", 59: "New Zealand",
    67: "North London", 68: "West Midlands Village", 69: "South Wales", 70: "London FC",
    71: "South East London", 72: "Merseyside Blue", 73: "West London White", 74: "Yorkshire Orange",
    75: "Merseyside Red", 76: "Man Blue", 77: "Manchester United", 78: "Tyneside",
    79: "Northluck C", 80: "Soton", 81: "The Potteries", 82: "Wearside", 83: "Swearcle",
    84: "North East London", 85: "West Midlands Stripes", 86: "East London", 87: "AC Ajaccio",
    88: "SC Bastia", 89: "Girondins de Bordeaux", 90: "Evian Thonon Gaillard", 91: "EA Guingamp",
    92: "LOSC Lille", 93: "FC Lorient", 94: "Olympique Lyonnais", 95: "Olympique de Marseille",
    96: "AS Monaco FC", 97: "Montpellier Herault SC", 98: "FC Nantes", 99: "OGC Nice",
    100: "Paris Saint-Germain", 101: "Stade de Reims", 102: "Stade Rennais FC", 103: "AS Saint-Etienne",
    104: "FC Sochaux-Montbeliard", 105: "Toulouse FC", 106: "Valenciennes FC", 107: "Atalanta B.C.",
    108: "Bologna", 109: "Cagliari Calcio", 110: "Calcio Catania", 111: "A.C. Chievo Verona",
    112: "Fiorentina", 113: "Genoa CFC", 114: "Internazionale", 115: "Juventus",
    116: "Lazio", 117: "A.S. Livorno", 118: "A.C. Milan", 119: "Napoli",
    120: "Parma FC", 121: "Roma", 122: "Sampdoria", 123: "Sassuolo",
    124: "Torino FC", 125: "Udinese Calcio", 126: "Verona", 127: "ADO Den Haag",
    128: "Ajax FC", 129: "AZ", 130: "Cambuur Leeuwarden", 131: "Feyenoord",
    132: "Go Ahead Eagles", 133: "FC Groningen", 134: "SC Heerenveen", 135: "Heracles Almelo",
    136: "NAC Breda", 137: "N.E.C. Nijmegen", 138: "PSV", 139: "RKC Waalwijk",
    140: "Roda JC Kerkrade", 141: "FC Twente", 142: "FC Utrecht", 143: "Vitesse",
    144: "PEC Zwolle", 145: "UD Almeria", 146: "Athletic Club", 147: "At. Madrid",
    148: "FC Barcelona", 149: "Real Betis", 150: "Celta de Vigo", 151: "Elche CF",
    152: "RCD Espanyol", 153: "Getafe CF", 154: "Granada CF", 155: "Malaga CF",
    156: "Levante UD", 157: "CA Osasuna", 158: "Rayo Vallecano", 159: "Real Madrid",
    160: "Real Sociedad", 161: "Sevilla FC", 162: "Valencia CF", 163: "Real Valladolid",
    164: "Villarreal CF", 165: "RSC Anderlecht", 166: "APOEL FC", 167: "Sparta Praha",
    168: "F.C. Copenhagen", 169: "Nordsjaelland", 170: "Bayer 04 Leverkusen", 171: "Bayern Munchen",
    172: "Schalke 04", 173: "Olympiacos FC", 174: "PAOK F.C.", 175: "Maccabi Tel Aviv",
    176: "Legia Warszawa", 177: "SL Benfica", 178: "S.C. Braga", 179: "Pacos de Ferreira",
    180: "FC Porto", 181: "CSKA Moskva", 182: "FC Zenit", 183: "Celtic FC",
    184: "Motherwell FC", 185: "Galatasaray A.S.", 186: "Shakhtar Donetsk", 187: "Almchendolf",
    188: "Ehrenhofstadt", 189: "Fineseeberg", 190: "Kriedbach", 191: "Lengerblitz",
    192: "Theeselvargen", 193: "PES United", 194: "WE United", 237: "Arsenal F.C.",
    238: "Boca Juniors", 239: "Newell's Old Boys", 240: "Tigre", 241: "Velez Sarsfield",
    242: "Club Bolivar", 243: "San Jose", 244: "The Strongest", 245: "Atletico Mineiro",
    246: "Corinthians", 247: "Fluminense", 248: "Gremio", 249: "Palmeiras",
    250: "Sao Paulo", 251: "Huachipato", 252: "Deportes Iquique", 253: "Universidad de Chile",
    254: "Deportes Tolima", 255: "Millonarios", 256: "Santa Fe", 257: "Barcelona S.C.",
    258: "Emelec", 259: "Liga de Quito", 260: "Leon", 261: "Tijuana",
    262: "Toluca", 263: "Cerro Porteno", 264: "Club Libertad", 265: "Olimpia",
    266: "Real Garcilaso", 267: "Sporting Cristal", 268: "Cesar Vallejo", 269: "Defensor Sporting",
    270: "Nacional", 271: "Penarol", 272: "Caracas F.C.", 273: "Deportivo Anzoategui",
    274: "Deportivo Lara", 275: "ML United", 276: "AC Maestore", 277: "AS Victoire",
    278: "CA Especialista", 279: "Bravona", 280: "FC Aries", 281: "FC Taurus",
    282: "AC Gemini", 283: "AS Cancer", 284: "AC Leo", 285: "AS Virgo",
    286: "Libra FC", 287: "Scorpio FC", 288: "FC Sagittarius", 289: "AS Capricorn",
    290: "AC Aquarius", 291: "Pisces FC", 292: "WE Japan", 293: "English All-Stars",
    294: "French", 295: "Germany", 296: "Italian", 297: "Dutch",
    298: "Spannish", 299: "Argentinian", 300: "Brazilian", 301: "AS Mohican",
    302: "FC Magerio", 303: "Longuedez", 304: "Bosedez", 305: "Maccingami FC",
    326: "Manchester United", 327: "Bayern Munchen", 328: "Bayer 04 Leverkusen", 329: "Schalke 04",
    330: "FC Barcelona", 331: "Real Madrid", 332: "At. Madrid", 333: "Real Sociedad",
    334: "Juventus", 335: "Napoli", 336: "A.C. Milan", 337: "FC Porto",
    338: "SL Benfica", 339: "Pacos de Ferreira", 340: "Paris Saint-Germain", 341: "Olympique de Marseille",
    342: "Olympique Lyonnais", 343: "CSKA Moskva", 344: "FC Zenit", 345: "Ajax FC",
    346: "PSV", 347: "Shakhtar Donetsk", 348: "Olympiacos FC", 349: "PAOK F.C.",
    350: "Galatasaray A.S.", 351: "RSC Anderlecht", 352: "F.C. Copenhagen", 353: "Nordsjaelland",
    354: "APOEL FC", 355: "Maccabi Tel Aviv", 356: "Celtic FC", 357: "Legia Warszawa"
}, default="")

rp.add_lookup("Period", {
    0: "1st Half",
    1: "2nd Half",
    2: "1st Half Extra Time",
    3: "2nd Half Extra Time",
    4: "Penalty Shootout"
}, default="")

# 2. ALIASES DE MEMÓRIA
mem_period = byte(0x00d41c06)
mem_lang   = byte(0x0056ae70)
mem_team1 = word(0x0062f4de)
mem_team2 = word(0x0062f4e0)

# Placar Tempo Normal
mem_score1 = byte(0x00d41bf6)
mem_score2 = byte(0x00d41bfa)

# Temporizador
mem_time_m10 = byte(0x00d41c09)
mem_time_m1  = byte(0x00d41c08)
mem_time_s10 = byte(0x00d41c0b)
mem_time_s1  = byte(0x00d41c0a)

# Placar Disputa de Pênaltis
mem_pen_score1 = byte(0x00d316ec)
mem_pen_score2 = byte(0x00d319e0)

rp.add_format("Value", "VALUE")

# 3. DISPLAYS
# Linguagem do jogo
rp.add_lookup("Language", {
    0: "🇺🇸",
    4: "🇪🇸",
    10: "🇵🇹",
    12: "🇷🇺",
    14: "🇸🇪",
    15: "🇳🇱",
    17: "🇹🇷"
}, default="")

# Partida no tempo regulamentar ou prorrogação
rp.add_display(
    [mem_period <= 3],
    f"{RichPresence.lookup('Language', mem_lang)}: "
    f"{RichPresence.lookup('Period', mem_period)} | "
    f"{RichPresence.lookup('Teams', mem_team1)} {RichPresence.value(mem_score1)}-{RichPresence.value(mem_score2)} {RichPresence.lookup('Teams', mem_team2)} | "
    f"⌚ Time: {RichPresence.value(mem_time_m10)}{RichPresence.value(mem_time_m1)}:{RichPresence.value(mem_time_s10)}{RichPresence.value(mem_time_s1)}"
)

# Partida nos pênaltis (4)
rp.add_display(
    [mem_period == 4],
    f"{RichPresence.lookup('Language', mem_lang)}: "
    f"{RichPresence.lookup('Period', mem_period)} | "
    f"{RichPresence.lookup('Teams', mem_team1)} {RichPresence.value(mem_pen_score1)}-{RichPresence.value(mem_pen_score2)} {RichPresence.lookup('Teams', mem_team2)}"
)

# Fallback
rp.add_display([], "Playing PES 2014: Pro Evolution Soccer")

print(rp)