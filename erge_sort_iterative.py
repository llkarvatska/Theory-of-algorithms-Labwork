def merge(a, left, mid, right):
    comparisons = 0
    assignments = 0
    L = a[left:mid]
    R = a[mid:right]
    n1, n2 = len(L), len(R)
    i = j = 0
    k = left
    assignments += 5  # створення списків, індекси, змінні

    while i < n1 and j < n2:
        comparisons += 1
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        assignments += 2
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
        assignments += 2

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
        assignments += 2

    return comparisons, assignments


def merge_sort_iterative(a):
    n = len(a)
    comparisons = assignments = 0
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            left, mid, right = j, j + i, min(j + 2 * i, n)
            c, a_count = merge(a, left, mid, right)
            comparisons += c
            assignments += a_count
            j += 2 * i
        i *= 2
    return a, comparisons, assignments


# --- Приклад ---
if __name__ == "__main__":
    data = [90, 10, 15, 80, 100, 6, 57, 5, 29]
    print("Оригінальний масив:", data)
    sorted_iter, comps_iter, assigns_iter = merge_sort_iterative(data.copy())
    print("Відсортований масив:", sorted_iter)
    print(f"Порівнянь: {comps_iter}, Присвоєнь: {assigns_iter}")
