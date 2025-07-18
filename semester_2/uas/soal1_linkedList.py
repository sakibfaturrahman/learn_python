class NodeSakib:
    # Mewakili satu node dalam linked list
    def __init__(self, npm, nama, ipk):
        self.npm = npm
        self.nama = nama
        self.ipk = ipk
        self.next = None  # Menunjuk ke node berikutnya


class LinkedListSakib:
    # Struktur linked list buatan Sakib
    def __init__(self):
        self.head = None  # Node pertama (head) dari linked list

    def sakib_tambah_di_awal(self, npm, nama, ipk):
        node_baru = NodeSakib(npm, nama, ipk)
        node_baru.next = self.head
        self.head = node_baru
        print(f" Mahasiswa {nama} (NPM: {npm}) berhasil ditambahkan di awal.")

    def sakib_tambah_di_akhir(self, npm, nama, ipk):
        node_baru = NodeSakib(npm, nama, ipk)
        if not self.head:
            self.head = node_baru
            print(f" Mahasiswa {nama} (NPM: {npm}) berhasil ditambahkan sebagai elemen pertama.")
            return

        sekarang = self.head
        while sekarang.next:
            sekarang = sekarang.next
        sekarang.next = node_baru
        print(f" Mahasiswa {nama} (NPM: {npm}) berhasil ditambahkan di akhir.")

    def sakib_hapus_berdasarkan_npm(self, npm):
        sekarang = self.head
        sebelumnya = None

        if not sekarang:
            print(f" List kosong. Tidak dapat menghapus NPM: {npm}.")
            return False

        if sekarang and sekarang.npm == npm:
            self.head = sekarang.next
            print(f" Mahasiswa dengan NPM: {npm} berhasil dihapus.")
            return True

        while sekarang and sekarang.npm != npm:
            sebelumnya = sekarang
            sekarang = sekarang.next

        if not sekarang:
            print(f" Mahasiswa dengan NPM: {npm} tidak ditemukan.")
            return False

        sebelumnya.next = sekarang.next
        print(f" Mahasiswa dengan NPM: {npm} berhasil dihapus.")
        return True

    def sakib_cari_npm(self, npm):
        sekarang = self.head
        while sekarang:
            if sekarang.npm == npm:
                print("\n--- Mahasiswa Ditemukan! ---")
                print(f"NPM : {sekarang.npm}")
                print(f"Nama: {sekarang.nama}")
                print(f"IPK : {sekarang.ipk}")
                print("----------------------------")
                return sekarang
            sekarang = sekarang.next
        print(f" Mahasiswa dengan NPM: {npm} tidak ditemukan.")
        return None

    def sakib_tampilkan_semua(self):
        if not self.head:
            print("Daftar mahasiswa saat ini kosong.")
            return

        print("\n--- Semua Data Mahasiswa ---")
        sekarang = self.head
        nomor = 1
        while sekarang:
            print(f"{nomor}. NPM: {sekarang.npm}, Nama: {sekarang.nama}, IPK: {sekarang.ipk}")
            sekarang = sekarang.next
            nomor += 1
        print("----------------------------")


def sakib_jalankan_program_linkedlist():
    daftar_mahasiswa_sakib = LinkedListSakib()

    while True:
        print("\n--- Sistem Manajemen Mahasiswa (Linked List by Sakib) ---")
        print("1. Tambah mahasiswa di awal")
        print("2. Tambah mahasiswa di akhir")
        print("3. Hapus mahasiswa berdasarkan NPM")
        print("4. Cari mahasiswa berdasarkan NPM")
        print("5. Tampilkan semua mahasiswa")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1' or pilihan == '2':
            npm = input("Masukkan NPM Mahasiswa: ")
            nama = input("Masukkan Nama Mahasiswa: ")
            try:
                ipk = float(input("Masukkan IPK Mahasiswa: "))
            except ValueError:
                print("IPK tidak valid. Harap masukkan angka.")
                continue
            if pilihan == '1':
                daftar_mahasiswa_sakib.sakib_tambah_di_awal(npm, nama, ipk)
            else:
                daftar_mahasiswa_sakib.sakib_tambah_di_akhir(npm, nama, ipk)

        elif pilihan == '3':
            npm = input("Masukkan NPM mahasiswa yang akan dihapus: ")
            daftar_mahasiswa_sakib.sakib_hapus_berdasarkan_npm(npm)

        elif pilihan == '4':
            npm = input("Masukkan NPM mahasiswa yang akan dicari: ")
            daftar_mahasiswa_sakib.sakib_cari_npm(npm)

        elif pilihan == '5':
            daftar_mahasiswa_sakib.sakib_tampilkan_semua()

        elif pilihan == '6':
            print("Keluar dari Sistem Manajemen Mahasiswa by Sakib. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    sakib_jalankan_program_linkedlist()
