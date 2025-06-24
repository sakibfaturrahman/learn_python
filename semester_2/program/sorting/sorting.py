# Buble Shoot
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

data = [64, 34, 25, 12, 22, 11, 90]
print("Data Sebelum Sorting: ", data)
sorted_data = buble_short(data.copy())
print("Data Setelah Buble Short: ", sorted_data)

# Selection Short
print("\n")

def selection_short(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1 , n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


data = [64, 34, 25, 12, 22, 11, 90]
print("Data Sebelum Sorting: ", data)
sorted_data = selection_short(data.copy())
print("Data Setelah Selection Short: ", sorted_data)

# insert short
print("\n")


def insertion_short(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

data = [12, 11, 13, 5, 6]
print("Data Sebelum Sorting: ", data)
sorted_data = insertion_short(data.copy())
print("Data Setelah insert Short: ", sorted_data)

# merge short
print("\n")

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

data = [38, 27, 43, 3, 9, 82, 10]
print("Data Sebelum Sorting: ", data)
sorted_data = merge_short(data.copy())
print("Data Setelah Merge Short: ", sorted_data)


# quick short
print("\n")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

data = [3, 6, 8, 10, 1, 2, 1]
print("Data Sebelum Sorting: ", data)
sorted_data = quick_sort(data.copy())
print("Data Setelah quick Short: ", sorted_data)