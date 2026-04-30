def heapify(arr, n, i):
    maior = i 
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[i] < arr[esquerda]:
        maior = esquerda

    if direita < n and arr[maior] < arr[direita]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

  
def merge_sor(arr)
    if len(arr) <= 1:
        return arr
    meio = lista // 2
    esquerda = mergesort(lista[:meio])
    direita = mergesort(lista[:meio])
    return merge(esquerda, direita)

def merge(esq, dir)
    lista = []
    j = i = 0
    while i < len(dir) and j < len(esq):
        if dir[i] < esq[j]:
            lista.append(dir[i])
            i += 1
        if esq[j] < dir[i]
            lista.append(esq[j])
            j+=1
    return lista

def quicksort(arr):
    if len(arr) < 2:
        return arr
    maiores=[]
    menores=[]
    pivo=arr[0]
    for i in arr[1:]:
        if i>pivo:
        maiores.append(i)
        if i<=pivo:
        menores.append(i)
    return quicksort(menores) + [pivo] + quicksort(maiores)

