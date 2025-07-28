# fungsi data film
def sakib_film():
    return [
        {"kode_film": "KF501" , "judul_film" : "Jumbo" ,"harga_tiket": 35000, "waktu": ["13:00","21:00"]},
        {"kode_film": "KF001" , "judul_film" : "Thunderbolts" ,"harga_tiket": 45000, "waktu": ["15:30"]},
        {"kode_film": "KF502" , "judul_film" : "Pabrik Gula" ,"harga_tiket": 35000, "waktu": ["09:30","13:00"]},
        {"kode_film": "KF002" , "judul_film" : "Mission Impossible" ,"harga_tiket": 45000, "waktu": ["16:00","21:00"]},
        {"kode_film": "KF503" , "judul_film" : "Angkara Murka" ,"harga_tiket": 45000, "waktu": ["13:00"]},
    ]
    
# generate kursi dengan perulangan berdasarkan abjad dengan ASCII
sakib_kursi = {chr(k) : [False] * 16 for k in range(65,75)}

# cek apakah kursi tersedia (sudah terisi) dan tampilkan
def cek_status_kursi_sakib(kode_kursi):
    print("======== Peta Kursi =========")

    for row in range(65,75):
        # buat beris berdasarkan ASCII
        baris = chr(row)
        # string penampung data kursi
        line = ""
        for col in range(1,17):
            kode = f"{baris}{col}"
            # jika kursi sudah dipesan maka tampilkan X
            status = "X" if sakib_kursi[baris][col-1] else f"{baris}{col:>2}"

            line += f"{status:>5}"
        print(line)
    print("\n Keterangan : X = Kursi sudah dipesan")

    if len(kode_kursi) < 2:
        return False
    baris = kode_kursi[0].upper()
    try:
        nomor = int(kode_kursi[1:]) - 1
    except ValueError:
        return False
    return baris in sakib_kursi and 0 <= nomor < 16 and not sakib_kursi[baris][nomor]

# pesan kursi, ubah status false menjadi true jika sudah dipesan
def pesan_kursi(kode_kursi):
    baris = kode_kursi[0].upper()
    nomor = int(kode_kursi[1:]) -1
    sakib_kursi[baris][nomor] = True


# looping view film
def view_film_sakib():
    print("------------- Daftar Film Minggu Ini ------------------")
    for film in sakib_film():
        print(f"| Kode film : {film['kode_film']} | {film['judul_film']} | Rp {film['harga_tiket']} | Jam:  {','.join(film['waktu'])}")
        print("-----------------------------------------------------------")

# keranjang kosong
sakib_keranjang = []

def pesan_tiket_sakib():
    while True:
        view_film_sakib()
        print("------------- Ketik 'Quit' Untuk kembali ke menu utama --------------------")
        kode_film = input("Pilih Kode film : ").upper()
        # jika user mengetik quit maka arahkan ke halaman menu
        if kode_film == "QUIT":
            break
        #  jika kode film benar
        film_terpilih = next((film for film in sakib_film() if film["kode_film"] == kode_film), None)

        if not film_terpilih:
            print("Opps, Sepertinya Film tidak ditemukan!")
            continue

        print(f"Judul Film: {film_terpilih["judul_film"]}")
        print(f"Harga: {film_terpilih["harga_tiket"]:,}")
        print(f"Waktu: {film_terpilih["waktu"]}")

        waktu_film = input("Pilih Waktu Tayang: ")
        if waktu_film not in film_terpilih["waktu"]:
            print("Opps, Sepertinya waktu tersebut  tidak ada!")
            continue

        tiket = int(input("Jumlah Tiket yang dipesan: "))
        if tiket < 1:
            print("Minimal Pemesanan 1 Tiket")
            continue

        # kursi kosong
        kursi_sakib = []
        cek_status_kursi_sakib("")
        for kursi in range(tiket):
            while True:
                kode_kursi = input(f"Pilih kursi untuk tiket ke {kursi+1} (Misal A1): ").upper()
                if not cek_status_kursi_sakib(kode_kursi):
                    print("Opps, Sepertinya Kursi tidak ada atau sudah dipesan!")
                else:
                    pesan_kursi(kode_kursi)
                    kursi_sakib.append(kode_kursi)
                    break
        
        simpan = input("Apakah simpan ke Keranjang? (Y/T): ").upper()
        if simpan == "Y":
            for kursi in kursi_sakib:
                sakib_keranjang.append({
                    "kode" : kode_film,
                    "judul" : film_terpilih["judul_film"],
                    "jam" : waktu_film,
                    "kursi" : kursi,
                    "harga" : film_terpilih["harga_tiket"],
                    "jumlah" : tiket
                })
            print("Yeayy, Tiket anda berhasil dimasukan kedalam keranjang! Cek keranjang anda.")
        else:
            print("Opps, Sepertinya pemesanan dibatalkan")

        lagi = input("Pesan tiket lagi? (Y/T): ").strip().upper()
        if lagi == "T":
            break

# fungsi view keranjang
def show_keranjang_sakib():
    print("----------- Keranjang anda -----------------")
    total = 0
    for data in sakib_keranjang:
        print(f"|Kode Film: {data['kode']} | - | Film : {data['judul']} | - |Jam tayang:  {data['jam']} | - |Kursi: {data['kode']} | - | Rp: {data['harga']:,} |")
        total += data['harga']

    print(f"Total pembayaran: Rp{total:,}")
    return total

def sakib_bayar():
    # cek keranjang
    if not sakib_keranjang:
        print("Opps, Keranjang Anda Kosong!")
        return False
    
    total_bayar = show_keranjang_sakib()
    nama = input("Nama anda: ")
    nama_bank = input("Pilih VA BANK: ")
    kode_va = int(input("Kode VA: "))
    print("Pembayaran berhasil!")
    print(f"Terimakasih {nama}, Telah memesan tiket di KibMovie! Selamat menonton")

    # kosongkan keranjang!
    sakib_keranjang.clear()


# buat menu untuk tampilan awal
def menu_home_sakib():
    while True:
        print("===================== KibMovie =====================")
        print("[1] Menu utama")
        print("[2] Daftar Film")
        print("[3] Pesan Tiket")
        print("[4] Keranjang")
        print("[5] Pembayaran")
        print(" 'Exit' Keluar")

        opsi = input("Pilih Menu: ").strip().lower()

        if opsi == "1":
           continue
        elif opsi == "2":
            view_film_sakib()
        elif opsi == "3":
            pesan_tiket_sakib()
        elif opsi == "4":
            show_keranjang_sakib()
        elif opsi == "5":
            sakib_bayar()
        elif opsi == "exit":
            print("Program Selesai!, terimakasih telah menggunakan KibMovie")
            break
        else:
            print("Opps, Menu tidak tersedia!")

menu_home_sakib()
