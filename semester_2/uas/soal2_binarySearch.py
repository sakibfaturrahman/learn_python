def sakib_binary_search(data_sakib, target_sakib):
   
    batas_bawah = 0
    batas_atas = len(data_sakib) - 1

    while batas_bawah <= batas_atas:
        tengah = (batas_bawah + batas_atas) // 2
        nilai_tengah = data_sakib[tengah]

        if nilai_tengah == target_sakib:
            return tengah
        elif nilai_tengah < target_sakib:
            batas_bawah = tengah + 1
        else:
            batas_atas = tengah - 1

    return -1


def sakib_jalankan_binary_search():
  
    while True:
        try:
            input_sakib = input("Masukkan daftar bilangan bulat terurut (misal: 5 10 15 20 25): ")
            data_sakib = [int(x) for x in input_sakib.split()]
            
            target_input = input("Masukkan nilai yang ingin dicari: ")
            target_sakib = int(target_input)

            hasil_index = sakib_binary_search(data_sakib, target_sakib)

            if hasil_index != -1:
                print(f"Elemen {target_sakib} ditemukan pada indeks: {hasil_index}")
            else:
                print(f" Elemen {target_sakib} tidak ditemukan dalam data.")
            break
        except ValueError:
            print(" Input tidak valid. Harap masukkan bilangan bulat yang dipisahkan spasi.")
        except Exception as error:
            print(f" Terjadi kesalahan: {error}")


if __name__ == "__main__":
    sakib_jalankan_binary_search()
