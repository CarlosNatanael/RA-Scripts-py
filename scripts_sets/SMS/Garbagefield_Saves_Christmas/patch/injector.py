import json
import sys

def inject_translation(original_rom, patched_rom, json_map_file):
    # Carrega o mapa de tradução
    with open(json_map_file, 'r', encoding='utf-8') as f:
        translation_map = json.load(f)

    # Carrega a ROM original em bytes
    with open(original_rom, 'rb') as f:
        rom_data = bytearray(f.read())

    erros = 0

    for orig_str, trans_str in translation_map.items():
        # Valida a presença de acentos (restrição da tabela ASCII do jogo)
        try:
            orig_bytes = orig_str.encode('ascii')
            trans_bytes = trans_str.encode('ascii')
        except UnicodeEncodeError:
            print(f"[ERRO DE ENCODING] Remova os acentos da string: '{trans_str}'")
            erros += 1
            continue

        # Localiza o offset da string no arquivo binário
        offset = rom_data.find(orig_bytes)
        if offset == -1:
            print(f"[AVISO] String original não encontrada na ROM: '{orig_str[:30]}...'")
            continue

        len_orig = len(orig_bytes)
        len_trans = len(trans_bytes)

        # Bloqueia se a tradução for maior que o espaço original
        if len_trans > len_orig:
            print(f"[ERRO DE LIMITE] A tradução excedeu em {len_trans - len_orig} bytes.")
            print(f"Original ({len_orig} bytes): {orig_str}")
            print(f"Tradução ({len_trans} bytes): {trans_str}\n")
            erros += 1
            continue

        # Preenchimento automático com espaços (Hex 20) até atingir o limite
        padded_trans = trans_bytes.ljust(len_orig, b' ')
        
        # Substitui os bytes na ROM
        rom_data[offset:offset+len_orig] = padded_trans

    if erros > 0:
        print(f"\nOperação abortada devido a {erros} erro(s). A ROM modificada não foi salva.")
        sys.exit(1)

    # Compila a nova ROM
    with open(patched_rom, 'wb') as f:
        f.write(rom_data)
    
    print("\n[SUCESSO] Patch validado, inserido e nova ROM compilada.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso correto: python injector.py <Garbagefield Saves Christmas (U).sms> <rom_traduzida.sms> <traducoes.json>")
        sys.exit(1)
        
    rom_in = sys.argv[1]
    rom_out = sys.argv[2]
    json_map = sys.argv[3]
    
    inject_translation(rom_in, rom_out, json_map)