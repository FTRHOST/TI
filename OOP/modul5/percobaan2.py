class SivitasAkademika:
    def __init__(self, nama, asal_daerah):
        self.nama = nama
        self.asal_daerah = asal_daerah

    def presensi(self):
        print(f"{self.nama} telah melakukan presensi.")

# Subclass Mahasiswa
class Mahasiswa(SivitasAkademika):
    def __init__(self, nama, asal_daerah, nim):
        # Memanggil __init__ dari Superclass
        super().__init__(nama, asal_daerah)
        # Menambahkan atribut spesifik untuk Mahasiswa
        self.nim = nim

    def info_mahasiswa(self):
        print(f"Mahasiswa: {self.nama}, NIM: {self.nim}")

# Subclass Dosen
class Dosen(SivitasAkademika):
    def __init__(self, nama, asal_daerah, nidn):
        super().__init__(nama, asal_daerah)
        self.nidn = nidn

    def mengajar(self):
        print(f"Dosen {self.nama} (NIDN: {self.nidn}) sedang mengajar di kelas.")

# Instansiasi
mhs = Mahasiswa("Siti Aminah", "Semarang", "12345678")
dsn = Dosen("Rudi Hermawan", "Yogyakarta", "987654321")

print("--- Pengujian Fungsi super() ---")
# Keduanya bisa melakukan presensi (Metode Induk)
mhs.presensi()
dsn.presensi()

# Memanggil metode spesifik masing-masing (Metode Anak)
mhs.info_mahasiswa()
dsn.mengajar()
