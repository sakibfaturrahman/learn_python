# class Converter:
#     def __init__(self, decimal_number):
#         self.decimal_number = decimal_number

#     def convert_to_binary(self):
#         if self.decimal_number < 0:
#             raise ValueError("Mohon maaf tidak mensupport negatif number yah.")
#         elif self.decimal_number == 0:
#             return "0"
#         else:
#             binary_number = ""
#             while self.decimal_number > 0:
#                 remainder = self.decimal_number % 2
#                 binary_number = str(remainder) + binary_number
#                 self.decimal_number //= 2
#             return binary_number

# # contoh penggunaan
# decimal_number = int(input("Masukkan bilangan desimal: "))
# converter = Converter(decimal_number)
# binary_number = converter.convert_to_binary()
# print(f"Bilangan biner dari {decimal_number} adalah: {binary_number}")


def desimal_ke_biner(n):
    stack = []

    while n > 0:
        sisa = n % 2
        stack.append(str(sisa))
        n = n // 2

    biner = ''.join(reversed(stack))
    return biner if biner else "0"  

# Contoh pemakaian
angka = int(input("Masukkan angka desimal: "))
print("Biner:", desimal_ke_biner(angka))
