film = [
    {"judul": "Ironman 2", "harga": 40000}, 
    {"judul": "Mufasa", "harga": 45000},
    {"judul": "Guardian Of Galaxy", "harga": 50000},
]

def tampil_film():
    print("\n------------ List Film-------------")
    for idx, films in enumerate(film, start=1):
        print(f"{idx}. {films['judul']} (Rp {films['harga']:,}): ")
    print('-----------------------------------')

def cetak_tiket(film, tiket):
    totalharga = film['harga'] * tiket
    print("\n---------- Struk Pemesanan Tiket -----------")
    print(f"Judul Film    : {film['judul']}")
    print(f"Harga Tiket   : Rp {film['harga']:,}")
    print(f"Jumlah Tiket  : {tiket}")
    print(f"Total Harga   : Rp {totalharga:,}")
    print('--------------------------------------------')

def pesan():
    while True:
        tampil_film()
        try:
            print("------ Pilih 0 untuk keluar dari pilihan -------")
            pilih = int(input("Pilih Nomor Film yang akan Anda tonton: "))
            if pilih == 0:
                print("Terima kasih telah menggunakan aplikasi ini.")
                break
            if pilih < 1 or pilih > len(film):
                print("Pilihan tidak valid!")
                continue
            
            terpilih = film[pilih - 1]
            tiket = int(input(f"Jumlah tiket yang dipesan untuk film '{terpilih['judul']}': "))
            if tiket < 1:
                print("Pesan tiket minimal 1.")
                continue
            
            cetak_tiket(terpilih, tiket)
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

pesan()
