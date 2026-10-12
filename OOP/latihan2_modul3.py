class Rekening:
    def __init__(self, nama_pemilik, nomor_rekening, saldo):
        self.nama_pemilik = nama_pemilik
        self.nomor_rekening = nomor_rekening
        self.saldo = saldo
        
    def simpan_uang(self, jumlah):
        self.saldo += jumlah
        print(f"--- STRUK TRANSAKSI ---")
        print(f"Simpan uang sebesar: Rp{jumlah}")
        print(f"Saldo saat ini menjadi: Rp{self.saldo}")
        print("-----------------------")
        
    def tarik_uang(self, jumlah):
        print(f"Mencoba menarik uang sebesar: Rp{jumlah}")
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"Penarikan berhasil. Sisa saldo: Rp{self.saldo}")
        else:
            print("Saldo tidak mencukupi")
            
    def cek_saldo(self):
        print(f"Sisa saldo saat ini untuk rekening {self.nomor_rekening} a/n {self.nama_pemilik}: Rp{self.saldo}")

# Membuat satu objek rekening
rekening_mahasiswa = Rekening("Andi", "1234567890", 100000)

print("--- Simulasi Transaksi ---")
# 1x Penyimpanan uang
rekening_mahasiswa.simpan_uang(50000)

print("\n")
# 2x Penarikan uang (satu sukses, satu gagal)
rekening_mahasiswa.tarik_uang(80000)  # Sukses
print("\n")
rekening_mahasiswa.tarik_uang(100000) # Gagal karena kurang saldo

print("\n--- Saldo Akhir ---")
# Menampilkan saldo akhir
rekening_mahasiswa.cek_saldo()
