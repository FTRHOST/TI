
# Membuat list kosong
data_angka = []

# Memakai perulangan supaya bisa di input 5 kali 
print("=== APLIKASI PERHITUNGAN ANGKA ===")
print("Masukkan 5 angka:")
for i in range(5):
    angka = float(input(f"Angka ke-{i+1}: "))
    data_angka.append(angka)

# Melakukan perhitungan
terbesar = max(data_angka)
terkecil = min(data_angka)
rata_rata = sum(data_angka) / len(data_angka)

# Menampilkan hasil
print("=== Menampilkan data angka dari semua nilai yang di input sampai dengan rata-rata")
print(f"Data angka     : {data_angka}")
print(f"Nilai terbesar : {terbesar}")
print(f"Nilai terkecil : {terkecil}")
print(f"Rata-rata      : {rata_rata}")
print("==== TERIMA KASIH ====")

