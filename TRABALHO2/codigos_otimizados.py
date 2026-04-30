def heapify(arr, n, i):
    maior = i
    esq, dir = 2 * i + 1, 2 * i + 2

    if esq < n and arr[esq] > arr[maior]: maior = esq
    if dir < n and arr[dir] > arr[maior]: maior = dir

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
   
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    meio = len(arr) // 2
    esq = mergesort(arr[:meio])
    dir = mergesort(arr[meio:]) 

    return merge(esq, dir)

def merge(esq, dir):
    res = []
    i = j = 0
   
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]: 
            res.append(esq[i])
            i += 1
        else:
            res.append(dir[j])
            j += 1
    
    res.extend(esq[i:])
    res.extend(dir[j:])
    return res
import random

def quicksort(arr, baixo=0, alto=None):
    if alto is None: alto = len(arr) - 1
    
    if baixo < alto:
       
        pivo_idx = particionar(arr, baixo, alto)
        quicksort(arr, baixo, pivo_idx)
        quicksort(arr, pivo_idx + 1, alto) 
    return arr

def particionar(arr, baixo, alto):
    
    pivo = arr[random.randint(baixo, alto)]
    i = baixo - 1
    j = alto + 1
    while True:
        i += 1
        while arr[i] < pivo: i += 1
        j -= 1
        while arr[j] > pivo: j -= 1
        if i >= j: return j
        arr[i], arr[j] = arr[j], arr[i]
