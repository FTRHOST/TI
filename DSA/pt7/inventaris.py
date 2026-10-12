inventaris = {}

def tampilkan_inventaris():
    print("\n--- Data Inventaris Saat Ini ---")
    if not inventaris:
        print("Inventaris kosong.")
    else:
        for barang, jumlah in inventaris.items():
            print(f"- {barang}: {jumlah} unit")
    print("--------------------------------\n")

# 1. Menambah barang ke inventaris
print("[+] Menambahkan barang...")
inventaris["Laptop"] = 10
inventaris["Mouse"] = 50
inventaris["Keyboard"] = 25
tampilkan_inventaris()

# 2. Menambah stok barang yang sudah ada (Restock)
print("[+] Menambah stok Mouse sebanyak 20 unit...")
inventaris["Mouse"] += 20
tampilkan_inventaris()

# 3. Menghapus barang dari inventaris
print("[-] Menghapus Keyboard dari inventaris...")
if "Keyboard" in inventaris:
    del inventaris["Keyboard"]
tampilkan_inventaris()
