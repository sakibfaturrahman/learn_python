def hitung_gaji(kategori, jam_kerja):
    gaji_per_jam = {
        "Manager" : 50000,
        "Supervisor" : 40000,
        "Staf" : 30000
    }

    kategori = kategori.capitalize()

    if kategori not in gaji_per_jam:
        return "Opps, Sepertinya gaji tidak tersedia"

    if jam_kerja < 0:
        return "Jumlah jam kerja harus berupa angka lebih dari atau sama dengan 0!"
    
    gaji = jam_kerja * gaji_per_jam[kategori]
    lembur = 0

    if jam_kerja > 160:
        lembur = (jam_kerja - 160)*(1.5 * gaji_per_jam[kategori])

    totalGaji = gaji + lembur
    return gaji, lembur , totalGaji

while True:
    try:
        print("Program Penghitung Gaji")
        print("Untuk keluar dari program Ketik Keluar")

        nama = input("Input Nama karyawan: ")
        if nama == 'keluar' or nama == 'Keluar':
            print("Terimakasih telah menggunaka aplikasi ini!")
            break

        kategori = input("Nama kategori: ")
        jam_kerja = int(input("input jam kerja karyawan: "))

        hasil = hitung_gaji(kategori, jam_kerja)
        if  isinstance(hasil, str):
            print(hasil)
        else:
            gaji, lembur, totalGaji = hasil
            print(f"\nNama Karyawan : {nama}")
            print(f"Gaji Pokok      : Rp{gaji:,}")
            print(f"Lembur          : Rp{lembur:,}")
            print(f"Total Gaji      : Rp{totalGaji:,}\n")
    except ValueError:
        print("Opps, Sepertinya ada kesalahan?")


