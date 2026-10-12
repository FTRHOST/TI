# Superclass
class PegawaiKampus:
    def __init__(self, nama):
        self.nama = nama

    def hitung_gaji(self):
        return 3000000 # Gaji pokok standar (Base/Default)

    def deskripsi_tugas(self):
        print(f"{self.nama} melakukan tugas umum administrasi kampus.")

# Subclass 1: Melakukan Overriding
class Dosen(PegawaiKampus):
    # Overriding metode hitung_gaji()
    def hitung_gaji(self):
        gaji_pokok = super().hitung_gaji() # Mengambil nilai dari induk
        tunjangan_mengajar = 200000
        return gaji_pokok + tunjangan_mengajar

    # Overriding metode deskripsi_tugas()
    def deskripsi_tugas(self):
        print(f"Dosen {self.nama} bertugas mengajar dan melakukan penelitian.")

# Subclass 2: Tidak melakukan Overriding pada gaji
class StafKeamanan(PegawaiKampus):
    def deskripsi_tugas(self):
        print(f"Bapak {self.nama} menjaga keamanan lingkungan fakultas.")

# Instansiasi Objek
pegawai1 = StafKeamanan("Budi")
dosen1 = Dosen("Ahmad")

print("--- Data Staf Keamanan ---")
pegawai1.deskripsi_tugas()
print(f"Gaji: Rp{pegawai1.hitung_gaji()}")

print("\n--- Data Dosen ---")
dosen1.deskripsi_tugas()
print(f"Gaji: Rp{dosen1.hitung_gaji()}")
