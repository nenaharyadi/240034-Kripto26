#Nama : Nena Haryadi Puspanegara
#NPM  : 140810240034

from PIL import Image

def text_to_binary(text):
    """Mengonversi teks menjadi deretan bit biner 8-bit."""
    return ''.join([format(ord(char), "08b") for char in text])

def binary_to_text(binary_data):
    """Mengonversi deretan bit biner kembali menjadi teks."""
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_text = ""
    for byte in all_bytes:
        if len(byte) == 8:
            decoded_text += chr(int(byte, 2))
    return decoded_text

def encode_lsb_sekuensial(image_path, secret_message, output_path):
    """Menyisipkan pesan secara berurutan piksel demi piksel dari pojok kiri atas."""
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    width, height = img.size
    
    # Penanda akhir pesan
    secret_message += "#####"
    binary_msg = text_to_binary(secret_message)
    data_len = len(binary_msg)
    
    # Cek kapasitas gambar
    if data_len > width * height * 3:
        raise ValueError("Ukuran pesan terlalu panjang untuk gambar ini.")
        
    data_index = 0
    
    # Iterasi sekuensial baris demi baris, kolom demi kolom
    for y in range(height):
        for x in range(width):
            if data_index >= data_len:
                break
                
            r, g, b = pixels[x, y]
            
            # Sisipkan ke LSB komponen Red
            if data_index < data_len:
                r = int(format(r, '08b')[:-1] + binary_msg[data_index], 2)
                data_index += 1
                
            # Sisipkan ke LSB komponen Green
            if data_index < data_len:
                g = int(format(g, '08b')[:-1] + binary_msg[data_index], 2)
                data_index += 1
                
            # Sisipkan ke LSB komponen Blue
            if data_index < data_len:
                b = int(format(b, '08b')[:-1] + binary_msg[data_index], 2)
                data_index += 1
                
            pixels[x, y] = (r, g, b)
            
        if data_index >= data_len:
            break
            
    img.save(output_path)
    print(f"[+] Encode Sekuensial Berhasil! Gambar disimpan di: {output_path}")

def decode_lsb_sekuensial(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    width, height = img.size
    
    binary_buffer = ""
    decoded_chars = []
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Ambil bit LSB komponen R, G, B
            for bit in (format(r, '08b')[-1], format(g, '08b')[-1], format(b, '08b')[-1]):
                binary_buffer += bit
                
                # Begitu terkumpul 8 bit, ubah jadi 1 karakter
                if len(binary_buffer) == 8:
                    char = chr(int(binary_buffer, 2))
                    decoded_chars.append(char)
                    binary_buffer = ""
                    
                    # Cek 5 karakter terakhir untuk penanda pembatas
                    if len(decoded_chars) >= 5 and "".join(decoded_chars[-5:]) == "#####":
                        return "".join(decoded_chars[:-5])
                        
    return "Pesan tidak ditemukan atau gambar rusak."

if __name__ == '__main__':
    print("Program Steganografi metode LSB")
    
    cover = "cover.png"
    stego = "steganografi.png"
    pesan = "hai aku nena salam kenal, ini pesan rahasia menggunakan lsb."
    
    # Encode
    print("\n[1] Memproses Encode...")
    encode_lsb_sekuensial(cover, pesan, stego)
    
    # Decode
    print("\n[2] Memproses Decode...")
    hasil = decode_lsb_sekuensial(stego)
    print(f"[+] Pesan terekstrak: {hasil}")