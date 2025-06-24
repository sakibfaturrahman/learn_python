class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan_info(self):
        print("\n--- Informasi Buku ---")
        print(f"Judul  : {self.judul}")
        print(f"Penulis: {self.penulis}")

judul_input = input("Masukkan judul buku: ")
penulis_input = input("Masukkan nama penulis: ")

buku1 = Buku(judul_input, penulis_input)
buku1.tampilkan_info()
