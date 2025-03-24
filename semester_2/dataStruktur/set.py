# Create
numbers = {1, 2, 3, 4}
print(numbers)

# Read (Tidak bisa akses indeks)
# print(numbers[0])  # Akan menyebabkan TypeError

# Update
numbers.add(5)  # Menambah elemen
numbers.remove(2)  # Menghapus elemen
print(numbers)

# Kesalahan umum
# numbers.remove(10)  # Akan menyebabkan KeyError jika elemen tidak ada
