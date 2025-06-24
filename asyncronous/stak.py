stack = []

def push(data):
    stack.append(data)
    print(f"Data pushed: {data}")

def pop():
    if not isEmpty():
        data = stack.pop()
        print('Data berhasil dikeluarkan', data)
        return data
    else:
        print('Tida ada stack didalam')
        return None
    
def peek():
    if not isEmpty():
       return stack[-1]
    else:
        print('Stack Kosong')
        return None

def isEmpty():
    return len(stack) == 0

def size():
    return len(stack)

def view():
    print('Data saat ini')



jumlah = int(input('Masukan jumlah data stack: '))

for i in range(jumlah):
    data = input(f'Masukan data ke {i+1} : ')
    push(data)

print('Jumlah data saat ini', stack)

print('Mengeluarkan data' ,pop())

print('Data saat ini', view())

print('Panjang Data', size())

print('Data kosong?: ', isEmpty())

print('Data teratas', peek())

