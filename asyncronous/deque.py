from collections import deque

queue = deque()

def enqueue(data):
    queue.append(data)
    print(f"Data '{data}' telah dimasukkan ke dalam antrian.")

def dequeue():
    if not isEmpty():
        data = queue.popleft()
        print(f"Data '{data}' telah dikeluarkan dari antrian.")
        return data
    else:
        print("Antrian kosong, tidak ada yang bisa dikeluarkan.")
        return None
    
def peek():
    if not isEmpty():
        return queue[0]
    else:
        print("Antrian kosong.")
        return None
    
def isEmpty():
    return len(queue) == 0

def size():
    return len(queue)

def view():
    print("Data saat ini dalam antrian:", list(queue))

jumlah = int(input("Masukkan jumlah data antrian: "))
for i in range(jumlah):
    data = input(f"Masukkan data ke-{i+1}: ")
    enqueue(data)

print("Jumlah data saat ini dalam antrian:", size())

print("Mengeluarkan data:", dequeue())

print("Data saat ini dalam antrian:", view())

print("Panjang antrian saat ini:", size())

print("Data kosong?:", isEmpty())

print("Data teratas dalam antrian:", peek())