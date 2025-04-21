gaji_pokok = {
    "kelas A": 5000000,
    "kelas B": 4000000,
    "kelas C": 3000000,
}

uang_lembur = {
    "kelas A": 40000,
    "kelas B": 30000,
    "kelas C": 20000,
}


def hitung_lembur(kelas, jam_lembur):
    if kelas in uang_lembur:
        return jam_lembur * uang_lembur[kelas]
    raise ValueError("Kelas tidak valid!")


def tunjangan_masa_kerja(masa_kerja):
    return 500000 if masa_kerja >= 10 else 100000


def hitung_status(kelas, status_menikah, jumlah_anak):
    gaji = gaji_pokok[kelas]
    if status_menikah == "y":
        tunjangan_istri = gaji * 0.1
        tunjangan_anak = gaji * 0.025 * jumlah_anak
        return tunjangan_istri + tunjangan_anak
    else:
        return gaji * 0.05

def total_gaji(nama, kelas, jam_lembur, masa_kerja, status_menikah, jumlah_anak):
    gaji = gaji_pokok[kelas]
    lembur = hitung_lembur(kelas, jam_lembur)
    tunjangan_kerja = tunjangan_masa_kerja(masa_kerja)
    tunjangan_status = hitung_status(kelas, status_menikah, jumlah_anak)
    
    total = gaji + lembur + tunjangan_kerja + tunjangan_status
    return total


while True:
    try:
        nama = input("Masukkan Nama: ")
        kelas = input("Masukkan Kelas (kelas A/kelas B/kelas C): ")
        if kelas not in gaji_pokok:
            raise ValueError("Kelas tidak valid!")
        
        jam_lembur = int(input("Masukkan Jam Lembur: "))
        masa_kerja = int(input("Masukkan Masa Kerja (dalam tahun): "))
        status_menikah = input("Status menikah (y/n): ").lower()
        if status_menikah == "y":
            jumlah_anak = int(input("Masukkan Jumlah Anak: "))
        else:
            jumlah_anak = 0

        total = total_gaji(nama, kelas, jam_lembur, masa_kerja, status_menikah, jumlah_anak)
        print("\nRincian Gaji:")
        print(f"Nama: {nama}")
        print(f"Kelas: {kelas}")
        print(f"Total Gaji: Rp {total:,}\n")
    except ValueError as e:
        print(f"Error: {e}")



# program setelah analisis ulangg

# ternyata baru inget bisa dibikin 1 dictionary pake dictionary nested
# data_gaji = {
#     "kelas A": {"gaji_pokok": 5000000, "uang_lembur": 40000},
#     "kelas B": {"gaji_pokok": 4000000, "uang_lembur": 30000},
#     "kelas C": {"gaji_pokok": 3000000, "uang_lembur": 20000},
# }


# def hitung_lembur(kelas, jam_lembur):
#     if kelas in data_gaji:
#         return jam_lembur * data_gaji[kelas]["uang_lembur"]
#     raise ValueError("Kelas tidak valid!")


# def tunjangan_masa_kerja(masa_kerja):
#     return 500000 if masa_kerja >= 10 else 100000


# def hitung_status(kelas, status_menikah, jumlah_anak):
#     gaji_pokok = data_gaji[kelas]["gaji_pokok"]
#     if status_menikah == "y":
#         tunjangan_istri = gaji_pokok * 0.1
#         tunjangan_anak = gaji_pokok * 0.025 * jumlah_anak
#         return tunjangan_istri + tunjangan_anak
#     else:
#         return gaji_pokok * 0.05  # Tabungan untuk yang belum menikah


# def total_gaji(nama, kelas, jam_lembur, masa_kerja, status_menikah, jumlah_anak):
#     gaji_pokok = data_gaji[kelas]["gaji_pokok"]
#     lembur = hitung_lembur(kelas, jam_lembur)
#     tunjangan_kerja = tunjangan_masa_kerja(masa_kerja)
#     tunjangan_status = hitung_status(kelas, status_menikah, jumlah_anak)
    
#     total = gaji_pokok + lembur + tunjangan_kerja + tunjangan_status
#     return total


# print("----Program hitung gaji dan tunjangan sederhana----")
# nama = input("Masukkan Nama: ")
# kelas = input("Masukkan Kelas (kelas A/kelas B/kelas C): ")
# if kelas not in data_gaji:
#     raise ValueError("Kelas tidak valid!")
        
# jam_lembur = int(input("Masukkan Jam Lembur: "))
# masa_kerja = int(input("Masukkan Masa Kerja (dalam tahun): "))
# status_menikah = input("Status menikah (y/n): ").lower()
# if status_menikah == "y":
#     jumlah_anak = int(input("Masukkan Jumlah Anak: "))
# else:
#     jumlah_anak = 0
# total = total_gaji(nama, kelas, jam_lembur, masa_kerja, status_menikah, jumlah_anak)

# print("\nRincian Gaji:")
# print(f"Nama: {nama}")
# print(f"Kelas: {kelas}")
# print(f"Total Gaji: Rp {total:,}")
   
