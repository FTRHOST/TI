from abc import ABC, abstractmethod
# 1. Membuat Abstract Base Class (ABC) 
class SistemPembayaran(ABC):
 # Mendefinisikan Abstract Method (Kontrak wajib) 
    @abstractmethod
    def proses_bayar(self, nominal):
        pass
 # Concrete method (Metode biasa yang langsung bisa dipakai)
    def cetak_struk(self):
        print("Mencetak bukti transaksi...") 
# 2. Membuat Subclass yang mewarisi class abstrak 
class PembayaranUKT(SistemPembayaran):
    # Wajib melakukan overriding pada metode abstrak! 
    def proses_bayar(self, nominal):
        print(f"Memproses pembayaran UKT sebesar Rp{nominal}")

class PembayaranPraktikum(SistemPembayaran):
    # Wajib melakukan overriding pada metode abstrak!
    def proses_bayar(self, nominal):
        print(f"Memproses biaya modul praktikum sebesar Rp{nominal}")

# Instansiasi objek dan Pengujian 
ukt_mhs = PembayaranUKT() 
ukt_mhs.proses_bayar(3000000) 
ukt_mhs.cetak_struk() 
modul_mhs = PembayaranPraktikum() 
modul_mhs.proses_bayar(150000) 
# Coba hapus/komentari fungsi proses_bayar() di dalam class PembayaranUKT, 
# lalu jalankan ulang. Program akan menghasilkan TypeError karena melanggar kontrak abstrak
