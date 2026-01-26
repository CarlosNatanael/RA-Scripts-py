# Code Notes for Game ID 36353
# Source: 36353-User.txt

from pycheevos.core.helpers import *

# 0x000000: .
unk_0x000000 = byte(0x000000)

# 0x090876: [8-bit] Input controler
input_controler = byte(0x090876)
#0xff = nada
#0xf7 = star
#0xfe = select
#0xdf = direita
#0x7f = esquerda
#0xbf = baixo
#0xef = cima

# 0x090877: [8-bit] Input controler
input_controler_2 = byte(0x090877)
#0xfb = L1
#0xfe = L2
#0xf7 = R1
#0xfd = R2

# 0x09f49c: map?
map = byte(0x09f49c)

# 0x100324: [16-bit] Valor total de pontos (Championship mode) acumulados
valor_total_de_pontos_acumulados = word(0x100324)

# 0x102ff4: [16-bit] Valor total de pontos (Championship mode) acumulados
valor_total_de_pontos_acumulados_2 = word(0x102ff4)

# 0x103d14: [16-bit] Valor total de pontos (Championship mode) acumulados
valor_total_de_pontos_acumulados_3 = word(0x103d14)

# 0x1d253c: indicador raund
indicador_raund = byte(0x1d253c)

# 0x1d290c: indicador raudo
indicador_raudo = byte(0x1d290c)

# 0x1db67a: [8-bit] Mensagem new bit-flag
mensagem_new_bit_flag = byte(0x1db67a)

# 0x1db990: [32-bit] Seleciona o personagem
seleciona_o_personagem = dword(0x1db990)
#Value:
#0x00 = Tanaka
#0x01 = Ryoko
#0x02 = Red
#0x03 = B. T.
#0x04 = Puma
#0x05 = Prince
#0x06 = Misha
#0x07 = Silver Man
#0x08 = Gio
#0x09 = Kojiromaru
#0x0a = Spice
#0x0b = Asteka
#0x0c = Mr.Crown

# 0x1dc070: [8-bit] Local Luta
local_luta = byte(0x1dc070)
#0x00 = National hall
#0x03 =  gym

# 0x1dc072: [8-bit] Quantidade de rounds
quantidade_de_rounds = byte(0x1dc072)
#0x00 = 4
#0x01 = 6
#0x02 = 8
#0x03 = 10
#0x04 = 12

# 0x1fe6d0: [8-bit] Tanaka - Scout
tanaka___scout = byte(0x1fe6d0)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d1: [8-bit] Ryoko - Scout
ryoko___scout = byte(0x1fe6d1)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d2: [8-bit] Red - Scout
red___scout = byte(0x1fe6d2)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d3: [8-bit] B.T. - Scout
b = byte(0x1fe6d3)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d4: [8-bit] Puma - Scout
puma___scout = byte(0x1fe6d4)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d5: [8-bit] Prince - Scout
prince___scout = byte(0x1fe6d5)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d6: [8-bit] Misha - Scout
misha___scout = byte(0x1fe6d6)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d7: [8-bit] Silver Man - Scout
silver_man___scout = byte(0x1fe6d7)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d8: [8-bit] Gio - Scout
gio___scout = byte(0x1fe6d8)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6d9: [8-bit] Kojiromaru - Scout
kojiromaru___scout = byte(0x1fe6d9)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6da: [8-bit] Spice - Scout
spice___scout = byte(0x1fe6da)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6db: [8-bit] Asteka - Scout
asteka___scout = byte(0x1fe6db)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6dc: [8-bit] Mr.Crown - Scout
mr = byte(0x1fe6dc)
#0x00 = Bloqueado
#0x01 = Desbloqueado
#0x02 = Revanche (Notas Extras Unlocked)

# 0x1fe6dd: [8-bit] Tanaka - Sign1
tanaka___sign1 = byte(0x1fe6dd)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6de: [8-bit] Tanaka - Sign2
tanaka___sign2 = byte(0x1fe6de)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6df: [8-bit] Tanaka - Sign3
tanaka___sign3 = byte(0x1fe6df)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6e3: [8-bit] Ryoko - Sign1
ryoko___sign1 = byte(0x1fe6e3)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6e4: [8-bit] Ryoko - Sign2
ryoko___sign2 = byte(0x1fe6e4)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6e5: [8-bit] Ryoko - Sign3
ryoko___sign3 = byte(0x1fe6e5)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6e9: [8-bit] Red - Sign1
red___sign1 = byte(0x1fe6e9)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6ea: [8-bit] Red - Sign2
red___sign2 = byte(0x1fe6ea)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6ef: [8-bit] B.T. - Sign1
b_2 = byte(0x1fe6ef)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6f0: [8-bit] B.T. - Sign2
b_3 = byte(0x1fe6f0)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6f1: [8-bit] B.T. - Sign3
b_4 = byte(0x1fe6f1)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6f2: [8-bit] B.T. - Sign4
b_5 = byte(0x1fe6f2)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6f5: [8-bit] Puma - Sign1
puma___sign1 = byte(0x1fe6f5)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6fb: [8-bit] Prince - Sign1
prince___sign1 = byte(0x1fe6fb)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6fc: [8-bit] Prince - Sign2
prince___sign2 = byte(0x1fe6fc)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe6fd: [8-bit] Prince - Sign3
prince___sign3 = byte(0x1fe6fd)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe701: [8-bit] Misha - Sign1
misha___sign1 = byte(0x1fe701)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe702: [8-bit] Misha - Sign2
misha___sign2 = byte(0x1fe702)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe707: [8-bit] Silver Man - Sign1
silver_man___sign1 = byte(0x1fe707)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe70d: [8-bit] Gio - Sign1
gio___sign1 = byte(0x1fe70d)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe70e: [8-bit] Gio - Sign2
gio___sign2 = byte(0x1fe70e)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe70f: [8-bit] Gio - Sign3
gio___sign3 = byte(0x1fe70f)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe713: [8-bit] Kojiromaru - Sign1
kojiromaru___sign1 = byte(0x1fe713)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe714: [8-bit] Kojiromaru - Sign2
kojiromaru___sign2 = byte(0x1fe714)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe719: [8-bit] Spice - Sign1
spice___sign1 = byte(0x1fe719)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe71a: [8-bit] Spice - Sign2
spice___sign2 = byte(0x1fe71a)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe71b: [8-bit] Spice - Sign3
spice___sign3 = byte(0x1fe71b)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe71f: [8-bit] Asteka - Sign1
asteka___sign1 = byte(0x1fe71f)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe725: [8-bit] Mr.Crown - Sign1
mr_2 = byte(0x1fe725)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe726: [8-bit] Mr.Crown - Sign2
mr_3 = byte(0x1fe726)
#0x00 = Bloqueado
#0x01 = Desbloqueado

# 0x1fe730: [8-bit] Tanaka - Competição Desbloqueada
tanaka___competio_desbloqueada = byte(0x1fe730)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe733: [8-bit] Tanaka - Categoria do lutador
tanaka___categoria_do_lutador = byte(0x1fe733)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe734: [16-bit] Tanaka - Quantidade de Lutas (Championship mode)
tanaka___quantidade_de_lutas = word(0x1fe734)

# 0x1fe736: [16-bit] Tanaka - Quantidade de Vitorias (Championship mode)
tanaka___quantidade_de_vitorias = word(0x1fe736)

# 0x1fe738: [16-bit] Tanaka - Quantidade de Derrotas (Championship mode)
tanaka___quantidade_de_derrotas = word(0x1fe738)

# 0x1fe73a: [16-bit] Tanaka - Quantidade de K.O (Championship mode)
tanaka___quantidade_de_k = word(0x1fe73a)

# 0x1fe73c: [16-bit] Tanaka - Ponto de Personagem (Championship mode)
tanaka___ponto_de_personagem = word(0x1fe73c)

# 0x1fe740: [8-bit] Tanaka - Cinturão Local Light - Contador de Vitórias e Defesas
tanaka___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fe740)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe742: [8-bit] Tanaka - Cinturão Nacional Light - Contador de Vitórias e Defesas
tanaka___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1fe742)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe744: [8-bit] Tanaka - Cinturão Mundial Light - Contador de Vitórias e Defesas
tanaka___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1fe744)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe746: [8-bit] Tanaka - Cinturão Secret Light - Contador de Vitórias e Defesas
tanaka___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fe746)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe748: [8-bit] Tanaka - Cinturão Local Middle - Contador de Vitórias e Defesas
tanaka___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fe748)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe74a: [8-bit] Tanaka - Cinturão Nacional Middle - Contador de Vitórias e Defesas
tanaka___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1fe74a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe74c: [8-bit] Tanaka - Cinturão Mundial Middle - Contador de Vitórias e Defesas
tanaka___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1fe74c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe74e: [8-bit] Tanaka - Cinturão Secret Middle - Contador de Vitórias e Defesas
tanaka___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1fe74e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe750: [8-bit] Tanaka - Cinturão Local Heavy - Contador de Vitórias e Defesas
tanaka___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fe750)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe752: [8-bit] Tanaka - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
tanaka___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1fe752)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe754: [8-bit] Tanaka - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
tanaka___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1fe754)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe756: [8-bit] Tanaka - Cinturão Secret Heavy - Contador de Vitórias e Defesas
tanaka___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fe756)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe760: [16-bit] Tanaka - Total de Pontos (Championship mode)
tanaka___total_de_pontos = word(0x1fe760)

# 0x1fe780: [8-bit] Ryoko - Competição Desbloqueada
ryoko___competio_desbloqueada = byte(0x1fe780)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe783: [8-bit] Ryoko - Categoria do lutador
ryoko___categoria_do_lutador = byte(0x1fe783)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe784: [16-bit] Ryoko - Quantidade de Lutas (Championship mode)
ryoko___quantidade_de_lutas = word(0x1fe784)

# 0x1fe786: [16-bit] Ryoko - Quantidade de Vitorias (Championship mode)
ryoko___quantidade_de_vitorias = word(0x1fe786)

# 0x1fe788: [16-bit] Ryoko - Quantidade de Derrotas (Championship mode)
ryoko___quantidade_de_derrotas = word(0x1fe788)

# 0x1fe78a: [16-bit] Ryoko - Quantidade de K.O (Championship mode)
ryoko___quantidade_de_k = word(0x1fe78a)

# 0x1fe78c: [16-bit] Ryoko - Ponto de Personagem (Championship mode)
ryoko___ponto_de_personagem = word(0x1fe78c)

# 0x1fe790: [8-bit] Ryoko - Cinturão Local Light - Contador de Vitórias e Defesas
ryoko___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fe790)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe792: [8-bit] Ryoko - Cinturão Nacional Light - Contador de Vitórias e Defesas
ryoko___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1fe792)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe794: [8-bit] Ryoko - Cinturão Mundial Light - Contador de Vitórias e Defesas
ryoko___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1fe794)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe796: [8-bit] Ryoko - Cinturão Secret Light - Contador de Vitórias e Defesas
ryoko___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fe796)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe798: [8-bit] Ryoko - Cinturão Local Middle - Contador de Vitórias e Defesas
ryoko___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fe798)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe79a: [8-bit] Ryoko - Cinturão Nacional Middle - Contador de Vitórias e Defesas
ryoko___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1fe79a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe79c: [8-bit] Ryoko - Cinturão Mundial Middle - Contador de Vitórias e Defesas
ryoko___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1fe79c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe79e: [8-bit] Ryoko - Cinturão Secret Middle - Contador de Vitórias e Defesas
ryoko___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1fe79e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7a0: [8-bit] Ryoko - Cinturão Local Heavy - Contador de Vitórias e Defesas
ryoko___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fe7a0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7a2: [8-bit] Ryoko - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
ryoko___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1fe7a2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7a4: [8-bit] Ryoko - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
ryoko___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1fe7a4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7a6: [8-bit] Ryoko - Cinturão Secret Heavy - Contador de Vitórias e Defesas
ryoko___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fe7a6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7b0: [16-bit] Ryoko - Total de Pontos (Championship mode)
ryoko___total_de_pontos = word(0x1fe7b0)

# 0x1fe7d0: [8-bit] Red - Competição Desbloqueada
red___competio_desbloqueada = byte(0x1fe7d0)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe7d3: [8-bit] Red - Categoria do lutador
red___categoria_do_lutador = byte(0x1fe7d3)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe7d4: [16-bit] Red - Quantidade de Lutas (Championship mode)
red___quantidade_de_lutas = word(0x1fe7d4)

# 0x1fe7d6: [16-bit] Red - Quantidade de Vitorias (Championship mode)
red___quantidade_de_vitorias = word(0x1fe7d6)

# 0x1fe7d8: [16-bit] Red - Quantidade de Derrotas (Championship mode)
red___quantidade_de_derrotas = word(0x1fe7d8)

# 0x1fe7da: [16-bit] Red - Quantidade de K.O (Championship mode)
red___quantidade_de_k = word(0x1fe7da)

# 0x1fe7dc: [16-bit] Red - Ponto de Personagem (Championship mode)
red___ponto_de_personagem = word(0x1fe7dc)

# 0x1fe7e0: [8-bit] Red - Cinturão Local Light - Contador de Vitórias e Defesas
red___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fe7e0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7e2: [8-bit] Red - Cinturão Nacional Light - Contador de Vitórias e Defesas
red___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1fe7e2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7e4: [8-bit] Red - Cinturão Mundial Light - Contador de Vitórias e Defesas
red___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1fe7e4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7e6: [8-bit] Red - Cinturão Secret Light - Contador de Vitórias e Defesas
red___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fe7e6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7e8: [8-bit] Red - Cinturão Local Middle - Contador de Vitórias e Defesas
red___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fe7e8)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7ea: [8-bit] Red - Cinturão Nacional Middle - Contador de Vitórias e Defesas
red___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1fe7ea)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7ec: [8-bit] Red - Cinturão Mundial Middle - Contador de Vitórias e Defesas
red___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1fe7ec)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7ee: [8-bit] Red - Cinturão Secret Middle - Contador de Vitórias e Defesas
red___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1fe7ee)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7f0: [8-bit] Red - Cinturão Local Heavy - Contador de Vitórias e Defesas
red___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fe7f0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7f2: [8-bit] Red - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
red___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1fe7f2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7f4: [8-bit] Red - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
red___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1fe7f4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe7f6: [8-bit] Red - Cinturão Secret Heavy - Contador de Vitórias e Defesas
red___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fe7f6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe800: [16-bit] Red - Total de Pontos (Championship mode)
red___total_de_pontos = word(0x1fe800)

# 0x1fe820: [8-bit] B.T. - Competição Desbloqueada
b_6 = byte(0x1fe820)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe823: [8-bit] B.T. - Categoria do lutador
b_7 = byte(0x1fe823)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe824: [16-bit] B.T. - Quantidade de Lutas (Championship mode)
b_8 = word(0x1fe824)

# 0x1fe826: [16-bit] B.T. - Quantidade de Vitorias (Championship mode)
b_9 = word(0x1fe826)

# 0x1fe828: [16-bit] B.T. - Quantidade de Derrotas (Championship mode)
b_10 = word(0x1fe828)

# 0x1fe82a: [16-bit] B.T. - Quantidade de K.O (Championship mode)
b_11 = word(0x1fe82a)

# 0x1fe82c: [16-bit] B.T. - Ponto de Personagem (Championship mode)
b_12 = word(0x1fe82c)

# 0x1fe830: [8-bit] B.T. - Cinturão Local Light - Contador de Vitórias e Defesas
b_13 = byte(0x1fe830)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe832: [8-bit] B.T. - Cinturão Nacional Light - Contador de Vitórias e Defesas
b_14 = byte(0x1fe832)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe834: [8-bit] B.T. - Cinturão Mundial Light - Contador de Vitórias e Defesas
b_15 = byte(0x1fe834)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe836: [8-bit] B.T. - Cinturão Secret Light - Contador de Vitórias e Defesas
b_16 = byte(0x1fe836)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe838: [8-bit] B.T. - Cinturão Local Middle - Contador de Vitórias e Defesas
b_17 = byte(0x1fe838)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe83a: [8-bit] B.T. - Cinturão Nacional Middle - Contador de Vitórias e Defesas
b_18 = byte(0x1fe83a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe83c: [8-bit] B.T. - Cinturão Mundial Middle - Contador de Vitórias e Defesas
b_19 = byte(0x1fe83c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe83e: [8-bit] B.T. - Cinturão Secret Middle - Contador de Vitórias e Defesas
b_20 = byte(0x1fe83e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe840: [8-bit] B.T. - Cinturão Local Heavy - Contador de Vitórias e Defesas
b_21 = byte(0x1fe840)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe842: [8-bit] B.T. - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
b_22 = byte(0x1fe842)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe844: [8-bit] B.T. - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
b_23 = byte(0x1fe844)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe846: [8-bit] B.T. - Cinturão Secret Heavy - Contador de Vitórias e Defesas
b_24 = byte(0x1fe846)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe850: [16-bit] B.T. - Total de Pontos (Championship mode)
b_25 = word(0x1fe850)

# 0x1fe870: [8-bit] Puma - Competição Desbloqueada
puma___competio_desbloqueada = byte(0x1fe870)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe873: [8-bit] Puma - Categoria do lutador
puma___categoria_do_lutador = byte(0x1fe873)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe874: [16-bit] Puma - Quantidade de Lutas (Championship mode)
puma___quantidade_de_lutas = word(0x1fe874)

# 0x1fe876: [16-bit] Puma - Quantidade de Vitorias (Championship mode)
puma___quantidade_de_vitorias = word(0x1fe876)

# 0x1fe878: [16-bit] Puma - Quantidade de Derrotas (Championship mode)
puma___quantidade_de_derrotas = word(0x1fe878)

# 0x1fe87a: [16-bit] Puma - Quantidade de K.O (Championship mode)
puma___quantidade_de_k = word(0x1fe87a)

# 0x1fe87c: [16-bit] Puma - Ponto de Personagem (Championship mode)
puma___ponto_de_personagem = word(0x1fe87c)

# 0x1fe880: [8-bit] Puma - Cinturão Local Light - Contador de Vitórias e Defesas
puma___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fe880)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe882: [8-bit] Puma - Cinturão Nacional Light - Contador de Vitórias e Defesas
puma___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1fe882)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe884: [8-bit] Puma - Cinturão Mundial Light - Contador de Vitórias e Defesas
puma___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1fe884)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe886: [8-bit] Puma - Cinturão Secret Light - Contador de Vitórias e Defesas
puma___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fe886)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe888: [8-bit] Puma - Cinturão Local Middle - Contador de Vitórias e Defesas
puma___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fe888)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe88a: [8-bit] Puma - Cinturão Nacional Middle - Contador de Vitórias e Defesas
puma___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1fe88a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe88c: [8-bit] Puma - Cinturão Mundial Middle - Contador de Vitórias e Defesas
puma___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1fe88c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe88e: [8-bit] Puma - Cinturão Secret Middle - Contador de Vitórias e Defesas
puma___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1fe88e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe890: [8-bit] Puma - Cinturão Local Heavy - Contador de Vitórias e Defesas
puma___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fe890)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe892: [8-bit] Puma - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
puma___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1fe892)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe894: [8-bit] Puma - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
puma___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1fe894)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe896: [8-bit] Puma - Cinturão Secret Heavy - Contador de Vitórias e Defesas
puma___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fe896)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8a0: [16-bit] Puma - Total de Pontos (Championship mode)
puma___total_de_pontos = word(0x1fe8a0)

# 0x1fe8c0: [8-bit] Prince - Competição Desbloqueada
prince___competio_desbloqueada = byte(0x1fe8c0)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe8c3: [8-bit] Prince - Categoria do lutador
prince___categoria_do_lutador = byte(0x1fe8c3)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe8c4: [16-bit] Prince - Quantidade de Lutas (Championship mode)
prince___quantidade_de_lutas = word(0x1fe8c4)

# 0x1fe8c6: [16-bit] Prince - Quantidade de Vitorias (Championship mode)
prince___quantidade_de_vitorias = word(0x1fe8c6)

# 0x1fe8c8: [16-bit] Prince - Quantidade de Derrotas (Championship mode)
prince___quantidade_de_derrotas = word(0x1fe8c8)

# 0x1fe8ca: [16-bit] Prince - Quantidade de K.O (Championship mode)
prince___quantidade_de_k = word(0x1fe8ca)

# 0x1fe8cc: [16-bit] Prince - Ponto de Personagem (Championship mode)
prince___ponto_de_personagem = word(0x1fe8cc)

# 0x1fe8d0: [8-bit] Prince - Cinturão Local Light - Contador de Vitórias e Defesas
prince___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fe8d0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8d2: [8-bit] Prince - Cinturão Nacional Light - Contador de Vitórias e Defesas
prince___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1fe8d2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8d4: [8-bit] Prince - Cinturão Mundial Light - Contador de Vitórias e Defesas
prince___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1fe8d4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8d6: [8-bit] Prince - Cinturão Secret Light - Contador de Vitórias e Defesas
prince___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fe8d6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8d8: [8-bit] Prince - Cinturão Local Middle - Contador de Vitórias e Defesas
prince___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fe8d8)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8da: [8-bit] Prince - Cinturão Nacional Middle - Contador de Vitórias e Defesas
prince___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1fe8da)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8dc: [8-bit] Prince - Cinturão Mundial Middle - Contador de Vitórias e Defesas
prince___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1fe8dc)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8de: [8-bit] Prince - Cinturão Secret Middle - Contador de Vitórias e Defesas
prince___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1fe8de)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8e0: [8-bit] Prince - Cinturão Local Heavy - Contador de Vitórias e Defesas
prince___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fe8e0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8e2: [8-bit] Prince - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
prince___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1fe8e2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8e4: [8-bit] Prince - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
prince___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1fe8e4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8e6: [8-bit] Prince - Cinturão Secret Heavy - Contador de Vitórias e Defesas
prince___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fe8e6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe8f0: [16-bit] Prince - Total de Pontos (Championship mode)
prince___total_de_pontos = word(0x1fe8f0)

# 0x1fe910: [8-bit] Misha - Competição Desbloqueada
misha___competio_desbloqueada = byte(0x1fe910)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe913: [8-bit] Misha - Categoria do lutador
misha___categoria_do_lutador = byte(0x1fe913)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe914: [16-bit] Misha - Quantidade de Lutas (Championship mode)
misha___quantidade_de_lutas = word(0x1fe914)

# 0x1fe916: [16-bit] Misha - Quantidade de Vitorias (Championship mode)
misha___quantidade_de_vitorias = word(0x1fe916)

# 0x1fe918: [16-bit] Misha - Quantidade de Derrotas (Championship mode)
misha___quantidade_de_derrotas = word(0x1fe918)

# 0x1fe91a: [16-bit] Misha - Quantidade de K.O (Championship mode)
misha___quantidade_de_k = word(0x1fe91a)

# 0x1fe91c: [16-bit] Misha - Ponto de Personagem (Championship mode)
misha___ponto_de_personagem = word(0x1fe91c)

# 0x1fe920: [8-bit] Misha - Cinturão Local Light - Contador de Vitórias e Defesas
misha___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fe920)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe922: [8-bit] Misha - Cinturão Nacional Light - Contador de Vitórias e Defesas
misha___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1fe922)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe924: [8-bit] Misha - Cinturão Mundial Light - Contador de Vitórias e Defesas
misha___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1fe924)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe926: [8-bit] Misha - Cinturão Secret Light - Contador de Vitórias e Defesas
misha___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fe926)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe928: [8-bit] Misha - Cinturão Local Middle - Contador de Vitórias e Defesas
misha___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fe928)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe92a: [8-bit] Misha - Cinturão Nacional Middle - Contador de Vitórias e Defesas
misha___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1fe92a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe92c: [8-bit] Misha - Cinturão Mundial Middle - Contador de Vitórias e Defesas
misha___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1fe92c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe92e: [8-bit] Misha - Cinturão Secret Middle - Contador de Vitórias e Defesas
misha___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1fe92e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe930: [8-bit] Misha - Cinturão Local Heavy - Contador de Vitórias e Defesas
misha___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fe930)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe932: [8-bit] Misha - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
misha___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1fe932)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe934: [8-bit] Misha - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
misha___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1fe934)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe936: [8-bit] Misha - Cinturão Secret Heavy - Contador de Vitórias e Defesas
misha___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fe936)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe940: [16-bit] Misha - Total de Pontos (Championship mode)
misha___total_de_pontos = word(0x1fe940)

# 0x1fe960: [8-bit] Silver Man - Competição Desbloqueada
silver_man___competio_desbloqueada = byte(0x1fe960)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe963: [8-bit] Silver Man - Categoria do lutador
silver_man___categoria_do_lutador = byte(0x1fe963)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe964: [16-bit] Silver Man - Quantidade de Lutas (Championship mode)
silver_man___quantidade_de_lutas = word(0x1fe964)

# 0x1fe966: [16-bit] Silver Man - Quantidade de Vitorias (Championship mode)
silver_man___quantidade_de_vitorias = word(0x1fe966)

# 0x1fe968: [16-bit] Silver Man - Quantidade de Derrotas (Championship mode)
silver_man___quantidade_de_derrotas = word(0x1fe968)

# 0x1fe96a: [16-bit] Silver Man - Quantidade de K.O (Championship mode)
silver_man___quantidade_de_k = word(0x1fe96a)

# 0x1fe96c: [16-bit] Silver Man - Ponto de Personagem (Championship mode)
silver_man___ponto_de_personagem = word(0x1fe96c)

# 0x1fe970: [8-bit] Silver Man - Cinturão Local Light - Contador de Vitórias e Defesas
silver_man___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fe970)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe972: [8-bit] Silver Man - Cinturão Nacional Light - Contador de Vitórias e Defesas
silver_man___cinturo_nacional_light___contador_de_vitrias_e_defes = byte(0x1fe972)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe974: [8-bit] Silver Man - Cinturão Mundial Light - Contador de Vitórias e Defesas
silver_man___cinturo_mundial_light___contador_de_vitrias_e_defesa = byte(0x1fe974)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe976: [8-bit] Silver Man - Cinturão Secret Light - Contador de Vitórias e Defesas
silver_man___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fe976)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe978: [8-bit] Silver Man - Cinturão Local Middle - Contador de Vitórias e Defesas
silver_man___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fe978)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe97a: [8-bit] Silver Man - Cinturão Nacional Middle - Contador de Vitórias e Defesas
silver_man___cinturo_nacional_middle___contador_de_vitrias_e_defe = byte(0x1fe97a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe97c: [8-bit] Silver Man - Cinturão Mundial Middle - Contador de Vitórias e Defesas
silver_man___cinturo_mundial_middle___contador_de_vitrias_e_defes = byte(0x1fe97c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe97e: [8-bit] Silver Man - Cinturão Secret Middle - Contador de Vitórias e Defesas
silver_man___cinturo_secret_middle___contador_de_vitrias_e_defesa = byte(0x1fe97e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe980: [8-bit] Silver Man - Cinturão Local Heavy - Contador de Vitórias e Defesas
silver_man___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fe980)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe982: [8-bit] Silver Man - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
silver_man___cinturo_nacional_heavy___contador_de_vitrias_e_defes = byte(0x1fe982)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe984: [8-bit] Silver Man - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
silver_man___cinturo_mundial_heavy___contador_de_vitrias_e_defesa = byte(0x1fe984)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe986: [8-bit] Silver Man - Cinturão Secret Heavy - Contador de Vitórias e Defesas
silver_man___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fe986)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe990: [16-bit] Silver Man - Total de Pontos (Championship mode)
silver_man___total_de_pontos = word(0x1fe990)

# 0x1fe9b0: [8-bit] Gio - Competição Desbloqueada
gio___competio_desbloqueada = byte(0x1fe9b0)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fe9b3: [8-bit] Gio - Categoria do lutador
gio___categoria_do_lutador = byte(0x1fe9b3)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fe9b4: [16-bit] Gio - Quantidade de Lutas (Championship mode)
gio___quantidade_de_lutas = word(0x1fe9b4)

# 0x1fe9b6: [16-bit] Gio - Quantidade de Vitorias (Championship mode)
gio___quantidade_de_vitorias = word(0x1fe9b6)

# 0x1fe9b8: [16-bit] Gio - Quantidade de Derrotas (Championship mode)
gio___quantidade_de_derrotas = word(0x1fe9b8)

# 0x1fe9ba: [16-bit] Gio - Quantidade de K.O (Championship mode)
gio___quantidade_de_k = word(0x1fe9ba)

# 0x1fe9bc: [16-bit] Gio - Ponto de Personagem (Championship mode)
gio___ponto_de_personagem = word(0x1fe9bc)

# 0x1fe9c0: [8-bit] Gio - Cinturão Local Light - Contador de Vitórias e Defesas
gio___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fe9c0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9c2: [8-bit] Gio - Cinturão Nacional Light - Contador de Vitórias e Defesas
gio___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1fe9c2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9c4: [8-bit] Gio - Cinturão Mundial Light - Contador de Vitórias e Defesas
gio___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1fe9c4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9c6: [8-bit] Gio - Cinturão Secret Light - Contador de Vitórias e Defesas
gio___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fe9c6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9c8: [8-bit] Gio - Cinturão Local Middle - Contador de Vitórias e Defesas
gio___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fe9c8)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9ca: [8-bit] Gio - Cinturão Nacional Middle - Contador de Vitórias e Defesas
gio___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1fe9ca)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9cc: [8-bit] Gio - Cinturão Mundial Middle - Contador de Vitórias e Defesas
gio___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1fe9cc)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9ce: [8-bit] Gio - Cinturão Secret Middle - Contador de Vitórias e Defesas
gio___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1fe9ce)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9d0: [8-bit] Gio - Cinturão Local Heavy - Contador de Vitórias e Defesas
gio___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fe9d0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9d2: [8-bit] Gio - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
gio___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1fe9d2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9d4: [8-bit] Gio - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
gio___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1fe9d4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9d6: [8-bit] Gio - Cinturão Secret Heavy - Contador de Vitórias e Defesas
gio___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fe9d6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fe9e0: [16-bit] Gio - Total de Pontos (Championship mode)
gio___total_de_pontos = word(0x1fe9e0)

# 0x1fea00: [8-bit] Kojiromaru - Competição Desbloqueada
kojiromaru___competio_desbloqueada = byte(0x1fea00)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fea03: [8-bit] Kojiromaru - Categoria do lutador
kojiromaru___categoria_do_lutador = byte(0x1fea03)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fea04: [16-bit] Kojiromaru - Quantidade de Lutas (Championship mode)
kojiromaru___quantidade_de_lutas = word(0x1fea04)

# 0x1fea06: [16-bit] Kojiromaru - Quantidade de Vitorias (Championship mode)
kojiromaru___quantidade_de_vitorias = word(0x1fea06)

# 0x1fea08: [16-bit] Kojiromaru - Quantidade de Derrotas (Championship mode)
kojiromaru___quantidade_de_derrotas = word(0x1fea08)

# 0x1fea0a: [16-bit] Kojiromaru - Quantidade de K.O (Championship mode)
kojiromaru___quantidade_de_k = word(0x1fea0a)

# 0x1fea0c: [16-bit] Kojiromaru - Ponto de Personagem (Championship mode)
kojiromaru___ponto_de_personagem = word(0x1fea0c)

# 0x1fea10: [8-bit] Kojiromaru - Cinturão Local Light - Contador de Vitórias e Defesas
kojiromaru___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fea10)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea12: [8-bit] Kojiromaru - Cinturão Nacional Light - Contador de Vitórias e Defesas
kojiromaru___cinturo_nacional_light___contador_de_vitrias_e_defes = byte(0x1fea12)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea14: [8-bit] Kojiromaru - Cinturão Mundial Light - Contador de Vitórias e Defesas
kojiromaru___cinturo_mundial_light___contador_de_vitrias_e_defesa = byte(0x1fea14)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea16: [8-bit] Kojiromaru - Cinturão Secret Light - Contador de Vitórias e Defesas
kojiromaru___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fea16)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea18: [8-bit] Kojiromaru - Cinturão Local Middle - Contador de Vitórias e Defesas
kojiromaru___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fea18)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea1a: [8-bit] Kojiromaru - Cinturão Nacional Middle - Contador de Vitórias e Defesas
kojiromaru___cinturo_nacional_middle___contador_de_vitrias_e_defe = byte(0x1fea1a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea1c: [8-bit] Kojiromaru - Cinturão Mundial Middle - Contador de Vitórias e Defesas
kojiromaru___cinturo_mundial_middle___contador_de_vitrias_e_defes = byte(0x1fea1c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea1e: [8-bit] Kojiromaru - Cinturão Secret Middle - Contador de Vitórias e Defesas
kojiromaru___cinturo_secret_middle___contador_de_vitrias_e_defesa = byte(0x1fea1e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea20: [8-bit] Kojiromaru - Cinturão Local Heavy - Contador de Vitórias e Defesas
kojiromaru___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fea20)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea22: [8-bit] Kojiromaru - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
kojiromaru___cinturo_nacional_heavy___contador_de_vitrias_e_defes = byte(0x1fea22)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea24: [8-bit] Kojiromaru - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
kojiromaru___cinturo_mundial_heavy___contador_de_vitrias_e_defesa = byte(0x1fea24)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea26: [8-bit] Kojiromaru - Cinturão Secret Heavy - Contador de Vitórias e Defesas
kojiromaru___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fea26)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea30: [16-bit] Kojiromaru - Total de Pontos (Championship mode)
kojiromaru___total_de_pontos = word(0x1fea30)

# 0x1fea50: [8-bit] Spice - Competição Desbloqueada
spice___competio_desbloqueada = byte(0x1fea50)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1fea53: [8-bit] Spice - Categoria do lutador
spice___categoria_do_lutador = byte(0x1fea53)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1fea54: [16-bit] Spice - Quantidade de Lutas (Championship mode)
spice___quantidade_de_lutas = word(0x1fea54)

# 0x1fea56: [16-bit] Spice - Quantidade de Vitorias (Championship mode)
spice___quantidade_de_vitorias = word(0x1fea56)

# 0x1fea58: [16-bit] Spice - Quantidade de Derrotas (Championship mode)
spice___quantidade_de_derrotas = word(0x1fea58)

# 0x1fea5a: [16-bit] Spice - Quantidade de K.O (Championship mode)
spice___quantidade_de_k = word(0x1fea5a)

# 0x1fea5c: [16-bit] Spice - Ponto de Personagem (Championship mode)
spice___ponto_de_personagem = word(0x1fea5c)

# 0x1fea60: [8-bit] Spice - Cinturão Local Light - Contador de Vitórias e Defesas
spice___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1fea60)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea62: [8-bit] Spice - Cinturão Nacional Light - Contador de Vitórias e Defesas
spice___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1fea62)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea64: [8-bit] Spice - Cinturão Mundial Light - Contador de Vitórias e Defesas
spice___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1fea64)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea66: [8-bit] Spice - Cinturão Secret Light - Contador de Vitórias e Defesas
spice___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1fea66)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea68: [8-bit] Spice - Cinturão Local Middle - Contador de Vitórias e Defesas
spice___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1fea68)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea6a: [8-bit] Spice - Cinturão Nacional Middle - Contador de Vitórias e Defesas
spice___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1fea6a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea6c: [8-bit] Spice - Cinturão Mundial Middle - Contador de Vitórias e Defesas
spice___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1fea6c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea6e: [8-bit] Spice - Cinturão Secret Middle - Contador de Vitórias e Defesas
spice___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1fea6e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea70: [8-bit] Spice - Cinturão Local Heavy - Contador de Vitórias e Defesas
spice___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1fea70)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea72: [8-bit] Spice - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
spice___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1fea72)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea74: [8-bit] Spice - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
spice___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1fea74)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea76: [8-bit] Spice - Cinturão Secret Heavy - Contador de Vitórias e Defesas
spice___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1fea76)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fea80: [16-bit] Spice - Total de Pontos (Championship mode)
spice___total_de_pontos = word(0x1fea80)

# 0x1feaa0: [8-bit] Asteka - Competição Desbloqueada
asteka___competio_desbloqueada = byte(0x1feaa0)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1feaa3: [8-bit] Asteka - Categoria do lutador
asteka___categoria_do_lutador = byte(0x1feaa3)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1feaa4: [16-bit] Asteka - Quantidade de Lutas (Championship mode)
asteka___quantidade_de_lutas = word(0x1feaa4)

# 0x1feaa6: [16-bit] Asteka - Quantidade de Vitorias (Championship mode)
asteka___quantidade_de_vitorias = word(0x1feaa6)

# 0x1feaa8: [16-bit] Asteka - Quantidade de Derrotas (Championship mode)
asteka___quantidade_de_derrotas = word(0x1feaa8)

# 0x1feaaa: [16-bit] Asteka - Quantidade de K.O (Championship mode)
asteka___quantidade_de_k = word(0x1feaaa)

# 0x1feaac: [16-bit] Asteka - Ponto de Personagem (Championship mode)
asteka___ponto_de_personagem = word(0x1feaac)

# 0x1feab0: [8-bit] Asteka - Cinturão Local Light - Contador de Vitórias e Defesas
asteka___cinturo_local_light___contador_de_vitrias_e_defesas = byte(0x1feab0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feab2: [8-bit] Asteka - Cinturão Nacional Light - Contador de Vitórias e Defesas
asteka___cinturo_nacional_light___contador_de_vitrias_e_defesas = byte(0x1feab2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feab4: [8-bit] Asteka - Cinturão Mundial Light - Contador de Vitórias e Defesas
asteka___cinturo_mundial_light___contador_de_vitrias_e_defesas = byte(0x1feab4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feab6: [8-bit] Asteka - Cinturão Secret Light - Contador de Vitórias e Defesas
asteka___cinturo_secret_light___contador_de_vitrias_e_defesas = byte(0x1feab6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feab8: [8-bit] Asteka - Cinturão Local Middle - Contador de Vitórias e Defesas
asteka___cinturo_local_middle___contador_de_vitrias_e_defesas = byte(0x1feab8)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feaba: [8-bit] Asteka - Cinturão Nacional Middle - Contador de Vitórias e Defesas
asteka___cinturo_nacional_middle___contador_de_vitrias_e_defesas = byte(0x1feaba)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feabc: [8-bit] Asteka - Cinturão Mundial Middle - Contador de Vitórias e Defesas
asteka___cinturo_mundial_middle___contador_de_vitrias_e_defesas = byte(0x1feabc)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feabe: [8-bit] Asteka - Cinturão Secret Middle - Contador de Vitórias e Defesas
asteka___cinturo_secret_middle___contador_de_vitrias_e_defesas = byte(0x1feabe)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feac0: [8-bit] Asteka - Cinturão Local Heavy - Contador de Vitórias e Defesas
asteka___cinturo_local_heavy___contador_de_vitrias_e_defesas = byte(0x1feac0)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feac2: [8-bit] Asteka - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
asteka___cinturo_nacional_heavy___contador_de_vitrias_e_defesas = byte(0x1feac2)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feac4: [8-bit] Asteka - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
asteka___cinturo_mundial_heavy___contador_de_vitrias_e_defesas = byte(0x1feac4)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feac6: [8-bit] Asteka - Cinturão Secret Heavy - Contador de Vitórias e Defesas
asteka___cinturo_secret_heavy___contador_de_vitrias_e_defesas = byte(0x1feac6)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1fead0: [16-bit] Asteka - Total de Pontos (Championship mode)
asteka___total_de_pontos = word(0x1fead0)

# 0x1feaf0: [8-bit] Mr.Crown - Competição Desbloqueada
mr_4 = byte(0x1feaf0)
#0x00 = Local
#0x01 = Nacional
#0x02 = Mundial
#0x03 = Secreto 1
#0x04 = Secreto Final

# 0x1feaf3: [8-bit] Mr.Crown - Categoria do lutador
mr_5 = byte(0x1feaf3)
#0x00 até 0x31 = novato
#0x32 = Pro
#0x65 = Veteran

# 0x1feaf4: [16-bit] Mr.Crown - Quantidade de Lutas (Championship mode)
mr_6 = word(0x1feaf4)

# 0x1feaf6: [16-bit] Mr.Crown - Quantidade de Vitorias (Championship mode)
mr_7 = word(0x1feaf6)

# 0x1feaf8: [16-bit] Mr.Crown - Quantidade de Derrotas (Championship mode)
mr_8 = word(0x1feaf8)

# 0x1feafa: [16-bit] Mr.Crown - Quantidade de K.O (Championship mode)
mr_9 = word(0x1feafa)

# 0x1feafc: [16-bit] Mr.Crown - Ponto de Personagem (Championship mode)
mr_10 = word(0x1feafc)

# 0x1feb00: [8-bit] Mr.Crown - Cinturão Local Light - Contador de Vitórias e Defesas
mr_11 = byte(0x1feb00)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb02: [8-bit] Mr.Crown - Cinturão Nacional Light - Contador de Vitórias e Defesas
mr_12 = byte(0x1feb02)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb04: [8-bit] Mr.Crown - Cinturão Mundial Light - Contador de Vitórias e Defesas
mr_13 = byte(0x1feb04)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb06: [8-bit] Mr.Crown - Cinturão Secret Light - Contador de Vitórias e Defesas
mr_14 = byte(0x1feb06)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb08: [8-bit] Mr.Crown - Cinturão Local Middle - Contador de Vitórias e Defesas
mr_15 = byte(0x1feb08)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb0a: [8-bit] Mr.Crown - Cinturão Nacional Middle - Contador de Vitórias e Defesas
mr_16 = byte(0x1feb0a)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb0c: [8-bit] Mr.Crown - Cinturão Mundial Middle - Contador de Vitórias e Defesas
mr_17 = byte(0x1feb0c)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb0e: [8-bit] Mr.Crown - Cinturão Secret Middle - Contador de Vitórias e Defesas
mr_18 = byte(0x1feb0e)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb10: [8-bit] Mr.Crown - Cinturão Local Heavy - Contador de Vitórias e Defesas
mr_19 = byte(0x1feb10)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb12: [8-bit] Mr.Crown - Cinturão Nacional Heavy - Contador de Vitórias e Defesas
mr_20 = byte(0x1feb12)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb14: [8-bit] Mr.Crown - Cinturão Mundial Heavy - Contador de Vitórias e Defesas
mr_21 = byte(0x1feb14)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb16: [8-bit] Mr.Crown - Cinturão Secret Heavy - Contador de Vitórias e Defesas
mr_22 = byte(0x1feb16)
#0x00 =  Nunca conquistou este título
#0x01 = Primeira conquista do cinturão
#0x02+ = Defesas de título bem-sucedidas ou novas conquistas no mesmo save

# 0x1feb20: [16-bit] Mr.Crown - Total de Pontos (Championship mode)
mr_23 = word(0x1feb20)

# 0x1fed60: [8-bit] Valor de Pontos recebidos (Championship mode)
valor_de_pontos_recebidos = byte(0x1fed60)

# 0x1fed62: [8-bit] Valor de Bonus recebido (Championship mode)
valor_de_bonus_recebido = byte(0x1fed62)

# 0x1fed64: [8-bit] Valor Total recebido (Championship mode)
valor_total_recebido = byte(0x1fed64)

# 0x1fedc0: [16-bit] Valor de ataque P1
valor_de_ataque_p1 = word(0x1fedc0)

# 0x1fedc8: [16-bit] Valor de defesa P1
valor_de_defesa_p1 = word(0x1fedc8)

# 0x1fedd0: [16-bit] valor do rush P1
valor_do_rush_p1 = word(0x1fedd0)

# 0x1fedd8: [16-bit] Primeira Vida P1
primeira_vida_p1 = word(0x1fedd8)

# 0x1feddc: [16-bit] Vida Final P1
vida_final_p1 = word(0x1feddc)

# 0x1fede0: [16-bit] Energia do lutador P1
energia_do_lutador_p1 = word(0x1fede0)

# 0x1fedf8: [16-bit] Valor de ataque P2
valor_de_ataque_p2 = word(0x1fedf8)

# 0x1fee00: [16-bit] Valor de defesa P2
valor_de_defesa_p2 = word(0x1fee00)

# 0x1fee08: [16-bit] Valor do Rush P2
valor_do_rush_p2 = word(0x1fee08)

# 0x1fee10: [16-bit] Primeira Vida P2
primeira_vida_p2 = word(0x1fee10)

# 0x1fee14: [32-bit] Vida Final P2
vida_final_p2 = dword(0x1fee14)

# 0x1fee18: [16-bit] Energia do lutador P2
energia_do_lutador_p2 = word(0x1fee18)

# 0x1fee20: [8-bit] Corrente de soco P1
corrente_de_soco_p1 = byte(0x1fee20)
#0x00 = nenhum soco
#0x01 = 1 soco
#0x02 = 2 soco

# 0x1fee24: [8-bit] Corrente de soco P2
corrente_de_soco_p2 = byte(0x1fee24)
#0x00 = nenhum soco
#0x01 = 1 soco
#0x02 = 2 soco

# 0x1fee54: [array] dano P1
dano_p1 = byte(0x1fee54)

# 0x1fee58: [array] dano P1
dano_p1_2 = byte(0x1fee58)

# 0x1fee5c: [array] dano P1
dano_p1_3 = byte(0x1fee5c)

# 0x1fee60: [array] dano P2
dano_p2 = byte(0x1fee60)

# 0x1fee64: [array] dano P2
dano_p2_2 = byte(0x1fee64)

# 0x1fee68: [array] dano P2
dano_p2_3 = byte(0x1fee68)

# 0x1fef74: [8-bit] Indicador de localição ele armazena aonde o player esta
indicador_de_localio_ele_armazena_aonde_o_player_esta = byte(0x1fef74)
#0x00 =  Ranking
#0x01 = Scout
#0x02 = VS
#0x03 = Record
#0x04 = Note
#0x05 = Memory Card

# 0x1feff0: [8-bit] Indicador de localição?
indicador_de_localio = byte(0x1feff0)
#09 = Menu inicial
#0e = Em luta
#0f = Visualização do Story
#0a = Menu game
#06 = Tela final

# 0x1ffea4: [8-bit] Menu opções?
menu_opes = byte(0x1ffea4)
#0x00 = start
#0x01 = Continue
