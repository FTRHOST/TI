# 1. Mendefinisikan Class
class Mahasiswa:
    # Fungsi inisialisasi awal (Constructor sederhana)
    def __init__(self, nama, nim):
        self.nama = nama # Ini adalah atribut
        self.nim = nim # Ini adalah atribut
        self.prodi = "Teknologi Informasi" # Atribut dengan nilai default

    # Mendefinisikan perilaku (Method)
    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}, NIM {self.nim} dari prodi {self.prodi}.")

# 2. Membuat Object (Instansiasi)
mhs1 = Mahasiswa("Ahmad Taufiq", "12345678")
mhs2 = Mahasiswa("Siti Aminah", "87654321")

# 3. Mengakses atribut object
print("--- Data Objek Mahasiswa 1 ---")
print("Nama :", mhs1.nama)
print("NIM :", mhs1.nim)

print("\n--- Data Objek Mahasiswa 2 ---")
print("Nama :", mhs2.nama)

# 4. Memanggil method dari object
print("\n--- Memanggil Method ---")
mhs1.perkenalan()
mhs2.perkenalan()

# Mengubah nilai atribut secara langsung
mhs1.prodi = "Sains Data"
print("\n--- Setelah Atribut Dimodifikasi ---")
mhs1.perkenalan()
