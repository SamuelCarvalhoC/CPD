def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def insertion_sort_optimized(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        if key >= arr[i-1]:
            continue
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def selection_sort_optimized(arr):
    n = len(arr)
    for i in range(n // 2):
        min_idx = i
        max_idx = i
        for j in range(i + 1, n - i):
            if arr[j] < arr[min_idx]: min_idx = j
            if arr[j] > arr[max_idx]: max_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if max_idx == i: max_idx = min_idx
        arr[n - i - 1], arr[max_idx] = arr[max_idx], arr[n - i - 1]

def shell_sort_optimized(arr):
    n = len(arr)
    h = 1
    while h < n // 3: h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            temp = arr[i]
            j = i
            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
        h //= 3
