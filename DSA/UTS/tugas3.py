antrian_layanan = []

# Tambah Antrian
antrian_layanan.append("Pasien_01")
antrian_layanan.append("Pasien_02")
antrian_layanan.append("Pasien_03")

print("Urutan antrian SEBELUM diproses:", antrian_layanan)

# Dequeue
# Menggunakan pop(0) untuk mengambil elemen pertama, index pertama gess yaitu 0
dilayani = antrian_layanan.pop(0)

print(f"\nMemproses layanan untuk: {dilayani}")
print("Urutan antrian SESUDAH diproses:", antrian_layanan)
