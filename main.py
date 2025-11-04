def sink(arr, i, n):
    k = i
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
        if arr[k] >= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j


def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sink(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sink(arr, 0, i)
    return arr


A = [90, 10, 15, 80, 100, 6, 57, 5, 29]
print("Відсортований масив:", heapsort(A))
