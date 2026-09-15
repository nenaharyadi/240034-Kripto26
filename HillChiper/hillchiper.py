# Nama : Nena Haryadi Puspanegara
# NPM  : 140810240034

import numpy as np

def invers_matriks_mod26(matriks):
    det = int(np.round(np.linalg.det(matriks))) % 26
    
    invers_det = 0
    for i in range(26):
        if (det * i) % 26 == 1:
            invers_det = i
            break
            
    if invers_det == 0:
        return None 
        
    matriks_inv = np.linalg.inv(matriks)
    adjoin = np.round(det * matriks_inv).astype(int) % 26
    
    return (invers_det * adjoin) % 26

def enkripsi_hill(teks, kunci, n):
    teks = teks.upper().replace(" ", "")
    
    sisa = len(teks) % n
    if sisa != 0:
        teks += 'X' * (n - sisa)
        
    angka_teks = [ord(c) - 65 for c in teks]
    matriks_p = np.array(angka_teks).reshape(-1, n).T 
    
    matriks_c = np.dot(kunci, matriks_p) % 26
    hasil_angka = matriks_c.T.flatten()
    
    return "".join([chr(int(angka) + 65) for angka in hasil_angka])

def dekripsi_hill(teks, kunci, n):
    teks = teks.upper().replace(" ", "")
    kunci_invers = invers_matriks_mod26(kunci)
    
    if kunci_invers is None:
        return "Error: Kunci matriks tidak memiliki invers modulo 26!"
        
    angka_teks = [ord(c) - 65 for c in teks]
    matriks_c = np.array(angka_teks).reshape(-1, n).T
    
    matriks_p = np.dot(kunci_invers, matriks_c) % 26
    hasil_angka = matriks_p.T.flatten()
    
    return "".join([chr(int(angka) + 65) for angka in hasil_angka])

def cari_kunci(plaintext, ciphertext, n):
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ciphertext.upper().replace(" ", "")
    
    # Ambil N*N huruf pertama untuk membuat matriks N x N
    butuh_huruf = n * n
    P = np.array([ord(c) - 65 for c in plaintext[:butuh_huruf]]).reshape(n, n).T
    C = np.array([ord(c) - 65 for c in ciphertext[:butuh_huruf]]).reshape(n, n).T
    
    P_invers = invers_matriks_mod26(P)
    if P_invers is None:
        return "Error: Plaintext tidak memiliki invers modulo 26!"
        
    K = np.dot(C, P_invers) % 26
    return K.astype(int)

if __name__ == "__main__":
    print("Program Hill Chiper")
    
    n = int(input("Masukkan ukuran ordo matriks : "))
    
    print(f"Masukkan {n*n} angka elemen matriks kunci :")
    input_kunci = input(">> ")
    
    angka_kunci = list(map(int, input_kunci.split()))
    K = np.array(angka_kunci).reshape(n, n)
    
    print("\nMatriks Kunci yang Digunakan:")
    print(K)
    
    teks_input = input("\nKetik teks yang ingin dienkripsi: ")
    
    hasil_enkripsi = enkripsi_hill(teks_input, K, n)
    print(f">> Hasil Enkripsi : {hasil_enkripsi}")
    
    hasil_dekripsi = dekripsi_hill(hasil_enkripsi, K, n)
    print(f">> Hasil Dekripsi : {hasil_dekripsi}")

    print(f"\n Mencari kunci")
    input_pt = input(f"Ketik minimal {n*n} huruf Plaintext  : ")
    input_ct = input(f"Ketik minimal {n*n} huruf Ciphertext : ")
    
    kunci_baru = cari_kunci(input_pt, input_ct, n)
    print(">> Matriks Kunci yang ditemukan:")
    print(kunci_baru)