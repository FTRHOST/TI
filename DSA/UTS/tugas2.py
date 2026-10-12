riwayat_aktivitas = []

# Memasukan sebuah aktifitas 
riwayat_aktivitas.append("Login ke sistem")
riwayat_aktivitas.append("Membuka menu layanan")
riwayat_aktivitas.append("Mengubah profil")

print("Aktivitas saat ini:", riwayat_aktivitas)

# Pop menghapus atau mengundo aktifitas
aktivitas_dibatalkan = riwayat_aktivitas.pop()
print("\nMelakukan Undo pada:", aktivitas_dibatalkan)
print("Aktivitas setelah Undo:", riwayat_aktivitas)
