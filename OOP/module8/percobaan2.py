class MahasiswaTI:
    def __init__(self, nama, nim): 
        self.nama = nama 
        self.nim = nim 
 # Representasi untuk End-User (Human Readable) 
    def __str__(self):
        return f"Mahasiswa: {self.nama} (NIM: {self.nim})" 
 # Representasi untuk Developer (Unambiguous) 
    def __repr__(self): 
        return f"<MahasiswaTI(nama='{self.nama}', nim='{self.nim}')>" 
mhs1 = MahasiswaTI("Irzaq", "43210987") 
# Menguji __str__ (Otomatis dipanggil saat menggunakan print) 
print("Output print():") 
print(mhs1) 
# Menguji __repr__ (Dipanggil menggunakan fungsi repr() atau saat di dalam sebuah List) 
print("\nOutput repr():") 
print(repr(mhs1)) 
# Tampilan di dalam List akan menggunakan __repr__ 
daftar_mhs = [mhs1] 
print("\nOutput dalam List:") 
print(daftar_mhs)
