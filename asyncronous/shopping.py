def hitung_total_harga(barang, jumlah):
    harga_per_unit = {
        "Elektronik": 1000000,
        "Pakaian": 200000,
        "Makanan": 50000
    }

    barang = barang.capitalize()

    if barang not in harga_per_unit:
        return "Oops, barang tidak tersedia."

    if jumlah < 0:
        return "Jumlah barang harus berupa angka lebih dari atau sama dengan 0!"

    total_harga = jumlah * harga_per_unit[barang]
    diskon = 0

  
    if total_harga > 5000000:
        diskon = 0.2 * total_harga 
    elif total_harga > 2000000:
        diskon = 0.1 * total_harga  
    elif total_harga > 1000000:
        diskon = 0.05 * total_harga  

    total_bayar = total_harga - diskon
    return total_harga, diskon, total_bayar

while True:
    try:
        print("Program Penghitung Total Harga Dagangan")
        print("Untuk keluar dari program, ketik 'keluar'.")

        nama = input("Input nama pelanggan: ")
        if nama.lower() == 'keluar':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break

        barang = input("Nama barang (Elektronik/Pakaian/Makanan): ")
        jumlah = int(input("Jumlah barang: "))

        hasil = hitung_total_harga(barang, jumlah)
        if isinstance(hasil, str):
            print(hasil)
        else:
            total_harga, diskon, total_bayar = hasil
            print(f"\nNama Pelanggan: {nama}")
            print(f"Total Harga: Rp{total_harga:,}")
            print(f"Diskon: Rp{diskon:,}")
            print(f"Total yang Harus Dibayar: Rp{total_bayar:,}\n")

    except ValueError:
        print("Oops, sepertinya ada kesalahan input. Harap masukkan data dengan benar!")
