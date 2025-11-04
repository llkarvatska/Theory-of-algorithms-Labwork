def partition(a, l, r):
    comparisons = 0
    assignments = 0

    pivot = a[l]  # опорний елемент
    assignments += 1

    i = l
    j = r

    while True:
        # Рухаємо i вправо, поки a[i] < pivot
        while a[i] < pivot:
            i += 1
            comparisons += 1
        comparisons += 1  # для виходу з циклу

        # Рухаємо j вліво, поки a[j] > pivot
        while a[j] > pivot:
            j -= 1
            comparisons += 1
        comparisons += 1  # для виходу з циклу

        # Коли індекси перетнулись — повертаємось
        if i >= j:
            return j, comparisons, assignments

        # Обмін елементів
        a[i], a[j] = a[j], a[i]
        assignments += 3

        # Зсуваємо індекси далі
        i += 1
        j -= 1


def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1

        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)

        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3

    else:
        return 0, 0, 0

    return comparisons, assignments, recursive_calls


# --- Приклад ---
data = [90, 10, 15, 80, 100, 6, 57, 5, 29]
print("Оригінальний масив:", data)

arr = data.copy()
total_comparisons, total_assignments, total_recursive_calls = quicksort(arr, 0, len(arr) - 1)

print("Відсортований масив:", arr)
print(f"Порівнянь: {total_comparisons}")
print(f"Присвоювань: {total_assignments}")
print(f"Рекурсивних викликів: {total_recursive_calls}")
