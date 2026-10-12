class Mahasiswa:
    def __init__ (self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.prodi = "Teknologi Informasi"

    def perkenalan(self):
        print(f'Hali perkenalkan nama saya {self.nama}, dengan NIM {self.nim} dan dari program studi {self.prodi}')

mhs1 = Mahasiswa("Muhammad Fathir Al Faruq", 43050250011)
mhs2 = Mahasiswa("Ahmad Taufiq", 43050250012)
mhs1.prodi = "Sains Data"

print("\n=== Data Objek Mahasiswa ===")
print("NAMA: ", mhs1.nama)
print("NIM: ", mhs1.nim)
print("PRODI: ", mhs1.prodi)

print("\n=== Data Objek Mahasiswa 2 ===")
print("NAMA: ", mhs2.nama)
print("NIM: ", mhs2.nim)
print("PRODI: ", mhs2.prodi)

print("\n=== Method ===")
mhs1.perkenalan()
mhs2.perkenalan()
