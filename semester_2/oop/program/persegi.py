class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar


try:
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))

    pp = PersegiPanjang(p, l)
    print("Luas persegi panjang:", pp.luas())
except ValueError:
    print("Input harus berupa angka.")
