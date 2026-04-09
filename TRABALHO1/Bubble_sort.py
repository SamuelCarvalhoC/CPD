import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


quantidade = int(input("Quantidade de elementos: "))
lista_aleatoria = [random.randint(1, 10000) for _ in range(quantidade)]


inicio = time.time() 

bubble_sort(lista_aleatoria)

fim = time.time()    
tempo_total = fim - inicio
