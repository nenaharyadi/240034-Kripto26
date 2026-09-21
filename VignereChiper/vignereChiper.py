# Nama : Nena Haryadi Puspanegara
# NPM  : 140810240034

def enkripsi_vigenere(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")

    print("\nProses Enkripsi")
    ciphertext = []
    for i in range(len(plaintext)):
        p_char = plaintext[i]
        k_char = key[i % len(key)]

        p_num = ord(p_char) - 65
        k_num = ord(k_char) - 65
        c_num = (p_num + k_num) % 26
        c_char = chr(c_num + 65)

        ciphertext.append(c_char)
        print(
            f"Karakter {i+1:2d} | PT: {p_char} ({p_num:2d}) + KEY: {k_char} ({k_num:2d}) "
            f"-> ({p_num:2d} + {k_num:2d}) mod 26 = {c_num:2d} -> CT: {c_char}"
        )

    return "".join(ciphertext)


def dekripsi_vigenere(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")

    print("\nProses Deskripsi" \
    "")
    plaintext = []
    for i in range(len(ciphertext)):
        c_char = ciphertext[i]
        k_char = key[i % len(key)]

        c_num = ord(c_char) - 65
        k_num = ord(k_char) - 65
        p_num = (c_num - k_num) % 26
        p_char = chr(p_num + 65)

        plaintext.append(p_char)
        print(
            f"Karakter {i+1:2d} | CT: {c_char} ({c_num:2d}) - KEY: {k_char} ({k_num:2d}) "
            f"-> ({c_num:2d} - {k_num:2d}) mod 26 = {p_num:2d} -> PT: {p_char}"
        )

    return "".join(plaintext)


if __name__ == "__main__":
    print("=== PROGRAM VIGENERE CIPHER ===")
    teks = input("Masukkan Teks/Plaintext: ")
    kunci = input("Masukkan Kunci (Nama Lengkap): ")

    hasil_enkripsi = enkripsi_vigenere(teks, kunci)
    hasil_dekripsi = dekripsi_vigenere(hasil_enkripsi, kunci)

    print("\n-------------------------------------------------------------")
    print(f"Hasil Enkripsi Akhir (CT) : {hasil_enkripsi}")
    print(f"Hasil Dekripsi Akhir (PT) : {hasil_dekripsi}")