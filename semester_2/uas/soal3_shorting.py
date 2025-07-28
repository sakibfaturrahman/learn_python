def sakib_selection_sort(arr):
   
    n = len(arr)
    # cek seluruh elemen dalam array
    for i in range(n):
        # Temukan indeks elemen terkecil dalam bagian array yang belum terurut
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # tuker elemen minimum dengan elemen di posisi i
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def sakib_jalankan_program_sorting():
    while True:
        try:
            input_str = input("Input angka: ")
            # konversi input string menjadi list bilangan bulat
            data_list = [int(x) for x in input_str.split()]

            print(f"\nArray sebelum diurutkan: {data_list}")

            # Salin array agar aslinya tidak berubah
            sorted_list = sakib_selection_sort(data_list.copy())

            print(f"Array setelah diurutkan: {sorted_list}")
            break
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat yang dipisahkan oleh spasi ya!")
        except Exception as e:
            print(f"Terjadi kesalahan yang tak terduga: {e}")

if __name__ == "__main__":
    sakib_jalankan_program_sorting()
