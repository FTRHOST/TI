class MataKuliah: 
    def __init__(self, nama_mk, sks):
        self.nama_mk = nama_mk 
        self.sks = sks 
    def __str__(self): 
        return f"{self.nama_mk} ({self.sks} SKS)" 
 # Memodifikasi operator penambahan (+) 
    def __add__(self, objek_lain): 
 # Memastikan objek_lain adalah instance dari MataKuliah 
        if isinstance(objek_lain, MataKuliah): 
            total_sks = self.sks + objek_lain.sks 
            return total_sks 
            return NotImplemented 
 # Memodifikasi operator kesamaan (==) 
 def __eq__(self, objek_lain):
    if isinstance(objek_lain, MataKuliah):
    return self.sks == objek_lain.sks
    return False 
# Instansiasi Objek 
mk1 = MataKuliah("Pemrograman Berorientasi Objek", 3) 
mk2 = MataKuliah("Kecerdasan Buatan", 3) 
mk3 = MataKuliah("Pancasila", 2) 
print(f"MK 1: {mk1}") 
print(f"MK 2: {mk2}") 
# Menguji Magic Method __add__
total_beban = mk1 + mk2 
print(f"\nTotal SKS gabungan: {total_beban} SKS") 
# Menguji Magic Method __eq__ 
print("\nApakah SKS PBO sama dengan AI?") 
if mk1 == mk2: 
    print("Ya, bobot SKS sama.") 
else:
    print("Tidak, bobot SKS berbeda.")
