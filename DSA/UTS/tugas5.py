ukuran_tabel = 5
hash_table = [[] for _ in range(ukuran_tabel)]

def fungsi_hash(id_pengguna):
    return id_pengguna % ukuran_tabel

def simpan_data(id_pengguna, nama):
    indeks = fungsi_hash(id_pengguna)
    hash_table[indeks].append({"id": id_pengguna, "nama": nama})
    print(f"Disimpan '{nama}' di indeks {indeks}")

def cari_data(id_pengguna):
    indeks = fungsi_hash(id_pengguna)
    for item in hash_table[indeks]:
        if item["id"] == id_pengguna:
            return item["nama"]
    return "Tidak ditemukan"

# Skenario manual membuat collision
# 102 % 5 = 2
# 207 % 5 = 2
# Nah nantikan akan menghasilakn index yang sama
# dengan begitu visualisasi hash table supaya tau adalah dengan membuatnya menjadi multidimensi
# yang nanti akan di simpan di array yang sama
simpan_data(101, "Andi")
simpan_data(102, "Budi")
simpan_data(207, "Citra") 

print("\nVisualisasi Hash Table saat ini:")
for i, bucket in enumerate(hash_table):
    print(f"Indeks {i}: {bucket}")

print(f"\nHasil pencarian ID 207: {cari_data(207)}")
