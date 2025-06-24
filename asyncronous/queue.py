from collections import deque

queue = deque()


n = int(input("Berapa banyak data yang ingin dimasukkan? "))
for i in range(n):
    data = input(f"Masukkan data ke-{i+1}: ")
    queue.append(data)

print("Antrian setelah input:", queue)


if queue:
    keluar = queue.popleft()
    print("Data yang keluar:", keluar)
    print("Antrian setelah dequeue:", queue)
else:
    print("Antrian kosong, tidak ada yang bisa dikeluarkan.")




tensi = 87

if tensi >= 85 and tensi <= 90:
    print("Tensi normal tinggi")
