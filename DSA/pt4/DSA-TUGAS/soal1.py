# Memberikan Variable yang akan di isi nantinya
print("====== Aplikasi Penghitung Nilai dan Standar kelulusan =====")
mhs = input("Silahkan masukan nama mahasiswa: ")
nTugas = int(input(f'Silahkan masukan nilai tugas dari mahasiswa ({mhs}): '))
nUTS = int(input(f'Silahkan masukan nilai UTS dari mahasiswa ({mhs}): '))
nUAS = int(input(f'Silahkan masukan nilai UAS dari mahasiswa ({mhs}): '))

# Rumus dari tugas akhir yang diberikan
nAkhir = (30/100 * nTugas) + (30/100 * nUTS) + (40/100 * nUAS)

# If condition ketika nilai lebih dari sama dengan 60 maka dinyatakan lulus
if nAkhir >= 60:
    print(f'Selamat untuk mahasiswa dengan nama "{mhs}", telah dinyatakan LULUS dengan nilai akhir: {nAkhir}')
else:
    print(f'Mohon maaf, untuk mahasiswa dengan nama "{mhs}", dinyatakan TIDAK LULUS dengan nilai akhir: {nAkhir}')

print("==== TERIMA KASIH ====")

