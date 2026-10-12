class Dosen:
    def __init__(self, nama, nidn, mata_kuliah):
        self.nama = nama
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def mengajar(self):
        print(f"Dosen {self.nama} dengan NIDN {self.nidn} sedang mengajar mata kuliah {self.mata_kuliah}.")

# Instansiasi dua objek dosen
dosen1 = Dosen("Ahmad Rois Syujak", "19850101", "Pemrograman Berorientasi Objek")
dosen2 = Dosen("Sari Wijaya, M.T.", "19900202", "Basis Data")

# Memanggil method mengajar()
print("--- Latihan Mandiri 1: Class Dosen ---")
dosen1.mengajar()
dosen2.mengajar()
