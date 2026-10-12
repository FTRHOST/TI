class SivitasAkademika:
    def __init__(self, nama, asal_daerah):
        self.nama = nama
        self.asal_daerah = asal_daerah
        pass
    def presensi(self):
        print(f'{self.nama} dari {self.asal_daerah} telah melakukan presensi kehadiran.')
        pass
    pass

class Mahasiswa(SivitasAkademika):
    pass

mhs1 = Mahasiswa("Ahmad Taufiq", "Salatiga")
print("--- Pengujian Inheritence Dasar ---")

print(f'Nama: {mhs1.nama}')
mhs1.presensi()
