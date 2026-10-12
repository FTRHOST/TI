class Akademisi:
    def aktivitas(self):
        print("Menjalankan Tri Dharma Perguruan Tinggi.")

class Peneliti(Akademisi):
    def aktivitas(self):
        print("Fokus melakukan riset dan publikasi jurnal ilmiah.")

class Pengajar(Akademisi):
    def aktivitas(self):
        print("Fokus memberikan materi kuliah dan membimbing mahasiswa.")

# Multiple Inheritance: Mewarisi dari Pengajar dan Peneliti
# Urutan di dalam kurung sangat menentukan MRO!
class AsistenAhli(Pengajar, Peneliti):
    pass

# Instansiasi Objek
dosen_muda = AsistenAhli()

print("--- Output Pemanggilan Metode ---")
# Metode mana yang akan dipanggil?
dosen_muda.aktivitas()

print("\n--- Method Resolution Order (MRO) ---")
# Mengecek urutan prioritas pencarian metode oleh Python
print(AsistenAhli.mro())
