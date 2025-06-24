def menu():
    print("Pilih Menu Short:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    return choice

def input_data():
    arr = []
    n = int(input("Masukkan jumlah elemen: "))
    for i in range(n):
        value = int(input(f"Masukkan elemen ke-{i + 1}: "))
        arr.append(value)
    return arr

def buble_short(arr):
    n = len(arr)
    for i in range(n):
        already_sorted = True
        for j in range(n -1 -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        if already_sorted:
            break
    return arr

def selection_short(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1 , n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_short(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_short(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_short(arr[:mid])
    right = merge_short(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


menu_choice = menu()
while menu_choice != '7':
    if menu_choice == '1':
        data = input_data()
        print("Data Sebelum Sorting: ", data)
        sorted_data = buble_short(data.copy())
        print("Data Setelah Bubble Sort: ", sorted_data)
    elif menu_choice == '2':
        data = input_data()
        print("Data Sebelum Sorting: ", data)
        sorted_data = selection_short(data.copy())
        print("Data Setelah Selection Sort: ", sorted_data)
    elif menu_choice == '3':
        data = input_data()
        print("Data Sebelum Sorting: ", data)
        sorted_data = insertion_short(data.copy())
        print("Data Setelah Insertion Sort: ", sorted_data)
    elif menu_choice == '4':
        data = input_data()
        print("Data Sebelum Sorting: ", data)
        sorted_data = merge_short(data.copy())
        print("Data Setelah Merge Sort: ", sorted_data)
    elif menu_choice == '5':
        data = input_data()
        print("Data Sebelum Sorting: ", data)
        sorted_data = quick_sort(data.copy())
        print("Data Setelah Quick Sort: ", sorted_data)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    menu_choice = menu()    

