# KELAS 1: SUPERCLAS
class BarangKantin:
    def __init__(self, nama, stok, harga_beli):
        self.nama = nama
        # Enkapsulasi: Mengamankan 2 atribut menggunakan private modifier (__)
        self.__stok = stok            
        self.__harga_beli = harga_beli 
        
    # Enkapsulasi: Menggunakan decorator @property sebagai Getter
    @property
    def stok(self):
        return self.__stok
        
    # Enkapsulasi: Setter untuk memastikan stok tidak diset menjadi negatif
    @stok.setter
    def stok(self, nilai_baru):
        if nilai_baru >= 0:
            self.__stok = nilai_baru
        else:
            print("Error: Stok tidak boleh bernilai negatif!")
            
    # Enkapsulasi: Getter untuk harga modal
    @property
    def harga_beli(self):
        return self.__harga_beli

    # Metode polimorfik yang akan di-Override di dalam Subclass
    def tentukan_harga_jual(self):
        pass
        
    def tampilkan_info(self):
        # Memanggil metode yang sifatnya polimorfik
        harga_jual = self.tentukan_harga_jual()
        print(f"Nama Barang : {self.nama}")
        print(f"Stok Sisa   : {self.stok} porsi/pcs")
        print(f"Harga Jual  : Rp{harga_jual}")


# KELAS 2: SUBCLASS (Barang yang dibuat sendiri oleh kantin)
class BarangSendiri(BarangKantin):
    def __init__(self, nama, stok, harga_beli, jenis_masakan):
        # Pewarisan: Wajib menggunakan fungsi super() minimal satu kali
        super().__init__(nama, stok, harga_beli) 
        self.jenis_masakan = jenis_masakan
        
    # Polimorfisme: Melakukan Overriding untuk logika harga jual
    def tentukan_harga_jual(self):
        # Barang produksi kantin mengambil margin keuntungan 25% dari harga modal
        return int(self.harga_beli * 1.25)
        
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kategori    : Produksi Kantin ({self.jenis_masakan})\n")


# KELAS 3: SUBCLASS (Barang jajanan yang dititipkan oleh orang luar)
class BarangTitipan(BarangKantin):
    def __init__(self, nama, stok, harga_beli, supplier):
        # Pewarisan: Menggunakan fungsi super()
        super().__init__(nama, stok, harga_beli) 
        self.supplier = supplier
        
    # Polimorfisme: Melakukan Overriding untuk logika harga jual
    def tentukan_harga_jual(self):
        # Barang titipan memiliki keuntungan tetap Rp1.000 per barang 
        return self.harga_beli + 1000

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kategori    : Barang Titipan (Supplier: {self.supplier})\n")


# --- IMPLEMENTASI & INSTANSIASI OBJECT ---

# Membuat minimal 4 Object yang berbeda
menu1 = BarangSendiri("Ayam Geprek", 20, 10000, "Makanan Berat")
menu2 = BarangSendiri("Es Kopi Susu", 15, 4000, "Minuman")
menu3 = BarangTitipan("Keripik Singkong Balado", 30, 3000, "Bu Siti Snack")
menu4 = BarangTitipan("Roti Coklat Lumer", 10, 4500, "Toko Roti Jaya")
menu5 = BarangTitipan("Sate Usus", 20, 2500, "Bu Indah")

print("="*45)
print(" SISTEM MANAJEMEN INVENTARIS KANTIN KAMPUS ")
print("="*45)

# Polimorfisme: Mendemonstrasikan eksekusi metode melalui perulangan (looping)
daftar_inventaris = [menu1, menu2, menu3, menu4, menu5]

for item in daftar_inventaris:
    item.tampilkan_info()

# Menguji Setter Enkapsulasi (Validasi mengubah stok barang setelah terjual)
print("-" * 45)
print("Simulasi Penjualan Ayam Geprek sebanyak 2 porsi...")
menu1.stok = menu1.stok - 2
print(f"Stok Ayam Geprek saat ini: {menu1.stok} porsi")
