class BukuPerpustakaan:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = False 

    def pinjam_buku(self):
        if self.status_pinjam == False:
            self.status_pinjam = True
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Maaf, buku '{self.judul}' sedang dipinjam.")

# Membuat dua objek buku
buku1 = BukuPerpustakaan("Laskar Pelangi", "Andrea Hirata", 2005)
buku2 = BukuPerpustakaan("Bumi Manusia", "Pramoedya Ananta Toer", 1980)

print("--- Proses Peminjaman Buku ---")
# Meminjam buku1 sebanyak dua kali secara berurutan
buku1.pinjam_buku()  # Percobaan pertama
buku1.pinjam_buku()  # Percobaan kedua
