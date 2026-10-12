# Inisialisasi minimal 5 data pengguna
pengguna = ["Andi", "Fathir", "Adit", "Parhan", "Azis"]
print("Data awal:", pengguna)

# Tambah data di posisi tertentu, misalksn nih di index 2
pengguna.insert(2, "Arkan")
print("Setelah insert di index 2:", pengguna)

# Hapus data di posisi tertentu misal di index ke 4
data_dihapus = pengguna.pop(4)
print(f"Setelah delete index 4 ({data_dihapus}):", pengguna)
