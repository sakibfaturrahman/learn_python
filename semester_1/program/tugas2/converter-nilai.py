def konversi_nilai(nilai):
    if nilai >= 90 and nilai <= 100:
        return "A"
    elif nilai >= 80 and nilai <= 89:
        return "B"
    elif nilai >= 70 and nilai <= 79:
        return "C"
    elif nilai >= 60 and nilai <= 69:
        return "D"
    elif nilai >= 0 and nilai <= 59:
        return "E"
    else:
        return "!"
    
while True:
    try:
        print("\n ---- Program Konversi nilai sederhana ----")
        print("Ketik Keluar untuk keluar dari aplikasi")

        input_nilai = input("Masukkan angka nilai: ")
        if input_nilai.lower() == 'keluar':
            print("Terima kasih telah menggunakan program ini!")
            break

        nilai_angka = int(input_nilai)
        print(f"Nilai dari {nilai_angka} adalah {konversi_nilai(nilai_angka)}")
    except ValueError:
        print("Terjadi kesalah ketika input berlangsung")
