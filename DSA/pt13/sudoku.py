
# Papan Sudoku 4x4 dengan beberapa angka kosong (0)
papan_mini = [
    [1, 0, 3, 0],
    [0, 0, 0, 2],
    [3, 0, 0, 0],
    [0, 1, 0, 0]
]

def cetak_sudoku():
    for baris in papan_mini:
        print(baris)
    print("=" * 15)

def aman_kah(angka, baris, kol):
    # 1. Cek Baris
    if angka in papan_mini[baris]:
        return False

    # 2. Cek Kolom
    for b in range(4):
        if papan_mini[b][kol] == angka:
            return False

    # 3. Cek Kotak Kecil 2x2
    awal_baris = (baris // 2) * 2
    awal_kol = (kol // 2) * 2
    for b in range(awal_baris, awal_baris + 2):
        for k in range(awal_kol, awal_kol + 2):
            if papan_mini[b][k] == angka:
                return False

    return True

def selesaikan_sudoku():
    # Cari kotak kosong (0)
    for baris in range(4):
        for kol in range(4):
            if papan_mini[baris][kol] == 0:

                # EKSPLORASI: Coba angka 1 sampai 4
                for angka in range(1, 5):
                    if aman_kah(angka, baris, kol):
                        # 1. PILIH
                        papan_mini[baris][kol] = angka
                        print(f"Coba angka {angka} di posisi ({baris},{kol})")

                        # 2. JELAJAHI
                        if selesaikan_sudoku():
                            return True

                        # 3. BACKTRACK
                        print(f"🔄 Angka {angka} di ({baris},{kol}) bikin buntu. Reset jadi 0.")
                        papan_mini[baris][kol] = 0

                return False # Trigger backtrack untuk fungsi pemanggil di atasnya
    return True # Semua kotak sudah terisi

# Jalankan praktikum
print("--- PAPAN AWAL SUDOKU ---")
cetak_sudoku()

if selesaikan_sudoku():
    print("🎉 SUDOKU SELESAI:")
    cetak_sudoku()
else:
    print("Tidak ada solusi.")
