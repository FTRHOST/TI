
print("=== Program Mengecek bilangan Prima ===")
angka = int(input("Masukkan angka: "))

# Bilangan prima harus lebih besar dari 1
if angka > 1:
    is_prima = True
    
    # Cek pembagi dari 2 sampai angka-1
    i = 2
    while i * i <= angka: # cek sampai akar kuadrat angka
        if angka % i == 0:
            is_prima = False
            break
        i += 1
        
    if is_prima:
        print(f"Input  : {angka}")
        print("Output : Bilangan Prima")
    else:
        print(f"Input  : {angka}")
        print("Output : Bukan Bilangan Prima")
else:
    print(f"Input  : {angka}")
    print("Output : Bukan Bilangan Prima")

print("==== TERIMA KASIH ====")

