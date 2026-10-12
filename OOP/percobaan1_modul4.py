class akunSIAKAD:
    def __init__(self, username, password):
        self.username = username
        self._status_aktif = True
        self.__password = password
        pass
    def tampilkan_info(self):
        print(f"Username: {self.username}, Aktif: {self._status_aktif}")
        # Atribut private BISA diakses dari dalam class itu sendiri
        print(f"Password tersimpan: {self.__password}")
        pass

akun1 = akunSIAKAD("fathir_ti", "Cihuy")
print("Akses Public:", akun1.username)
