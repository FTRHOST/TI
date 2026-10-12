# Program: Sistem Manajemen Layanan Sederhana
# Integrasi Tugas 1 - Tugas 5 (UTS)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def hapus_node(self, target):
        temp = self.head
        if temp is not None and temp.data == target:
            self.head = temp.next
            temp = None
            return True
        prev = None
        while temp is not None and temp.data != target:
            prev = temp
            temp = temp.next
        if temp is None:
            return False
        prev.next = temp.next
        temp = None
        return True

    def tampilkan(self):
        temp = self.head
        if not temp:
            print("Daftar pengguna kosong.")
            return
        hasil = []
        while temp:
            hasil.append(temp.data)
            temp = temp.next
        print("Data Pengguna (Linked List):", " -> ".join(hasil))

# Inisialisasi Komponen Utama
data_pengguna = LinkedList()
antrian_layanan = []  # FIFO (Queue)
riwayat_aktivitas = [] # LIFO (Stack)

# Komponen Hash Table untuk Pencarian (Tugas 5)
UKURAN_TABEL = 5
hash_table = [[] for _ in range(UKURAN_TABEL)]

def fungsi_hash(id_pengguna):
    return id_pengguna % UKURAN_TABEL

def simpan_ke_hash(id_pengguna, nama):
    indeks = fungsi_hash(id_pengguna)
    hash_table[indeks].append({"id": id_pengguna, "nama": nama})

def cari_di_hash(id_pengguna):
    indeks = fungsi_hash(id_pengguna)
    for item in hash_table[indeks]:
        if item["id"] == id_pengguna:
            return item["nama"]
    return None

def catat_aktivitas(pesan):
    riwayat_aktivitas.append(pesan)

def main():
    while True:
        print("\n=== SISTEM MANAJEMEN LAYANAN SEDERHANA ===")
        print("1. Tambah Data Pengguna")
        print("2. Lihat Semua Pengguna")
        print("3. Tambah Antrian Layanan")
        print("4. Proses Antrian (Dequeue)")
        print("5. Cari Data Pengguna (ID)")
        print("6. Lihat Riwayat Aktivitas")
        print("7. Batalkan Aktivitas Terakhir (Undo)")
        print("0. Keluar")
        
        pilihan = input("Pilih menu (0-7): ")

        if pilihan == '1':
            nama = input("Masukkan Nama Pengguna: ")
            try:
                id_user = int(input("Masukkan ID Pengguna (Angka): "))
                data_pengguna.tambah_node(nama)
                simpan_ke_hash(id_user, nama)
                catat_aktivitas(f"Menambahkan pengguna: {nama} (ID: {id_user})")
                print(f"Berhasil menambahkan {nama}.")
            except ValueError:
                print("Error: ID harus berupa angka!")

        elif pilihan == '2':
            data_pengguna.tampilkan()

        elif pilihan == '3':
            nama_pasien = input("Masukkan Nama untuk Antrian: ")
            antrian_layanan.append(nama_pasien)
            catat_aktivitas(f"Menambah antrian: {nama_pasien}")
            print(f"{nama_pasien} telah masuk antrian.")

        elif pilihan == '4':
            if antrian_layanan:
                dilayani = antrian_layanan.pop(0) # FIFO logic
                catat_aktivitas(f"Memproses layanan untuk: {dilayani}")
                print(f"Sedang melayani: {dilayani}")
            else:
                print("Antrian kosong.")

        elif pilihan == '5':
            try:
                id_cari = int(input("Masukkan ID yang dicari: "))
                hasil = cari_di_hash(id_cari)
                if hasil:
                    print(f"Data ditemukan! Nama: {hasil}")
                else:
                    print("Data tidak ditemukan.")
            except ValueError:
                print("Error: Masukkan ID angka.")

        elif pilihan == '6':
            print("Riwayat Aktivitas (Stack):", riwayat_aktivitas)

        elif pilihan == '7':
            if riwayat_aktivitas:
                dibatalkan = riwayat_aktivitas.pop() # LIFO logic
                print(f"Aktivitas '{dibatalkan}' telah dibatalkan (Undo).")
            else:
                print("Tidak ada riwayat untuk dibatalkan.")

        elif pilihan == '0':
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
