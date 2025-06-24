
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
print("Desimal:", angka, "Biner:", desimal_ke_biner(angka))
