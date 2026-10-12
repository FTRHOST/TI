class Kendaraan:
    def __init__(self, merk, warna, tahun_keluaran):
        self.merk = merk
        self.warna = warna
        self.tahun_keluaran = tahun_keluaran
        self.status_mesin = "Mati" # Nilai default

    def nyalakan_mesin(self):
        self.status_mesin = "Menyala"
        print(f"Mesin {self.merk} telah dinyalakan.")

    def matikan_mesin(self):
        self.status_mesin = "Mati"
        print(f"Mesin {self.merk} telah dimatikan.")

# Instansiasi 3 objek kendaraan
mobil1 = Kendaraan("Toyota Avanza", "Putih", 2022)
mobil2 = Kendaraan("Honda Civic", "Hitam", 2023)
motor1 = Kendaraan("Yamaha NMAX", "Biru", 2021)

# Nyalakan mesin dua kendaraan
print("--- Menjalankan Aksi Kendaraan ---")
mobil1.nyalakan_mesin()
motor1.nyalakan_mesin()

# Cetak status seluruh kendaraan di akhir
print("\n--- Status Akhir Seluruh Kendaraan ---")
print(f"Kendaraan 1: {mobil1.merk} ({mobil1.warna}) - Status: {mobil1.status_mesin}")
print(f"Kendaraan 2: {mobil2.merk} ({mobil2.warna}) - Status: {mobil2.status_mesin}")
print(f"Kendaraan 3: {motor1.merk} ({motor1.warna}) - Status: {motor1.status_mesin}")
