#Sakib Faturrohman
#2403010015
#buatlah program bilangan ganjil dan genap untuk range (31,77) 
#dengan menggunakan looping yang disimpan dalam array genap dan array ganji

#program dengan menggunakan for
ganjil = []
genap = []
for i in range(31,77):
    if int(i /2) * 2 == i:
        genap.append(i)
    else:
        ganjil.append(i)

print("Ini adalah program dengan for")
print("ini adalah bilangan ganjil :" + str(ganjil))
print("ini adalah bilangan genap :" + str(genap))

#program dengan menggunakan while

ganjil = []
genap = []
i = 31
while i < 77:
    if int(i /2) * 2 == i:
        genap.append(i)
    else:
        ganjil.append(i)
    i += 1

print("ini adalah program dengan while")    
print("ini adalah bilangan ganjil :" + str(ganjil))
print("ini adalah bilangan genap :" + str(genap))