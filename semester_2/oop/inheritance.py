class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

class MahasiswaAktif(Mahasiswa):  # turunan dari Mahasiswa
    def status(self):
        print(self.nama, "sedang aktif kuliah")

m = MahasiswaAktif("Sakib Faturrahman")
m.status()
