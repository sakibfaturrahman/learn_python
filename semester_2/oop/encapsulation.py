# Menyembunyikan atribut supaya tidak bisa diakses langsung.
class Mahasiswa:
    def __init__(self, nama):
        self.__nama = nama  # atribut private

    def get_nama(self):
        return self.__nama

m = Mahasiswa("Sakib Faturrahman")
print(m.get_nama())  # Sakib Faturrahman")
