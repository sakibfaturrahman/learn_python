# program python untuk cetak Data dari KTP (Sakib Faturrahman)

nik = "3206320407060003"        # NIK menurut saya menggunakan string karena tidak mungkin akan ada operasi matematika pada NIK
nama = "Sakib Faturrahman"       # Nama menggunakan string karena nama berupa huruf
tempat_lahir = "Tasikmalaya"    # Tempat lahir menggunakan string karena tempat lahir berupa huruf
tanggal_lahir = "04-07-2006"    # Tanggal lahir menggunakan string karena tanggal lahir berupa angka
jenis_kelamin = "LAKI-LAKI"     # Jenis kelamin menggunakan string karena jenis kelamin berupa huruf
golongan_darah = "-"            # Golongan darah menggunakan string karena golongan darah berupa huruf
alamat = "KP CIMONYET"          # Alamat menggunakan string karena alamat berupa huruf
rt_rw = "004/003"               # RT/RW menggunakan string karena RT/RW berupa angka dan terdapat tanda "/" diantara RT dan RW
kelurahan = "PURWASARI"         # Kelurahan menggunakan string karena kelurahan berupa huruf
kecamatan = "CISAYONG"          # Kecamatan menggunakan string karena kecamatan berupa huruf
agama = "ISLAM"                 # Agama menggunakan string karena agama berupa huruf
status_perkawinan = "BELUM KAWIN" # Status perkawinan menggunakan string karena status perkawinan berupa huruf
pekerjaan = "PELAJAR/MAHASISWA" # Pekerjaan menggunakan string karena pekerjaan berupa huruf
kewarganegaraan = "WNI"         # Kewarganegaraan menggunakan string karena kewarganegaraan berupa huruf
berlaku_hingga = "SEUMUR HIDUP" # Berlaku hingga menggunakan string karena berlaku hingga berupa huruf

# print data KTP
print("===== PROVINSI JAWA BARAT =====")
print("==== KABUPATEN TASIKMALAYA ====")
print(f"NIK: {nik}")
print(f"Nama: {nama}")
print(f"Tempat, Tgl Lahir: {tempat_lahir}, {tanggal_lahir}")
print(f"Jenis Kelamin: {jenis_kelamin} | Gol. Darah: {golongan_darah}")
print(f"Alamat: {alamat}")
print(f"RT/RW: {rt_rw}")
print(f"Kel/Desa: {kelurahan}")
print(f"Kecamatan: {kecamatan}")
print(f"Agama: {agama}")
print(f"Status Perkawinan: {status_perkawinan}")
print(f"Pekerjaan: {pekerjaan}")
print(f"Kewarganegaraan: {kewarganegaraan}")
print(f"Berlaku Hingga: {berlaku_hingga}")


#oleh: Sakib Faturrahman
# operasi cetak struk minimarket 
nama_toko = "CV ANUGERAH TERINDAH SELAMANYA"  # string karena nama toko berupa huruf
lokasi = "LINGGAJAYA/F [LGJY]"  # string karena lokasi berupa huruf
alamat = "JL IR H DJUANDA RT 001 RW 004 MANGKUBUMI"  # string karena alamat berupa huruf
npwp = "99.090.715.6-425.000"  # string karena NPWP berupa angka dan terdapat tanda "- dan ." diantara angka
nomor_bon = "BI44-234-0403MWV7"  # string karena nomor bon berupa huruf dan angka
kasir = "BANI A"  # string karena kasir berupa huruf

# data barang dibuat variabel terpisah
barang1_nama = "KP BRANDING (M)"  # string karena barang berupa huruf
barang1_jumlah = 1  # integer karena jumlah barang berupa angka dan digunakan untuk operasi matematika
barang1_harga_satuan = 200  # integer karena harga satuan berupa angka dan digunakan untuk operasi matematika
barang1_total_harga = barang1_jumlah * barang1_harga_satuan  # integer karena total harga berupa angka dan digunakan untuk operasi matematika

barang2_nama = "ASIA ATB 180G"  
barang2_jumlah = 1  
barang2_harga_satuan = 9400  
barang2_total_harga = barang2_jumlah * barang2_harga_satuan  

barang3_nama = "MINTZ DM 99G"  
barang3_jumlah = 1  
barang3_harga_satuan = 8800  
barang3_total_harga = barang3_jumlah * barang3_harga_satuan  

diskon = 900  # integer karena diskon berupa angka dan digunakan untuk operasi matematika

# operasi perhitungan total belajaan dan kembalian
total_item = 3  # integer karena total item berupa angka dan digunakan untuk operasi matematika
total_belanja = (barang1_total_harga + barang2_total_harga + barang3_total_harga) - diskon  # integer karena total belanja berupa angka dan digunakan untuk operasi matematika
tunai = 50000  # integer karena tunai berupa angka dan digunakan untuk operasi matematika
kembalian = tunai - total_belanja  # integer karena kembalian berupa angka dan digunakan untuk operasi matematika

dpp = 16306.0  # float karena DPP berupa angka desimal
ppn = 1793.0  # float karena PPN berupa angka desimal
tanggal_transaksi = "04-03-2025"  # string karena tanggal transaksi berupa angka dan terdapat tanda "-"
waktu_transaksi = "13:13:12"  # string karena waktu transaksi berupa angka dan terdapat tanda ":"

# Cetak struk belanja
print("=" * 40)
print(f"{nama_toko}\n{lokasi}\n{alamat}")
print(f"NPWP: {npwp}")
print("=" * 40)
print(f"Bon: {nomor_bon} | Kasir: {kasir}")
print("=" * 40)

# Cetak daftar barang
print(f"{barang1_nama:<20} {barang1_jumlah:<3} {barang1_harga_satuan:<7} {barang1_total_harga:<7}")
print(f"{barang2_nama:<20} {barang2_jumlah:<3} {barang2_harga_satuan:<7} {barang2_total_harga:<7}")
print(f"{barang3_nama:<20} {barang3_jumlah:<3} {barang3_harga_satuan:<7} {barang3_total_harga:<7}")

print(f"\nDiskon: {diskon}")
print("=" * 40)
print(f"Total Item: {total_item}")
print(f"Total Belanja: {total_belanja}")
print(f"Tunai: {tunai}")
print(f"Kembalian: {kembalian}")
print("=" * 40)
print(f"DPP: {dpp} | PPN: {ppn}")
print(f"Tanggal: {tanggal_transaksi} {waktu_transaksi}")
print("=" * 40)

