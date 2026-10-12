
# Membuat fungsi untuk menghitung luas persegi
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

print("=== Program Hitung Luas Persegi ===")

# Memasukan input nilai sisi persegi
sisi_input = float(input("Masukkan panjang sisi persegi: "))

# Memanggil fungsi dan menyimpan hasilnya
hasil_luas = hitung_luas_persegi(sisi_input)

# Menampilkan hasil
print(f"Luas persegi dengan sisi {sisi_input} adalah: {hasil_luas}")
print("==== TERIMA KASIH ====")
