from pycheevos.core.helpers import byte
from pycheevos.models.achievement import Achievement
from pycheevos.models.set import AchievementSet
from pycheevos.core.constants import AchievementType

meu_set = AchievementSet(game_id=36353, title="Veteran Rank")

# =======================================================================
# 1. ALIAS DE MEMÓRIA (Core)
# =======================================================================
mem_screen = byte(0x1feff0) # Screen ID / Game State
mem_char   = byte(0x1fef66) # P1 Character ID (Championship/Ranking)

# =======================================================================
# 2. CONSTANTES DE ENDEREÇOS
# =======================================================================
BASE_RANK   = 0x1fe733 # Endereço "Fighter Rank Category" do Tanaka
OFFSET_CHAR = 0x50     # Distância de bytes entre os lutadores

# =======================================================================
# 3. CRIAÇÃO DA CONQUISTA
# =======================================================================
ach = Achievement(
    id=118000,
    title="True Veteran",
    description="Reach Veteran level with any character",
    points=10,
    badge="00000",
    type=AchievementType.PROGRESSION
)

# --- CORE GROUP (Segurança) ---
# Evita que a conquista ative na tela de Load/Save (19 em decimal / 0x13)
ach.add_core([
    mem_screen != 19
])

# --- ALT GROUPS (Checando os personagens) ---
# Loop que passa por todos os 13 lutadores (IDs de 0 a 12)
for char_id in range(13):
    
    # Calcula o endereço do Rank específico para este lutador
    # O Python faz a conta sozinho: 0x1fe733 + (ID * 0x50)
    char_rank = byte(BASE_RANK + (char_id * OFFSET_CHAR))
    
    # Adiciona o grupo Alt com as 3 condições para este lutador
    ach.add_alt([
        mem_char == char_id,        # 1: Lutador é o correto (Tanaka, Ryoko, etc)
        char_rank.delta() < 101,    # 2: Frame passado: Rank era menor que 101
        char_rank == 101            # 3: Frame atual: Rank chegou a 101 (Veteran)
    ])

meu_set.add_achievement(ach)

# =======================================================================
# 4. SALVAR
# =======================================================================
meu_set.save()


# from pycheevos.core.helpers import byte, bit0, word
# from pycheevos.models.achievement import Achievement
# from pycheevos.models.set import AchievementSet
# from pycheevos.core.constants import AchievementType
# from functools import reduce
# import operator

# meu_set = AchievementSet(game_id=36353, title="Unshakable Perfection")

# # =======================================================================
# # 1. ALIAS DE MEMÓRIA (Core)
# # =======================================================================
# mem_screen = byte(0x1feff0)
# mem_rank   = byte(0x1fef68)
# mem_win    = bit0(0x1fef6a)
# mem_char   = byte(0x1fef66)

# # =======================================================================
# # 2. CONSTANTES DE ENDEREÇOS (Base Tanaka)
# # =======================================================================
# BASE_LOSSES = 0x1fe75c # Total Losses (Persistent) do Tanaka
# BASE_BELT   = 0x1fe764 # Primeiro cinto do Tanaka (Light Local)
# OFFSET_CHAR = 0x50     # Distância entre os lutadores

# ach = Achievement(
#     id=117000,
#     title="Unshakable Perfection",
#     description="Win all Championships across all weight classes without ever losing a match.",
#     points=50,
#     badge="00000",
#     type=AchievementType.MISSABLE
# )

# # --- CORE GROUP ---
# ach.add_core([
#     mem_screen != 0x13,
#     mem_rank == 1,
#     mem_win.delta() == 0,
#     mem_win == 1
# ])

# # --- ALT GROUPS ---
# for char_id in range(13):
    
#     # 1. Endereço de Derrotas deste lutador
#     char_losses = word(BASE_LOSSES + (char_id * OFFSET_CHAR))
    
#     # 2. Gera uma lista com os endereços dos 12 cinturões deste lutador
#     # O loop `i` vai de 0 a 11 e soma 2 bytes (0x02) a cada passo.
#     belts = [word(BASE_BELT + (char_id * OFFSET_CHAR) + (i * 2)) for i in range(12)]
    
#     # 3. Cria a corrente de OrNext para os Deltas (Frame passado)
#     # Isso transforma: [A, B, C] em (A | B | C), gerando o OrNext automaticamente!
#     delta_checks = [b.delta() == 0 for b in belts]
#     or_next_deltas = reduce(operator.or_, delta_checks)
    
#     # 4. Cria a lista de checagens normais (Frame atual)
#     current_checks = [b > 0 for b in belts]
    
#     # 5. Junta tudo no Alt Group atual
#     # O PyCheevos 'achata' a lista automaticamente, unindo tudo perfeitamente
#     alt_logic = [
#         mem_char == char_id,
#         char_losses == 0,
#         or_next_deltas      # Adiciona as 12 linhas de OrNext Delta
#     ] + current_checks      # Adiciona as 12 linhas de Mem Atual
    
#     ach.add_alt(alt_logic)

# meu_set.add_achievement(ach)
# meu_set.save()



# from pycheevos.core.helpers import byte, bit0, word
# from pycheevos.models.achievement import Achievement
# from pycheevos.models.set import AchievementSet

# meu_set = AchievementSet(game_id=36353, title="Undefeated Champion")

# # =======================================================================
# # 1. ALIAS DE MEMÓRIA (Core)
# # =======================================================================
# mem_champ = byte(0x1fef70) # Current Championship (0=Heavy Local, 1=Middle Local)
# mem_rank  = byte(0x1fef68) # Opponent Rank (1 = Championship Match)
# mem_win   = bit0(0x1fef6a) # Match Win Indicator
# mem_char  = byte(0x1fef66) # P1 Character ID

# # =======================================================================
# # 2. CONSTANTES DE ENDEREÇOS
# # =======================================================================
# BASE_LOSSES = 0x1fe738 # Endereço de "Total Losses (Session)" do Tanaka
# OFFSET_CHAR = 0x50     # Distância estrutural entre os personagens

# # =======================================================================
# # 3. CRIAÇÃO DA CONQUISTA
# # =======================================================================
# ach = Achievement(
#     id=116000,
#     title="Flawless Local Victory",
#     description="Win the Heavy or Middle Local Championship without a single loss during the session.",
#     points=10,
#     badge="00000"
# )

# # --- CORE GROUP ---
# ach.add_core([
#     mem_champ <= 1,           # 0 = Heavy Local, 1 = Middle Local
#     mem_rank == 1,            # Luta pelo título (contra o Rank #1)
#     mem_win.delta() == 0,     # Frame passado: ainda não tinha vencido
#     mem_win == 1              # Frame atual: Venceu a luta!
# ])

# # --- ALT GROUPS (Loop Mágico para os 13 lutadores) ---
# # Gera os Alts de 0 a 12
# for char_id in range(13):
    
#     # O Python calcula o endereço das derrotas do lutador atual automaticamente
#     # Como as derrotas são 16-bit nas suas notas, usamos word()
#     char_losses = word(BASE_LOSSES + (char_id * OFFSET_CHAR))
    
#     ach.add_alt([
#         mem_char == char_id,  # Checa se é este lutador
#         char_losses == 0      # Garante que as derrotas na sessão são 0
#     ])

# meu_set.add_achievement(ach)

# # Salva o arquivo final
# meu_set.save()


# meu_set = AchievementSet(game_id=36353, title="Champion's Retirement")

# mem_screen = byte(0x1feff0)
# ptr_base = word(0x1fe480)
# match_status = ptr_base >> byte(0x000018) # I:0xW1fe480_0xH000018
# mem_char = byte(0x1fef66)                 # P1 Character ID

# BASE_LIGHT = 0x1fe768
# BASE_MID   = 0x1fe770
# BASE_HEAVY = 0x1fe778

# # Distância em bytes entre os personagens na memória
# OFFSET_CHAR = 0x50

# ach = Achievement(
#     id=115000,
#     title="Champion's Retirement",
#     description="Win the World Championship in all three weight classes with the same fighter.",
#     points=50,
#     badge="00000"
# )

# # --- LÓGICA CORE ---
# # 0x13 = 19 em decimal (Champion / Load Screen)
# ach.add_core([
#     mem_screen != 0x13,
#     match_status == 0x13
# ])

# for char_id in range(13):
    
#     # O Python calcula o endereço exato para nós!
#     t_light = word(BASE_LIGHT + (char_id * OFFSET_CHAR))
#     t_mid   = word(BASE_MID   + (char_id * OFFSET_CHAR))
#     t_heavy = word(BASE_HEAVY + (char_id * OFFSET_CHAR))

#     # --- ALT A: Ganhou o Light World por último ---
#     ach.add_alt([
#         mem_char == char_id,
#         t_light.delta() == 0, t_light > 0,
#         t_mid > 0,
#         t_heavy > 0
#     ])

#     # --- ALT B: Ganhou o Middle World por último ---
#     ach.add_alt([
#         mem_char == char_id,
#         t_light > 0,
#         t_mid.delta() == 0, t_mid > 0,
#         t_heavy > 0
#     ])

#     # --- ALT C: Ganhou o Heavy World por último ---
#     ach.add_alt([
#         mem_char == char_id,
#         t_light > 0,
#         t_mid > 0,
#         t_heavy.delta() == 0, t_heavy > 0
#     ])

# meu_set.add_achievement(ach)
# meu_set.save()