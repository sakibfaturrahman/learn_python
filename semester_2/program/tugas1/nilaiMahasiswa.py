# def hitung_lambang(nilai):
#     return "A" if nilai >= 80 else "B" if nilai >= 70 else "C" if nilai >= 60 else "D" if nilai >= 50 else "E"

# def hitung_mutu(lambang, sks):
#     nilai_mutu = [["A", 4], ["B", 3], ["C", 2], ["D", 1], ["E", 0]]
#     for item in nilai_mutu:
#         if item[0] == lambang:
#             return item[1] * sks
#     return 0

# # mahasiswa = [
# #     input("Nama: "), input("NIM: "), input("Kelas: "), input("Fakultas: "), input("Prodi: "), []
# # ]

# nm_mhs = input("Nama: ")
# nim_mhs = input("NIM: ")
# kelas_mhs = input("Kelas: ")
# fakultas_mhs = input("Fakultas: ")
# prodi_mhs = input("Prodi: ")

# matkuls = []

# jumlah_matkul = int(input("Jumlah mata kuliah: "))
# jumlah_sks = 0
# ipk = 0
# for _ in range(jumlah_matkul):
#     print('')
#     print('Matkul ke ', _+1)
#     kode = input("Kode Mata Kuliah: ")
#     nama = input("Nama Mata Kuliah: ")
#     sks = int(input("SKS: "))
#     nilai = int(input("Nilai: "))
#     matkuls.append([kode, nama, sks, nilai])
#     jumlah_sks += sks
#     ipk += hitung_mutu(hitung_lambang(nilai), sks)

# print(f"\nNama: {nm_mhs}, NIM: {nim_mhs}, Kelas: {kelas_mhs}, Fakultas: {fakultas_mhs}, Prodi: {prodi_mhs}")
# print("Kode | Mata Kuliah | SKS | Nilai | Lambang | Jumlah Mutu")
# for matkul in matkuls:
#     lambang = hitung_lambang(matkul[3])
#     mutu = hitung_mutu(lambang, matkul[2])
#     print(f"{matkul[0]} | {matkul[1]} | {matkul[2]} | {matkul[3]} | {lambang} | {mutu}")
#     print('')

# print(f"Jumlah SKS: {jumlah_sks}, IPK: {round(ipk / jumlah_sks, 2) if jumlah_sks > 0 else 0}")

# # print(matkuls)





nm_mhs = input("Nama: ")
nim_mhs = input("NIM: ")
kelas_mhs = input("Kelas: ")
fakultas_mhs = input("Fakultas: ")
prodi_mhs = input("Prodi: ")

matkuls = []
jumlah_sks = 0
total_mutu = 0

jumlah_matkul = int(input("Jumlah mata kuliah: "))

for _ in range(jumlah_matkul):  
    print('')
    print('Matkul ke ', _+1)
    kode = input("Kode Mata Kuliah: ")
    nama = input("Nama Mata Kuliah: ")
    sks = int(input("SKS: "))
    nilai = int(input("Nilai: "))

    if nilai >= 80:
        lambang = "A"
        nilai_mutu = 4
    elif nilai >= 70:
        lambang = "B"
        nilai_mutu = 3
    elif nilai >= 60:
        lambang = "C"
        nilai_mutu = 2
    elif nilai >= 50:
        lambang = "D"
        nilai_mutu = 1
    else:
        lambang = "E"
        nilai_mutu = 0

    jumlah_mutu = nilai_mutu * sks

    matkuls.append([kode, nama, sks, nilai, lambang, jumlah_mutu])
    jumlah_sks += sks
    total_mutu += jumlah_mutu

print(f"\nNama: {nm_mhs}, NIM: {nim_mhs}, Kelas: {kelas_mhs}, Fakultas: {fakultas_mhs}, Prodi: {prodi_mhs}")
print("Kode | Mata Kuliah | SKS | Nilai | Lambang | Jumlah Mutu")
for matkul in matkuls:
    print(f"{matkul[0]} | {matkul[1]} | {matkul[2]} | {matkul[3]} | {matkul[4]} | {matkul[5]}")
    print('')

ipk = round(total_mutu / jumlah_sks, 2) if jumlah_sks > 0 else 0
print(f"Jumlah SKS: {jumlah_sks}, IPK: {ipk}")











# class Converter:
#     def __init__(self, decimal_number):
#         self.decimal_number = decimal_number

#     def convert_to_binary(self):
#         if self.decimal_number < 0:
#             raise ValueError("Mohon maaf tidak mensupport negatif number yah.")
#         elif self.decimal_number == 0:
#             return "0"
#         else:
#             binary_number = ""
#             while self.decimal_number > 0:
#                 remainder = self.decimal_number % 2
#                 binary_number = str(remainder) + binary_number
#                 self.decimal_number //= 2
#             return binary_number

# # contoh penggunaan
# decimal_number = int(input("Masukkan bilangan desimal: "))
# converter = Converter(decimal_number)
# binary_number = converter.convert_to_binary()
# print(f"Bilangan biner dari {decimal_number} adalah: {binary_number}")

