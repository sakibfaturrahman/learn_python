# Create
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)

# Read
print(fruits[0])

# Update
fruits.append("Mango")  # Menambah elemen
fruits[1] = "Blueberry"  # Mengubah elemen
print(fruits)

# Delete
fruits.remove("Apple")  # Menghapus berdasarkan nilai
print(fruits)
del fruits[0]  # Menghapus berdasarkan indeks
print(fruits)

# Kesalahan umum
# print(fruits[5])  # Akan menyebabkan IndexError