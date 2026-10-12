# Memberikan Variable yang akan di isi nantinya
print("==== APLIKASI PENGKATEGORIAN UMUR ====")
nama = input("Halo, siapakah namamu?: ")
umur = int(input(f'Hai {nama}, Silahkan masukan umurmu: '))


# If condition ketika umur sudah memasuki kategori atau kriteria
if umur > 35:
    print(f'Hai {nama}, umurmu adalah {umur} dengan kategori DEWASA TUA')
elif umur > 17:
    print(f'Hai {nama}, umurmu adalah {umur} dengan kategori DEWASA')
elif umur > 12:
    print(f'Hai {nama}, umurmu adalah {umur} dengan kategori REMAJA')
else:
    print(f'Hai {nama}, umurmu adalah {umur} dengan kategori ANAK-ANAK')

print("==== TERIMA KASIH ====")

