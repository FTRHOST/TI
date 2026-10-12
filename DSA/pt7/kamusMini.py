kamus_mini = {
    "makan": "eat",
    "tidur": "sleep",
    "buku": "book",
    "kucing": "cat",
    "sekolah": "school",
    "belajar": "study"
}

print("=== PROGRAM KAMUS MINI (INDO - ENG) ===")
kata_cari = input("Masukkan kata dalam Bahasa Indonesia: ").lower()

# Mencari kata di dalam dictionary (Hash Table)
if kata_cari in kamus_mini:
    terjemahan = kamus_mini[kata_cari]
    print(f"Terjemahan '{kata_cari}' ke Bahasa Inggris adalah: {terjemahan}")
else:
    print(f"Maaf, kata '{kata_cari}' tidak ditemukan di dalam kamus.")
