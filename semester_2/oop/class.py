class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama  # menyimpan ke atribut milik objek

    def sapa(self):
        print("Halo, saya", self.nama)

mhs1 = Mahasiswa("Sakib Faturrahman")
mhs1.sapa()