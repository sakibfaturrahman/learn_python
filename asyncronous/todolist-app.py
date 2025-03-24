# aplikasi todo list sederhana dengan pyhton

print("Selamat Datang di Aplikasi Todo List Sederhana")

todolist = []
while True:
    print("\nMenu:")
    print("1. Tambahkan Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        tugas = input("Masukkan tugas baru: ")
        todolist.append(tugas)
        print(f"Tugas '{tugas}' berhasil ditambahkan.")
    elif pilihan == "2":
        print("Daftar Tugas:")
        for idx, tugas in enumerate(todolist, start=1):
            print(f"{idx}. {tugas}")
    elif pilihan == "3":
        print("Daftar Tugas:")
        for idx, tugas in enumerate(todolist, start=1):
            print(f"{idx}. {tugas}")
        try:
            index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if index >= 1 and index <= len(todolist):
                todolist.pop(index - 1)
                print("Tugas berhasil dihapus.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
    elif pilihan == "4":
        print("Terimakasih telah menggunakan aplikasi ini")
