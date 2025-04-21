def struk():
    trx = input("Masukkan Nomor Transaksi: ")
    tanggal = input("Masukkan Tanggal: ")
    nama_kasir = input("Masukkan Nama Kasir: ")
    print("\nStruk Pembelian")
    print(f"Nomor Transaksi: {trx}")
    print(f"Tanggal: {tanggal}")
    print(f"Nama Kasir: {nama_kasir}")
    print("\n")
    return trx, tanggal, nama_kasir

def barang():
    keranjang = []
    while True:
        nama = input("Masukkan Nama Barang: ")
        harga = int(input("Masukkan Harga Barang: "))
        qty = int(input("Masukkan Jumlah Barang: "))
        keranjang.append([nama, harga, qty])
        print("Barang berhasil ditambahkan!")
        print("\n")
        lagi = input("Tambah barang lagi? (y/n): ").lower()
        if lagi != "y":
            break
        
    return keranjang

def total(keranjang):
    total_harga = 0
    total_item = 0
    for nama, harga, qty in keranjang:
        total_harga += harga * qty
        total_item += qty  
    return total_harga, total_item  

def bayar(total_harga, keranjang):
    print("Nama Barang | Harga | Jumlah | Total")
    for nama, harga, qty in keranjang:
        total_per_barang = harga * qty
        print(f"{nama} | Rp {harga:,} | {qty} | Rp {total_per_barang:,}")
        print(f"Total Bayar: Rp", total_harga)
    while True:
        print("\n")
        uang_bayar = int(input("Masukkan Uang Bayar: "))
        if uang_bayar < total_harga:
            print("Uang bayar kurang!")
        else:
            break
    return uang_bayar

def cetak(info_struk, barang, total_harga, total_item, uang_bayar):
    print("\n==================================================")
    print("          Warung Serba Ada (WASERBA)              ")
    print("   Jl. Cisayong, Kec. Cisayong, Kab. Tasikmalaya  ")
    print("==================================================")
    print(f"Nomor Transaksi : {info_struk[0]}  Kasir : {info_struk[2]}")
    print(f"Tanggal         : {info_struk[1]}")
    print("==================================================")
    
    print("Nama Barang      Harga       Qty     Total")
    
    for nama, harga, qty in barang:
        total_per_barang = harga * qty
        print(f"{nama}      {harga}     {qty}       {total_per_barang}")
    
    print("==================================================")
    print(f"Total Item                  : {total_item} pcs")
    print(f"Total Harga                 : Rp {total_harga}")
    print(f"Uang Bayar                  : Rp {uang_bayar}")
    print(f"Kembalian                   : Rp {uang_bayar - total_harga}")
    print("==================================================")
    print("   Terima kasih telah berbelanja di WASERBA!      ")
    print("==================================================")


info_struk = struk()           
keranjang_belanja = barang()    
total_harga, total_item = total(keranjang_belanja) 
uang_dibayar = bayar(total_harga, keranjang_belanja)    

cetak(info_struk, keranjang_belanja, total_harga, total_item, uang_dibayar)
